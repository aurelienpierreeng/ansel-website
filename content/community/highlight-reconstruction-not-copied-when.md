---
title: "Highlight reconstruction not copied when copying the development stack"
date: 2024-09-24
slug: "highlight-reconstruction-not-copied-when"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/highlight-reconstruction-not-copied-when"
wayback_url: "https://web.archive.org/web/20250519020908/https://community.ansel.photos/view-discussion/highlight-reconstruction-not-copied-when"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/highlight-reconstruction-not-copied-when`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250519020908/https://community.ansel.photos/view-discussion/highlight-reconstruction-not-copied-when).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2024-09-24.*

When copying the development stack from a picture where highlight reconstruction is active to similar pictures, in the result highlight reconstruction is not active (but set to the value of the first picture). So I need to switch it on manually. Again, version 85f2b8b, self-compiled under Gentoo-Linux.

## Replies

**Jiyone** — 2024-09-24

You should report bug on github

[https://github.com/aurelienpierreeng/ansel/issues](https://github.com/aurelienpierreeng/ansel/issues)

---

**Aurélien Pierre** — 2024-10-21

Might be related to https://github.com/aurelienpierreeng/ansel/issues/376

---

**koslowj** — 2024-11-16

Possibly a related problem, in version [922.g7f23d9d38](https://github.com/aurelienpierreeng/ansel/releases/download/v0.0.0/ansel-0.0.0+922.g7f23d9d38-win64.exe), self-compiled on Linux:

For black-and-white pictures I like to develop the color version first, then open a second instance of the color calibration and move this above filmic in the development stack. Then I use this second copy as a channel mixer.

When I try to copy such a development stack to a different picture, the second instance of the color calibration is moved back to its original position and no longer sits above filmic; I have to move it back there again.

