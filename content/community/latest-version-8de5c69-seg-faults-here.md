---
title: "latest version 8de5c69 seg-faults here when compiled under Gentoo Linux 6.12.21; version dd6127b works fine"
date: 2025-04-15
slug: "latest-version-8de5c69-seg-faults-here"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/latest-version-8de5c69-seg-faults-here"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/latest-version-8de5c69-seg-faults-here`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-04-15.*

I don't recall having seg-faults for a long time, but unfortunately, version 8de5c69 does so on my system. Fortunately I saved my previous version, which happened to be dd6127b, and it starts fine, even after recompiling it. Unfortunately, the file /tmp/ansel_bt_2MRV42.txt only contains the line "this is ansel 8de5c69 reporting a segfault:" and nothing else. The on-screen error messages start with

\[lib_load_module\] failed to open \`midi': /opt/ansel/lib64/ansel/plugins/lighttable/libmidi.so: undefined symbol: dt_register_input_driver

\[lib_load_module\] failed to open \`menu': /opt/ansel/lib64/ansel/plugins/lighttable/libmenu.so: undefined symbol: dt_ui_thumbtable

\[lib_load_module\] failed to open \`filmstrip': libOpenEXR-3_2.so.31: cannot open shared object file: No such file or directory

and then go on for quite a while (which I can send, if required). Please advise how I can supply more meaningful error messages. What's also strange is that I cannot find dd6127b in the list of commits. We've been on vacation for a week and it cannot be much older than that. \[I just noticed that I have openexr version 3.3.2-r1 installed.\]

## Replies

**koslowj** — 2025-04-17

Concerning the mystery code number dd6127b: in the file build/CPackConfig.cmake in the source-tree that produces this version of ansel, the code d005a00 is mentioned instead. This indeed corresponds to a commit of about 2 weeks ago. I suppose that going through the subsequent patches one by one I should be able to find the one where things go wrong on my system, like looking for a bad Easter egg ;-)

---

**koslowj** — 2025-04-18

The AppImage for 8de5c69 works fine, so the problem must be with the rest of my set-up :-(( Should have tried this earlier.

---

**Aurélien Pierre** — 2025-04-18

You need to delete /opt/ansel completely. What happens here is the midi and menu plugins were deleted in the source code since one of your earlier builds, but you still have their .so files in your install, and Ansel will load them automatically.

---

**koslowj** — 2025-04-19

Thanks, that does the trick!

