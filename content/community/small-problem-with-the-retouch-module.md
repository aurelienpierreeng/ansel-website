---
title: "Small problem with the retouch module"
date: 2025-01-18
slug: "small-problem-with-the-retouch-module"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/small-problem-with-the-retouch-module"
wayback_url: "https://web.archive.org/web/20250520201650/https://community.ansel.photos/view-discussion/small-problem-with-the-retouch-module"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/small-problem-with-the-retouch-module`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250520201650/https://community.ansel.photos/view-discussion/small-problem-with-the-retouch-module).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-01-18.*

The elliptical shape in the retouch module gives me some problems: after initially placing an ellipse to remove a blemish, I no longer can shift or rotate it at will. It seems to jump back into its original position in most cases; rotation especially is almost impossible. Edit: forgot to mention that this concerns version e2f5d0a.

## Replies

**koslowj** — 2025-01-19

In version 55f5596 ellipses still show some reluctance to be placed exactly where I want them, both with respect to rotation as well as translation. Circles seem to show this also for translation. These operations used to be much smoother.

---

**Aurélien Pierre** — 2025-01-19

See https://github.com/aurelienpierreeng/ansel/issues/405

---

**koslowj** — 2025-01-19

Apparently, this phenomenon is not restricted to the retouch module but affects elliptical masks in other settings as well. Other masks, e.g. triangular ones, are also difficult to translate precisely: the seem to jump a little bit from their intended position.

