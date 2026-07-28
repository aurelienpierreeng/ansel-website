---
title: "ansel via linux-on-ARM virtualization on macbook?"
date: 2024-11-04
slug: "ansel-via-linux-on-arm-virtualization-on"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Installing help"
forum_url: "https://community.ansel.photos/view-discussion/ansel-via-linux-on-arm-virtualization-on"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/ansel-via-linux-on-arm-virtualization-on`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2024-11-04.*

The new M4 Macbooks look quite attractive, and apparently both windows 11 and linux-on-ARM can be virtualized either by using Parallels or UTM. Would it be feasible to run ansel in such a virtual machine, preferably under one of the several linux distributions supporting ARM (I'm not really interested in windows)? Emulation of x86 hardware may be too slow, even if my current desktop is rather slow anyway.

I've already asked the developers of ansel on native Apple ARM hardware about the current status of their projects.

## Replies

**blankslatephoto** — 2024-12-02

This would be nice to have, both for "optimized" ARM platforms like the Mac, but for ARM in general; I like to do all of my developing on one software package, and right now I have to wait to get back to the laptop/desktop to produce jpegs, even for family photos (unless I want to just share what is in camera...). I played with compiling darktable a couple of years ago for ARM to no avail: with how fast the M4 and some snapdragon chips have become, perhaps basic edits can be completed in a linux VM... would be nice to have ansel on a tablet...

Has anyone tried compiling or running Ansel in a VM on something other than x86 recently?

To answer the post: from your last posts, it looks like you have a need/want to run Ansel on ARM/Mac hardware: do you have access to an M4 (or the other ARM based macs?): might be easy to spin up a VM and see if the appimage will run and report back?

It might not be that helpful (and I should do not while I should be working...), but I will try to spin up a VM in QEMU and see if the appimage runs (it should): don't know how helpful that will be, but if it is painfully slow or breaks while Fedora on a Ryzen 7 is under the VM, it might give us a data point...

---

**koslowj** — 2024-12-02

Thanks for your answer! I'm trying to decide whether to buy an M4 machine, but it has to be able to run ansel in some form or shape, either directly (some people have reported on that a while ago), or via Linux virtualization. Looking forward to your experimental results!

