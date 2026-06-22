#!/usr/bin/env python3
"""Assign orphaned, resolved issues to the next-release milestone on GitHub.

Many issues were closed as *completed* without ever being attached to a milestone,
so they don't show up in the per-release progress chart. This finds every *typed*
issue (Bug, Task or Feature) closed with reason "completed" (i.e. actually resolved
- NOT "not planned" / duplicate / won't-fix) and with no milestone, and assigns it
to the next release milestone (the lowest-version open milestone, chosen
dynamically so nothing needs editing per release).

DRY-RUN BY DEFAULT: prints what it would do. Pass --apply to actually change the
issues. Re-running is safe/idempotent (already-milestoned issues are excluded by
the search), so it can also be scheduled to keep new fixed bugs tidy.

Auth: GITHUB_TOKEN env or a .github-auth file at the repo root. Needs a token with
write access to issues (repo scope).

Usage:
  python tools/backfill-bug-milestones.py            # dry run
  python tools/backfill-bug-milestones.py --apply     # do it
  python tools/backfill-bug-milestones.py --milestone 0.1 --apply
"""

import argparse
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request

REPO = os.environ.get("GITHUB_REPO", "aurelienpierreeng/ansel")
API = "https://api.github.com"
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def die(msg):
    print("error: %s" % msg, file=sys.stderr)
    sys.exit(1)


def get_token():
    tok = os.environ.get("GITHUB_TOKEN", "").strip()
    if tok:
        return tok
    path = os.path.join(REPO_ROOT, ".github-auth")
    if os.path.isfile(path):
        with open(path, encoding="utf-8") as f:
            return f.read().strip()
    return None


def gh(token, path_or_url, method="GET", body=None):
    url = path_or_url if path_or_url.startswith("http") else API + path_or_url
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(url, data=data, method=method, headers={
        "Authorization": "Bearer %s" % token,
        "Accept": "application/vnd.github+json",
        "User-Agent": "ansel-bug-milestone-backfill",
    })
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp), resp.headers


def _version_key(title):
    nums = re.findall(r"\d+", title or "")
    return tuple(int(n) for n in nums) if nums else (9999,)


def resolve_milestone(token, wanted):
    milestones, _ = gh(token, "/repos/%s/milestones?state=open&per_page=100" % REPO)
    if not milestones:
        die("no open milestones on %s" % REPO)
    if wanted:
        for m in milestones:
            if str(m["number"]) == wanted or m["title"] == wanted:
                return m
        die("milestone %r not found among open milestones" % wanted)
    return sorted(milestones, key=lambda m: _version_key(m.get("title", "")))[0]


ISSUE_TYPES = ("Bug", "Task", "Feature")


def find_orphan_typed_issues(token):
    """Numbers of *typed* (Bug/Task/Feature) issues closed as 'completed' with no
    milestone. GitHub search can't OR types, so we query each and merge."""
    numbers = set()
    for t in ISSUE_TYPES:
        q = ("repo:%s is:issue type:%s is:closed reason:completed no:milestone"
             % (REPO, t))
        page = 1
        seen = 0
        while True:
            url = "%s/search/issues?per_page=100&page=%d&q=%s" % (API, page, urllib.parse.quote(q))
            payload, _ = gh(token, url)
            items = payload.get("items", [])
            numbers.update(it["number"] for it in items)
            seen += len(items)
            if len(items) < 100 or seen >= payload.get("total_count", 0):
                break
            page += 1
            time.sleep(1)  # be gentle with the search API
    return sorted(numbers)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--apply", action="store_true", help="actually assign the milestone")
    ap.add_argument("--milestone", help="milestone number or title (default: lowest open)")
    args = ap.parse_args()

    token = get_token()
    if not token:
        die("no token (set GITHUB_TOKEN or add .github-auth)")

    ms = resolve_milestone(token, args.milestone)
    print("Target milestone: %s (#%d)" % (ms["title"], ms["number"]))

    numbers = find_orphan_typed_issues(token)
    print("Orphaned resolved issues (bug/task/feature) to assign: %d" % len(numbers))
    if not numbers:
        return 0
    print("  issues: %s" % ", ".join("#%d" % n for n in numbers))

    if not args.apply:
        print("\nDRY RUN - nothing changed. Re-run with --apply to assign them.")
        return 0

    done = 0
    for n in numbers:
        try:
            gh(token, "/repos/%s/issues/%d" % (REPO, n), method="PATCH",
               body={"milestone": ms["number"]})
            done += 1
            print("  assigned #%d -> %s" % (n, ms["title"]))
        except Exception as exc:  # noqa: BLE001
            print("  FAILED #%d: %s" % (n, exc), file=sys.stderr)
        time.sleep(0.3)
    print("\nDone: %d/%d issues assigned to %s." % (done, len(numbers), ms["title"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
