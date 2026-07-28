---
title: "Ctrl-Key doesn't work for selecting shapes in the retouch module"
date: 2025-01-20
slug: "ctrl-key-doesn-t-work-for-selecting-shapes"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/ctrl-key-doesn-t-work-for-selecting-shapes"
wayback_url: "https://web.archive.org/web/20250514051330/https://community.ansel.photos/view-discussion/ctrl-key-doesn-t-work-for-selecting-shapes"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/ctrl-key-doesn-t-work-for-selecting-shapes`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250514051330/https://community.ansel.photos/view-discussion/ctrl-key-doesn-t-work-for-selecting-shapes).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-01-20.*

In version 43e3443 the retouch module shows another small problem: in order to repeatedly use one of the given shapes, one is supposed to press Ctrl when selecting the shape. Presently this does not work anymore.

## Replies

**Aurélien Pierre** — 2025-01-20

It's not a problem, the special behaviours triggered by "silly key shortcut + mouse click" regarding masks are being removed. Since masks are supposed to be drawn, and drawing devices are Wacom tablets but not keyboards, those silly modes are migrated to a toolbar that will be clickable with a pen.

---

**koslowj** — 2025-01-21

I'm not quite convinced. General masks, OK, but having to use a Wacom tablet just for efficiently fixing some blemishes in a portrait or dust spots that require just circular shapes seems overkill. Can the user at least re-create those short-cuts?

---

**Aurélien Pierre** — 2025-01-24

Wacom tablets are only a particular kind of pointing device. Pointing devices should not require keyboard interaction for typical user events. Here, the Ctrl+click feature is well hidden to users, and is used as a workaround for lack of proper mask GUI allowing to quickly toggle ON/OFF the mask editing mode.

Retouch masks are general masks. There is only one library for all masks in the software. But the continuous editing mode is a special case inside a special case, inside generic masks. Special cases are being removed, because they are a liability (plus the code has been copy-pasted everywhere, it's a mess).

Masks are currently being reworked entirely. See https://github.com/aurelienpierreeng/ansel/issues/418

