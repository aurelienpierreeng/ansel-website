---
title: Reporting bugs
date: 2026-07-27
weight: 5
authors:
    - Aurélien Pierre
---

A bug report is testimony: what you did, what happened, what you expected. That is all the
project asks of you — the translation into causes, diagnoses and fixes is our work, not
yours. You will never be blamed for not knowing computers, for imperfect English, or for a
report that turns out to be a documentation problem: a user who cannot follow a technical
instruction has found a design or documentation defect, not committed a personal failing
([code of conduct](./code-of-conduct.md)).

## Before reporting

1. **Update first.** If you can, check whether the problem still exists in the latest
   [nightly build](https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0) — many
   reports are already fixed.
2. **Search the [existing issues](https://github.com/aurelienpierreeng/ansel/issues).** If
   your problem is already reported, add your information there — one more context is
   valuable; one more thread is noise. Do not bump old threads that only *resemble* your
   problem: one thread, one topic.
3. **Sort what you have.** A *regression* is something that worked before and broke — say
   which version still worked, it shortens the hunt enormously. A *bug* is something that
   never worked. A *question* ("how do I…?") belongs in
   [Discussions](https://github.com/aurelienpierreeng/ansel/discussions), not in the
   tracker — asking there is not a lesser contribution, and unclear cases are welcome
   wherever you put them: triage exists to sort, not to judge.

## Writing the report

Use the [bug report form](https://github.com/aurelienpierreeng/ansel/issues/new/choose) and
follow [the problem-solving culture](./problem-solving.md). The substance:

- **what you did** — the exact steps, on what image, in what order;
- **what happened** — including exact error messages, screenshots, or the output file;
- **what you expected** — this is where your testimony is irreplaceable: nobody but you
  knows what "correct" looks like for your work;
- **your context** — software version and origin, OS and version, graphics drivers, GPU
  brand and generation, and the kind of photography you do when it matters;
- **attach the evidence** when relevant: the RAW file and its `.xmp` edit history attached
  directly to the issue, never behind a third-party link that will die before we get to it.

Write in the language you can; broken English is fine, so is French — and machine
translation is an accepted tool on both sides.

## What happens next

Your report enters [the triage protocol](./triaging.md): it gets a nature (regression, bug,
enhancement…), a priority, and a milestone when it implies compatibility breaks. The
priorities are rules, not moods — regressions before enhancements, data loss and crashes
before comfort, wide impact without workaround before niche cases with one. Two honest
warnings, so silence never reads as contempt:

- **Capacity is small and the queue is real.** No answer yet means "not reached yet",
  never "you don't matter". The [Kanban board](https://github.com/orgs/aurelienpierreeng/projects/1)
  shows what is being worked on.
- **No robot will close your report for being old.** An issue closes when it is fixed,
  refused with a reason, or established as invalid or duplicate — never by an automated
  stale-bot sweep. If it closes, you will know why, and you can contest it with evidence.

## What a report cannot do

A bug report states a problem; it does not commission a solution. If your report is
actually a feature wish, it will be redirected to
[Discussions](https://github.com/aurelienpierreeng/ansel/discussions) and measured against
[the scope](./scope.md) — refusal there is the project keeping its perimeter, not a
judgment on you. And if what you found is real but out of our reach — a third-party library
defect, an upstream driver — the report will say so and point where it belongs, rather
than pretending we can fix what we cannot.

Testing nightly builds and confirming fixes is the single most useful contribution a
non-programmer can make to this project: it is [the pact](./pact.md) working in your
direction.
