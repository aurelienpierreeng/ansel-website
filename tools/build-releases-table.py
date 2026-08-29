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


PLATFORMS = ("linux", "windows", "macos")


def platform_of_environment(env):
    """The platform an environment name ends with, or None for the bare channel.

    The app names its Sentry environment "<channel>-<platform>" (nightly-windows,
    package-fedora-linux); sessions from before that carry the bare channel. A channel
    can contain hyphens, so the platform is whatever follows the LAST one."""
    tail = (env or "").rsplit("-", 1)[-1].lower()
    return tail if tail in PLATFORMS else None


def _sentry_sessions(token):
    """Sessions grouped by release AND environment over the reliability window."""
    params = [("project", rel.PROJECT_ID), ("field", "sum(session)"), ("field", "crash_free_rate(session)"),
              ("field", "count_unique(user)"), ("groupBy", "release"), ("groupBy", "environment"),
              ("statsPeriod", rel.STATS_PERIOD), ("interval", "1d")]
    url = "%s/api/0/organizations/%s/sessions/?%s" % (rel.HOST, rel.ORG, urllib.parse.urlencode(params))
    req = urllib.request.Request(url, headers={"Authorization": "Bearer %s" % token})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp).get("groups", [])


def aggregate_sentry(groups):
    """{hash: {"all": stats, "by_platform": {platform: stats}}} with stats =
    {"sessions", "healthy", "users"}; prefix-related release names cluster together."""
    out = {}
    for grp in groups:
        by = grp.get("by") or {}
        release, env = by.get("release"), by.get("environment")
        h = rel._commit_hash(release) if release else None
        if not h:
            continue
        t = grp.get("totals") or {}
        sessions = int(t.get("sum(session)") or 0)
        rate = t.get("crash_free_rate(session)")
        users = int(t.get("count_unique(user)") or 0)
        entry = bucket(out, h, {"all": {"sessions": 0, "healthy": 0.0, "users": 0}, "by_platform": {}})
        targets = [entry["all"]]
        platform = platform_of_environment(env)
        if platform:
            targets.append(entry["by_platform"].setdefault(platform, {"sessions": 0, "healthy": 0.0, "users": 0}))
        for cur in targets:
            cur["sessions"] += sessions
            cur["healthy"] += sessions * float(rate) if rate is not None else 0.0
            cur["users"] += users
    return out


def sentry_by_hash(token):
    """Per commit: "all" from the release-only query, "by_platform" from the query
    grouped by environment.

    The two are not the same population: grouping by environment drops every session
    that carries no environment value (measured: 12 773 sessions by release, 11 494 by
    release and environment -- ten percent gone, eleven of one build's 73). So the
    build's overall figures come from the release-only query, which is complete, and
    the environment query contributes only the platform split, which is all it can."""
    if not token:
        return {}
    try:
        out = aggregate_sentry(_sentry_sessions(token))
        for grp in rel.fetch_groups(token).get("groups", []):
            release = (grp.get("by") or {}).get("release")
            h = rel._commit_hash(release) if release else None
            if not h:
                continue
            t = grp.get("totals") or {}
            sessions = int(t.get("sum(session)") or 0)
            rate = t.get("crash_free_rate(session)")
            entry = bucket(out, h, {"all": None, "by_platform": {}})
            cur = entry.setdefault("all_complete", {"sessions": 0, "healthy": 0.0, "users": 0})
            cur["sessions"] += sessions
            cur["healthy"] += sessions * float(rate) if rate is not None else 0.0
            cur["users"] += int(t.get("count_unique(user)") or 0)
        for entry in out.values():
            if entry.get("all_complete"):
                entry["all"] = entry.pop("all_complete")
        return out
    except Exception as e:  # noqa: BLE001
        print("sentry: %s" % e, file=sys.stderr)
        return {}


def rate_of(stats):
    return (stats["healthy"] / stats["sessions"]) if stats and stats["sessions"] else None


FAMILY_OF_PLATFORM = {"linux": "Linux", "windows": "Windows", "macos": "macOS"}


def merged_by_hash(sentry_token, posthog_key):
    """{hash: {platform: (crashed, sessions)}} -- the per-OS estimate the reliability
    trend chart is built from, so the table agrees with the chart above it: crashed
    sessions per OS from Sentry's crash events (os.name, deduplicated by session), over
    sessions started per OS from PostHog. Two opt-in populations stitched together,
    hence an estimate; the environment split, when a build has it, is exact."""
    if not (sentry_token and posthog_key):
        return {}
    try:
        crashed_raw = rel.fetch_crashed_sessions_by_os(sentry_token)
        sessions_raw = rel.fetch_sessions_by_os(posthog_key)
    except Exception as e:  # noqa: BLE001
        print("merged per-OS estimate: %s" % e, file=sys.stderr)
        return {}
    out = {}
    for h, fams in sessions_raw.items():
        entry = bucket(out, h, {})
        for platform, family in FAMILY_OF_PLATFORM.items():
            n = int(fams.get(family, 0))
            if n:
                c, s = entry.get(platform, (0, 0))
                entry[platform] = (c, s + n)
    for h, fams in crashed_raw.items():
        entry = bucket(out, h, {})
        for platform, family in FAMILY_OF_PLATFORM.items():
            k = int(fams.get(family, 0))
            if k:
                c, s = entry.get(platform, (0, 0))
                entry[platform] = (c + k, s)
    return out


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


def posthog_ids_by_hash(key):
    """{hash: {platform: set(install ids)}} from PostHog session starts, plus "all"."""
    if not key:
        return {}
    hogql = ("SELECT coalesce(properties.commit, properties.app_version) AS r, toString(properties.os) AS o, distinct_id "
             "FROM events WHERE event = 'session_start' AND timestamp > now() - INTERVAL %d DAY "
             "AND isNotNull(coalesce(properties.commit, properties.app_version)) GROUP BY r, o, distinct_id" % rel.PERIOD_DAYS)
    try:
        rows = rel._posthog_query(key, hogql)
    except Exception as e:  # noqa: BLE001
        print("posthog: %s" % e, file=sys.stderr)
        return {}
    out = {}
    for r, o, uid in rows:
        h = rel._commit_hash(str(r))
        if not h or not uid:
            continue
        entry = bucket(out, h, {"all": set()})
        entry["all"].add(uid)
        entry.setdefault(platform_of(str(o)), set()).add(uid)
    return out


def sentry_ids_by_hash(token):
    """{hash: {platform: set(install ids)}} from Sentry crash events -- the only Sentry
    source that names users -- plus "all". The Sentry user id IS the PostHog distinct_id
    (both are the app's anonymous install id), which is what makes the union honest."""
    if not token:
        return {}
    out = {}
    try:
        for ev in rel._sentry_events(token, "event.type:error", ("user", "os.name", "release", "timestamp")):
            uid = ev.get("user") or ""
            if uid.startswith("id:"):
                uid = uid[3:]
            h = rel._commit_hash(ev.get("release") or "")
            if not uid or not h:
                continue
            entry = bucket(out, h, {"all": set()})
            entry["all"].add(uid)
            fam = rel._os_family(ev.get("os.name"))
            platform = {"Windows": "windows", "macOS": "macos", "Linux": "linux"}.get(fam)
            if platform:
                entry.setdefault(platform, set()).add(uid)
    except Exception as e:  # noqa: BLE001
        print("sentry users: %s" % e, file=sys.stderr)
    return out


def testers_for(posthog_ids, sentry_ids, h, platform):
    """(merged, posthog, sentry) distinct installs on build h on this platform, the
    merge being a union on the shared install id -- the same merge the site's
    unique-users chart makes. platform=None means every platform."""
    p = (lookup(posthog_ids, h) or {}).get(platform or "all", set())
    s = (lookup(sentry_ids, h) or {}).get(platform or "all", set())
    return len(p | s), len(p), len(s)


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
    posthog_ids = posthog_ids_by_hash(rel.get_posthog_key())
    sentry_ids = sentry_ids_by_hash(rel.get_token())
    merged = merged_by_hash(rel.get_token(), rel.get_posthog_key())
    out = {"generated": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
           "window_days": rel.PERIOD_DAYS, "formats": []}
    for key, label, _ in FORMATS:
        items = []
        for a in rows[key]:
            c = commits.get(a["hash"], {})
            s = lookup(sentry, a["hash"]) or {}
            platform = PLATFORM_OF_FORMAT[key]
            testers, t_posthog, t_sentry = testers_for(posthog_ids, sentry_ids, a["hash"], platform)
            testers_all, _, _ = testers_for(posthog_ids, sentry_ids, a["hash"], None)
            # Crash-free on this platform when sessions were recorded under the
            # platform-suffixed environment (ansel#1336); before that, the build's rate
            # over every platform, flagged so the page can say so. Testers come from
            # PostHog, which has always known the platform.
            # Three tiers, best available first: exact (Sentry sessions under this
            # platform's environment, ansel#1336), then the estimate the reliability
            # chart uses (Sentry crashes over PostHog sessions on this platform), then
            # the build's rate over every platform.
            own = (s.get("by_platform") or {}).get(platform)
            est = (lookup(merged, a["hash"]) or {}).get(platform)
            if own and own["sessions"]:
                crash_free, sessions, scope = rate_of(own), own["sessions"], "platform"
            elif est and est[1]:
                crash_free, sessions, scope = max(1.0 - est[0] / est[1], 0.0), est[1], "merged"
            else:
                crash_free, sessions, scope = rate_of(s.get("all")), (s.get("all") or {}).get("sessions"), "all"
            items.append({**a, "sha": c.get("sha"), "date": c.get("date"),
                          "crash_free": crash_free, "sessions": sessions or None, "crash_free_scope": scope,
                          "testers": testers or None, "testers_posthog": t_posthog, "testers_sentry": t_sentry,
                          "testers_all_platforms": testers_all or None})
        out["formats"].append({"key": key, "label": label, "builds": items})
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=1)
    print("releases: " + ", ".join("%s %d" % (f["key"], len(f["builds"])) for f in out["formats"]))


if __name__ == "__main__":
    main()
