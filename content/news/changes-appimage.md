---
title: "Changes in distribution support for Linux AppImage package"
date: 2023-11-18
tags:
  - Announcement
authors: ["Aurélien Pierre"]
---

Rawspeed (the library providing the decoders for camera raw files) has deprecated support for GCC < 12. As a result, I can no longer build the AppImage on Ubuntu 20.04 (using Github runners) but I have to build it on 22.04.

It means any Linux distribution having libc older than 2.35 will not be able to start the new AppImages starting today. That should not affect most users running distributions upgraded in 2021 or more recently. Ubuntu 20.04 and other LTS/old stable distributions (Debian stable) may be affected.
