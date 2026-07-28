---
title: "Bottom panel suddenly missing in light table"
date: 2023-09-29
slug: "bottom-panel-suddenly-missing-in-light"
tags:
  - Community archive
forum_author: "Alain Oguse"
forum_category: "Configuring help"
forum_url: "https://community.ansel.photos/view-discussion/bottom-panel-suddenly-missing-in-light"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/bottom-panel-suddenly-missing-in-light`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Alain Oguse** on 2023-09-29.*

Windows 10 - Ansel ( ansel-eb70788-win64.exe )

Bonjour à tous,

Suddenly the bottom panel disappeared into the light table. But it is still present in the form of a very thin edging (1mm) at the foot of Ansel's window in the same gray as the left and right panels. And I can't find any way to enlarge it...

I tried to pass all values bottom_visible to TRUE in the anselrc file, but without success. I also deleted this file then relaunched Ansel without further success.

Furthermore, I also noticed that in the darkroom I no longer have access to the button allowing you to clone an image.

Last info, without being entirely certain, this seems to have happened after installing the ansel-eb70788-win64.exe version. I then reverted to ansel-26acfc2-win64.exe. But still no change.

Thank you for any help you can give me.

## Replies

**Jan-Jan** — 2023-09-29

- +1; I'm experiencing the exact same problem using AppImage on Ubuntu
- problem persists even if I go back 3 versions
- I see no errors in the command line

---

**Jan-Jan** — 2023-09-30

I suspect that this is WAI

---

**Alain Oguse** — 2023-10-02

I just noticed that when exporting, if I choose a file format it is the format just below the one I chose which is selected. For exemple, to export in TIFF I must therefore select PPM :-(

It looks like we are facing a lag issue at the bottom of the left panel.

---

**photux** — 2023-10-05

Hi,

I see the same behavior.

Below is my configuration

> Ansel ff82b58, Debian 11 (bullseye), Xfce desktop

---

**Alain Oguse** — 2023-10-07

Oops ! Aurelien Pierre has just told me that the command to make clones can now be found in the general menus / Edit / Duplicate existing development (Ctrl+D). This modification seems relevant to me ;-)

