#!/usr/bin/env python3
"""data/releases.json for the /download page: the last builds of every package format,
each with its date, commit, download link, crash rate and how many people tested it.

Sources, in the order they are joined:
  GitHub releases   the assets themselves, newest-first per format by the commit count in
                    the filename ("+4833"). The date and the full SHA come from the COMMIT
                    the hash names, not from the asset: an asset moved between releases is
                    created anew on the day it was moved.
  Sentry            crash-free sessions and unique users per release, over the last 90 days,
                    matched to the asset by commit-hash prefix (Sentry knows the same build
                    under several release names, all carrying the hash).
  PostHog           unique users per commit over the same window (opt-in telemetry).

Tokens are optional: without GITHUB_TOKEN the API is rate-limited but works; without the
Sentry / PostHog keys those columns are null and the page shows a dash.
"""
import datetime
import importlib.util
import json
import os
import re
import sys
import urllib.parse
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "data", "releases.json")
REPO = "aurelienpierreeng/ansel"
API = "https://api.github.com"
PER_FORMAT = 15
TAG_RE = re.compile(r"^(nightly-\d{4}-\d{2}|v0\.0\.0)$")
FORMATS = [  # key, label, filename suffix
    ("appimage", "Linux AppImage", "-x86_64.AppImage"),
    ("flatpak", "Linux Flatpak", "-x86_64.flatpak"),
    ("exe", "Windows installer", "-win64.exe"),
    ("dmg-arm64", "macOS, Apple Silicon", "-arm64.dmg"),
    ("dmg-i386", "macOS, Intel", "-i386.dmg"),
    ("docker", "Docker image", "-docker.tar.zst"),
]
VERSION_RE = re.compile(r"^[Aa]nsel-(?P<version>[0-9][^-]*?\+(?P<n>\d+)\.g(?P<hash>[0-9a-f]+))-")

# The Sentry/PostHog helpers live in the reliability script; import it rather than copy.
_spec = importlib.util.spec_from_file_location("reliability", os.path.join(ROOT, "tools", "fetch-sentry-reliability.py"))
rel = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(rel)


def gh(url, token):
    req = urllib.request.Request(url, headers={"Accept": "application/vnd.github+json", "User-Agent": "ansel-website",
                                               **({"Authorization": "Bearer %s" % token} if token else {})})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def github_assets(token):
    """{format: [asset dict, ...]} newest-first by commit count, at most PER_FORMAT each."""
    releases = []
    page = 1
    while True:
        batch = gh("%s/repos/%s/releases?per_page=100&page=%d" % (API, REPO, page), token)
        if not batch:
            break
        releases += [r for r in batch if TAG_RE.match(r["tag_name"]) and not r["draft"]]
        page += 1
    rows = {k: [] for k, _, _ in FORMATS}
    for r in releases:
        for a in r["assets"]:
            m = VERSION_RE.match(a["name"])
            if not m:
                continue
            for key, _, suffix in FORMATS:
                if a["name"].endswith(suffix):
                    rows[key].append({"name": a["name"], "url": a["browser_download_url"], "size": a["size"],
                                      "release": r["tag_name"], "version": m.group("version"),
                                      "n": int(m.group("n")), "hash": m.group("hash"), "downloads": a.get("download_count", 0)})
    for key in rows:
        rows[key].sort(key=lambda x: -x["n"])
        rows[key] = rows[key][:PER_FORMAT]
    return rows


def commit_info(hashes, token):
    """{short hash: {"sha", "date"}} -- one call per distinct commit, tolerant of misses."""
    out = {}
    for h in sorted(set(hashes)):
        try:
            c = gh("%s/repos/%s/commits/%s" % (API, REPO, h), token)
            out[h] = {"sha": c["sha"], "date": c["commit"]["committer"]["date"][:10]}
        except Exception as e:  # noqa: BLE001
            print("commit %s: %s" % (h, e), file=sys.stderr)
    return out


def bucket(table, h, new):
    """The entry for commit hash h, merging prefix-related keys into one.

    One build is named several ways -- a full 40-char SHA in one source, the ten
    characters from the filename in another, seven in a third -- and every name of one
    commit is a prefix of the longest. Keyed naively they split the build's numbers
    across entries, and a prefix lookup then returns whichever came first (the first
    version of this script did, and reported a build's testers on one platform only).
    The longest name becomes the key; shorter ones fold into it."""
    for k in list(table):
        if k.startswith(h) or h.startswith(k):
            if len(h) > len(k):
                table[h] = table.pop(k)
                return table[h]
            return table[k]
    table[h] = new
    return new


def sentry_by_hash(token):
    """{hash prefix: {"crash_free": float|None, "users": int}} aggregated over release names."""
    if not token:
        return {}
    try:
        payload = rel.fetch_groups(token)
    except Exception as e:  # noqa: BLE001
        print("sentry: %s" % e, file=sys.stderr)
        return {}
    out = {}
    for grp in payload.get("groups", []):
        release = (grp.get("by") or {}).get("release")
        h = rel._commit_hash(release) if release else None
        if not h:
            continue
        t = grp.get("totals") or {}
        sessions = int(t.get("sum(session)") or 0)
        rate = t.get("crash_free_rate(session)")
        users = int(t.get("count_unique(user)") or 0)
        cur = bucket(out, h, {"sessions": 0, "healthy": 0.0, "users": 0})
        cur["sessions"] += sessions
        cur["healthy"] += sessions * float(rate) if rate is not None else 0.0
        cur["users"] += users
    return {h: {"crash_free": (v["healthy"] / v["sessions"]) if v["sessions"] else None,
                "sessions": v["sessions"], "users": v["users"]} for h, v in out.items()}


# The app reports `os` as the platform's pretty name ("Windows 11", "macOS 15.6", a
# Linux distribution's name). A package format is one platform, so testers are counted
# on the platform the package runs on; the two macOS packages share one count, since no
# architecture is reported.
def platform_of(os_name):
    o = (os_name or "").lower()
    if o.startswith("windows"):
        return "windows"
    if o.startswith("macos") or o.startswith("mac os") or "darwin" in o:
        return "macos"
    return "linux"


PLATFORM_OF_FORMAT = {"appimage": "linux", "flatpak": "linux", "docker": "linux",
                      "exe": "windows", "dmg-arm64": "macos", "dmg-i386": "macos"}


def posthog_by_hash(key):
    """{hash: {"linux": n, "windows": n, "macos": n, "all": n}} distinct users per commit."""
    if not key:
        return {}
    hogql = ("SELECT coalesce(properties.commit, properties.app_version) AS r, toString(properties.os) AS o, "
             "count(DISTINCT distinct_id) AS u "
             "FROM events WHERE event = 'session_start' AND timestamp > now() - INTERVAL %d DAY "
             "AND isNotNull(coalesce(properties.commit, properties.app_version)) GROUP BY r, o" % rel.PERIOD_DAYS)
    try:
        rows = rel._posthog_query(key, hogql)
    except Exception as e:  # noqa: BLE001
        print("posthog: %s" % e, file=sys.stderr)
        return {}
    out = {}
    for r, o, u in rows:
        h = rel._commit_hash(str(r))
        if not h:
            continue
        cur = bucket(out, h, {"linux": 0, "windows": 0, "macos": 0, "all": 0})
        cur[platform_of(str(o))] += int(u or 0)
        cur["all"] += int(u or 0)
    return out


def lookup(table, h):
    """Prefix match either way: the asset carries ten hex chars, Sentry seven to forty."""
    for k, v in table.items():
        if k.startswith(h) or h.startswith(k):
            return v
    return None


def main():
    gh_token = os.environ.get("GITHUB_TOKEN") or None
    rows = github_assets(gh_token)
    commits = commit_info([a["hash"] for v in rows.values() for a in v], gh_token)
    sentry = sentry_by_hash(rel.get_token())
    posthog = posthog_by_hash(rel.get_posthog_key())
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "window_days": rel.PERIOD_DAYS, "formats": []}
    for key, label, _ in FORMATS:
        items = []
        for a in rows[key]:
            c = commits.get(a["hash"], {})
            s = lookup(sentry, a["hash"]) or {}
            p = lookup(posthog, a["hash"]) or {}
            # Sentry knows the build, not the package: crash-free and its user count
            # cover every platform of this commit. PostHog knows the platform, so the
            # testers column is the count on the platform this package runs on.
            items.append({**a, "sha": c.get("sha"), "date": c.get("date"),
                          "crash_free": s.get("crash_free"), "sessions": s.get("sessions"),
                          "testers": p.get(PLATFORM_OF_FORMAT[key]) if p else None,
                          "testers_all_platforms": max([x for x in (s.get("users"), p.get("all")) if x] or [0]) or None})
        out["formats"].append({"key": key, "label": label, "builds": items})
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("releases: " + ", ".join("%s %d" % (f["key"], len(f["builds"])) for f in out["formats"]))


if __name__ == "__main__":
    main()
