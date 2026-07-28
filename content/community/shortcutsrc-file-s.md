---
title: "shortcutsrc file(s)"
date: 2023-04-03
slug: "shortcutsrc-file-s"
tags:
  - Community archive
forum_author: "bridgemen"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/shortcutsrc-file-s"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/shortcutsrc-file-s`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **bridgemen** on 2023-04-03.*

Duplicate lines in shortcutsrc file.

appimage version: Ansel-0.0.0+283.g9405171cc-x86_64.AppImage

linuxmint 21.1

  

When the first time ansel in started up then it shows in

\$HOME/.config/ansel 2 shortcutsrc files, **both at 5.4kB**.

  

After starting and stopping ansel a few times even without editing photos

and not editing trough "Edit - Key Shortcuts", I find in the config directory 4 files shortcutsrc:

shortcutsrc ***6.2kB***

shortcutsrc.backup 6.2kB

shortcutsrc.defaults ***5.4kB***

shortcutsrc.edit 6.2kB

I assume only shortcutsrc is used while using ansel gui ?

  

While shortcutsrc.defaults remains at 5.4kb, the file shortcutsrc has 6.2kB

and contains 16 double lines:

  

type in terminal:

sort shortcutsrc \| uniq -c \| grep "2 "

this gives:

  

   2 a;shift;ctrl=global/Selection/Clear selection

   2 b;shift;ctrl=global/Display/Toggle bottom bar visibility

   2 d;shift;ctrl=lib/image/duplicate virgin

   2 f;shift;ctrl=global/Display/Toggle filmstrip visibility

   2 g;shift;ctrl=lib/image/ungroup

   2 h;shift;ctrl=views/darkroom/histogram/hide histogram

   2 i;shift;ctrl;alt=global/reinitialize input devices

   2 i;shift;ctrl=lib/import/import from camera

   2 l;shift;ctrl=global/Display/Toggle left panel visibility

   2 n;shift;ctrl=views/darkroom/hide navigation thumbnail

   2 o;shift=views/darkroom/raw overexposed/toggle

   2 p;shift;ctrl=global/toggle focus peaking

   2 r;shift;ctrl=global/Display/Toggle right panel visibility

   2 s;shift=lib/map_settings/thumbnail display

   2 t;shift;ctrl=global/Display/Toggle top bar visibility

   2 v;shift;ctrl=global/Edit/Paste development (parts)

  

You also see those duplicates in "Help - Table of key shortcuts", column global,

and unsorted.

## Replies

**Aurélien Pierre** — 2023-04-03

Actions can be mapped to more than one combinations of shortcuts, if that's what you mean. I don't understand the problem here. What doesn't work ?

---

**bridgemen** — 2023-04-04

Hi Aurélien, thanks for the reply,

I was just wondering why there is for example twice the line

" b;shift;ctrl=global/Display/Toggle bottom bar visibility "

occurs in shortcutsrc, as some other lines as mentioned earlier ...

Eric.

---

**Aurélien Pierre** — 2023-04-04

Well, the whole thing is coded like shit, so that might be why. You never know what you are going to break when change something. Be my guest… https://github.com/aurelienpierreeng/ansel/blob/master/src/gui/accelerators.c

I'm seriously considering removing this at all.

---

**bridgemen** — 2023-04-05

Hi Aurélien, thank you for your answer.

I don't know much about programming, only (shell) basic scripts to automate somewhat, so ...

I like your setup of the graphical environment of ansel because I find it more organized and therefore easier to use.

I follow further developments.

Eric.

