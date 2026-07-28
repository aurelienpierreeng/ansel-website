---
title: "Problem Importing From Network Location"
date: 2025-01-08
slug: "problem-importing-from-network-location"
tags:
  - Community archive
forum_author: "Vintage Lens Lover"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/problem-importing-from-network-location"
wayback_url: "https://web.archive.org/web/20250120192941/https://community.ansel.photos/view-discussion/problem-importing-from-network-location"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/problem-importing-from-network-location`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250120192941/https://community.ansel.photos/view-discussion/problem-importing-from-network-location).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Vintage Lens Lover** on 2025-01-08.*

I'm trying import photos from an SMB share on my NAS, however, no network locations show up while trying to import on my Linux Mint 22 workstation, even though I'm properly logged into the share and can access it from the file browser. On the other hand, my older PC (running Mint 21.3) has no problem doing the same thing and the network locations show up underneath the computer's local resources. Both instances are using "Ansel-0.0.0+980.ga329ee63-x86_64.AppImage". Any ideas what's going wrong?

## Replies

**Vintage Lens Lover** — 2025-01-10

I have now also tried Linux Mint Debian Edition 6 on the same machine, that works, but Ansel does not see the network shares in Mint 22.

---

**Aurélien Pierre** — 2025-01-10

You need to install the GVFS packages for your system, noticeably the relevant SMB driver for GVFS. SMB networks have been confirmed to work with Ansel on Ubuntu and PopOS. GVFS provides the abstraction layer and handles the I/O through its own drivers, Ansel simply connects to that.

---

**Vintage Lens Lover** — 2025-01-10

I think I had already checked that but I will check again, thanks.

---

**Vintage Lens Lover** — 2025-01-10

I had these packages installed:

gvfs

gvfs-backends

gvfs-common

gvfs-daemon

gvfs-fuse

gvfs-libs

I think gvfs-backends handles the SMB stuff. I can also access my KeePassXC database which is a gvfs SMB link.

---

**siamak** — 2025-05-20

I have the very same problem with Darktable and Ansel with many linux distro. The only linux that seems to work for me out of the box is MX Linux. Too bad no one seems to want to give the solution to this issue. It does limit my linux choices for these apps. BTW, I came to like MX for ease of use and features.

---

**Vintage Lens Lover** — 2025-05-20

Are those clean installs without copying over some home folder?

My workstation install has been through several Mint upgrades and I think the upgrade from 21.3 to 22 had problems and I had to restore from backup. That computer is on Mint 22.1 now and still has the problem, even though KeePassXC accesses GVFS stuff fine. I am not sure when the problem started.

My other computer which runs Mint 21.3 accesses the network shares fine, I wonder if it's some configuration file or something that went wrong during an upgrade.

If you have a spare disk maybe try a fresh install to that without copying anything over and try that, I bet it will work.

---

**siamak** — 2025-05-20

I repeatedly installed all versions of Ubuntu and Debian Mint linux as a vm and virtual box as well as in new laptop running only linux with no success. Network does work in all of them and I can see the files and do read and write. However, in Darktable I can only locate the drives and files yet does not show any files for import. In Ansel, I can not even see the folders or files. I installed GVFS as noted and did not changed anything. Only MX linux as VM as well as OP can and does show the files and folders and can import both in Ansel and Darktable. Which is fine with me since I like MX.

---

**Vintage Lens Lover** — 2025-05-20

This is strange. Importing from network used to work on my workstation then it stopped working. I suspect in my case it's to do with a Mint upgrade, but I really don't know. Some time I'll put Mint 22.1 on a blank disk and try again. Could it be some sort of permissions thing?

---

**siamak** — 2025-05-20

Yes it is puzzling. Hope others, specially developers look into this.

