---
title: "Vectorscope size"
date: 2024-12-21
slug: "vectorscope-size"
tags:
  - Community archive
forum_author: "Massimo"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/vectorscope-size"
wayback_url: "https://web.archive.org/web/20250501035617/https://community.ansel.photos/view-discussion/vectorscope-size"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/vectorscope-size`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250501035617/https://community.ansel.photos/view-discussion/vectorscope-size).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Massimo** on 2024-12-21.*

I struggle to set up the size of GUI with my system. My monitor is 5120x2880, 27 inches (218 DPI) and Windows resize is set to 250%. The best compromise is character 5.0 points (minimum) and DPI GUI and text 218. I would prefer a smaller layout, but if I reduce DPI I get non homogeneous text.

But the problem is with vectorscope. It resizes downto 22% of the display approximately (that is huge), then it is clipped on both sides.

By the way, I'm using 0.0.0+922~g7f23d9d38 on Windows 10.

## Replies

**Massimo** — 2025-04-18

Having understood that is possible to change the GUI in the CSS text box, I roll back to system font size and resolution, that yields a much better overall layout size, and I try to fix the non homogeneous text with CSS tweaks.

Unfortunately I don't find any way to reduce the huge text shown in left and right panel, see attached image. Does someone has a suggestion?

*\[attachment lost: image was hosted on the retired forum\]*

