#!/usr/bin/env python3
"""Turn data/download-stats.json into two Plotly figures for the home page.

The series is written by Ansel's nightly CI (tools/download_stats.py there): one snapshot
per day of every lifetime download counter -- GitHub release assets per format and per
build month, Docker Hub pulls. Two figures come out of it, consumed by the existing
{{< plotly src=... dynamic="true" >}} shortcode:

  assets/downloads-monthly.json   downloads per month, all packages
  assets/downloads-formats.json   share of each package format, lifetime

"Per month" is two things stitched together. Before the series starts, the only monthly
signal is the build month of the asset that was downloaded (nightly users download the
current nightly, so it is a fair proxy). From the first snapshot on, the difference
between the last snapshot of one month and the last of the previous is the number of
downloads that actually happened that month, all assets and Docker pulls included, and
that is what is plotted from then on. The caption says so.

No data, or an unreadable file, writes placeholder figures so the build never fails.
"""

import datetime
import json
import os
import sys
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SERIES = os.path.join(ROOT, "data", "download-stats.json")
OUT_MONTHLY = os.path.join(ROOT, "assets", "downloads-monthly.json")
OUT_FORMATS = os.path.join(ROOT, "assets", "downloads-formats.json")

# Colours: the soft pastel colorway every other chart on the site uses, imported from
# the script that draws them so the two cannot drift apart.
import importlib.util as _ilu
_spec = _ilu.spec_from_file_location("reliability", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fetch-sentry-reliability.py"))
_rel = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_rel)
PALETTE = _rel.PALETTE

LABELS = {
    "appimage": "Linux AppImage", "flatpak": "Linux Flatpak", "exe": "Windows installer",
    "dmg-arm64": "macOS (Apple Silicon)", "dmg-i386": "macOS (Intel)",
    "docker": "Docker (pulls)", "docker-archive": "Docker (archive)", "zsync": "AppImage updater (zsync)",
    "other": "other",
}
FORMAT_ORDER = ["exe", "appimage", "dmg-arm64", "dmg-i386", "flatpak", "docker", "docker-archive", "other"]
COLORS = {k: PALETTE[i % len(PALETTE)] for i, k in enumerate(FORMAT_ORDER)}

LAYOUT = {
    "paper_bgcolor": "rgba(0,0,0,0)", "plot_bgcolor": "rgba(0,0,0,0)",
    "margin": {"l": 50, "r": 20, "t": 30, "b": 60},
    "legend": {"orientation": "h", "y": -0.25},
}


def placeholder(text):
    return {"data": [], "layout": {**LAYOUT, "annotations": [{"text": text, "showarrow": False, "xref": "paper", "yref": "paper", "x": 0.5, "y": 0.5}]}}


def write(path, fig):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(fig, f, separators=(",", ":"))


MONTHS_SHOWN = 12
# GitHub asset name suffix -> format key, as in the stats collector.
SUFFIXES = [("-x86_64.AppImage", "appimage"), ("-x86_64.flatpak", "flatpak"), ("-arm64.dmg", "dmg-arm64"),
            ("-i386.dmg", "dmg-i386"), ("-win64.exe", "exe"), ("-docker.tar.zst", "docker-archive")]
MONTH_TAG = re.compile(r"^nightly-(\d{4}-\d{2})$")


def github_by_month_format(token):
    """{month: {format: lifetime downloads}} by BUILD month, from the release assets.

    The daily series carries per-format totals but not per-month-per-format, so the
    months before the series started can only be attributed by the month the package was
    built -- a fair proxy for nightlies, whose users download the current one. The month
    is the release tag's (nightly-YYYY-MM) when it carries one, else the asset's creation
    date. Best effort: no token or no network yields nothing, and the chart falls back to
    unstacked totals for those months."""
    out = {}
    try:
        page = 1
        while True:
            req = urllib.request.Request("https://api.github.com/repos/aurelienpierreeng/ansel/releases?per_page=100&page=%d" % page,
                                         headers={"Accept": "application/vnd.github+json", "User-Agent": "ansel-website",
                                                  **({"Authorization": "Bearer %s" % token} if token else {})})
            with urllib.request.urlopen(req, timeout=60) as r:
                batch = json.loads(r.read().decode("utf-8"))
            if not batch:
                break
            for rel in batch:
                m = MONTH_TAG.match(rel["tag_name"])
                for a in rel["assets"]:
                    key = next((k for suf, k in SUFFIXES if a["name"].endswith(suf)), None)
                    if not key:
                        continue
                    month = m.group(1) if m else (a.get("created_at") or "")[:7]
                    out.setdefault(month, {}).setdefault(key, 0)
                    out[month][key] += int(a.get("download_count") or 0)
            page += 1
    except Exception as e:  # noqa: BLE001
        print("github: %s (build-month breakdown unavailable)" % e, file=sys.stderr)
    return out


def monthly(series, by_month_format):
    """(months, {format: [value per month]}, note per month) for the last MONTHS_SHOWN.

    From the first snapshot on, a month's downloads per format are the differences of
    the per-format lifetime totals between the last snapshots of consecutive months --
    what actually happened that month -- and Docker Hub pulls the same way. Before the
    series, the build-month attribution above."""
    latest = series[-1]
    first_month = series[0]["date"][:7]
    last_of = {}
    for s in series:
        last_of[s["date"][:7]] = s

    def fmt_totals(s):
        return dict(s["github"].get("by_format") or {})

    def hub(s):
        return ((s.get("docker_hub") or {}).get("pull_count")) or 0

    # The past calendar year, every month present, zero where nothing happened -- not
    # the last twelve months that happen to have data, which spanned four years once the
    # retired release had been pruned down to scattered survivors.
    today = datetime.date.today().replace(day=1)
    months = []
    y, mo = today.year, today.month
    for _ in range(MONTHS_SHOWN):
        months.append("%04d-%02d" % (y, mo))
        mo -= 1
        if mo == 0:
            y, mo = y - 1, 12
    months.reverse()
    formats = [k for k in FORMAT_ORDER if k not in ("docker-archive", "zsync", "other")]
    values = {k: [] for k in formats}
    note = []
    prev = None
    for m in months:
        if m < first_month or m not in last_of:
            src = by_month_format.get(m, {})
            for k in formats:
                values[k].append(src.get(k, 0) if k != "docker" else 0)
            note.append("by build month")
        else:
            cur = last_of[m]
            if prev is None:
                src = by_month_format.get(m, {})
                for k in formats:
                    values[k].append(src.get(k, 0) if k != "docker" else 0)
                note.append("by build month (first month on record)")
            else:
                ct, pt = fmt_totals(cur), fmt_totals(prev)
                for k in formats:
                    if k == "docker":
                        values[k].append(max(hub(cur) - hub(prev), 0))
                    else:
                        values[k].append(max(ct.get(k, 0) - pt.get(k, 0), 0))
                note.append("measured")
            prev = cur
    return months, values, note


def build(series):
    if not series:
        return placeholder("No download statistics yet"), placeholder("No download statistics yet")
    latest = series[-1]

    months, values, note = monthly(series, github_by_month_format(os.environ.get("GITHUB_TOKEN")))
    traces = []
    for k, ys in values.items():
        if not any(ys):
            continue
        traces.append({
            "type": "bar", "x": months, "y": ys, "name": LABELS.get(k, k),
            "marker": {"color": COLORS[k]},
            "hovertemplate": "%{x}: %{y:,} " + LABELS.get(k, k) + "<br>%{customdata}<extra></extra>",
            "customdata": note,
        })
    fig_monthly = {
        "data": traces,
        "layout": {**LAYOUT, "title": {"text": "Downloads per month, past year, by package"}, "margin": {**LAYOUT["margin"], "t": 60},
                   "barmode": "stack", "xaxis": {"type": "category", "title": {"text": "month"}},
                   "yaxis": {"title": {"text": "downloads"}, "rangemode": "tozero"}, "showlegend": True},
    }

    counts = dict(latest["github"]["by_format"])
    hub = (latest.get("docker_hub") or {}).get("pull_count")
    if hub:
        counts["docker"] = hub
    counts.pop("zsync", None)  # updater traffic, not a person choosing a package
    items = [(k, v) for k, v in counts.items() if v > 0]
    items.sort(key=lambda kv: -kv[1])
    fig_formats = {
        "data": [{
            "type": "pie", "labels": [LABELS.get(k, k) for k, _ in items], "values": [v for _, v in items],
            "marker": {"colors": [COLORS.get(k, PALETTE[-1]) for k, _ in items]},
            "textinfo": "label+percent", "hovertemplate": "%{label}: %{value:,} (%{percent})<extra></extra>",
            "sort": False,
        }],
        "layout": {**LAYOUT, "title": {"text": "Share of each package format, all time downloads"}, "margin": {**LAYOUT["margin"], "t": 60}, "showlegend": False},
    }
    return fig_monthly, fig_formats


def main():
    try:
        with open(SERIES, encoding="utf-8") as f:
            series = json.load(f)
        series = [s for s in series if isinstance(s, dict) and "github" in s]
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"download charts: no usable series ({e}); placeholders written", file=sys.stderr)
        series = []
    fig_monthly, fig_formats = build(series)
    write(OUT_MONTHLY, fig_monthly)
    write(OUT_FORMATS, fig_formats)
    print(f"download charts: {len(series)} day(s) of data -> {os.path.relpath(OUT_MONTHLY, ROOT)}, {os.path.relpath(OUT_FORMATS, ROOT)}")


if __name__ == "__main__":
    main()
