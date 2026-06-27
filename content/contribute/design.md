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

## Pro tips from a seasoned designer

### Not all _software_ problems are _coding_ problems

Many problems don't require more tools (or toys), and more code. More code is always bad anyway, and should be avoided whenever possible. Very often, user's problem is they can't see how to bend existing features to fulfill their needs. This is solved by education, aka better documentation and more tutorials, and sometimes by better UI.

### Listen but don't listen to users

Users express what they want and what they like, never what they need. And you don't need to listen to them to know what it will be:

1. they will want the same thing as their neighbour just got,
2. they will like what they are used to. 

And then, for everything one likes, you will find another one to dislike it. So the Darktable way of solving conflict is to not solve conflict, but give everyone an option, a mode, a preference to enable that special thing they like, how they like it. This means more `case` in your `switch`, more nested `if`, more codepaths you will need to test now, debug, and maintain in the future, and then more preferences hiding the others in the pref window. Before you know it, the code is a tumor that nobody understands anymore, and fixing it only makes it more complicated.

When you scratch beneath the surface, you find than what people actually need is much closer to other people's needs than what they say they want. So you can reconcile the needs much easier than the desires, and without compromising. But then you have to trace the root needs below the will, and that takes abstraction skills and psychology.

### UI designers are dangerous idiots

Everybody who only sees, focuses and cares about the UI is a dangerous idiot. If your GUI is complicated, it means a lot more than just a "complicated GUI" : it means that __the complexity of your backend has reached your frontend__. I have found the hard way that GUI complexity is never separate, and can't be solved separately, from backend complexity and overall application architecture. GUI is not parallel to backend architecture, it's the termination of it.

The problem of UI designers is they typically don't code, or if they do, they suck at low-level programming and software architecture. So they focus on what little they see and understand (typical [streetlight effect](https://en.wikipedia.org/wiki/Streetlight_effect)), and they only produce non-actionnable designs that conflicts with what the software actually needs to work. Because that GUI is only connecting user input to the backend, and if we need that many widgets, it's because the architecture needs that many inputs. You can't escape it : to remove widgets, you need to remove inputs, which means your architecture will have to work with fewer degrees of freedom __first__. That starts with simplifying the backend, which means stinky refactoring of dusty old code nobody understands anymore.

You don't solve GUI issues with drawings and mockups, you solve GUI issues with solving backend issues. But then you need guys who understand both levels, and they may be too expensive for you.

### Ask yourself 36 times per day what was the problem you were trying to solve

It's super easy to get lost into technicalities when programming in a low-level language and fighting third-party libs or APIs, but sometimes the solution is simple and elegant and you got carried away too far into pointers and thread locks. Always go back to the initial problem at hand, that's your lifeline to simplicity.

What is the problem ? Who faces it ? When ? How often ? Doing what ? 

The best path is the simplest path towards your solution : low techs, little code, few layers.

### Document your shitty design

Many times, I completely redid a design while documenting it, because it's when you try to explain it that your realize it's too complicated to explain, which means it's too complicated to understand. If you can't explain your design in a couple of paragraphs, or your documentation has too many "if this, then that", there are usually two reasons :

1. your GUI doesn't expose the relevant info where user needs it, so you have to link half the documentation in your explanation to redirect users to everything they need to know or check before using the one thing you were documenting. The solution is to bring back relevant info where it's needed.
2. your GUI has too many trays, collapsible stuff, contextual behaviours, use cases or hidden preferences, and covering all bases makes you write a novel. The solution is to linearize the workflow, maybe remove options or split features.

GUI is how users control the backend, but it's also where they learn about existing features and what they do. The documentation should provide context, guidelines and references regarding how we do stuff, but the GUI should explain what it does itself.

Of course, there is an obvious limitation to that : in a photography application, users need to understand photography and its language, which involves things like _dynamic range_, _color gamut_, _tone mapping_, etc. The GUI should be self-explanatory on _how it's supposed to be used_, not remove the need to learn the trade (what should be done and how).

### Design is an iterative process

An application is a virtual world in which one small change can reorder how the rest of the ecosystem adapts around it. Therefore any design change can trigger the need to change other things around (refactor tools, move widgets, prune features). Which then might trigger the need to correct the initial change again. It's a step by step process in which it is foolish to even try to get everything right at each step, what matters it that each steps improves the environment from the previous.

Sometimes, (re)design can't be done by small steps but by large leaps : that's when you redo the architecture. These leaps will break many things around them, which is ok if the newer architecture is simpler and more robust overall, and if you give it some time to recover before taking the sledgehammer again. But that will create a transient state in which the new design will appear worse than the previous. This is telling us that how the design is percieved is not a valid input : design quality has to be assessed against its goals and evaluated with objective metrics, not with feelings and quick tests.

And sometimes, some steps are mistakes and should be reverted. The [sunk cost fallacy](https://en.wikipedia.org/wiki/Sunk_cost) should not be used to justify that some redesign should be kept because it was a lot of work to achieve. It's expected that all research & development doesn't make it into production.

### Whack-a-mole sessions mean your architecture has run its course

Whether you keep creating new bugs while fixing old ones, or you keep creating edge cases by extending some feature, it all points in the same direction : your architecture can't be bent any more because it has outgrown its design requirements. It might be that the backend has grown too convoluted or it might be that the existing architecture was really not planned for what you are trying to make it do, but both ways, you will have to redo the architecture and stop hacking in-place. Otherwise, you are only adding technical debt.

But then, the development cost changes scale and that saturday-afternoon project might become a month-long project.

### Best-practices are guidelines, not rules

Best-practices help developing sane habits and clean code, unless you don't understand the problem they tried to solve and use them out of their scope of validity. In that case, they become cargo cult : trying to mimic the effects in the hope that it will magically fix the causes too.

The first that comes to mind is code reuse/code sharing. If reusing the same code for (seemingly similar) features leads to too much internal branching (nested `if`, `switch`/`case`, etc.), to handle all possible paths, what you win on code volume is lost on cyclomatic complexity, and, by the way, your features are not as similar as you thought. 

Also, duplicating code might be a starting point to locally optimize the duplicate later: once you have the complete procedure in front of you, you may spot steps that can be cached or factorized. Whereas if the procedure is only opaque, high-level, reusable API methods, then you loose the ability to spot and remove redundant computations. So, there is a principle of __data reuse/sharing__ (aka caching computed data that will be used later with no change, to spare CPU cycles) that can be made impossible by __code reuse/sharing__, because it obfuscates and abstracts data lifecycle.

This becomes critical on pixel loops: you want to collapse all pixel-wise operations into the same loop, to pay the memory I/O price only once. Which means that you will have to re-implement the same affine correction ($y = a * x + b$) into each loop using it, rather than having a reusable method that does just that in its own loop.

### Don't brace yourself

If you find yourself overwhelmed by some cryptic and random bugs that keep coming and that you can't make sense of, don't keep fighting blindly and take a step back. Then instrument debug helpers, or higher-level managers that keep track of internal states and give you a map of the software data values at any relevant point in its lifecycle. This is especially critical in asynchronous setups, where several threads create, access or compute stuff in parallel on different timelines, and the actual ordering sequence depends on runtime context.