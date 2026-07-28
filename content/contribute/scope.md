---
title: Scope
date: 2026-07-27
weight: 2
aliases:
    - /contribute/audience/
authors:
    - Aurélien Pierre
---

Knowing the audience is the first step of design, and declaring the scope is the first step
of governance: every request, bug report and contribution is measured against this page.
There are two honest ways to criticize the project. Holding it to what this page promises —
that critique is always receivable, and the project cannot dismiss it without contradicting
itself. Measuring it against a goal it never adopted — that is a wish, receivable as a wish
and refusable as one. This page exists so everyone can tell which is which.

## What Ansel is

Ansel lets a photographer **manage, edit and export collections of RAW photographs on a
desktop computer, through a graphical interface, putting visual image quality above all
else** — from ingestion to print, archive or publication. Concretely, three goals: cull
efficiently the photographs coming out of the camera, to pick the ones worth processing;
edit them in the most direct way possible, with unit controls affecting one perceptual or
optical property at a time; index and retrieve the results for archival. It is an instrument of visual
expression, much like a musical instrument: generic controls, direct access to the image
data, no ceiling on mastery. It is optimized for defined workflows ([described here](./introduction.md)); deviating uses may work but are not supported, and
will not be made supported at the cost of complicating the nominal case.

## Who it is for

The target user is a photographer — amateur or professional — with intermediate to advanced
knowledge of their trade:

- **color theory**: brightness vs. lightness vs. luminance, chroma vs. saturation, additive
  color models;
- **cameras**: ISO, dynamic range, exposure bias;
- **light**: illuminants, color rendering, how shadows fall.

and **average computer skills**: comfortable with a desktop GUI, no scripting, no compiling,
no command line. The technical rootedness exists to unlock finer and more accurate control
over the image — never technique for its own sake. Image-processing theory must be learned
(we document it); GUI navigation must not: standard interactions follow decades-old
conventions, and needing a manual for them is a design failure on our side, not a knowledge
failure on yours. Technical terms are kept as published in the scientific literature, and as
they appear on their Wikipedia entry so
what you learn here transfers everywhere — Ansel will not rename methods to look friendlier,
because keeping the doors of understanding open matters more than appearing easy.

## What Ansel is not

- **Not a free Lightroom.** A dozen volunteers working evenings will not clone the product
  of a multi-billion-dollar company, and will not try: mass-appeal editors deliberately
  trade away the fine control this project exists to provide. Requests of the form "do it
  like software X" are wishes measured against someone else's scope.
- **Not for beginners.** Ansel will not give up visual quality or control granularity to
  smooth the learning curve. Simplifying means removing steps from a defined task — it does
  not mean allowing use without understanding, which turns a tool into a toy.
- **Not a platform.** No plug-in ecosystem, no scripting-first workflows, no ports to
  mobile or the web, no adoption of the framework of the day. Every technology choice is
  measured against maintainability with current resources.
- **Not an experiment.** New techniques enter when they solve a stated problem of the
  nominal workflow, not because they are novel. "AI", or any other buzzword, is not a
  reason; it can at most be a means, evaluated like any other.

## What "possible" means here

A request is possible when three conditions hold: it can be done at all; it can be done
with the resources the project currently has; and it can be **maintained in the future**
with those same resources. The third is the one everyone forgets, and the one that kills
projects: the industry is full of better technologies abandoned because their maintenance
cost was too high. A feature that cannot be enclosed — whose repair would require opening
half the application — will be refused even if it works, even if it is already written.
That refusal is the pact being honoured, not broken: it is how the tool stays alive for
the people who depend on it.

## Changing the scope

This scope is declared, not eternal. Changing it is a real decision with a real cost, and
it is made openly — announced, argued against the project's engagements
([the pact](./pact.md)), and recorded — never by drift, never by accumulation of small
exceptions. If you believe the scope itself is wrong, that is a legitimate discussion to
open; opening it looks like an argument about who the project should serve, not like a
feature request repeated until it wins.
