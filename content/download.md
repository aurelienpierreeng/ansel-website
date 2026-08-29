---
title: Download
date: 2026-08-29T18:00:00+02:00
draft: false
weight: 5
---

<div class="lead my-5 ps-3">Every recent nightly build of Ansel, per package format, with the crash rate and the number of people who ran it. The newest build of each format is also on the <a href="/">home page</a>; older months are on the <a href="https://github.com/aurelienpierreeng/ansel/releases">GitHub releases</a>.</div>

Builds are named `Ansel-x.y.z+N.g<commit>`: a higher `N` is a newer build, and the commit links to the exact source it was built from. Nightlies are the "fairly stable" channel — quickly broken, quickly fixed — so the crash-free rate is there to help you pick: a build that many people ran without crashing is a safer bet than yesterday's. Reading the columns:

- **Crash-free** — share of sessions on that build that ended without a crash, from the users who opted in to crash reports (Sentry).
- **Testers** — how many distinct people ran that build, from opt-in crash reports and usage statistics (Sentry and PostHog), whichever of the two counted more.
- **Downloads** — the lifetime download count of that file on GitHub.

{{< release-table >}}
