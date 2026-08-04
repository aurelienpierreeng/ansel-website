---
title: The pact
date: 2026-07-27
weight: 1
authors:
    - Aurélien Pierre
---

Free software runs on two one-way transactions. Users take the product without giving
anything back, because three centuries of market taught us that a thing endlessly
downloadable has no price. Developers decide without answering to anyone, because the
license says they owe nothing — not even an explanation. One side takes without paying,
the other rules without accounting. These are not two problems: they are the same problem,
seen from both ends, and most of what is wrong with free software grows on it.

Ansel refuses both halves. When people depend on a tool to get their work done — years of
learning, entire libraries of edits, sometimes a livelihood — a responsibility exists,
whether we like it or not. And it cannot be discharged by technical promises alone: keeping
old edits readable forever is necessary, but a project can honour its file formats and
still fail the people who produce the files. This page states both directions of the
contract explicitly. It is written to be *opposable*: if the project breaks an engagement
below, quote it back at us — that is what it is for.

## Why this pact exists

Ansel was forked from Darktable 4.0 in May 2022, and the fork was not a technical disagreement:
it was a refusal to keep working inside a set of organizational failures that no amount of
code could fix. Those failures are documented — measured on the public record, archives and
registers in hand, in
[*La conception et l'ingénierie malgré l'open-source*](https://editions.aurelienpierre.com/concevoir/) —
and this pact is their point-by-point negation. Stating them explicitly is not
score-settling: a project that does not name the mistakes it forked away from has no way to
notice itself repeating them.

1. **Features without problems.** Ambitious refactors shipped without a stated problem, a
   defined user or acceptance criteria — serving the pleasure of building over the needs of
   the base. *Hence: problems before features, and a [design protocol](./design.md) that
   refuses solutions before the problem is scoped.*
2. **Ambition stopping at delivery.** Nobody priced what a feature would cost to maintain;
   new code was woven through the old instead of enclosed, until interface bugs could no
   longer be traced to causes. *Hence: maintenance before novelty, and enclosure as an
   acceptance criterion.*
3. **A veto that was never used.** The one written rule — never stop anyone from coding
   when they're having fun — made refusal culturally impossible: nearly everything merged,
   unconcerted, and the technical debt was acknowledged in public and paid by no one.
   *Hence: written acceptance criteria, and refusal as a duty owed to the users.*
4. **Users' capital treated as expendable.** Workflows, trained habits and working setups
   broken release after release, regressions reframed as design choices, and the user's
   account of their own experience rewritten for them. *Hence: your capital is untouchable,
   and your testimony is sovereign.*
5. **The register silenced instead of answered.** Bug reports left unread and swept by a
   robot, testers driven away by silence, critique reclassified as toxicity and moderated
   on tone while its substance went unanswered. *Hence: no stale-bot
   ([reporting bugs](./report-a-bug.md)), and a [code of conduct](./code-of-conduct.md)
   whose first section protects criticism before it protects anyone's comfort.*
6. **Power without structure.** No mandate, no term, no appeal — decisions held by whoever
   held the merge rights and the moderation tools, and the maintainer's solitude narrated
   as heroism instead of treated as an organizational defect. *Hence: reasons given,
   decisions appealable, the same rules for everyone, and this written constitution itself.*

None of this requires believing the fork's side of the story: every mistake above is stated
so that Ansel can be checked against it. The day this project ships features without
problems, merges without refusing, breaks your edits, silences its register or moderates
its critics on tone — quote this page.

## What the project owes its users

1. **Your capital is untouchable.** Your data, your edit histories, your learned workflow
   are years of your life. No release will destroy them: old edits stay readable and
   reproduce the same output, and changes that would break them are confined to major
   versions, announced as such.
2. **Problems before features.** Work starts from a problem someone actually has, stated
   and scoped before any solution is discussed ([the design protocol](./design.md)). No
   feature lands because it would be cool, because another software has it, or because it
   was fun to write.
3. **Maintenance before novelty.** Most of the cost of a feature comes after it ships.
   Anything we cannot maintain with current resources will be refused or removed — refusal
   is not hostility, it is the tool staying trustworthy. The answer "no, because we could
   not maintain it" is a promise being kept, not a door slammed. A large part of the maintenance
   concerns is supporting 3 platforms (Windows, Linux and MacOS), which needs to be done
   using the least amount of platform-centric heuristics and idiomatic paradigms.
4. **Your testimony is heard; your prescriptions are not.** You are the sole authority on
   your goals, your context and your pain — nobody will rewrite your experience for you or
   tell you that what you hit "is not a bug, it's a design choice" as a way to close the
   discussion. Deciding *solutions* stays with the people who answer for their maintenance;
   the reasons for a decision are stated, and decisions are reversible until real use has
   validated them.
5. **You will not be blamed for the tool's complexity.** Two difficulties must not be
   confused. Ansel expects you to master your trade — color, cameras, light
   ([scope](./scope.md)) — and documents its theory precisely because it must be learned:
   being pointed to the right chapter on a trade question is legitimate help, and learning
   is part of the deal you accepted by choosing this tool. The *tool itself* is another
   matter: when you cannot find, understand or operate something that standard GUI
   conventions should make obvious, you have found a design or documentation defect on our
   side, not a personal failing on yours. The boundary between the two is not anyone's
   opinion — it has a test: photography existed before computers. What already had to be
   learned in a darkroom — exposure, contrast, dodging and burning, color casts, grain — is
   the trade, and it cannot be made simpler without amputating your capability. What exists
   only because of computers — file formats, pipeline order, display profiles, error
   messages — is the tool, and simplifying it takes nothing away from anyone. If you
   started photography with software, the two arrive welded together and every difficulty
   looks like a software difficulty; the distinction is still owed to you. The craft may
   demand a manual; the tool must not — and which of the two your question touches is
   judged on the question, never on you.
6. **The tool is documented for what it does *to* you, not only *for* you** — its
   assumptions, its limits, its costs in learning time, not just its features.
7. **The prospectus stays honest.** What Ansel is and is not is written in
   [Scope](./scope.md), and requests are judged against it — never against the mood of the
   day. If the project drifts from its declared values, that page is the evidence to hold
   against it.

## What the project asks of its users

1. **Report problems as testimony.** What you did, what happened, what you expected, in
   your own words and your own language — following
   [the problem-solving culture](./problem-solving.md). You owe nothing more technical than
   that; the translation into causes and solutions is our work, not yours.
2. **Accept the perimeter.** Ansel is one tool with one scope. A request outside it will be
   refused with the scope quoted — that refusal is legitimate, and repeating the request
   does not make it grow legs. "Make it a free Lightroom" is a wish, not a grievance.
3. **Respect the working conditions.** There are many of you and few of us. Insistence,
   pile-ons and deadlines are pressure on unpaid people; one clear report is worth more
   than ten reminders. The absence of an answer means "not yet possible", never "you don't
   matter".
4. **Give back what you can.** Test the nightly builds, confirm fixes, improve the
   documentation, answer another user, [fund the work](../donate.md). The
   project answers for your needs; its workers' conditions are, in return, partly your
   responsibility — that is the pact.

## What contributors owe, and what they receive

1. **Entry is declared.** What the project expects you to know is written before you
   invest: the [scope](./scope.md), the [design protocol](./design.md), the
   [coding style](./coding-style.md). Nobody should discover the rules by breaking them.
2. **Authority follows demonstrated work, in a bounded perimeter.** Trust grows with the
   track record: a newcomer decides within a small, enclosed area; scope widens as the
   dossier does. Volume and tone earn nothing; verifiable improvement of the project —
   code, docs, tests, support — earns everything.
3. **Learning happens outside production.** Experiments live in branches and prototypes,
   not in the tool people work with. The project owes you honest review and mentorship
   within its capacity; it does not owe you a merge.
4. **Every feature is a maintenance debt, and its author is its first maintainer.** A
   contribution is evaluated on what it will cost to keep alive, not on what it cost to
   write. "It works" is not the bar; "it can be repaired by someone else" is.
5. **Refusals come with reasons, and decisions with an appeal.** A rejected contribution
   is measured against written criteria you can contest with evidence. Exclusion — of code
   or of people — is bounded, notified, and appealable ([code of conduct](./code-of-conduct.md));
   it protects the collective, it does not punish a person.

## The honest limits of this pact

Today, Ansel is maintained by one person with help. The engagements above are held by that
person, which means they are held within human limits: capacity, health, and funding decide
the pace, and the [priorities are public](./triaging.md) rather than negotiated
individually. The pact is not a service-level agreement; it is a declaration of values
precise enough to be checked. The long-term structure this project aims at — where users
and workers share ownership and vote, where these engagements are held by an institution
rather than a man — is described in the book
[*La conception et l'ingénierie malgré l'open-source*](https://editions.aurelienpierre.com/concevoir/).
Until then, this page is the contract, and the record is public: hold us to it.
