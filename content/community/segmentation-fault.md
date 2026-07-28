---
title: "Segmentation fault"
date: 2025-05-12
slug: "segmentation-fault"
tags:
  - Community archive
forum_author: "Maurizio Paglia"
forum_category: "Installing help"
forum_url: "https://community.ansel.photos/view-discussion/segmentation-fault"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/segmentation-fault`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Maurizio Paglia** on 2025-05-12.*

Compiling from source I obtain no errors but when launching /opt/ansel/bin/ansel I obtain a segmentation fault.

Backtrace should be written to a text file in /tmp but file contains only: "this is ansel 0.0.0+1838~gc8b6d5574e reporting a segfault:"

## Replies

**Jiyone** — 2025-05-12

👋 hi

``` ql-syntax
can you run ansel with -d all in a terminal ?
```

---

**Maurizio Paglia** — 2025-05-13

Ciao and thank you for your interest.

Just for the records I updated Ansel to the latest GitHub version right now. Compiled and installed but the problem is still the same...

If I run \<ansel -d all\> from the terminal same result: segmentation fault

---

**Jiyone** — 2025-05-13

Can you copy all the content in the terminal, then go to pastebin.com, past the text and send to the website then give the link ?

---

**Maurizio Paglia** — 2025-05-13

Thank you again for your kind support.

Link here: https://pastebin.com/DBLH9rCe#CYCGHaTS

---

**Jiyone** — 2025-05-13

isn’t there anything before this ?

---

**Maurizio Paglia** — 2025-05-13

This is the output of the command: ansel 2\>&1 \> OUTPUT

Then I pasted the content of OUTPUT as requested.

---

**Aurélien Pierre** — 2025-05-13

Your backtrace contains a reference to /home/mau/Sistema/git/ansel/src/libs/tools/menu.c:83. This file does not exist anymore. Clean your /opt directory and rebuild from scratch.

---

**Maurizio Paglia** — 2025-05-14

It works perfectly, thank you.

I thought --clean-all during the build process will clean also the /opt dir.

---

**Aurélien Pierre** — 2025-05-15

you need --sudo too to clean /opt, otherwise the permissions are not enough.

---

**Maurizio Paglia** — 2025-05-16

The command I use is

sh build.sh --install --sudo --clean-all

Probably I am missing something else... I will try again checking twice.

Thank you very much!

