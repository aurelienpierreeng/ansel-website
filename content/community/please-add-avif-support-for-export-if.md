---
title: "Please add AVIF support for export (if possible)"
date: 2023-05-24
slug: "please-add-avif-support-for-export-if"
tags:
  - Community archive
forum_author: "ariznaf"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/please-add-avif-support-for-export-if"
wayback_url: "https://web.archive.org/web/20231001111327/https://community.ansel.photos/view-discussion/please-add-avif-support-for-export-if"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/please-add-avif-support-for-export-if`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001111327/https://community.ansel.photos/view-discussion/please-add-avif-support-for-export-if).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **ariznaf** on 2023-05-24.*

AVIF support was already introduced in darktable 4.2, but as Ansel is based in darktable 4.0 it seems it is not able to export in AVIF yet.

I know that is not extensively used yet, as support for it is quite new in some web browsers, but it is support in many of them and many forums do support it already.

It provides more quality than jpeg for the same compression, I have tested it and you really can see the difference.

It would be great to have it in ansel.

I don't know how programming intensive that could be or if it is just a matter of using a newer library for exporting images, but if the effort is not too much, it would be a great addition.

## Replies

**ariznaf** — 2023-06-15

Avif has been added to the appimage today and will be available from now in the nightly builds.

It was allwasy available if you compiled from sources and had the libavif-dev library installed, but that library is not available in ubuntu version under which appimage is created.

Devs have added libavif compiling from sources and now it is available in the appimage too.

So the issue is solved.

