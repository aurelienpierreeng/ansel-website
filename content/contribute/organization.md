---
title: Project organization
date: 2024-07-14
weight: 4
---

The project is run by Aurélien Pierre, who tries to balance his photography work (mostly unexistent since 2019), developing & maintaining the software, and handling user education in individual training sessions. This calls for low-overhead project management strategies, relying on cloud-based collaborative tools.


## Departments

### Software development

Development is done on [Github](https://github.com/aurelienpierreeng/ansel),

Feature requests are not taken from users at this point. Users are consulted by the developer regarding their needs when a (re)design project is started. This is to prevent disruptive inputs at random times that would only slow-down the opened projects.

The time planning of issues being currently worked is available on the [Kanban board](https://github.com/orgs/aurelienpierreeng/projects/1). Developers can pick issues in the _To Do_ column. New changes to watch and test are in the _Done_ column. Pull requests that don't follow the [design protocol](./design.md) will be refused.

Developers that need help, introduction to the code base, or code reviews can [book an appointment with Aurélien Pierre](https://cal.com/aurelien-pierre/developer-mentorship) to do it by videoconferencing (possibly using [Visual Studio Live Share](https://visualstudio.microsoft.com/fr/services/live-share/)).

News about development projects closed or milestones are published on the [blog](/news). A dedicated [Matrix chat](https://matrix.to/#/#ansel-dev:matrix.org) centralizes all updates and notifications from new commits, Github issues, new blog posts and new community forum posts.

### Nightly builds

Installable packages for Windows (`.exe`) and Linux (`.AppImage`) are built automatically on Github around 1:00 am UTC, if new commits were pushed the day before. The direct download links are published to a dedicated [Matrix chat](https://matrix.to/#/#ansel-builds:matrix.org), so you can get see the notifications pop and get the new builds, all in one place.

Nightly builds are meant to promote early testing from users who can't or don't want to build themselves from source. They can be instable.

### Bugs

Bugs (as in, stuff that breaks the software), are handled on [Github](https://github.com/aurelienpierreeng/ansel/issues) when they are confirmed.

They can be discussed on [the community forum](https://community.ansel.photos) or the [Matrix chats](https://app.element.io/#/room/#ansel:matrix.org), especially to confirm that they are actually bugs (and not design changes).

Opening issues on Github is important to include them to the project management and track them from a single place.

{{< note >}}
More details : read [a culture of problem solving in open-source software](https://community.ansel.photos/view-discussion/a-culture-of-problem-solving-in).
{{</ note >}}

### Website

The website is generated using [Hugo static website builder](https://gohugo.io/), which is a fairly low-overhead way of writing technical websites using Markdown syntax.

The source code of the website is on [Github](https://github.com/aurelienpierreeng/ansel-website/). You can correct typos or help translating directly by editing the source files on Github UI. Otherwise, you can install Hugo on your computer, then the `Readme` file on Github explains how to build a preview website locally, using a test server on your computer, to better preview (and debug) your changes.

Changes to the website have to use the typical Git + Pull Request (on Github) workflow, which can deter non-programmers, but it's the least shitty way of remote-collaborating on somethng text-based, while ensuring reversible versionning and backups.

### Documentation

The documentation is not included in the website repository for licensing reasons (GPL v3), so it is imported as an external Hugo module. The source code is on [Github](https://github.com/aurelienpierreeng/ansel-doc), and everything else applies the same as for the website. The `Readme` presents the available shortcodes that you can use to format the content, in Markdown files.

There is a caveat, though, if you want to build the documentation locally, because it imports the theme from the main Ansel website, so the easiest way is actually to build the main website while linking locally the documentation as a module. The procedure is detailed on the `Readme` of the main website.

The documentation is currently undergoing structural changes, along with software design changes, so don't hesitate to ask on [Matrix](https://matrix.to/#/#ansel-en:matrix.org) if you have a particular project in mind, before you commit to something on the verge of being removed.


### Teaching and user education

As many "bugs" report show, insufficiently-trained users have wrong expectations, and if you take their feature requests too seriously, you end up with crippled software duplicating features and CPU load. Those need to be solved at the root : with teaching.

1. The community forum has a place to post links to [video tutorials](https://community.ansel.photos/videos-home),
1. The community forum has a place for users to write educational [blog posts](https://community.ansel.photos/posts-home),
1. The [documentation](../doc) is meant to provide usage information closely tied to the software GUI, so users could learn about the features in linear order of GUI appearance.
1. The main website [workflow](../workflows/) section is meant to provide usage information tied to a specific task to achieve, so users could learn "how to".
1. The main website [resources](../resources/) section is meant to provide background theoritical information to help building a deeper understanding of color and photography, and empower users to troubleshoot retouching issues themselves.
1. Users can [book 1-on-1 training sessions](https://cal.com/aurelien-pierre/darktable-ansel-editing-class-en) (classes) with Aurélien Pierre, for faster and more focused training.


## Management

This is mostly a one-guy operation, so things have to be efficient and low-overhead. Which requires some discipline.

### Programming management

There are usually 2 open programming projects at the same time, that are chosen because independent from each other. This allows to switch to project #2 while waiting for user feedback on changes made in #1, in a way that still allows to identify which one created regressions and new bugs. Think of it as alternate single focus.

In the middle of a project, the developer will typically not deal with, care about nor listen to issues related to anything but that project, because brainpower is a precious resource, faster spent than recovered. In particular, feature requests on other parts of the software will be disregarded.

The day-to-day focus is subjected to change unexpectedly, depending on the shit uncovered while fixing other shit, thanks to Darktable crappy legacy of semi-broken non-modular madness-inducing spaghetti code, which often requires partial or full rewrites (in any case, cleaning up) before attempting to fix anything (in a way that doesn't induce more future problems, that is).

### Communication

We live in a World where the volume of information and communication has become overwhelming and humans don't have the bandwidth to process all of it. Endless threads and unregulated conversations are actively harming communication by diluting important information and exhausting the reader. **Discussion is solely meant to reach an understanding and proceed to actionable decisions**. There is a subtle trade-off between completeness and conciseness to find.

For chat or general questions, please use the [Matrix space](https://app.element.io/#/room/#ansel:matrix.org). But even there, conciseness is key.

In pull requests and issues, whether on Github or on the [Community forum](https://community.ansel.photos) please try to stay concise and on-point :

* Technical details (like OS, use of OpenCL, screen size, etc.) should make use of bullet-point lists.
* Screenshots and drawings can go a long way.
* If you are replying to a particular point or person, quote the section of text you are replying to.
* Break your text into paragraphs of roughly 4 to 8 lines, but avoid sending each sentence to a new paragraph.
* Keep in mind everybody speaks English but very few people are native speakers, so try to stick to basic [Globish](https://en.wikipedia.org/wiki/Globish_(Nerri%C3%A8re)).

Good principles on issues/tickets interactions can be found [here](https://www.yegor256.com/2014/11/24/principles-of-bug-tracking.html).

## Updates and notifications

Many centralized and automated ways are offered to keep track of what's new in the project :

- The main website has a central RSS feed, where new and updated page goes : [global RSS](../index.xml),
- For more granularity, each section of the website (News, Doc, Workflows, etc.) has its own RSS feed too. The <i class="fas fa-rss-square"></i> icon you find on section index pages and on every page links to that RSS feed in the current language.
- The Community website has a [central public RSS feed](https://community.ansel.photos/m/timeline/rss/public/) too (truncated to the 25 most recent events).
- Code changes can be tracked from commits index on [Github](https://github.com/aurelienpierreeng/ansel/commits/master/), or using the [Github Atom feed](https://github.com/aurelienpierreeng/ansel/commits/master.atom) (truncated to the 20 most recent commits). Commit messages are usually quite verbose and should explain well enough what was changed and why.
- New commits, Github issues updates (created, edited, closed), new community posts and new website pages are all posted to a [dedicated Matrix chat](https://matrix.to/#/#ansel-dev:matrix.org).
- Nightly builds packages are posted to a [dedicated Matrix chat](https://matrix.to/#/#ansel-builds:matrix.org). They are also listed on the [Github pre-release page](https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0).
- Open and closed project/issues can be seen on the Github [Kanban board](https://github.com/orgs/aurelienpierreeng/projects/1).

{{< note >}}
The website RSS feeds are untruncated (all items since forever are kept), and have the `pubDate` and `updated` tags properly set. On each page content update, the `guid` tag is changed to force RSS readers to bump updated pages on top.
{{< /note >}}
