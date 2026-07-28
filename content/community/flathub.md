---
title: "Flathub"
date: 2023-04-07
slug: "flathub"
tags:
  - Community archive
forum_author: "starborn"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/flathub"
wayback_url: "https://web.archive.org/web/20231001111852/https://community.ansel.photos/view-discussion/flathub"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/flathub`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001111852/https://community.ansel.photos/view-discussion/flathub).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **starborn** on 2023-04-07.*

I've just stumbled upon your project on Flickr and downloaded the Appimage. Would it be possible that you could distribute Ansel via Flathub? That would immediately make Ansel not only available on every Linux distribution but would also be an easy way to update the app in the future. Using Appimages is always a small pain in the ass.

## Replies

**Aurélien Pierre** — 2023-04-07

No. I provide an AppImage, it was 70 h of work to make it work ok-ish (still not entirely working), it's the only official way to get snapshot builds as it can be built straight on Github.

Flatpak sucks. It needs to run a power-hungry service in background, needs to reinstall packages for graphic drivers (not sure if they are bindings or actual drivers), then it sandboxes software and config files in weird places : the whole thing is bloatware serving bloatware and only feeding the Snap vs. Flatpak church war.

AppImage doesn't need sandboxes, extra config, GPU bindings, and background services. It's the .exe of Linux.

Not going to lose my time on this, sorry.

---

**ariznaf** — 2023-05-25

I agree that flathub is like killing flies with cannons.

May be a good solution when the base OS and environment is too different from the environment that is needed by the target program, and it is a complex program with many dependencies.

For example to run an obsolete program that does not run on a modern environment and it depens on many deprecated libraries.

But for general use it generates too much overburden.

Appimage seems a better way, more light and still seems to provide isolation and distribution of needed dependencies.

The only draw back is that it does not provide an installation or updating process nor integration with the graphics environment (for example links in the application menu) that has to be made by hand, but not a difficult task.

