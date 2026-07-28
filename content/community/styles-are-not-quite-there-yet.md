---
title: "Styles are not quite there yet"
date: 2025-01-15
slug: "styles-are-not-quite-there-yet"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/styles-are-not-quite-there-yet"
wayback_url: "https://web.archive.org/web/20250520185425/https://community.ansel.photos/view-discussion/styles-are-not-quite-there-yet"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/styles-are-not-quite-there-yet`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250520185425/https://community.ansel.photos/view-discussion/styles-are-not-quite-there-yet).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-01-15.*

While styles are still not working as intended, there seems to be some progress: I've always been able to save styles. As of version 39ca7b3, when I attempt to apply a style in Darkroom mode, the image in question disappears, and clicking on the any preview image in the filmstrip leads to a Segmentation fault. Unfortunatley, the error message seems to be too long to fit into the history of my terminal, and is not written to the file /tmp/ansel_bt_MO6F02.txt that is supposed to contain the backtrace; it only contains one line "this is ansel 39ca7b3 reporting a segfault:". However, when I reopen ansel, the style has been applied to the image in question! Previously, when attempting to apply a style, ansel seemd to freeze and eventually offered me the option to either wait or to kill ansel. I don't recall the style being applied when I re-opened ansel. In the lighttable mode, the "styles" button on the top left does not show the available styles, though. If a complete error message is useful, I need some instructions as to how to save it.

## Replies

**koslowj** — 2025-01-17

Also some progress here: no more seg-faults, instead the option to close ansel or to wait. After closing and re-starting ansel, the style seems to be applied to the image in question.

---

**siamak** — 2025-05-08

I am new here and testing Ansel on My VMware on my mac using Linux Mint. So far I am loving it. It seems faster than Darktable for mac!! However, I have an issue with Style. Trying to delete a style that I created for testing. Now can not delete it. Clicking the Style on the menubar does not do anything. Is it disabled?

