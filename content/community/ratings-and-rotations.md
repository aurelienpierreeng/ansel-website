---
title: "ratings and rotations"
date: 2025-05-09
slug: "ratings-and-rotations"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/ratings-and-rotations"
wayback_url: "https://web.archive.org/web/20250519014939/https://community.ansel.photos/view-discussion/ratings-and-rotations"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/ratings-and-rotations`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250519014939/https://community.ansel.photos/view-discussion/ratings-and-rotations).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-05-09.*

Two observations concerning version 16cfad7, self-compiled on Gentoo Linux. Both probably apply to some earlier versions as well:

\(1\) Presently I can only apply ratings (1-5 or R) to images in the Thumbnail view by means of the mouse. Keyboard inputs don't seem to work, especially when a picture is opened. Having to return to the Thumbnail view just in order to reject or rate a picture is not so nice.

\(2\) This is an old oddity in the module "Horizon and perspective" module. I usually have "Automatic cropping" set to "largest area". When manually applying some rotation, initially no cropping occurs and the black wedges are still visible. Only when I then change the angle a little bit, they disappear.

## Replies

**Lukas** — 2025-05-09

Hey ﻿@koslowj﻿,

there has been an update for keyboard shortcuts: You can assign your own shortcuts using "Edit \> Keyboard shortcuts" from the global menu. Regarding your (1) I have noticed too, that since this update ratings and color labels are not assigned by default. While I think that will be fixed soon, you could simply assign your own (1-5 and R).

