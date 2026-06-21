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
    for rel, n_start, n_end, dur_sum, dur_n, ts in results:
        h = _commit_hash(rel) if rel else None
        if not h:
            continue
        rows.append({"hash": h, "n_start": int(n_start or 0), "n_end": int(n_end or 0),
                     "dur_sum": float(dur_sum or 0.0), "dur_n": int(dur_n or 0)})
        t = _parse_ts(ts) if isinstance(ts, str) else None
        if t and (first_ts is None or t < first_ts):
            first_ts = t
    return rows, first_ts


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
    """Per-commit time-to-crash from Sentry crash events.

    MTBF here is the mean uptime before a crash: the length of the sessions that
    ended in a crash. Ansel stamps that on every crash event as the session_seconds
    tag (see _sentry_stamp_session_length in sentry.c). We read the raw events,
    canonicalize the release to a commit hash, and return rows to aggregate.

    Returns (rows, first_ts) with rows [{"hash", "sec_sum", "n"}] and the earliest
    crash timestamp seen (for the data span).
    """
    rows = []
    first_ts = None
    base = "%s/api/0/organizations/%s/events/" % (HOST, ORG)
    params = [
        ("project", PROJECT_ID),
        ("field", "release"),
        ("field", "session_seconds"),
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
            h = _commit_hash(ev.get("release") or "")
            try:
                sec = float(ev.get("session_seconds"))
            except (TypeError, ValueError):
                continue
            if h and sec > 0:
                rows.append({"hash": h, "sec_sum": sec, "n": 1})
            t = _parse_ts(ev.get("timestamp"))
            if t and (first_ts is None or t < first_ts):
                first_ts = t
        # Follow pagination only while the next page reports results.
        cursor = None
        for part in link.split(","):
            if 'rel="next"' in part and 'results="true"' in part:
                m = re.search(r'cursor="([^"]+)"', part)
                if m:
                    cursor = m.group(1)
        if not cursor:
            break
    return rows, first_ts


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
        total = int(total)
        healthy = total * float(rate)
        g_total += total
        g_healthy += healthy

        h = _commit_hash(release)
        rev = _revision(release)

        match = None
        if h is not None:
            for c in clusters:
                if c["hash"] is not None and (h.startswith(c["hash"]) or c["hash"].startswith(h)):
                    match = c
                    break
        if match is None:
            clusters.append({"hash": h, "revision": rev, "releases": [release],
                             "total": total, "healthy": healthy,
                             "dur_sum": 0.0, "dur_n": 0, "ph_start": 0, "ph_end": 0,
                             "crash_sec": 0.0, "crash_n": 0})
        else:
            # keep the longest (most specific) hash as the cluster key
            if h is not None and (match["hash"] is None or len(h) > len(match["hash"])):
                match["hash"] = h
            if rev and not match["revision"]:
                match["revision"] = rev
            match["releases"].append(release)
            match["total"] += total
            match["healthy"] += healthy

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
        g_dur_sum += c["dur_sum"]
        g_dur_n += c["dur_n"]
        # Time-to-crash (MTBF) from the crash events of this commit.
        for r in crash_rows:
            if r["hash"].startswith(c["hash"]) or c["hash"].startswith(r["hash"]):
                c["crash_sec"] += r["sec_sum"]
                c["crash_n"] += r["n"]
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

    def label(c):
        if c["revision"]:
            return "r%s" % c["revision"]     # revision count, matches the About box
        if c["hash"]:
            return c["hash"][:7]             # commit SHA, abbreviated
        return _strip(c["releases"][0])

    def name(c):
        if c["revision"] and c["hash"]:
            return "r%s (g%s)" % (c["revision"], c["hash"][:7])
        if c["hash"]:
            return "g%s" % c["hash"][:7]
        return _strip(c["releases"][0])

    labels = [label(c) for c in shown]
    rates = [round(c["healthy"] / c["total"] * 100.0, 2) for c in shown]
    healthy_counts = [int(round(c["healthy"])) for c in shown]
    totals = [c["total"] for c in shown]
    hover = []
    for c, hc, tt, rt in zip(shown, healthy_counts, totals, rates):
        line = "%s<br>%.2f%% crash-free<br>%d / %d sessions" % (name(c), rt, hc, tt)
        avg_len = (c["dur_sum"] / c["dur_n"]) if c["dur_n"] else None
        if avg_len:
            line += "<br>avg session: %s" % _fmt_duration(avg_len)
        # MTBF = mean uptime before a crash: average of the session length that led
        # to each crash (session_seconds stamped on the crash events).
        if c["crash_n"]:
            line += "<br>MTBF: %s (avg uptime before crash, n=%d)" % (
                _fmt_duration(c["crash_sec"] / c["crash_n"]), c["crash_n"])
        elif (c["total"] - c["healthy"]) >= 0.5:
            line += "<br>MTBF: n/a (crashes not timed)"   # crashed, but pre-instrumentation
        else:
            line += "<br>MTBF: no crash yet"
        if len(c["releases"]) > 1:
            line += "<br>(merged %d release names)" % len(c["releases"])
        hover.append(line)
    bar_text = ["%d/%d" % (h, t) for h, t in zip(healthy_counts, totals)]

    # MTBF series for the secondary axis: mean uptime before a crash, in minutes.
    # None (gap) where a release has no timed crash, so the line skips it.
    mtbf_min = []
    mtbf_hover = []
    for c in shown:
        if c["crash_n"]:
            sec = c["crash_sec"] / c["crash_n"]
            mtbf_min.append(round(sec / 60.0, 3))
            mtbf_hover.append("%s<br>MTBF %s<br>(avg uptime before crash, n=%d)"
                              % (name(c), _fmt_duration(sec), c["crash_n"]))
        else:
            mtbf_min.append(None)
            mtbf_hover.append("%s<br>no timed crash" % name(c))

    y_floor = 0
    if rates:
        y_floor = max(0, int(min(rates)) - 5)

    # Global summary for the title (no MTBF here - MTBF is per-release, it is the
    # uptime before a crash and is not meaningful averaged across the whole line).
    g_avg_len = (g_dur_sum / g_dur_n) if g_dur_n else None
    g_parts = ["global %.1f%% crash-free" % global_rate]
    if g_avg_len:
        g_parts.append("avg session %s" % _fmt_duration(g_avg_len))
    global_summary = " · ".join(g_parts)

    title = (
        "Crash-free sessions per release — %s over %d sessions (%s)"
        % (global_summary, global_total, span_label)
    )

    data = [
        {
            "type": "bar",
            "x": labels,
            "y": rates,
            "text": bar_text,
            "textposition": "auto",
            "hovertext": hover,
            "hoverinfo": "text",
            "marker": {
                "color": rates,
                "colorscale": "RdYlGn",
                "cmin": max(0, y_floor),
                "cmax": 100,
                "showscale": False,
            },
            "name": "Crash-free %",
        },
        {
            "type": "scatter",
            "mode": "lines+markers",
            "x": labels,
            "y": mtbf_min,
            "yaxis": "y2",
            "connectgaps": False,
            "hovertext": mtbf_hover,
            "hoverinfo": "text",
            "marker": {"color": "#1f3a5f", "size": 8},
            "line": {"color": "#1f3a5f", "width": 1.5, "dash": "dot"},
            "name": "MTBF (uptime before crash)",
        },
    ]

    layout = {
        "title": {"text": title},
        "xaxis": {"title": {"text": "Release"}, "type": "category"},
        "yaxis": {
            "title": {"text": "Crash-free sessions (%)"},
            "range": [y_floor, 100],
            "ticksuffix": "%",
        },
        "yaxis2": {
            "title": {"text": "MTBF: mean uptime before crash (min)"},
            "overlaying": "y",
            "side": "right",
            "rangemode": "tozero",
            "showgrid": False,
            "ticksuffix": " min",
        },
        "legend": {"orientation": "h", "x": 0, "y": 1.08},
        "shapes": [
            {
                "type": "line",
                "xref": "paper",
                "x0": 0,
                "x1": 1,
                "yref": "y",
                "y0": global_rate,
                "y1": global_rate,
                "line": {"color": "#444", "width": 1.5, "dash": "dash"},
            }
        ],
        "annotations": [
            {
                "xref": "paper",
                "yref": "y",
                "x": 1,
                "y": global_rate,
                "xanchor": "right",
                "yanchor": "bottom",
                "text": "global %.1f%%" % global_rate,
                "showarrow": False,
            }
        ],
        "margin": {"t": 70, "r": 70, "b": 60, "l": 60},
        "showlegend": True,
    }

    return {"data": data, "layout": layout}, len(shown), global_total


def main():
    token = get_token()
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
    ph_key = get_posthog_key()
    if ph_key:
        try:
            posthog_rows, ph_first = fetch_posthog(ph_key)
            span_starts.append(ph_first)
        except Exception as exc:  # noqa: BLE001
            warn("PostHog request failed (%s); session length omitted." % exc)
    else:
        warn("no PostHog key (POSTHOG_QUERY_KEY / .posthog-auth); session length omitted.")

    span_start = min((t for t in span_starts if t), default=None)
    span_label = _format_span(span_start, datetime.now(timezone.utc))

    figure, n_shown, global_total = build_figure(groups, posthog_rows, crash_rows, span_label)
    if n_shown == 0:
        warn("no release meets the >=%d sessions threshold over %s; "
             "skipping reliability chart." % (MIN_SESSIONS, STATS_PERIOD))
        return 0

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(figure, f, indent=2)
    print("[reliability] wrote %s (%d releases, %d total sessions)"
          % (OUT_PATH, n_shown, global_total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
