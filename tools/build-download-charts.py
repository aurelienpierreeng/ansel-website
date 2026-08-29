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


def monthly(series):
    """(months, github, docker, note): downloads per month.

    GitHub: build-month attribution before the series starts, snapshot differences from
    then on. Docker Hub: the public API exposes one lifetime pull_count and nothing per
    month, so its monthly line exists only from the series on -- the difference between
    the last snapshots of two months -- and is 0 before that, honestly."""
    latest = series[-1]
    by_build_month = latest["github"]["by_month"]
    first_month = series[0]["date"][:7]

    last_of = {}
    for s in series:
        last_of[s["date"][:7]] = s

    def gh(s):
        return s["github"]["total"]

    def hub(s):
        return ((s.get("docker_hub") or {}).get("pull_count")) or 0

    months = sorted(set(m for m in by_build_month if m) | set(last_of))
    github, docker, note = [], [], []
    prev = None
    for m in months:
        if m < first_month or m not in last_of:
            github.append(by_build_month.get(m, 0)); docker.append(0); note.append("by build month")
        else:
            cur = last_of[m]
            if prev is None:
                # first month on record: no earlier snapshot to subtract; the build-month
                # count is the best available figure for GitHub, nothing for Docker
                github.append(by_build_month.get(m, 0)); docker.append(0); note.append("by build month (first month on record)")
            else:
                github.append(max(gh(cur) - gh(prev), 0)); docker.append(max(hub(cur) - hub(prev), 0)); note.append("measured")
            prev = cur
    return months, github, docker, note


def build(series):
    if not series:
        return placeholder("No download statistics yet"), placeholder("No download statistics yet")
    latest = series[-1]

    months, github, docker, note = monthly(series)
    fig_monthly = {
        "data": [
            {
                "type": "bar", "x": months, "y": github, "name": "packages (GitHub releases)",
                # one palette colour; the estimate (by build month) is the same hue, lighter
                "marker": {"color": PALETTE[0], "opacity": [1.0 if n == "measured" else 0.55 for n in note]},
                "hovertemplate": "%{x}: %{y:,} package downloads<br>%{customdata}<extra></extra>",
                "customdata": note,
            },
            {
                "type": "bar", "x": months, "y": docker, "name": "Docker Hub pulls",
                "marker": {"color": PALETTE[2]},
                "hovertemplate": "%{x}: %{y:,} Docker pulls<extra></extra>",
            },
        ],
        "layout": {**LAYOUT, "barmode": "stack", "xaxis": {"type": "category", "title": {"text": "month"}},
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
        "layout": {**LAYOUT, "showlegend": False},
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
