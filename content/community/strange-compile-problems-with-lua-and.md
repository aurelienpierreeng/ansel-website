---
title: "Strange compile problems with Lua and clang compiler"
date: 2023-11-28
slug: "strange-compile-problems-with-lua-and"
tags:
  - Community archive
forum_author: "Maurizio Paglia"
forum_category: "Installing help"
forum_url: "https://community.ansel.photos/view-discussion/strange-compile-problems-with-lua-and"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/strange-compile-problems-with-lua-and`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Maurizio Paglia** on 2023-11-28.*

I switched to Suse Tumbleweed and compiled Ansel on my own.

No problem detected with my previous Suse Leap 15.4 distro.

Now seems Ansel cannot detect Lua on my system so Lua support is not included.

Moreover I receive an error (or advice?) message saying a clang compiler cannot be found despite the fact clang is duly installed on my system and Ansel is compiled and installed.

Can someone help?

Thanks,

Maurizio

## Replies

**Aurélien Pierre** — 2023-11-28

The CLang issue may be linked to https://github.com/aurelienpierreeng/ansel/commit/91bac822b26f2b35cfaa6761bf7b13b1aface503

Ansel looks for Lua 5.3 exactly, if I recall correctly, it doesn't accept anything older or newer. But anyway, since the Lua overlay is looking for a binary called \`darktable\` (it's hard-coded), it has never worked since renaming to Ansel and that needs to be changed upstream.

---

**Faber** — 2023-12-22

Do you know what it would take to get lua scripts working in Ansel?

I really appreciate what you have done with Ansel, and have been wanting to switch to it for awhile. Darktable is now grabbing/stealing global window manager keybindings (super key) and that was a final straw for me.

I've grown accustom to a couple workflow related scripts and would like to get them working before jumping fully into Ansel. I'm by no means a developer, but if the required fixes are on the lua side only, I might be able to hack it.

Any pointers would be greatly appreciated.

---

**Maurizio Paglia** — 2024-01-01

I have lua 5.4.6 installed on my distro and now Ansel can compile with lua support.

Some scripts works out of the box, other cannot and other (in my case photils.lua) cause a segmentation fault.

---

**Maurizio Paglia** — 2024-01-03

Recompiled Ansel right now from sources and lua support disappeared again... sorry...

---

**Aurélien Pierre** — 2024-01-15

The default CMake build options don't enable Lua support by default because Lua is currently wonky (as you saw, some plugins work, some make the app crash). You can manually enable it using CMake options at building.

