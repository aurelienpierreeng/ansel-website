---
title: "strange behavior in \"Color Calibration\""
date: 2023-03-31
slug: "strange-behavior-in-color-calibration"
tags:
  - Community archive
forum_author: "Jofial"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/strange-behavior-in-color-calibration"
wayback_url: "https://web.archive.org/web/20231001124154/https://community.ansel.photos/view-discussion/strange-behavior-in-color-calibration"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/strange-behavior-in-color-calibration`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001124154/https://community.ansel.photos/view-discussion/strange-behavior-in-color-calibration).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Jofial** on 2023-03-31.*

Hello,

I have detected a strange behavior in one of the Ansel modules. Specifically in the "Color calibration" module.

I have observed the following:

1.  I create a new instance of "Color calibration".
2.  I duplicate this instance for the B&W preset.
3.  I move the present over the "color balance RGB".
4.  I activate the present for B&W and in the "History" it is duplicated. Now I have two "Color calibration" with the same numeral "1".

*\[attachment lost: image was hosted on the retired forum\]*

Now if I don't like the result and I want to undo what I have done, I go to "History" select the initial instance of "Color calibration" and....

*\[attachment lost: image was hosted on the retired forum\]*

The instance that I had duplicated is placed at the beginning of the module group "color".

*\[attachment lost: image was hosted on the retired forum\]*

If I compress the "History" to leave it as at the beginning, it is still at the beginning. If I activate it, this happens:

*\[attachment lost: image was hosted on the retired forum\]*

It cannot be moved (Ctrl+Shift) and I can only delete it. Or close Ansel and reopen it. Only then the duplicated instance disappears.

I have tried the same with "Exposure" and it doesn't behave like that.

*\[attachment lost: image was hosted on the retired forum\]*

My Ansel is an AppImage, specifically:

*\[attachment lost: image was hosted on the retired forum\]*

If I am doing something wrong, I would appreciate your corrections.

Note: I often duplicate this instance because I like B&W and this module is very versatile. The reason for placing it above the "RGB color balance" is so that it affects all the lower modules with respect to the modifications I have applied to them. It is the last module I use in the transformation to B&W.

Thanks for reading and trying

## Replies

**Aurélien Pierre** — 2023-03-31

That looks like an unhandled case mixing history (old code) and pipeline reordering (fairly new code, 3 years old but not methodically tested).

