---
title: "Different renderings"
date: 2024-08-16
slug: "different-renderings"
tags:
  - Community archive
forum_author: "Steve"
forum_category: "Configuring help"
forum_url: "https://community.ansel.photos/view-discussion/different-renderings"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/different-renderings`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Steve** on 2024-08-16.*

I was wondering if anyone knew why a jpeg opened in other apps takes on a different appearance. 1. change in color on watermark. 2. lower brightness level. Original RAW rendering in Ansel in the centre.

## Replies

**Jiyone** — 2024-08-16

Color management ? ﻿🤔﻿

Ansel uses your monitor profile, and if you export in sRGB color, then some color will change if they are outside of sRGB

What color profile do you use to export ?

---

**Steve** — 2024-08-16

I have not touched any setting except 'target storage' location and 'set size'

Profile : "same as original"

---

**Steve** — 2024-08-16

Thanks for pointing me in the right direction. I switched Profile: 'sRGB' and now, ALL GOOD !

---

**Jiyone** — 2024-08-16

would be interesting to set sRGB by default

