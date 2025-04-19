---
title: Designing Ansel
date: 2024-07-14
weight: 3
---

Ansel is __designed__, not hacked. Hackers may enjoy "working" on accelerating the demise of Darktable by increasing its [technical debt](https://en.wikipedia.org/wiki/Technical_debt).

## What is design ?

Design is a process by which you unroll a methodology to bring a technical solution to an human's problem. The design process is meant to converge to the most suitable solution, while fighting the natural urge to rush into the first or the most comfortable idea.

{{< quote author="Louis Srygley" >}}
Without requirements and design, programming is the art of adding bugs to an empty text file.
{{< /quote >}}

1. __Design starts with an usecase__ : a defined task to achieve (on a picture), by a defined user, into a defined timeframe. If no usecase, then no problem to solve, then keep away from your code editor.
2. __Design requires to know the target user__ : education/training, level of craftmanship/mastership, etc.
3. __Design requires to understand the needs__ : in the context of Ansel, that will often need some art history and darkroom photography knowledge,
4. Once the problem and the user are understood, design requires to specify :
    - the expected functionnalities of the solution,
    - the scope of the solution (where in the lifecycle of an image does the solution stand ?),
    - the constraints and requirements of the solution (supporting some standard, allowing to process _n_ images per time unit, etc.),
    - a series of tests to complete that would validate the quality of the solution, as to limit unproductive opinions, biases and subjectivity in the validation process.
5. __Only then__ can the mockups and brainstorming begin, followed be prototypes.


## What design is not ?

Design does not deal with :

- vague requirements of an undefined, future, or fantasized user,
- "it would be cool if…" (that's how you create inconsistent plugins collections),
- what people like (for everything someone likes, you will find someone to hate it),
- what people think they want (it's often not what they need),
- magic tech buzzwords that "are the future" and, as such, need to be plugged everywhere, regardless of their relevance or feasibility (yes, I'm talking about AI, NFT, blockchain, etc.)

## What is good design

Good design is :

- minimalistic,
- robust,
- future-proof,
- generic and generalized,
- maintainable with limited resources,
- informed by science,
- compatible/interoperable with industry standards.

Since Ansel is a workflow-based application, good design also minds the workflow as a whole, and where the problem/solution fit in it.

## How is good design done ?

To help the design process, communication should remain concise, on-focus, and the people taking part to that process should ensure they have a proper understanding of the theory and technical background involved in the problem/solution scope.

It should be stressed that, although the project is software-driven, not all solutions involve coding. Sometimes (often ?), better education or better documentation is all that is needed.

The purpose of a sane design process is to avoid biasing the solutions too early with one's pet design/tech and to avoid getting lost in the technicalities, but to always come back to the core basics and principles of what we are doing: post-processing possibly large batches of raw images for all kinds of output media.

This is backed up by the fact that users rarely know their own needs, or rather, the needs they express are rarely the root of what they actually want. The difficult task of designing is to cut through the branches to go to the root, because solving the root problem usually ends up in more elegant, generic and minimalistic solutions.

### Problems come first

The first step of Ansel design process is to submit a feature request, on the [Community](https://community.ansel.photos/discussions-category?category=6). Feature requests have been moved out of Github because this platform is unwelcoming to non-programmers and non-English-speakers (although the Community supports only French and English).

This feature request will focus on the problem to solve and refrain from proposing any solution. The problem will be defined in terms of tasks to achieve in a photographer's workflow or expected visual outcome of the processed image, aka in terms of the end goal to achieve, not in terms of tooling or technicalities thought to be needed. This may lead to a discussion to dig into the roots of the problem, which are usually [well hidden beneath what the user thinks their problem is](https://eng.aurelienpierre.com/2020/04/the-designer-and-the-drilling-machine/).

No solution proposal is accepted at this stage.

### Solutions come second

When the definition and scope of the problem is agreed upon between the people involved in the discussion, solutions may be proposed. Further discussion may be necessary to evaluate the drawbacks and benefits of each solution, leading to the best solution being adopted on principle. Solutions are defined by their functionnalities (aka what they should do), not by their technology or means (how they should do it).

No prototype proposal is accepted at this stage.

Adopted solutions will lead to a new issue getting triaged in the [project management Kanban board](https://github.com/users/aurelienpierre/projects/1/views/1).

They might be conditional to researching theoretical and technical aspects to assess their feasibility, in which case they will be triaged into the _To research_ column of the Kanban board. The research findings will be added to the original issue until the feasibility of the solution is proven. When it is, the issue will be moved in the "To do" column of the Kanban board.

Adopted solutions might get directly triaged to the _To do_ column if they require only well-known tools and techs.

Ideally, the points to test and the testing procedure to validate the prototype should be written even before having a working prototype. At very least, the tests should ensure no regression happened in related features and tools.

### Prototypes come third

Only the issues triaged in the "To do" column of the [project management Kanban board](https://github.com/users/aurelienpierre/projects/1/views/1) will be worked on, by myself or by anyone willing to tackle them.

The prototype of the solution will be proposed in a pull request of a topic branch linking the original issue. Topic branches need to be rebased on the `master` branch e.g. `git rebase ustream master` or, if you update your branch locally with new master commits, do `git pull upstream master --rebase` or [globally set up git](https://git-scm.com/docs/git-pull#Documentation/git-pull.txt---rebasefalsetruemergesinteractive) to pull through `rebase` rather than `merge`. This ensures your branch history is kept clean with minimal effort, and keeps the `master` history clean too when your PR gets merged.

When the prototype pull request is reviewed and if it fits the [code quality standards](./coding-style.md) (see below) while fitting the specifications of the adopted solution, it gets approved and automatically triaged to the "To test/validating" column of the [project management Kanban board](https://github.com/users/aurelienpierre/projects/1/views/1).

### Validation comes fourth

Approved pull requests will be merged early in the `candidate` or `dev` branch for testing, depending whether they may break image editing histories (by adding new module parameters or changing database scheme). This branch will always be the master branch with all pull requests pending validation on top. This is meant to help testing from people who are not necessarily up-to-speed with manual git branches merging. Unlike the `dev` branch, `candidate` should not break your edits.

If no bug or breakage is reported after some time and the prototype fulfils its initial purpose correctly, it will get merged in `master` and the related issue will be closed and moved to the "Done" column of the [project management Kanban board](https://github.com/users/aurelienpierre/projects/1/views/1).

If the prototype proves itself unsatisfactory, it may be rejected and another one will need to be worked out.
