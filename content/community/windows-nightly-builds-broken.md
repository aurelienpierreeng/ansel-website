---
title: "Windows nightly builds broken"
date: 2024-06-04
slug: "windows-nightly-builds-broken"
tags:
  - Community archive
forum_author: "Aurélien Pierre"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/windows-nightly-builds-broken"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/windows-nightly-builds-broken`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Aurélien Pierre** on 2024-06-04.*

Windows nightly builds (.exe) are currently broken due to a bug with the libcurl dependency that got updated to v8.8.0 last weeks in MSYS2 package manager. The bug makes both Ansel and Exiv2 builds fail. I have gotten in touch with the libcurl team, waiting for an answer.

## Replies

**Aurélien Pierre** — 2024-06-05

Fixed today by ﻿@Alynx Zhou﻿, thanks a lot !

