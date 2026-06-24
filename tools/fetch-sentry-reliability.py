#!/usr/bin/env python3
"""Fetch crash-free session stats from Sentry and write a Plotly figure JSON.

The output (assets/reliability.json) is a ready-to-render Plotly figure
({"data": [...], "layout": {...}}) consumed by the existing `{{< plotly >}}` Hugo
shortcode on the front page. It shows the crash-free session rate (reliability) of
each currently-used release plus a global reference line.

Why build-time, not browser-time: the Sentry API needs an auth token, which must
never ship to visitors. So we fetch during the Hugo build (locally or in CI) and
publish only the aggregate, non-sensitive numbers.

Crash-free rate, session counts and MTBF (mean sessions between failures) come from
Sentry. Average session length and a time-based MTBF come from PostHog (Sentry has
no per-session duration for this app), cross-validated against Sentry by joining on
the git commit. Both sources are optional: whichever token is missing is skipped,
and the build falls back to the committed placeholder chart.

Auth:
  SENTRY_AUTH_TOKEN   env, or .sentry-auth-perso / .sentry-auth file (org:read +
                      project:read).
  POSTHOG_QUERY_KEY   env, or .posthog-auth file. A PostHog *personal* API key
                      (phx_...) with query read scope. Without it, the chart simply
                      omits session length / time-based MTBF.

Tunables (env vars, with defaults):
  SENTRY_ORG=aurelienpierreeng
  SENTRY_PROJECT_ID=4511598693253200
  SENTRY_HOST=https://de.sentry.io          (EU region, matches the DSN)
  POSTHOG_HOST=https://eu.posthog.com
  POSTHOG_PROJECT_ID=206740
  RELIABILITY_STATS_PERIOD=90d              (rolling window = "currently used")
  RELIABILITY_MIN_USERS=25                  (drop revisions used by too few unique
                                             users to be statistically meaningful)
  RELIABILITY_MAX_RELEASES=12               (cap bars for readability)
  RELIABILITY_ENVIRONMENT=                  (e.g. "nightly" to show only official
                                             builds; empty = all environments)
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Consumed by the existing {{< plotly src="reliability.json" >}} shortcode, whose
# get_resource partial resolves it from the assets/ directory.
OUT_PATH = os.path.join(REPO_ROOT, "assets", "reliability.json")
OUT_PATH_USERS = os.path.join(REPO_ROOT, "assets", "reliability-users.json")
OUT_PATH_FILES = os.path.join(REPO_ROOT, "assets", "usage-files.json")
OUT_PATH_MODULES = os.path.join(REPO_ROOT, "assets", "usage-modules.json")
OUT_PATH_OS = os.path.join(REPO_ROOT, "assets", "usage-os.json")
OUT_PATH_OPENCL = os.path.join(REPO_ROOT, "assets", "usage-opencl.json")
OUT_PATH_GPU = os.path.join(REPO_ROOT, "assets", "usage-gpu.json")
OUT_PATH_RAM = os.path.join(REPO_ROOT, "assets", "usage-ram.json")
OUT_PATH_DISPLAY = os.path.join(REPO_ROOT, "assets", "usage-display.json")
OUT_PATH_DISTRO = os.path.join(REPO_ROOT, "assets", "usage-distro.json")
OUT_PATH_SCREEN = os.path.join(REPO_ROOT, "assets", "usage-screen.json")
OUT_PATH_CPU = os.path.join(REPO_ROOT, "assets", "usage-cpu.json")
OUT_PATH_BUGS = os.path.join(REPO_ROOT, "assets", "bugs.json")

# Soft pastel colorway (sage / blush / blue + extras) shared by all usage charts.
PALETTE = ["#8ec1a8", "#e8a598", "#9db4d0", "#d8c19a", "#b9a6cc", "#a8ccc9",
           "#e0b0c0", "#c5ca8e", "#9fb6c9", "#cdae8f", "#a9b8a0", "#d2a6a6"]

GITHUB_REPO = os.environ.get("GITHUB_REPO", "aurelienpierreeng/ansel")
GITHUB_API = "https://api.github.com"

ORG = os.environ.get("SENTRY_ORG", "aurelienpierreeng")
PROJECT_ID = os.environ.get("SENTRY_PROJECT_ID", "4511598693253200")
HOST = os.environ.get("SENTRY_HOST", "https://de.sentry.io")
POSTHOG_HOST = os.environ.get("POSTHOG_HOST", "https://eu.posthog.com")
POSTHOG_PROJECT_ID = os.environ.get("POSTHOG_PROJECT_ID", "206740")
STATS_PERIOD = os.environ.get("RELIABILITY_STATS_PERIOD", "90d")
MIN_USERS = int(os.environ.get("RELIABILITY_MIN_USERS", "25"))
MAX_RELEASES = int(os.environ.get("RELIABILITY_MAX_RELEASES", "12"))
ENVIRONMENT = os.environ.get("RELIABILITY_ENVIRONMENT", "").strip()

# Window length in days, parsed from STATS_PERIOD ("90d" -> 90), for HogQL INTERVAL.
_m = re.match(r"(\d+)\s*d", STATS_PERIOD)
PERIOD_DAYS = int(_m.group(1)) if _m else 90


def warn(msg):
    print("[reliability] %s" % msg, file=sys.stderr)


def _read_token(env_name, *files):
    tok = os.environ.get(env_name, "").strip()
    if tok:
        return tok
    for name in files:
        path = os.path.join(REPO_ROOT, name)
        if os.path.isfile(path):
            with open(path) as f:
                return f.read().strip()
    return None


def get_token():
    return _read_token("SENTRY_AUTH_TOKEN", ".sentry-auth-perso", ".sentry-auth")


def get_posthog_key():
    return _read_token("POSTHOG_QUERY_KEY", ".posthog-auth", ".posthog-auth-perso")


def fetch_groups(token):
    params = [
        ("project", PROJECT_ID),
        ("field", "sum(session)"),
        ("field", "crash_free_rate(session)"),
        ("field", "count_unique(user)"),
        ("field", "crash_free_rate(user)"),
        ("groupBy", "release"),
        ("statsPeriod", STATS_PERIOD),
        ("interval", "1d"),
    ]
    if ENVIRONMENT:
        params.append(("environment", ENVIRONMENT))
    url = "%s/api/0/organizations/%s/sessions/?%s" % (HOST, ORG, urllib.parse.urlencode(params))
    req = urllib.request.Request(url, headers={"Authorization": "Bearer %s" % token})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)  # full payload: "groups" + "intervals"


def fetch_global_users(token):
    """Project-wide, de-duplicated unique-user counts (no per-release grouping), so
    the crash-free-users headline isn't inflated by users active in several
    releases. Returns (users, healthy_users) or None."""
    params = [
        ("project", PROJECT_ID),
        ("field", "count_unique(user)"),
        ("field", "crash_free_rate(user)"),
        ("statsPeriod", STATS_PERIOD),
        ("interval", "1d"),
    ]
    if ENVIRONMENT:
        params.append(("environment", ENVIRONMENT))
    url = "%s/api/0/organizations/%s/sessions/?%s" % (HOST, ORG, urllib.parse.urlencode(params))
    req = urllib.request.Request(url, headers={"Authorization": "Bearer %s" % token})
    with urllib.request.urlopen(req, timeout=30) as resp:
        groups = json.load(resp).get("groups", [])
    if not groups:
        return None
    totals = groups[0].get("totals") or {}
    users = int(totals.get("count_unique(user)") or 0)
    rate = totals.get("crash_free_rate(user)")
    healthy = users * float(rate) if (users and rate is not None) else 0.0
    return users, healthy


def sentry_first_session(payload):
    """Earliest daily interval that actually has sessions (data start, day precision)."""
    intervals = payload.get("intervals") or []
    groups = payload.get("groups") or []
    for i, iv in enumerate(intervals):
        for g in groups:
            series = (g.get("series") or {}).get("sum(session)") or []
            if i < len(series) and series[i]:
                return _parse_ts(iv)
    return None


def fetch_posthog(key):
    """Per-commit session stats from PostHog: started/ended counts and avg length.

    Returns (rows, first_ts) where rows are {"hash","n_start","n_end","dur_sum",
    "dur_n"} keyed by the canonical commit hash (same extraction as Sentry releases,
    so the duplicate naming — bare hash vs full version vs full SHA — collapses and
    joins) and first_ts is the earliest telemetry event seen (for the data span).
    The PostHog key is coalesce(commit, app_version): session_start has carried
    app_version for a while; both events carry the commit once the new telemetry is
    deployed.
    """
    hogql = (
        "SELECT coalesce(properties.commit, properties.app_version) AS rel, "
        "countIf(event = 'session_start') AS n_start, "
        "countIf(event = 'session_end') AS n_end, "
        "sumIf(toFloat(properties.session_seconds), "
        "event = 'session_end' AND isNotNull(properties.session_seconds)) AS dur_sum, "
        "countIf(event = 'session_end' AND isNotNull(properties.session_seconds)) AS dur_n, "
        "sumIf(toFloat(properties.images_processed), "
        "event = 'session_end' AND isNotNull(properties.images_processed)) AS pics, "
        "min(timestamp) AS first_ts "
        "FROM events "
        "WHERE event IN ('session_start','session_end') "
        "AND isNotNull(coalesce(properties.commit, properties.app_version)) "
        "AND timestamp > now() - INTERVAL %d DAY "
        "GROUP BY rel"
    ) % PERIOD_DAYS
    body = json.dumps({"query": {"kind": "HogQLQuery", "query": hogql}}).encode()
    url = "%s/api/projects/%s/query/" % (POSTHOG_HOST, POSTHOG_PROJECT_ID)
    req = urllib.request.Request(
        url, data=body,
        headers={"Authorization": "Bearer %s" % key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        results = json.load(resp).get("results", [])

    rows = []
    first_ts = None
    for rel, n_start, n_end, dur_sum, dur_n, pics, ts in results:
        h = _commit_hash(rel) if rel else None
        if not h:
            continue
        rows.append({"hash": h, "revision": _revision(rel),
                     "n_start": int(n_start or 0), "n_end": int(n_end or 0),
                     "dur_sum": float(dur_sum or 0.0), "dur_n": int(dur_n or 0),
                     "pics": int(pics or 0)})
        t = _parse_ts(ts) if isinstance(ts, str) else None
        if t and (first_ts is None or t < first_ts):
            first_ts = t
    return rows, first_ts


def _posthog_query(key, hogql):
    body = json.dumps({"query": {"kind": "HogQLQuery", "query": hogql}}).encode()
    url = "%s/api/projects/%s/query/" % (POSTHOG_HOST, POSTHOG_PROJECT_ID)
    req = urllib.request.Request(
        url, data=body,
        headers={"Authorization": "Bearer %s" % key, "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp).get("results", [])


def fetch_file_types(key):
    """Number of image files opened per file type, from the file_opened events.

    Bucketed by extension, except DNG (which can be a mosaiced raw or an already
    demosaiced/linear file) which is split by needs_demosaic. Returns sorted
    (labels, values, hover)."""
    hogql = (
        "SELECT lower(properties.extension) AS ext, "
        "toString(properties.needs_demosaic) AS demo, count() AS n "
        "FROM events WHERE event = 'file_opened' AND isNotNull(properties.extension) "
        "AND timestamp > now() - INTERVAL %d DAY GROUP BY ext, demo"
    ) % PERIOD_DAYS
    agg = {}
    for ext, demo, n in _posthog_query(key, hogql):
        ext = (ext or "?").lower()
        # Merge equivalent extensions so they count as one type.
        ext = {"tif": "tiff", "jpeg": "jpg"}.get(ext, ext)
        n = int(n or 0)
        if ext == "dng":
            mosaiced = str(demo).lower() in ("true", "1")
            label = "DNG (mosaiced)" if mosaiced else "DNG (demosaiced)"
        else:
            label = ext.upper()
        agg[label] = agg.get(label, 0) + n
    items = sorted(agg.items(), key=lambda kv: kv[1], reverse=True)
    labels = [k for k, _ in items]
    values = [v for _, v in items]
    hover = ["%s<br>%d files opened" % (k, v) for k, v in items]
    return labels, values, hover


def fetch_modules(key, limit=25):
    """Most-used features (views / panels / modules), from the module_used events.
    Returns (labels, values, hover) for the top `limit` by usage."""
    hogql = (
        "SELECT properties.category AS cat, properties.name AS nm, count() AS n "
        "FROM events WHERE event = 'module_used' AND isNotNull(properties.name) "
        "AND timestamp > now() - INTERVAL %d DAY "
        "GROUP BY cat, nm ORDER BY n DESC LIMIT %d"
    ) % (PERIOD_DAYS, limit)
    labels, values, hover = [], [], []
    for cat, nm, n in _posthog_query(key, hogql):
        labels.append(nm or "?")
        values.append(int(n or 0))
        hover.append("%s<br>%s · used %d times" % (nm or "?", cat or "?", int(n or 0)))
    return labels, values, hover


def _usage_bar_figure(labels, values, hover, title, y_title, color):
    """Single-series bar chart in the same pastel theme as the reliability charts."""
    return {
        "data": [{
            "type": "bar", "x": labels, "y": values,
            "hovertext": hover, "hoverinfo": "text", "marker": {"color": color},
        }],
        "layout": {
            "title": {"text": title},
            "xaxis": {"type": "category", "tickangle": -40, "automargin": True},
            "yaxis": {"title": {"text": y_title}, "rangemode": "tozero"},
            "margin": {"t": 70, "r": 30, "b": 80, "l": 60},
            "showlegend": False,
        },
    }


def _usage_span(key):
    """Actual data window for the usage events, phrased like the other charts."""
    rows = _posthog_query(key, "SELECT min(timestamp) FROM events WHERE event IN "
                          "('file_opened','module_used') AND timestamp > now() - "
                          "INTERVAL %d DAY" % PERIOD_DAYS)
    first = _parse_ts(rows[0][0]) if rows and rows[0] and isinstance(rows[0][0], str) else None
    return _format_span(first, datetime.now(timezone.utc))


def _usage_pie_figure(labels, values, title, hover=None):
    """Donut pie chart in the shared pastel theme."""
    return {
        "data": [{
            "type": "pie", "labels": labels, "values": values, "hole": 0.45,
            "hovertext": hover, "hoverinfo": "text" if hover else "label+value+percent",
            "textinfo": "label+percent", "sort": True,
            "marker": {"colors": PALETTE},
        }],
        "layout": {
            "title": {"text": title},
            "margin": {"t": 70, "r": 20, "b": 20, "l": 20},
            "showlegend": True,
            "legend": {"orientation": "h", "x": 0, "y": -0.05},
        },
    }


# --- Hardware / platform demographics (PostHog session_start, per unique user) ---

# Linux distro families, matched (case-insensitive substring) against the reported
# OS string. Fedora-derived atomic spins are listed before "Fedora" so they stay
# distinct; order matters (first match wins).
KNOWN_DISTROS = [
    "Linux Mint", "LMDE", "Ubuntu", "Kubuntu", "Pop!_OS", "Debian", "Bluefin",
    "Bazzite", "Nobara", "Perfido", "Fedora", "Arch Linux", "EndeavourOS",
    "CachyOS", "Manjaro", "Garuda", "Void", "openSUSE", "Gentoo", "NixOS",
    "Alpine", "Zorin", "elementary", "Solus", "Slackware",
]


def _os_family(s):
    """Classify a reported OS string into Linux / macOS / Windows, or None."""
    if not s:
        return None
    t = s.lower()
    if "windows" in t:
        return "Windows"
    if "mac" in t or "darwin" in t or "os x" in t:
        return "macOS"
    return "Linux"  # every other reported OS string is a Linux distro


def _distro_name(s):
    """Normalise a Linux OS string to a distro name ("Ubuntu 24.04.4 LTS" ->
    "Ubuntu", "Fedora Linux 44 (...)" -> "Fedora")."""
    if not s:
        return "Other"
    for d in KNOWN_DISTROS:
        if d.lower() in s.lower():
            return d
    return s.split()[0]  # fall back to the first word


def _ram_class(v):
    """2 GB-wide RAM class for a reported gigabyte figure; returns (low, label)."""
    try:
        g = float(v)
    except (TypeError, ValueError):
        return None
    if g <= 0:
        return None
    low = int(g // 2 * 2)
    return low, "%d–%d GiB" % (low, low + 2)


def _truthy(v):
    return str(v).strip().lower() in ("true", "1", "yes")


def _clean_gpu(name):
    """Drop parenthesised noise from a GPU name for legibility, e.g.
    "Intel(R) UHD Graphics 630" -> "Intel UHD Graphics 630",
    "AMD Radeon RX 6700 (radeonsi, navi22, ACO, DRM 3.16)" -> "AMD Radeon RX 6700".
    """
    name = re.sub(r"\([^)]*\)", "", name)
    return re.sub(r"\s+", " ", name).strip()


def _num(v):
    """Round a numeric-ish value to int, e.g. "1920.0" -> 1920, or None."""
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return int(round(f)) if f > 0 else None


def _screen_label(sw, sh, ppd):
    """Screen geometry as (pixel_count, "width×height"), or None.

    The reported geometry is divided by the scaling factor (GTK ppd) to get the
    device (logical) resolution. pixel_count is returned for sorting by surface
    area."""
    w, h = _num(sw), _num(sh)
    if not w or not h:
        return None
    try:
        s = float(ppd)
    except (TypeError, ValueError):
        s = 1.0
    if s <= 0:
        s = 1.0
    # Reported geometry is in physical pixels; divide by the scaling factor to get
    # the device (logical) resolution actually used to lay out the UI.
    w = int(round(w / s))
    h = int(round(h / s))
    return w * h, "%d×%d" % (w, h)


def fetch_user_platforms(key):
    """One row per unique user with their most-recent reported platform facts.

    Uses argMax(..., timestamp) so each user contributes a single, latest value
    (dedup by unique user as requested). Returns a list of dicts."""
    props = ["os", "opencl", "gpu", "ram_gb", "display_server",
             "screen_width", "screen_height", "ppd", "cpu_cores"]
    sel = ", ".join("argMax(properties.%s, timestamp) AS %s" % (p, p) for p in props)
    hogql = (
        "SELECT %s FROM events WHERE event = 'session_start' "
        "AND timestamp > now() - INTERVAL %d DAY GROUP BY person_id"
    ) % (sel, PERIOD_DAYS)
    rows = []
    for os_s, opencl, gpu, ram, disp, sw, sh, ppd, cores in _posthog_query(key, hogql):
        rows.append({"os": os_s, "opencl": opencl, "gpu": gpu,
                     "ram": ram, "disp": disp,
                     "sw": sw, "sh": sh, "ppd": ppd, "cores": cores})
    return rows


def _count_sorted(counter, reverse=True):
    items = sorted(counter.items(), key=lambda kv: kv[1], reverse=reverse)
    return [k for k, _ in items], [v for _, v in items]


def _weighted_quantile_idx(counts, q):
    """Index of the category (in the given display order) at which the cumulative
    count first reaches quantile q of the total. q=0.5 is the weighted median,
    0.1 / 0.9 the first / last decile. Or None when there is no data."""
    total = sum(counts)
    if total <= 0:
        return None
    thresh = total * q
    cum = 0
    for i, v in enumerate(counts):
        cum += v
        if cum >= thresh:
            return i
    return len(counts) - 1


def _weighted_median_idx(counts):
    return _weighted_quantile_idx(counts, 0.5)


def _ref_line(cat, span, orient, name, color="#222222", width=2):
    """Dotted reference line trace at category `cat`, with the name written as a
    text overlay at the line's end. orient 'v' draws a vertical line at x=cat over
    y in [0, span] (label on top); 'h' a horizontal line at y=cat over x in
    [0, span] (label at the right)."""
    trace = {"type": "scatter", "mode": "lines+text", "name": name,
             "hoverinfo": "name", "showlegend": False, "cliponaxis": False,
             "line": {"color": color, "width": width, "dash": "dot"},
             "textfont": {"color": color, "size": 11}}
    if orient == "v":
        trace["x"], trace["y"] = [cat, cat], [0, span]
        trace["text"], trace["textposition"] = ["", name], "top center"
    else:
        trace["x"], trace["y"] = [0, span], [cat, cat]
        trace["text"], trace["textposition"] = ["", name], "middle left"
    return trace


def _quantile_lines(labels, counts, span, orient):
    """P10 / median / P90 reference lines for a weighted histogram. Returns
    (traces, median_idx). The median is drawn bold and dark, the deciles thinner
    and lighter."""
    specs = [("P10", 0.1, "#9aa0a6", 1),
             ("median", 0.5, "#222222", 2),
             ("P90", 0.9, "#9aa0a6", 1)]
    traces, median_idx = [], None
    for name, q, color, width in specs:
        idx = _weighted_quantile_idx(counts, q)
        if idx is None:
            continue
        traces.append(_ref_line(labels[idx], span, orient, name, color, width))
        if q == 0.5:
            median_idx = idx
    return traces, median_idx


def write_platform_figures(key):
    """Build and write the per-user hardware/platform charts (PostHog only)."""
    rows = fetch_user_platforms(key)
    if not rows:
        warn("no PostHog session_start data; keeping platform placeholders.")
        return
    n_users = len(rows)

    fam, opencl, gpu, ram, disp, distro, screen, cpu = {}, {}, {}, {}, {}, {}, {}, {}
    for r in rows:
        f = _os_family(r["os"])
        # macOS reports no OS string (telemetry gap), but Apple-Silicon machines
        # are unambiguous from the GPU name, so recover them as macOS.
        if not f and (r["gpu"] or "").strip().lower().startswith("apple "):
            f = "macOS"
        if f:
            fam[f] = fam.get(f, 0) + 1
        # OpenCL on/off (only meaningful when reported).
        if r["opencl"] is not None and str(r["opencl"]).strip() != "":
            k = "With OpenCL" if _truthy(r["opencl"]) else "Without OpenCL"
            opencl[k] = opencl.get(k, 0) + 1
        # GPU brand + model (only when one was reported), parentheses stripped.
        g = _clean_gpu(r["gpu"] or "")
        if g:
            gpu[g] = gpu.get(g, 0) + 1
        # RAM in 2 GB classes.
        rc = _ram_class(r["ram"])
        if rc:
            ram[rc] = ram.get(rc, 0) + 1
        # Linux-only: display server and distribution.
        if f == "Linux":
            d = (r["disp"] or "").strip().lower()
            if d in ("x11", "xorg"):
                disp["X11"] = disp.get("X11", 0) + 1
            elif d == "wayland":
                disp["Wayland"] = disp.get("Wayland", 0) + 1
            elif d:
                disp["Other"] = disp.get("Other", 0) + 1
            distro[_distro_name(r["os"])] = distro.get(_distro_name(r["os"]), 0) + 1
        # Screen geometry as width×height@scaling.
        sc = _screen_label(r["sw"], r["sh"], r["ppd"])
        if sc:
            key_sc = (sc[0], sc[1])  # (sort key = pixel count, display label)
            screen[key_sc] = screen.get(key_sc, 0) + 1
        # CPU logical core count.
        cc = _num(r["cores"])
        if cc:
            cpu[cc] = cpu.get(cc, 0) + 1

    jobs = []

    # 2. Users per OS family (pie).
    fl, fv = _count_sorted(fam)
    jobs.append((OUT_PATH_OS, fl, _usage_pie_figure(
        fl, fv, "Operating systems in use — %d users" % n_users,
        ["%s<br>%d users" % (k, v) for k, v in zip(fl, fv)])))

    # 3. OpenCL on/off (pie).
    ol, ov = _count_sorted(opencl)
    jobs.append((OUT_PATH_OPENCL, ol, _usage_pie_figure(
        ol, ov, "GPU acceleration (OpenCL) — %d users" % sum(ov),
        ["%s<br>%d users" % (k, v) for k, v in zip(ol, ov)])))

    # 4. GPU models (vertical bar, most common first).
    gl, gv = _count_sorted(gpu)
    gl, gv = gl[:20], gv[:20]
    gpu_fig = {
        "data": [{
            "type": "bar", "x": gl, "y": gv,
            "hovertext": ["%s<br>%d users" % (k, v) for k, v in zip(gl, gv)],
            "hoverinfo": "text", "marker": {"color": "#9db4d0"},
        }],
        "layout": {
            "title": {"text": "Graphics cards in use — %d users" % sum(gv)},
            "xaxis": {"type": "category", "tickangle": -40, "automargin": True},
            "yaxis": {"title": {"text": "Users"}, "rangemode": "tozero"},
            "margin": {"t": 70, "r": 30, "b": 120, "l": 60},
            "showlegend": False,
        },
    }
    jobs.append((OUT_PATH_GPU, gl, gpu_fig))

    # 5. RAM in 2 GB classes (bar, ordered by size, median marked).
    ram_items = sorted(ram.items(), key=lambda kv: kv[0][0])
    rl = [lbl for (_, lbl), _ in ram_items]
    rv = [v for _, v in ram_items]
    rlines, rmid = _quantile_lines(rl, rv, max(rv) if rv else 0, "v")
    ram_data = [{
        "type": "bar", "x": rl, "y": rv,
        "hovertext": ["%s<br>%d users%s" % (l, v, " · median" if i == rmid else "")
                      for i, (l, v) in enumerate(zip(rl, rv))],
        "hoverinfo": "text", "marker": {"color": "#d8c19a"},
    }]
    ram_data.extend(rlines)
    ram_fig = {
        "data": ram_data,
        "layout": {
            "title": {"text": "Installed memory (RAM) — %d users" % sum(rv)},
            "xaxis": {"type": "category", "tickangle": -40, "automargin": True},
            "yaxis": {"title": {"text": "Users"}, "rangemode": "tozero"},
            "margin": {"t": 70, "r": 30, "b": 80, "l": 60},
            "showlegend": False,
        },
    }
    jobs.append((OUT_PATH_RAM, rl, ram_fig))

    # 6. X11 vs Wayland, Linux only (pie).
    dl, dv = _count_sorted(disp)
    jobs.append((OUT_PATH_DISPLAY, dl, _usage_pie_figure(
        dl, dv, "Display server on Linux — %d users" % sum(dv),
        ["%s<br>%d users" % (k, v) for k, v in zip(dl, dv)])))

    # 7. Linux distributions (pie).
    nl, nv = _count_sorted(distro)
    jobs.append((OUT_PATH_DISTRO, nl, _usage_pie_figure(
        nl, nv, "Linux distributions — %d users" % sum(nv),
        ["%s<br>%d users" % (k, v) for k, v in zip(nl, nv)])))

    # 8. Screen geometry width×height (horizontal bar, sorted by surface area;
    # smallest at the bottom, largest at top). The median screen (by surface area,
    # weighted across users) is highlighted.
    sc_items = sorted(screen.items(), key=lambda kv: kv[0][0])  # by pixel count asc
    sl = [lbl for (_, lbl), _ in sc_items]
    sv = [v for _, v in sc_items]
    total = sum(sv)
    slines, smid = _quantile_lines(sl, sv, max(sv) if sv else 0, "h")
    hover = ["%s<br>%d users%s" % (l, v, " · median" if i == smid else "")
             for i, (l, v) in enumerate(zip(sl, sv))]
    median_label = sl[smid] if smid is not None else "?"
    screen_data = [{
        "type": "bar", "orientation": "h", "x": sv, "y": sl,
        "hovertext": hover, "hoverinfo": "text", "marker": {"color": "#a8ccc9"},
    }]
    screen_data.extend(slines)
    screen_fig = {
        "data": screen_data,
        "layout": {
            "title": {"text": "Screen size in device pixels, after high-DPI "
                      "scaling — %d users" % total},
            "xaxis": {"title": {"text": "Users"}, "rangemode": "tozero"},
            "yaxis": {"type": "category", "automargin": True},
            "margin": {"t": 70, "r": 30, "b": 50, "l": 60},
            "showlegend": False,
        },
    }
    jobs.append((OUT_PATH_SCREEN, sl, screen_fig))

    # 9. CPU logical cores (vertical bar, ordered by core count, P10/median/P90).
    cpu_items = sorted(cpu.items(), key=lambda kv: kv[0])
    cl = [str(k) for k, _ in cpu_items]
    cv = [v for _, v in cpu_items]
    clines, cmid = _quantile_lines(cl, cv, max(cv) if cv else 0, "v")
    cpu_data = [{
        "type": "bar", "x": cl, "y": cv,
        "hovertext": ["%s cores<br>%d users%s" % (l, v, " · median" if i == cmid else "")
                      for i, (l, v) in enumerate(zip(cl, cv))],
        "hoverinfo": "text", "marker": {"color": "#b9a6cc"},
    }]
    cpu_data.extend(clines)
    cpu_fig = {
        "data": cpu_data,
        "layout": {
            "title": {"text": "CPU logical cores — %d users" % sum(cv)},
            "xaxis": {"type": "category", "title": {"text": "Logical cores"},
                      "automargin": True},
            "yaxis": {"title": {"text": "Users"}, "rangemode": "tozero"},
            "margin": {"t": 70, "r": 30, "b": 60, "l": 60},
            "showlegend": False,
        },
    }
    jobs.append((OUT_PATH_CPU, cl, cpu_fig))

    for path, labels, fig in jobs:
        if not labels:
            warn("no data for %s; keeping placeholder." % os.path.basename(path))
            continue
        with open(path, "w") as f:
            json.dump(fig, f, indent=2)
        print("[usage] wrote %s (%d entries)" % (path, len(labels)))


def write_usage_figures(key):
    """Build and write the two "How is Ansel used?" charts (PostHog only)."""
    fl, fv, fh = fetch_file_types(key)
    ml, mv, mh = fetch_modules(key)
    span = _usage_span(key)
    # Grand total of all activations (the bars only show the top features).
    mtot = _posthog_query(key, "SELECT count() FROM events WHERE event = "
                          "'module_used' AND timestamp > now() - INTERVAL %d DAY" % PERIOD_DAYS)
    modules_total = int(mtot[0][0]) if mtot and mtot[0] else sum(mv)
    # Median file type: the one at which the cumulative count of images opened
    # crosses half the total (bars are already ordered by count), marked with a
    # vertical line.
    flines, fmid = _quantile_lines(fl, fv, max(fv) if fv else 0, "v")
    files_title = ("Image files opened, by type — %d files (%s)"
                   % (sum(fv), span))
    files_fig = _usage_bar_figure(fl, fv, fh, files_title, "Files opened", "#8ec1a8")
    files_fig["data"].extend(flines)
    modules_title = ("Most-used features — %d activations (%s)"
                     % (modules_total, span))
    jobs = (
        (OUT_PATH_FILES, fl, files_fig),
        (OUT_PATH_MODULES, ml, _usage_bar_figure(
            ml, mv, mh, modules_title, "Times used", "#9db4d0")),
    )
    for path, labels, fig in jobs:
        if not labels:
            warn("no data for %s; keeping placeholder." % os.path.basename(path))
            continue
        with open(path, "w") as f:
            json.dump(fig, f, indent=2)
        print("[usage] wrote %s (%d entries)" % (path, len(labels)))


# --- GitHub bug-report progress -------------------------------------------------

def _gh_request(token, url):
    req = urllib.request.Request(url, headers={
        "Authorization": "Bearer %s" % token,
        "Accept": "application/vnd.github+json",
        "User-Agent": "ansel-website-stats",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def fetch_packaged_hashes(token):
    """Commit hashes of our officially packaged builds (nightly + stable).

    The nightly/stable builds are shipped as release assets, whose file names embed
    the commit hash, e.g. "Ansel-0.0.0+1008.g05e82c55-x86_64.AppImage". We take the
    last two published releases (including pre-releases, since the nightly channel is
    a rolling pre-release) and union the hashes found in their asset names. Returned
    lowercased so revisions that match a packaged build can be flagged with an
    asterisk on the chart. Returns a set (possibly empty)."""
    try:
        releases = _gh_request(
            token, "%s/repos/%s/releases?per_page=2" % (GITHUB_API, GITHUB_REPO))
    except Exception as exc:  # noqa: BLE001
        warn("GitHub releases request failed (%s); no packaged-build markers." % exc)
        return set()
    hashes = set()
    for rel in releases or []:
        for asset in rel.get("assets", []):
            m = re.search(r"[.~]g([0-9a-f]{7,40})", asset.get("name", ""))
            if m:
                hashes.add(m.group(1).lower())
    return hashes


def _is_packaged(cluster_hash, packaged_hashes):
    """True if a release cluster's commit hash matches a packaged build. Abbreviated
    and full hashes are reconciled by prefix matching (either way), as elsewhere."""
    if not cluster_hash or not packaged_hashes:
        return False
    return any(cluster_hash.startswith(p) or p.startswith(cluster_hash)
               for p in packaged_hashes)


ISSUE_TYPES = ("Bug", "Task", "Feature")


def _gh_count(token, qualifiers):
    """Count issues in the repo matching the search qualifiers."""
    q = "repo:%s is:issue %s" % (GITHUB_REPO, qualifiers)
    url = "%s/search/issues?per_page=1&q=%s" % (GITHUB_API, urllib.parse.quote(q))
    return int(_gh_request(token, url).get("total_count", 0))


def _bucket_counts(token, bucket_q):
    """For a milestone/no-milestone bucket, count resolved (closed as completed)
    and still-open issues per type. Returns (fixed_total, open_total, per_type)."""
    per_type = {}
    f_total = o_total = 0
    for t in ISSUE_TYPES:
        f = _gh_count(token, 'type:%s state:closed reason:completed %s' % (t, bucket_q))
        o = _gh_count(token, 'type:%s state:open %s' % (t, bucket_q))
        per_type[t] = (f, o)
        f_total += f
        o_total += o
    return f_total, o_total, per_type


def _version_key(title):
    nums = re.findall(r"\d+", title or "")
    return tuple(int(n) for n in nums) if nums else (9999,)


def fetch_github_issues(token):
    """Issue-resolution progress (bugs + tasks + features) for the NEXT release
    only - the lowest-version open milestone, chosen dynamically so nothing needs
    editing per revision. Later milestones and unscheduled issues are ignored.

    Returns (milestone_title, per_type, total_fixed, total_open) or None."""
    try:
        milestones = _gh_request(
            token, "%s/repos/%s/milestones?state=open&per_page=100" % (GITHUB_API, GITHUB_REPO))
    except Exception as exc:  # noqa: BLE001
        warn("GitHub milestones request failed (%s)." % exc)
        return None
    if not milestones:
        return None
    nxt = sorted(milestones, key=lambda m: _version_key(m.get("title", "")))[0]
    title = nxt.get("title", "?")
    f, o, per_type = _bucket_counts(token, 'milestone:"%s"' % title)
    if f + o == 0:
        return None
    return title, per_type, f, o


def _issues_figure(milestone, per_type, total_fixed, total_open):
    """Horizontal stacked bars for the next release: number of issues (x) per type
    (y = bugs / tasks / features), Resolved (green) + Still open (blush). The
    milestone number goes in the title."""
    labels, x_res, x_open, hov_res, hov_open, txt_res, txt_open = [], [], [], [], [], [], []
    for t in reversed(ISSUE_TYPES):  # reversed so bugs ends up on top
        rf, ro = per_type[t]
        if rf + ro == 0:
            continue
        labels.append(t.lower() + "s")
        x_res.append(rf)
        x_open.append(ro)
        txt_res.append(str(rf) if rf else "")
        txt_open.append(str(ro) if ro else "")
        hov_res.append("%s<br>%d resolved" % (t.lower() + "s", rf))
        hov_open.append("%s<br>%d still open" % (t.lower() + "s", ro))

    title = ("Next release %s — %d issues resolved, %d still open"
             % (milestone, total_fixed, total_open))
    return {
        "data": [
            {"type": "bar", "orientation": "h", "y": labels, "x": x_res, "name": "Resolved",
             "marker": {"color": "#8ec1a8"}, "text": txt_res,
             "textposition": "inside", "insidetextanchor": "middle",
             "hovertext": hov_res, "hoverinfo": "text"},
            {"type": "bar", "orientation": "h", "y": labels, "x": x_open, "name": "Still open",
             "marker": {"color": "#e8a598"}, "text": txt_open,
             "textposition": "inside", "insidetextanchor": "middle",
             "hovertext": hov_open, "hoverinfo": "text"},
        ],
        "layout": {
            "title": {"text": title},
            "barmode": "stack",
            "xaxis": {"title": {"text": "Number of issues"}, "rangemode": "tozero"},
            "yaxis": {"type": "category", "automargin": True},
            "legend": {"orientation": "h", "x": 0, "y": 1.12},
            "margin": {"t": 80, "r": 30, "b": 50, "l": 80},
            "showlegend": True,
        },
    }


def write_bugs_figure(token):
    data = fetch_github_issues(token)
    if not data:
        warn("no GitHub issue data; keeping bugs placeholder.")
        return
    milestone, per_type, total_fixed, total_open = data
    with open(OUT_PATH_BUGS, "w") as f:
        json.dump(_issues_figure(milestone, per_type, total_fixed, total_open), f, indent=2)
    print("[bugs] wrote %s (next release %s: %d resolved, %d open)"
          % (OUT_PATH_BUGS, milestone, total_fixed, total_open))


def _strip(release):
    return release[len("ansel@"):] if release.startswith("ansel@") else release


def _commit_hash(release):
    """Lowercased commit hash for a release, or None if it isn't commit-based.

    The same build appears in Sentry under several names, all carrying the same
    commit hash (the abbreviated forms are prefixes of the full SHA):
      - full version    "0.0.0+3836~g8f7c553fb6"  -> "8f7c553fb6"
      - bare short SHA  "8f7c553"                 -> "8f7c553"
      - full 40-char SHA (current release scheme) -> itself
    """
    r = _strip(release)
    m = re.match(r"^\d+\.\d+\.\d+\+\d+~g([0-9a-f]+)$", r)
    if m:
        return m.group(1).lower()
    if re.fullmatch(r"[0-9a-f]{7,40}", r):
        return r.lower()
    return None


def _revision(release):
    """Commit count from a full version string ("0.0.0+3836~g..." -> "3836")."""
    m = re.match(r"^\d+\.\d+\.\d+\+(\d+)~g[0-9a-f]+$", _strip(release))
    return m.group(1) if m else None


def _fmt_duration(seconds):
    """Human-readable duration, or None."""
    if not seconds or seconds <= 0:
        return None
    if seconds < 90:
        return "%.0f s" % seconds
    if seconds < 5400:
        return "%.0f min" % (seconds / 60.0)
    return "%.1f h" % (seconds / 3600.0)


def _parse_ts(s):
    """Parse an ISO-8601 timestamp (handles a trailing 'Z') to an aware datetime."""
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def _format_span(start, end):
    """Human window from the actual data extent, e.g. 'the last 27 h' / '5 days'."""
    if not start or not end or end <= start:
        return "recent history"
    secs = (end - start).total_seconds()
    if secs < 36 * 3600:           # under ~1.5 days: report in hours
        return "the last %d h" % max(1, round(secs / 3600.0))
    return "the last %d days" % max(1, round(secs / 86400.0))


def fetch_crash_times(token):
    """Per-commit crash stats from Sentry crash events.

    Each crash event carries (from sentry.c) the session_seconds and
    images_processed at crash time, plus the shared session_id. We DEDUPE by
    session_id so one crashed session counts once (multiple events per crash, or
    re-sent envelopes, don't inflate the figures), then aggregate per commit:
      sec_sum / sec_n  -> mean uptime before a crash (MTBF)
      pics_sum         -> images processed before a crash
    Returns (rows, first_ts) with rows [{"hash","sec_sum","sec_n","pics_sum"}].
    """
    agg = {}        # hash -> aggregate
    seen = set()    # session_ids already counted
    first_ts = None
    base = "%s/api/0/organizations/%s/events/" % (HOST, ORG)
    params = [
        ("project", PROJECT_ID),
        ("field", "release"),
        ("field", "session_seconds"),
        ("field", "images_processed"),
        ("field", "session_id"),
        ("field", "timestamp"),
        ("query", "event.type:error has:session_seconds"),
        ("statsPeriod", STATS_PERIOD),
        ("per_page", "100"),
    ]
    cursor = None
    for _ in range(20):  # bounded pagination
        p = list(params)
        if cursor:
            p.append(("cursor", cursor))
        req = urllib.request.Request(base + "?" + urllib.parse.urlencode(p),
                                     headers={"Authorization": "Bearer %s" % token})
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = json.load(resp)
            link = resp.headers.get("Link", "")
        for ev in payload.get("data", []):
            t = _parse_ts(ev.get("timestamp"))
            if t and (first_ts is None or t < first_ts):
                first_ts = t
            # One record per crashed session (fall back to event id pre-session_id).
            sid = ev.get("session_id") or ev.get("id")
            if sid in seen:
                continue
            seen.add(sid)
            h = _commit_hash(ev.get("release") or "")
            if not h:
                continue
            try:
                sec = float(ev.get("session_seconds"))
            except (TypeError, ValueError):
                sec = None
            try:
                pics = int(float(ev.get("images_processed")))
            except (TypeError, ValueError):
                pics = 0
            a = agg.setdefault(h, {"hash": h, "sec_sum": 0.0, "sec_n": 0, "pics_sum": 0})
            if sec and sec > 0:
                a["sec_sum"] += sec
                a["sec_n"] += 1
            a["pics_sum"] += pics
        # Follow pagination only while the next page reports results.
        cursor = None
        for part in link.split(","):
            if 'rel="next"' in part and 'results="true"' in part:
                m = re.search(r'cursor="([^"]+)"', part)
                if m:
                    cursor = m.group(1)
        if not cursor:
            break
    return list(agg.values()), first_ts


def build_figure(groups, posthog_rows, crash_rows, span_label, global_users=None,
                 packaged_hashes=None):
    # Unify releases that are the same commit under different names. Cluster by
    # commit hash: two releases belong together when one hash is a prefix of the
    # other (e.g. "8f7c553" ⊂ "8f7c553fb6" ⊂ the full 40-char SHA). Sessions are
    # summed across the cluster so each commit appears once.
    clusters = []
    g_total = 0.0
    g_healthy = 0.0

    for grp in groups:
        release = (grp.get("by") or {}).get("release")
        totals = grp.get("totals") or {}
        total = totals.get("sum(session)") or 0
        rate = totals.get("crash_free_rate(session)")
        if not release or total <= 0 or rate is None:
            continue

        # Skip releases that are not tied to a commit (e.g. the "dsn-verify" test
        # tag, or any manual/test release): they are not real usage and must not
        # count toward any release or the global totals.
        h = _commit_hash(release)
        if h is None:
            continue
        rev = _revision(release)

        total = int(total)
        healthy = total * float(rate)
        g_total += total
        g_healthy += healthy

        users = int(totals.get("count_unique(user)") or 0)
        u_rate = totals.get("crash_free_rate(user)")
        healthy_users = users * float(u_rate) if (users and u_rate is not None) else 0.0

        match = None
        if h is not None:
            for c in clusters:
                if c["hash"] is not None and (h.startswith(c["hash"]) or c["hash"].startswith(h)):
                    match = c
                    break
        if match is None:
            clusters.append({"hash": h, "revision": rev, "releases": [release],
                             "total": total, "healthy": healthy,
                             "users": users, "healthy_users": healthy_users,
                             "dur_sum": 0.0, "dur_n": 0, "ph_start": 0, "ph_end": 0,
                             "pics": 0, "crash_sec": 0.0, "crash_n": 0, "crash_pics": 0})
        else:
            # keep the longest (most specific) hash as the cluster key
            if h is not None and (match["hash"] is None or len(h) > len(match["hash"])):
                match["hash"] = h
            if rev and not match["revision"]:
                match["revision"] = rev
            match["releases"].append(release)
            match["total"] += total
            match["healthy"] += healthy
            match["users"] += users
            match["healthy_users"] += healthy_users

    # Join PostHog (session length + start/end counts) onto each commit cluster by
    # prefix, and cross-validate session counts against Sentry. dur_sum/dur_n drive
    # the average session length and the time-based MTBF.
    g_dur_sum = 0.0
    g_dur_n = 0
    for c in clusters:
        if not c["hash"]:
            continue
        for r in posthog_rows:
            if r["hash"].startswith(c["hash"]) or c["hash"].startswith(r["hash"]):
                c["dur_sum"] += r["dur_sum"]
                c["dur_n"] += r["dur_n"]
                c["ph_start"] += r["n_start"]
                c["ph_end"] += r["n_end"]
                c["pics"] += r["pics"]
                # Keep the revision number (from app_version) as metadata even when
                # the Sentry release is a bare commit SHA, so the label survives the
                # move to commit-only aggregation / shallow-clone builds.
                if r.get("revision") and not c["revision"]:
                    c["revision"] = r["revision"]
        g_dur_sum += c["dur_sum"]
        g_dur_n += c["dur_n"]
        # Time-to-crash (MTBF) and images-before-crash from this commit's crashes.
        for r in crash_rows:
            if r["hash"].startswith(c["hash"]) or c["hash"].startswith(r["hash"]):
                c["crash_sec"] += r["sec_sum"]
                c["crash_n"] += r["sec_n"]
                c["crash_pics"] += r["pics_sum"]
        if c["ph_start"] > 0:
            tag = ("r%s" % c["revision"]) if c["revision"] else c["hash"][:7]
            sentry_cf = (c["healthy"] / c["total"] * 100.0) if c["total"] else 0.0
            ph_completed = c["ph_end"] / c["ph_start"] * 100.0
            warn("cross-check %s: Sentry %d sessions / %.1f%% crash-free  vs  "
                 "PostHog %d starts / %d ends (%.1f%% completed cleanly)"
                 % (tag, c["total"], sentry_cf, c["ph_start"], c["ph_end"], ph_completed))

    global_rate = (g_healthy / g_total * 100.0) if g_total > 0 else 0.0
    global_total = int(round(g_total))

    # Only statistically meaningful revisions (used by enough distinct people),
    # most-active first, capped for readability.
    shown = [c for c in clusters if c["users"] >= MIN_USERS]
    shown.sort(key=lambda c: c["total"], reverse=True)
    shown = shown[:MAX_RELEASES]

    # Display order: by release number (revision count), so the x-axis reads
    # oldest -> newest left to right. Releases without a revision number (pure-SHA
    # builds) trail at the end.
    def _order_key(c):
        rev = c.get("revision")
        return (rev is None, int(rev) if rev else 0)
    shown.sort(key=_order_key)

    # Fold everything that didn't make the cut (below the session threshold, beyond
    # the MAX_RELEASES cap, or not tied to a release - intermediate commits, test
    # events) into a single "Other" entry kept last on the x-axis. Counts are
    # additive; note "Other" users sum count_unique across releases, so a user
    # active in several minor releases can be counted more than once there.
    shown_ids = {id(c) for c in shown}
    other = [c for c in clusters if id(c) not in shown_ids]
    if other:
        _keys = ("total", "healthy", "users", "healthy_users", "dur_sum", "dur_n",
                 "ph_start", "ph_end", "pics", "crash_sec", "crash_n", "crash_pics")
        agg = {k: sum(c[k] for c in other) for k in _keys}

        def _member(c):
            if c["hash"]:
                return "g%s" % c["hash"][:12]   # commit hash (abbreviated)
            if c["revision"]:
                return "r%s" % c["revision"]
            return _strip(c["releases"][0])
        members = sorted(_member(c) for c in other)
        # wrap the list a few per line so the hover stays readable
        members_str = "<br>".join(", ".join(members[i:i + 5])
                                  for i in range(0, len(members), 5))

        agg.update({"is_other": True, "n_releases": len(other), "members": members_str,
                    "hash": None, "revision": None, "releases": []})
        shown.append(agg)

    packaged = packaged_hashes or set()

    def label(c):
        # Aggregate by commit hash: label every revision by its abbreviated SHA so
        # the x-axis is consistent (no mix of revision numbers and hashes). An
        # asterisk marks commits that we shipped as a packaged nightly/stable build.
        if c.get("is_other"):
            return "Other"
        if c["hash"]:
            star = "*" if _is_packaged(c["hash"], packaged) else ""
            return c["hash"][:7] + star
        return _strip(c["releases"][0])

    def name(c):
        if c.get("is_other"):
            return "Other (%d releases)" % c["n_releases"]
        if c["hash"]:
            star = " ★ packaged build" if _is_packaged(c["hash"], packaged) else ""
            if c["revision"]:
                return "g%s (r%s)%s" % (c["hash"][:7], c["revision"], star)
            return "g%s%s" % (c["hash"][:7], star)
        return _strip(c["releases"][0])

    labels = [label(c) for c in shown]
    # Soft pastel palette: low-saturation sage / blush for crash-free vs crashed.
    # The secondary-axis line is near-black and bold so it stays legible over the
    # pastel bars it overlaps.
    GREEN, RED, ACCENT = "#8ec1a8", "#e8a598", "#222222"

    def _stacked_figure(healthy, crashed, ratio_text, hover_h, hover_c, count_title,
                        sec_y, sec_hover, sec_name, sec_axis_title, sec_suffix, title):
        # Absolute counts as stacked bars (left axis); the per-release ratio is the
        # in-bar label. An optional secondary metric (a COUNT or time) is drawn as a
        # line on the right axis - and dropped entirely (axis + legend) when it has
        # no data, so we never show an empty series.
        has_sec = any(v is not None for v in sec_y)
        data = [
            {"type": "bar", "x": labels, "y": healthy, "name": "Crash-free",
             "text": ratio_text, "textposition": "inside", "insidetextanchor": "middle",
             "hovertext": hover_h, "hoverinfo": "text", "marker": {"color": GREEN}},
            {"type": "bar", "x": labels, "y": crashed, "name": "Crashed",
             "hovertext": hover_c, "hoverinfo": "text", "marker": {"color": RED}},
        ]
        if has_sec:
            data.append(
                {"type": "scatter", "mode": "lines+markers", "x": labels, "y": sec_y,
                 "yaxis": "y2", "name": sec_name, "hovertext": sec_hover,
                 "hoverinfo": "text", "connectgaps": False,
                 "marker": {"color": ACCENT, "size": 9,
                            "line": {"color": "#ffffff", "width": 1}},
                 "line": {"color": ACCENT, "width": 3}})
        # Account for title line wrap (manual)
        n_lines = title.count("<br") + 1
        layout = {
            "title": {"text": title},
            "barmode": "stack",
            "xaxis": {"title": {"text": "Revision"}, "type": "category"},
            "yaxis": {"title": {"text": count_title}, "rangemode": "tozero"},
            "legend": {"orientation": "h", "x": 0, "y": 1.10},
            "margin": {"t": 60 * n_lines, "r": 70 if has_sec else 30, "b": 60, "l": 60},
            "showlegend": True,
        }
        if has_sec:
            layout["yaxis2"] = {"title": {"text": sec_axis_title}, "overlaying": "y",
                                "side": "right", "rangemode": "tozero",
                                "ticksuffix": sec_suffix, "showgrid": False}
        return {"data": data, "layout": layout}

    # ---------- Figure 1: SESSIONS (counts + ratio text, MTBF line) ----------
    s_healthy, s_crashed, s_text, s_hh, s_hc = [], [], [], [], []
    mtbf_min, mtbf_hover = [], []
    for c in shown:
        total = c["total"]
        healthy = int(round(c["healthy"]))
        crashed = max(0, total - healthy)
        ratio = (healthy / total * 100.0) if total else 0.0
        s_healthy.append(healthy)
        s_crashed.append(crashed)
        s_text.append("%.0f%%" % ratio if total else "")
        hh = "%s<br>%d crash-free / %d sessions (%.1f%%)" % (name(c), healthy, total, ratio)
        avg_len = (c["dur_sum"] / c["dur_n"]) if c["dur_n"] else None
        if avg_len:
            hh += "<br>avg session: %s" % _fmt_duration(avg_len)
        if c.get("is_other"):
            hh += "<br><i>⚠ minor / intermediate commits — likely development or pre-release builds</i>"
            hh += "<br>aggregated commits:<br>%s" % c["members"]
        s_hh.append(hh)
        s_hc.append("%s<br>%d crashed sessions" % (name(c), crashed))
        if c["crash_n"]:
            sec = c["crash_sec"] / c["crash_n"]
            mtbf_min.append(round(sec / 60.0, 3))
            mtbf_hover.append("%s<br>MTBF %s<br>(mean uptime before crash, n=%d)"
                              % (name(c), _fmt_duration(sec), c["crash_n"]))
        else:
            mtbf_min.append(None)
            mtbf_hover.append("%s<br>no timed crash" % name(c))

    g_avg_len = (g_dur_sum / g_dur_n) if g_dur_n else None
    sessions_title = ("Sessions per revision (%s)<br />%.1f%% crash-free over %d sessions"
                      % (span_label, global_rate, global_total))
    sessions_figure = _stacked_figure(
        s_healthy, s_crashed, s_text, s_hh, s_hc, "Sessions",
        mtbf_min, mtbf_hover, "MTBF (uptime before crash)",
        "MTBF: mean uptime before crash (min)", " min", sessions_title)

    # ---------- Figure 2: USERS (counts + ratio text, pictures-edited line) ----------
    u_healthy, u_crashed, u_text, u_hh, u_hc = [], [], [], [], []
    pics_y, pics_hover = [], []
    for c in shown:
        u = c["users"]
        hu = int(round(c["healthy_users"]))
        cu = max(0, u - hu)
        ur = (hu / u * 100.0) if u else 0.0
        u_healthy.append(hu)
        u_crashed.append(cu)
        u_text.append("%.0f%%" % ur if u else "")
        uh = ("%s<br>%d crash-free / %d users (%.1f%%)" % (name(c), hu, u, ur)
              if u else "%s<br>no user data" % name(c))
        if c.get("is_other"):
            uh += "<br><i>⚠ minor / intermediate commits — likely development or pre-release builds</i>"
            uh += "<br>aggregated commits:<br>%s" % c["members"]
        u_hh.append(uh)
        u_hc.append("%s<br>%d users hit a crash" % (name(c), cu))
        total_pics = c["pics"] + c["crash_pics"]
        if c["ph_end"] > 0 or c["crash_pics"] > 0:
            pics_y.append(total_pics)
            pics_hover.append("%s<br>%d pictures edited<br>(%d clean + %d before a crash)"
                              % (name(c), total_pics, c["pics"], c["crash_pics"]))
        else:
            pics_y.append(None)
            pics_hover.append("%s<br>no image data yet" % name(c))

    # Global unique-user counts: use the deduplicated project-wide figures when
    # available (count_unique over all releases), since summing per-release uniques
    # double-counts a user who ran more than one release. Fall back to the sum.
    if global_users:
        g_users, g_healthy_users = global_users
    else:
        g_users = sum(c["users"] for c in shown)
        g_healthy_users = sum(c["healthy_users"] for c in shown)
    g_user_rate = (g_healthy_users / g_users * 100.0) if g_users else 0.0
    users_title = ("Users per revision (%s)<br />%.1f%% crash-free over %d unique users"
                   % (span_label, g_user_rate, int(round(g_users))))
    users_figure = _stacked_figure(
        u_healthy, u_crashed, u_text, u_hh, u_hc, "Users",
        pics_y, pics_hover, "Pictures edited",
        "Pictures edited (count)", "", users_title)

    return sessions_figure, users_figure, len(shown), global_total


def main():
    token = get_token()
    ph_key = get_posthog_key()
    os.makedirs(os.path.join(REPO_ROOT, "assets"), exist_ok=True)

    # "How is Ansel used?" charts come from PostHog alone, so build them regardless
    # of whether Sentry (reliability) is available.
    if ph_key:
        try:
            write_usage_figures(ph_key)
        except Exception as exc:  # noqa: BLE001
            warn("usage figures failed (%s); keeping placeholders." % exc)
        try:
            write_platform_figures(ph_key)
        except Exception as exc:  # noqa: BLE001
            warn("platform figures failed (%s); keeping placeholders." % exc)
    else:
        warn("no PostHog key (POSTHOG_QUERY_KEY / .posthog-auth); usage figures skipped.")

    # Bug-report progress from GitHub (independent of everything above), and the
    # commit hashes of our packaged builds (to flag them on the reliability chart).
    gh_token = _read_token("GITHUB_TOKEN", ".github-auth")
    packaged_hashes = set()
    if gh_token:
        try:
            write_bugs_figure(gh_token)
        except Exception as exc:  # noqa: BLE001
            warn("bug figure failed (%s); keeping placeholder." % exc)
        try:
            packaged_hashes = fetch_packaged_hashes(gh_token)
            warn("packaged builds: %d commit hashes from the last 2 releases."
                 % len(packaged_hashes))
        except Exception as exc:  # noqa: BLE001
            warn("packaged-hash lookup failed (%s); no asterisks." % exc)
    else:
        warn("no GitHub token (GITHUB_TOKEN / .github-auth); bug figure skipped.")

    if not token:
        warn("no Sentry token (set SENTRY_AUTH_TOKEN or add .sentry-auth-perso); "
             "skipping reliability chart.")
        return 0

    try:
        payload = fetch_groups(token)
    except Exception as exc:  # noqa: BLE001 - best effort, never break the build
        warn("Sentry request failed (%s); skipping reliability chart." % exc)
        return 0
    groups = payload.get("groups", [])

    # Earliest data point, to label the chart with the ACTUAL window rather than the
    # full query period (which is misleading early on). Day precision from Sentry
    # sessions, refined to the exact timestamp by crash events / PostHog when present.
    span_starts = [sentry_first_session(payload)]

    # Per-commit time-to-crash (MTBF = mean uptime before a crash) from crash events.
    crash_rows = []
    try:
        crash_rows, crash_first = fetch_crash_times(token)
        span_starts.append(crash_first)
    except Exception as exc:  # noqa: BLE001
        warn("Sentry crash-times request failed (%s); MTBF omitted." % exc)

    # Optional second source: PostHog, for session length / time-based MTBF that
    # Sentry can't provide. Missing key or failure just omits those metrics.
    posthog_rows = []
    if ph_key:
        try:
            posthog_rows, ph_first = fetch_posthog(ph_key)
            span_starts.append(ph_first)
        except Exception as exc:  # noqa: BLE001
            warn("PostHog request failed (%s); session length omitted." % exc)

    span_start = min((t for t in span_starts if t), default=None)
    span_label = _format_span(span_start, datetime.now(timezone.utc))

    try:
        global_users = fetch_global_users(token)
    except Exception as exc:  # noqa: BLE001
        warn("global unique-user query failed (%s); using per-release sum." % exc)
        global_users = None

    figure, users_figure, n_shown, global_total = build_figure(
        groups, posthog_rows, crash_rows, span_label, global_users, packaged_hashes)
    if n_shown == 0:
        warn("no revision meets the >=%d unique-users threshold over %s; "
             "skipping reliability chart." % (MIN_USERS, STATS_PERIOD))
        return 0

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    for path, fig in ((OUT_PATH, figure), (OUT_PATH_USERS, users_figure)):
        with open(path, "w") as f:
            json.dump(fig, f, indent=2)
    print("[reliability] wrote %s and %s (%d releases, %d total sessions)"
          % (OUT_PATH, OUT_PATH_USERS, n_shown, global_total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
