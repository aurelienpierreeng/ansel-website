---
title: "Some usability issues"
date: 2025-03-28
slug: "some-usability-issues"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/some-usability-issues"
wayback_url: "https://web.archive.org/web/20250427215827/https://community.ansel.photos/view-discussion/some-usability-issues"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/some-usability-issues`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250427215827/https://community.ansel.photos/view-discussion/some-usability-issues).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-03-28.*

While I haven't posted in a while, I've kept updating Ansel almost daily. I appreciate the amount of changes "under the hood", but certain usability features seem to have been lost, some of which actually worked quite well a while ago:

- presently I cannot rotate gradient-masks; I can shift them, bend them, change their width, but rotation seems to be broken.
- retouching is (still) very difficult:
- -- I cannot use the brush, it produces a weird sequence of rectangles along a curve with no discernible effect;
- -- I cannot use the ellipse, as it's shape is fixed; while I can grow and shrink it, I cannot grab the horizontal resp. vertical extreme points to change its shape
- -- even circles and paths are hard to use, as it seems impossible to smoothly move the selected areas; they jump around uncontrollably;
- adjusting horizons or vertical lines has become difficult: when drawing a straight line that should be vertical or horizontal in the modified picture, an angle is displayed, but the resulting rotation is by a different angle which does not achieve the intended result. I have to remember the initial displayed angle and then rotate manually by that amount.
- the filmstrip no longer moves along and doesn't indicate the picture that's currently being worked on; if I have several similar pictures, I lose track of which one I'm working on.
- currently I cannot unfold grouped pictures; so it becomes very difficult to delete a whole group, as only the top picture is selected and then removed, leaving the rest of the group unaffected.
- adjusting the exposure correction by clicking on the pipette on the right makes dng-pictures way too dark (this is a long-standing problem, not quite as important as the ones above)

Sorry about the rant, but losing features that already worked quite well is a bit annoying. I'm using version 62f9a4c, self-compiled on Gentoo Linux 6.12.16.

-- Jürgen

## Replies

**koslowj** — 2025-03-30

Unfortunately, all my formatting was lost, so the above may be hard to read (a preview function before posting might be useful). I've since found two other problems:

  

- grouping does not work anymore
- I no longer can assign a purple color label by pressing F5; F1 through F4 work as before, but a purple color label requires using the menus

---

**koslowj** — 2025-03-30

Rotation of images doesn't seem to be possible anymore.

---

**Jiyone** — 2025-03-30

yes it is on [1a5027b](https://github.com/aurelienpierreeng/ansel/commit/1a5027bc5861c2222205fcac2e641e36a15615f5)﻿ 😐﻿

---

**Jiyone** — 2025-03-30

Grouping is work in progress,

If you see F5 along the "purple color label" in the global menu, then it's correctly assigned.

There is a known bug where accels can't be fired in certain condition.

---

**Jiyone** — 2025-03-30

Ansel is currently work in progress, so yea there can be some broken features right now.

---

**Aurélien Pierre** — 2025-03-31

> Sorry about the rant, but losing features that already worked quite well is a bit annoying. I'm using version 62f9a4c, self-compiled on Gentoo Linux 6.12.16.

Ignorance is bliss. You don't know at what cost they were "working". Walls were holding because of the paint. There is a lot of shit going on under the GUI and you don't want to see how critically messed up they are.

Regarding masks and shapes: https://github.com/aurelienpierreeng/ansel/issues/418

Regarding showing/hiding grouped images: go in main menu Display -\> Collapse grouped images. That will affect all groups, the ability to affect only one has been removed.

---

**koslowj** — 2025-03-31

OK, thanks for the answers. I've been reporting these phenomena since I don't know if they might be unintended(?) consequences of other maintenance efforts. If useful/established features like the ability to unfold individual groups are removed, is this documented anywhere besides the source code? This would cut down on unnecessary reports from blissful users like me ;-)

