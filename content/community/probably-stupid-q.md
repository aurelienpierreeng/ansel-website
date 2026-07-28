---
title: "Probably stupid Q"
date: 2023-03-22
slug: "probably-stupid-q"
tags:
  - Community archive
forum_author: "newmikey"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/probably-stupid-q"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/probably-stupid-q`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **newmikey** on 2023-03-22.*

I cannot find the RGB Levels module even if I filter on "levels". Has it been ditched in favour of something newer? If no, where should I find it and if yes, how can I manually adjust levels?

Version info: I'm running the V0.0.0+280~g34f3da09a as an appimage on Manjaro Linux

This issue (if it is an issue and not my inexperience with Ansel) is present both on my laptop as well as my desktop

*\[attachment lost: image was hosted on the retired forum\]*

## Replies

**Scorpion078** — 2023-03-22

You have to use the color calibration module.

The first tab is CAT what is used for white balance after that you RGB tabs for each of the color channel.

---

**newmikey** — 2023-03-22

That doesn't really look like the levels tool described in the documentation or the one I'm used to in DT - I think you're very kind to help but I may have misrepresented my question. This is the tool I'm searching for:

*\[attachment lost: image was hosted on the retired forum\]*

---

**Scorpion078** — 2023-03-22

The levels and rgb levels modules are deprecated

---

**Scorpion078** — 2023-03-22

Check this link:

https://ansel.photos/en/doc/special-topics/from-darktable/#modules-deprecated

---

**Scorpion078** — 2023-03-22

RGB levels is display referred, Ansel's philosophy is scene referred

---

**newmikey** — 2023-03-22

Thanks for the help!

---

**Aurélien Pierre** — 2023-03-23

The whole story is the GUI of levels expect bounded signals in 0-100%. Scene-referred is unbounded by nature, so it's not compatible. Also, the levels tools is internally just an offset (black) and a gain/exposure (white), with a power function in the middle (grey), so you have already all that in color balance RGB. More on https://ansel.photos/en/workflows/scene-referred/

---

**newmikey** — 2023-03-23

Thnks!

