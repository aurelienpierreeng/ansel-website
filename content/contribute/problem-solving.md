---
title: A culture of problem solving
date: 2026-07-27
weight: 4
authors:
    - Aurélien Pierre
---

Everything in open source is public: the code, the bugs, the requests, the discussion.
Everyone can chime in — which is a strength only if the conversation is disciplined, and a
slow-motion disaster otherwise. This page is the discipline. It is not etiquette: every
rule here exists because its violation has a measurable cost in wasted work, and the
[bug-reporting protocol](./report-a-bug.md) and [design protocol](./design.md) both build
on it.

For background, see [The designer and the drilling machine](https://eng.aurelienpierre.com/2020/04/the-designer-and-the-drilling-machine/)
and [Design by committee will not save FLOSS](https://eng.aurelienpierre.com/2022/06/design-by-committee-will-not-save-floss/).

## Discussion exists to reach decisions

The volume of information everyone faces is already past what humans can process. Endless
threads and unregulated conversations actively harm communication: they dilute the
important information and exhaust the reader. **Discussion is solely meant to reach an
understanding and proceed to actionable decisions.** Everything else is informal chat —
welcome, but on the chat channels, outside the problem-solving process.

## What is a problem?

A photograph has a life cycle, from the moment the shutter fires to the moment the final
image is printed, archived or published. Problems are anything that makes this work more
time-consuming, complicated or unreliable than it should be. **A problem is something
preventing you from getting things done.**

"What it should be" is bounded by what is possible, and "possible" means three things at
once: it can be done at all; it can be done with currently available resources; and it can
be **maintained in the future** with those same resources. The third condition is the most
overlooked, because it lives in a distant and fuzzy future — and it is the one that kills
projects. The industry is full of better technologies abandoned because their maintenance
cost was too high.

## Define problems by the goal, not by the fix

Users are poorly placed to define their own problems — not a personal failing, a
structural fact: you are too close to your problem to see its shape, and you see only the
interface, with no view of what is wired behind it. So the natural way to ask is "add a
button that does this", "make that graph", "tweak this existing thing". These GUI-based
definitions **always** promote solutions that lack generality and add complexity, because
thinking in graphical elements bypasses abstract thinking — and abstraction is the only
way of simplifying complex matters.

State the goal instead:

- *good*: "I want my picture to look more X or less Y", "I need to export pictures for Z",
  "I find myself repetitively doing W all the time";
- *bad*: "X is broken" (what were you doing?), "Y should be like software Z" (measured
  against someone else's scope), "I don't like W" (someone else likes it — taste is not
  actionable), "I need this tool, designed for A, to also do B and C".

The problem you see is usually the end of a branch. Focus on the end and you miss the stem
and the root; find the root and the solution comes out simpler, more general, and often
fixes other branch-end problems along the way. Focusing on branch ends produces contextual
patches, and contextual patches are how software rots. A good problem definition is one
that helps find the root — which is why it names the goal, never the implementation.

## Stick to the problem

The number-one mistake is suggesting a solution alongside the problem definition, hoping
to help. It does the opposite: it biases the process from the first message, in favour of
the pet technology of whoever spoke first. Humans are lazy — as they should be — so any
half-baked solution already on the table will always look better than sitting longer with
the problem. Rigour takes incompressible time; rushing it costs more time later, when the
sub-optimal solution and everything built on top of it must be redone. During problem
definition, no solutions. There is a stage for them ([the design protocol](./design.md)),
and it comes second.

## Contextualize the problem

Design and engineering do not solve technical problems — a common misconception. They
solve *people's* problems, with technology. There is therefore no solution before we know
who has the problem. Proper context includes:

- what kind of photography you do and how (wedding → large batches; art → few pictures,
  individually fine-tuned);
- how comfortable you are with computers — this calibrates the answer, it never disqualifies
  the question;
- the software version and where you got it;
- the operating system (name, version, graphics drivers);
- the hardware, especially GPU brand and generation.

Too much context dilutes; too little leaves open questions. It is genuinely hard to gauge —
err on the side of completeness for the technical facts, and of brevity for everything
else.

## One thread, one topic

For the reader, for project management, and for the search engine that will serve the next
person with the same problem: each thread, bug report or feature request carries exactly
one topic. Open new threads for new topics.

## Compromises are not solutions

A compromise is a lose-lose arrangement: conflicts resolved by meeting halfway in losses.
You want the cinema, your partner wants the restaurant; the compromise is half a meal and
half a film, and a bad evening guaranteed for both. Investigate the motives instead: the
restaurant was about not cooking and not washing up, the cinema was about unwinding —
takeout and a film at home achieve both goals in full, and nobody compromised anything.

Whenever a compromise seems necessary, it usually means the root goals were never
investigated — a design process stopped too early, at the tip of the iceberg. In this
project, "let's do both halves" and "let's make it an option" are read as symptoms, not
solutions: the discussion goes back to the root.

## Working towards a solution

Once the problem is defined, scoped and contextualized, solutions are explored under
[the design protocol](./design.md) — specification first, prototypes after, validation
last. Designing is a skill like any other in this project: those who have demonstrated it
carry the decision, and anyone willing to learn it is welcome to start — with the same
apprenticeship that any skill demands.
