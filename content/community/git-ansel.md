---
title: "git ansel"
date: 2024-01-31
slug: "git-ansel"
tags:
  - Community archive
forum_author: "seans"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/git-ansel"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/git-ansel`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **seans** on 2024-01-31.*

Hi Ansel Community, 

  

OS: Arch Linux x86_64

 Host: 82Y3 Legion Slim 7 16IRH8

 Kernel: 6.7.2-arch1-1

 Shell: bash 5.2.26

 Resolution: 3200x2000

 DE: GNOME 45.3

 CPU: 13th Gen Intel i9-13900H (20) @ 5

 GPU: NVIDIA GeForce RTX 4070 Max-Q / M

 GPU: Intel Raptor Lake-P \[Iris Xe Grap

 Memory: 4480MiB / 31821MiB

  

I don't know if this is a bug or not, in compiling Ansel from Git, I got ...

"... po4a-translate is deprecated. The unified po4a(1) program is more

convenient and less error prone.  \[23/328\] Checking validity of

noiseprofiles.json /usr/bin/jsonschema:5: DeprecationWarning: The

jsonschema CLI is deprecated and will be removed in a future

version. Please use check-jsonschema instead, which can be installed

from https://pypi.org/project/check-jsonschema/ from jsonschema.cli

import main ninja: build stopped: subcommand failed ..."

  

po4a 0.70 was released the other day, but I don't know enough about it

to know if that'll solve the first problem. I sure would appreciate any

guidance on how to move forward.

  

Regards,

Sean

## Replies

**Aurélien Pierre** — 2024-02-20

It's a warning, disregard it.

