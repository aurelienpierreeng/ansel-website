---
title: Download
date: 2026-08-29T18:00:00+02:00
draft: false
weight: 5
---

<div class="lead my-5 ps-3">Get Ansel for Linux, Windows and macOS, see how stable the nightly builds are, and pick any recent build of every package with its crash rate and the number of people who ran it.</div>

## Install

{{% row %}}
{{% card icon="linux fab" title="Linux" %}}
Distribution-agnostic, portable AppImage executable
{{< release-assets release="https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0" extension=".appimage" label="Download latest" >}}
{{< release-assets release="https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0" extension=".appimage" label="Download previous" offset="1" display="link" >}}
{{% /card %}}

{{% card icon="windows fab" title="Windows" %}}
Windows 7 to 11 installer
{{< release-assets release="https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0" extension=".exe" label="Download latest" >}}
{{< release-assets release="https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0" extension=".exe" label="Download previous" offset="1" display="link" >}}
{{% /card %}}

{{% card icon="apple fab" title="MacOS X" %}}
Distribution for MacOS X 15 and newer.
{{< release-assets release="https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0" extension="arm64.dmg" label="Download latest (Apple M)" >}}
{{< release-assets release="https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0" extension="i386.dmg" label="Download latest (Intel)" >}}
{{% /card %}}

{{% card icon="terminal" title="Build from source" %}}
Best performance for your hardware
{{< button url="/doc/install" label="Building instructions" icon="wrench" >}}
{{% /card %}}
{{% /row %}}

---

{{% row %}}

{{% column class="text-center" %}}
{{< button url="/doc/install/" label="Installation help" icon="mouse" >}}
{{% /column %}}

{{% column class="text-center" %}}
{{< button url="/doc/getting-started/" label="Getting started" icon="hands-helping" >}}
{{% /column %}}

{{% /row %}}

---

### Is it stable ?

_Stats updated automatically every 4h from opt-in Sentry.io crash logs collection. Last update : {{% build-time %}}_

{{% row %}}
{{% column %}}
{{% card %}}

{{< plotly title="Crash-free sessions plotted against the date each build was committed — not the date it was used (data collected by opt-in sentry.io and posthog)." caption="false" src="reliability-trend.json" class="full-width" dynamic="true" >}}

{{% /card %}}
{{% /column %}}
{{% column %}}
{{% card %}}

{{< plotly title="Share of all crashes versus share of all bug reports, per operating system (crashes from opt-in sentry.io, bug reports from Github)." caption="false" src="reliability-os.json" class="full-width" dynamic="true" >}}

{{% /card %}}
{{% /column %}}
{{% /row %}}

{{% row %}}
{{% column %}}
{{% card %}}

{{< plotly title="Crash-free sessions and Mean Time Before Failure (MTBF) per nightly build (data collected by opt-in sentry.io)" caption="false" src="reliability.json" class="full-width" dynamic="true" >}}

{{% /card %}}
{{% /column %}}
{{% column %}}
{{% card %}}

{{< plotly title="Crash-free users and number of pictures edited without crashing, per nightly build (data collected by opt-in sentry.io and posthog)" caption="false" src="reliability-users.json" class="full-width" dynamic="true" >}}

{{% /card %}}
{{% /column %}}
{{% /row %}}

The two charts on the top row read the whole fleet, the two below read one revision at a time. Wherever a date appears, it is the date the build was committed, never the day someone happened to be editing.

**Crash-free sessions by build date** : one line per operating system, each averaged over about a week. **The dates are when the code was written, not when it was run** — a crash today on last week's nightly counts against last week's build. So reading left to right shows the code getting better, not the calendar going by. A bad build dips at its own date, and the lines say which platform it hit.

**Where crashes happen, and where bug reports come from** : Windows carries just over half of all crashes — and crashes nearly three times more often per session than Linux — yet files under a quarter of the bug reports. Linux is the mirror image. macOS sits closer to Linux than its share of reports would suggest, and that is not luck : it is a UNIX, so a good deal of what we fix on Linux reaches it for free. Windows shares almost none of that code — it is a different architecture, not a variant — so a Windows bug exists until a Windows user tells us about it. **A bug nobody reports is a bug nobody can fix**, and it keeps crashing for everyone on that platform. Ansel is free, and written by people who cannot test on your machine : telling us what breaks is the contribution we actually need. Whatever happens, your edits are written to disk as you make them, so a crash costs you the last action at most.

{{% row %}}
{{% column %}}
{{% card %}}

{{< plotly title="Reported issues (bugs, tasks and features) already resolved versus still open, per release (source: Github). Much has already been done; what remains is tracked openly." caption="false" src="bugs.json" class="full-width" dynamic="true" >}}

{{% /card %}}
{{% /column %}}

{{% column %}}

Ansel has not published a stable release yet and there is no ETA for one : a new release is published when the list of all bugs have been cleared, so we _know_ the software and stable. So far, Ansel only publishes __revisions__, which are intermediate states of the sourcecode. Once a revision has been tested by at least 25 unique users, its reliability stats can show above : the charts display the 30 most recent revisions that reached that threshold. An asterisk (\*) marks revisions we shipped as a packaged nightly build.

On the two per-revision charts above, the crash-free rate is shown as a percentage whose **bar opacity encodes our confidence** : the solid part (*almost certain*) is the rate we are confident the software reaches, the *likely* range goes up to the currently recorded average, then *optimistic* reaches up to the best plausible rate written in parentheses on top. The fewer people tested a revision, the more incertainty there is on the average, the larger the {*likely* + *optimistic*} range gets : it is the margin of error of the current average at 95% confidence.

Bugs need to be reported on [Github](https://github.com/aurelienpierreeng/ansel/issues) or they will never be fixed. This free software is only guaranteed to work on the computers of its developers, who are not in front of yours. __Ansel saves your editing histories immediately after each change__: in case of a crash you loose at most the last action.

The links above always point to the latest nightly build of the "fairly stable" branch. If you want a particular revision or need to roll back, [you can find all intermediate versions on Github](https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0).


{{% /column %}}
{{% /row %}}

{{< divider >}}

{{< divider >}}

## Every recent build, per package

Builds are named `Ansel-x.y.z+N.g<commit>`: a higher `N` is a newer build, and the commit links to the exact source it was built from. Nightlies are the "fairly stable" channel — quickly broken, quickly fixed — so the crash-free rate is there to help you pick: a build that many people ran without crashing is a safer bet than yesterday's. Reading the columns:

- **Crash-free, all platforms** — share of sessions on that build that ended without a crash, from the users who opted in to crash reports (Sentry). Crash reports identify the build, not the package, so this is the same figure for every package of one build.
- **Testers, this platform** — how many distinct people ran that build on this platform, from the opt-in usage statistics (PostHog). The two macOS packages share one count, as no architecture is reported.

{{< release-table >}}
