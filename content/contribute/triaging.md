---
title: Triaging issues
date: 2024-07-15
weight: 8
---

This page is written for people helping triaging issues on the issue Github tracker.

## Preamble

- Any project has limited resources, the difference between projects will be the threshold.
- Any project should have clear goals. For Ansel, it is to manage, edit and export collections of RAW images on a desktop computer by an end-user who is not a CLI user but puts visual image quality above all else.
- Any project has overhead, that is actions requested to meet the goals, although they are not directly the goal and therefore should stay minimal. For Ansel, it is the maintenance of the website, documentation, servers, nightly-built packages, code cleanups, debugging, regression tests, cross-OS support, issues triaging, etc.
- Goals and overhead should be expressed in terms of __tasks__ to perform in order to __solve problems__ (issues). If no problem to solve, then no work to do: status quo is great too, don't create work for the sake of it.
- because of resource limitation, tasks have to be ordered depending on their priority.

The following document aims at defining this priority.

Ansel was forked on Darktable because Darktable has no clear goal, no priority management, and the overhead is increasing every year, which is the trademark of burn-out factories and is unsustainable mid-term.

## Defining good issues

Project management works better with SMART tasks. S.M.A.R.T. stands for:

- Specific _(ex: finding URI of pictures Ansel exported on the filesystem and open them)_
- Measurable _(ex: number of clicks/steps required, CPU time to perform the task on some target platform)_
- Actionnable/Achievable _(ex: can be integrated on current code base with only minor rewrites, needs only a few hundreds of lines of code)_
- Relevant/Reasonable _(ex: is part of a fairly-general photography workflow, would be used by a signicative part of users)_
- Time-bound _(ex: requires at most 70 man-hours)_.

__A good issue is one that leads to a SMART task__. For Ansel, that means issues focusing on a clearly-defined problem affecting a clearly-defined step of the picture editing workflow ("I have problems doing X because Y and I would like Z").

Questions and general discussions should happen on <https://community.ansel.photos>.

Bad issues are:

- too broad _("automatize workflow", "improve UX")_,
- focusing on the means _("use neural network", "extend tone curve")_ instead of the goal _("mask the sky out", "control saturation selectively")_,
- out of scope _("port to Android", "switch to Qt", "switch to Vulkan")_
- affecting third-party libraries/projects _(Rawspeed, Libraw, Exiv2, Lensfun, GPhoto2, Gtk, etc.)_,
- too subjective _("please do things like that other software I used in the past and really like")_. What user A likes will be disliked by user B, we can't work with that.

Side note: some issues may sound like things in need for more code, whereas they actually need better documentation of current features, or slight GUI touch-ups (renaming labels, reorganizing widgets), so that's something to keep in mind before jumping on the guns.

## Defining priorities

In an ideal world, tasks (aka good issues) would be added to the to-do list in a linear fashion, as milestones are reached, and their code product would be tested for a couple of weeks while the code is otherwise frozen, until it is proven that everything holds, in which case we would unfreeze the code and move on to the next task in the to-do list.

Problem is this implies everybody on deck for the testing phase, so it doesn't freeze the code for too long. Because that doesn't happen (people take vacations, have kids, move homes, change jobs, have a life…), we have to parallelize testing the product of previous tasks while we are working on the next, to be efficient.

This is to say the to-do list is not linear and some important things might get added or removed dynamically, depending on what happens. The problem is then to determine what constitutes something important enough as to disrupt the schedule.

There is no definitive rule here, so you will have to use your best judgment, but there are some rules of thumbs:

- something recently broken (a regression) is easier to spot and fix sooner than later, so in the grand scheme of things, it might be less work overall to do it sooner,
- something that prevents the software from working at all (crash, corrupted output files, loss of data) is critical enough to take precedence over improvements and more cosmetic fixes,
- something that impacts a large number of users and where no work-around can be found will take precedence too.

On the contrary, anything impacting a small number of users, or niche/secondary features, or minor annoyances that have work-arounds, are not critical enough to justify disrupting the schedule. Those will be added on the queue in a first-in/first-out way.

Ansel has 4 levels of priorities, set as issue tags:

- `priority: critical`: Affects basic and core functionnalities of the software in a way that prevents it to work at all,
- `priority: high`: Affects basic and core functionnalities of the software in a way that severly degrades usability,
- `priority: medium`: Affects basic and core functionnalities of the software in a way that mildly degrades usability (work-arounds available),
- `priority: low`: Affects optional and niche functionnalities

## Defining milestones

Modules parameters are saved as binary blobs. We deal with these by handling their bit size. When a new parameter is added, we need to write code to handle the conversion, aka the different bit size of the parameter blob, and we increase the internal version of modules parameters. No code is written for backward compatibility, so pictures edited with newer modules can't be opened in older modules. Modules parameters are used in styles, in presets and in XMP files too.

For these reasons, any issue that would lead to adding parameters in modules (either the image processing modules in darkroom, or the lighttable modules dealing with export & metadata), would break backwards compatibility and needs to be planned for the next major version of the software (1.0, 2.0, 3.0, etc.). This means that only GUI & behaviour changes are allowed within the same major version, and can be planned for the next minor version (0.1, 0.2, 0.3, then 1.1, 1.2, 1.3, etc.).

Ansel has only 2 milestones at all time: the next minor version and the next major version.

## Defining difficulty

Difficulty is directly related to the amount of work required by a task, that is:

- the number of lines of code to write,
- the number of files to change,
- the probability of breaking existing features, leading to extra testing work,
- the existence of similar features or written theory to achieve the task,
- the overhead of making changes and features work reliable across operating systems.

Estimating difficulty in an accurate fashion is something only an experienced developer can do.

## Defining nature

The nature of the issues is handled with labels. We have:

- regressions (stuff that use to work but was broken by recent-ish changes),
- bugs (stuff that has never worked in the past years),
- enhancements (stuff that needs to be improved or added),
- wontfix (not a bug, but a feature or design choice or necessity imposed by third-party dependencies),
- question (should not be on Github, but on <https://community.ansel.photos>),
- duplicate (issue already reported),
- unclear (issue can't be understood),
- invalid (issue is "bad" according to the above definition of a good issue).

## Priority are relative

See <https://www.youtube.com/watch?v=8fnfeuoh4s8>. Having to repair the car in order to change the light-bulb is a great metaphor of doing code on a 12 years-old software having hundreds of thousands of lines of code written by people who didn't talk to each other and didn't document their changes. Fixing the car is not top-priority until it becomes the pre-requisite to fix the high-priority light.

## Your triager job

Ultimately, only an experienced developer will be able to accurately triage issues. But reason requires that an experienced developer would be employed to do things that only an experienced developer can do: write simple code to efficiently solve technical problems requiring some amount of theory and design.

The trade-off is to have triagers help prioritize obvious issues so developers only have to deal with the least-obvious issues and focus on coding.

1. label only issues you understand and you feel comfortable triaging. You don't have to do them all, it's fine if you don't know.
2. for issues you understand:
   - assign a priority label if you can,
   - assign a nature label if you can,
   - assign a milestone if you can,
   - immediately close the issue if it is invalid or duplicate.
3. for issues you don't understand:
   - try asking more questions to the author,
   - ensure authors fill all relevant info (OS, hardware, reproducing steps for bugs),
4. it's better if you do nothing than if you do it wrong: issues without labels are easier to spot than issues with wrong labels.
5. don't hesitate to call-in video meetings: better sit together for 30 min to have a productive chat and adjust decisions than exchange endless threads of useless messages.

Thank you !
