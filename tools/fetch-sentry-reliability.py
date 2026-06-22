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
  RELIABILITY_MIN_SESSIONS=25               (drop releases with too few sessions to
                                             be statistically meaningful)
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
OUT_PATH_BUGS = os.path.join(REPO_ROOT, "assets", "bugs.json")

GITHUB_REPO = os.environ.get("GITHUB_REPO", "aurelienpierreeng/ansel")
GITHUB_API = "https://api.github.com"

ORG = os.environ.get("SENTRY_ORG", "aurelienpierreeng")
PROJECT_ID = os.environ.get("SENTRY_PROJECT_ID", "4511598693253200")
HOST = os.environ.get("SENTRY_HOST", "https://de.sentry.io")
POSTHOG_HOST = os.environ.get("POSTHOG_HOST", "https://eu.posthog.com")
POSTHOG_PROJECT_ID = os.environ.get("POSTHOG_PROJECT_ID", "206740")
STATS_PERIOD = os.environ.get("RELIABILITY_STATS_PERIOD", "90d")
MIN_SESSIONS = int(os.environ.get("RELIABILITY_MIN_SESSIONS", "25"))
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


def write_usage_figures(key):
    """Build and write the two "How is Ansel used?" charts (PostHog only)."""
    fl, fv, fh = fetch_file_types(key)
    ml, mv, mh = fetch_modules(key)
    span = _usage_span(key)
    # Grand total of all activations (the bars only show the top features).
    mtot = _posthog_query(key, "SELECT count() FROM events WHERE event = "
                          "'module_used' AND timestamp > now() - INTERVAL %d DAY" % PERIOD_DAYS)
    modules_total = int(mtot[0][0]) if mtot and mtot[0] else sum(mv)
    files_title = ("Image files opened, by type — %d files (%s)"
                   % (sum(fv), span))
    modules_title = ("Most-used features — %d activations (%s)"
                     % (modules_total, span))
    jobs = (
        (OUT_PATH_FILES, fl, _usage_bar_figure(
            fl, fv, fh, files_title, "Files opened", "#8ec1a8")),
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


def _gh_bug_count(token, extra):
    """Count issues of the "Bug" type in the repo matching the extra qualifiers."""
    q = "repo:%s is:issue type:Bug %s" % (GITHUB_REPO, extra)
    url = "%s/search/issues?per_page=1&q=%s" % (GITHUB_API, urllib.parse.quote(q))
    return int(_gh_request(token, url).get("total_count", 0))


def _version_key(title):
    nums = re.findall(r"\d+", title or "")
    return tuple(int(n) for n in nums) if nums else (9999,)


def fetch_github_bugs(token):
    """Bug-fixing progress, bucketed by milestone (+ an "Unscheduled" bucket for
    bugs not yet assigned to one). The next release is the lowest-version open
    milestone, picked dynamically so nothing needs editing per release.

    Returns (rows, total_closed, total_open) where rows is a list of
    (label, fixed, remaining) ordered next-release first, then later milestones,
    then "Unscheduled"; or None if the data can't be fetched."""
    try:
        milestones = _gh_request(
            token, "%s/repos/%s/milestones?state=open&per_page=100" % (GITHUB_API, GITHUB_REPO))
    except Exception as exc:  # noqa: BLE001
        warn("GitHub milestones request failed (%s)." % exc)
        return None
    milestones.sort(key=lambda m: _version_key(m.get("title", "")))

    rows = []
    for i, m in enumerate(milestones):
        title = m.get("title", "?")
        closed = _gh_bug_count(token, 'state:closed milestone:"%s"' % title)
        opened = _gh_bug_count(token, 'state:open milestone:"%s"' % title)
        if closed + opened == 0:
            continue
        label = "%s (next release)" % title if i == 0 else title
        rows.append((label, closed, opened))

    # Bugs not (yet) attached to any milestone - they exist and matter too.
    u_closed = _gh_bug_count(token, "state:closed no:milestone")
    u_open = _gh_bug_count(token, "state:open no:milestone")
    if u_closed + u_open > 0:
        rows.append(("Unscheduled", u_closed, u_open))

    total_closed = _gh_bug_count(token, "state:closed")
    total_open = _gh_bug_count(token, "state:open")
    return rows, total_closed, total_open


def _bugs_figure(rows, total_closed, total_open):
    """Horizontal stacked bars: fixed (green) vs remaining (blush) per bucket."""
    labels = [r[0] for r in rows]
    fixed = [r[1] for r in rows]
    remaining = [r[2] for r in rows]
    hover_f, hover_r = [], []
    for label, f, r in rows:
        tot = f + r
        pct = (100.0 * f / tot) if tot else 0.0
        hover_f.append("%s<br>%d fixed of %d (%.0f%% done)" % (label, f, tot, pct))
        hover_r.append("%s<br>%d still open" % (label, r))
    title = ("Bug reports — %d fixed, %d still open"
             % (total_closed, total_open))
    return {
        "data": [
            {"type": "bar", "orientation": "h", "y": labels, "x": fixed, "name": "Fixed",
             "marker": {"color": "#8ec1a8"}, "text": [str(f) for f in fixed],
             "textposition": "inside", "insidetextanchor": "middle",
             "hovertext": hover_f, "hoverinfo": "text"},
            {"type": "bar", "orientation": "h", "y": labels, "x": remaining, "name": "Remaining",
             "marker": {"color": "#e8a598"}, "text": [str(r) for r in remaining],
             "textposition": "inside", "insidetextanchor": "middle",
             "hovertext": hover_r, "hoverinfo": "text"},
        ],
        "layout": {
            "title": {"text": title},
            "barmode": "stack",
            "xaxis": {"title": {"text": "Bug reports"}, "rangemode": "tozero"},
            "yaxis": {"automargin": True, "autorange": "reversed"},  # next release on top
            "legend": {"orientation": "h", "x": 0, "y": 1.12},
            "margin": {"t": 80, "r": 30, "b": 50, "l": 60},
            "showlegend": True,
        },
    }


def write_bugs_figure(token):
    data = fetch_github_bugs(token)
    if not data or not data[0]:
        warn("no GitHub bug data; keeping bugs placeholder.")
        return
    rows, total_closed, total_open = data
    with open(OUT_PATH_BUGS, "w") as f:
        json.dump(_bugs_figure(rows, total_closed, total_open), f, indent=2)
    print("[bugs] wrote %s (%d fixed, %d open across %d buckets)"
          % (OUT_PATH_BUGS, total_closed, total_open, len(rows)))


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


def build_figure(groups, posthog_rows, crash_rows, span_label):
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

    # Only statistically meaningful, most-active releases, capped for readability.
    shown = [c for c in clusters if c["total"] >= MIN_SESSIONS]
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

    def label(c):
        if c.get("is_other"):
            return "Other"
        if c["revision"]:
            return "r%s" % c["revision"]     # revision count, matches the About box
        if c["hash"]:
            return c["hash"][:7]             # commit SHA, abbreviated
        return _strip(c["releases"][0])

    def name(c):
        if c.get("is_other"):
            return "Other (%d releases)" % c["n_releases"]
        if c["revision"] and c["hash"]:
            return "r%s (g%s)" % (c["revision"], c["hash"][:7])
        if c["hash"]:
            return "g%s" % c["hash"][:7]
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
        layout = {
            "title": {"text": title},
            "barmode": "stack",
            "xaxis": {"title": {"text": "Release"}, "type": "category"},
            "yaxis": {"title": {"text": count_title}, "rangemode": "tozero"},
            "legend": {"orientation": "h", "x": 0, "y": 1.10},
            "margin": {"t": 80, "r": 70 if has_sec else 30, "b": 60, "l": 60},
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
    s_extra = (" · avg session %s" % _fmt_duration(g_avg_len)) if g_avg_len else ""
    sessions_title = ("Sessions per release — global %.1f%% crash-free%s over %d sessions (%s)"
                      % (global_rate, s_extra, global_total, span_label))
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

    g_users = sum(c["users"] for c in shown)
    g_healthy_users = sum(c["healthy_users"] for c in shown)
    g_user_rate = (g_healthy_users / g_users * 100.0) if g_users else 0.0
    users_title = ("Users per release — global %.1f%% crash-free over %d users (%s)"
                   % (g_user_rate, int(round(g_users)), span_label))
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
    else:
        warn("no PostHog key (POSTHOG_QUERY_KEY / .posthog-auth); usage figures skipped.")

    # Bug-report progress from GitHub (independent of everything above).
    gh_token = _read_token("GITHUB_TOKEN", ".github-auth")
    if gh_token:
        try:
            write_bugs_figure(gh_token)
        except Exception as exc:  # noqa: BLE001
            warn("bug figure failed (%s); keeping placeholder." % exc)
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

    figure, users_figure, n_shown, global_total = build_figure(
        groups, posthog_rows, crash_rows, span_label)
    if n_shown == 0:
        warn("no release meets the >=%d sessions threshold over %s; "
             "skipping reliability chart." % (MIN_SESSIONS, STATS_PERIOD))
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
