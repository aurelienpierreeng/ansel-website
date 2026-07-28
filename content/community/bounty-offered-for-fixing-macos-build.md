---
title: "Bounty offered for fixing macOS build process and shipping macOS applications regularly"
date: 2024-12-31
slug: "bounty-offered-for-fixing-macos-build"
tags:
  - Community archive
forum_author: "sneak"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/bounty-offered-for-fixing-macos-build"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/bounty-offered-for-fixing-macos-build`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **sneak** on 2024-12-31.*

I'm offering \$500 in bitcoin or ethereum to anyone who fixes the macOS build process.

I'll also reimburse you up to another \$500 for the cost of a mac development system (with proof of purchase) if you need to get one (but I'd hope that you'd use it to keep the build working for some time, like a few months or something).

Binary signing is not required; it's common for free software (especially nightlies) to not be signed. An apple developer subscription is not required to claim this bounty.

## Replies

**sneak** — 2024-12-31

To claim the bounty, contact me at sneak@sneak.berlin.

---

**Aurélien Pierre** — 2025-01-01

The problem of "fixing" CI/nightly builds is whatever you fix is only going to be temporary. It's the same issue for Windows (using Arch Linux repositories through MSYS2 and Pacman) and MacOS (using Brew or Macports repositories) : they are rolling-release, so the packages are always built with the last version of third-party libraries, which may deprecate API, force versions bumps for CMake, C/C++, Clang, GCC, etc. possibly clashing with our owns configs, all that without prior notice (unless you subscribe to all mailing-lists around, spend time reading all news, etc. – Not really feasible, if you ask me). For MacOS, there is also the matter of ARM-based and x86_64-based variants to support, that depends on the host system used to build packages (and have their own set of issues with third-party libs).

So, I'm more and more leaning towards building static Windows and Mac disk images, shipping static versions of libraries (that will **not** be updated before each build), so we know they work until someone manually updates the images when enough time is available to troubleshoot. Because, right now, stuff breaks out of any schedule and we just wake up with new problems, but not necessarily time to fix them *again.* It's not only time-consuming, it's overwhelming, unglamourous and verging on depressing.

Now, the problem is Github Actions don't allow to use static disk images, so that would mean deferring the build to something Amazon Elastic Cloud 2, and then firing the EC2 instance from Github, building, sending the packages back to Github. That's the most future-proof approach I can think of, instead of shoveling shit on a random basis, but it's going to cost money to run the EC2 instances and a lot of time to wire and debug everything.

TL;DR: fixing Win/MacOS builds now and for the few next weeks is no "big" issue. Committing to shoveling shit again and again as things unexpectedly break in the future is the real issue here.

---

**cendalc** — 2025-01-01

I run Ansel on Window so it's a pity for me the latest builds are not available. I very much understand your pain with rolling-releases - it's crazy to maintain with because you have no reproducibility.

I tried to look into the possible solutions (although I have no experience with MSYS2, Pacman, C/C++, ...) and I think either hosting tool versions in custom Pacman repository or creating a docker container with all tools could be a solution - probably docker being simpler solution. The disadvantage is longer build time and probably cost with downloading the docker image every day...

