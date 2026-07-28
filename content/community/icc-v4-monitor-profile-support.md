---
title: "ICC v4 monitor profile support"
date: 2025-01-09
slug: "icc-v4-monitor-profile-support"
tags:
  - Community archive
forum_author: "Massimo"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/icc-v4-monitor-profile-support"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/icc-v4-monitor-profile-support`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Massimo** on 2025-01-09.*

When system display profile is an ICC version 4, darkroom visualization is noticeable darker, see attached comparison image.

Ansel version is 0.0.0+984~gbe2369ae and operating system is Windows 10.

## Replies

**Aurélien Pierre** — 2025-01-10

Why are you using ICC v4 ? They bring no improvement over v2, which explains why many software didn't bother implementing support. More details : https://www.argyllcms.com/doc/iccgamutmapping.html

---

**Massimo** — 2025-01-10

Version 4 is the default of my calibration tool from x-rite, but actually in my current workflow I do not have any constraint that prevents me to use a version 2 profile.

That being said, a version 4 support is likely more future proof as this version in constantly updated from ICC consortium, for example HDR support has been recently added.

---

**Aurélien Pierre** — 2025-01-10

HDR support is the ICCmax version, not v4 as far as I'm aware. ICC v4 is not supported by ArgyllCMS (see link above), therefore not supported by Display Cal. The ICC workflow being printer-centric, HDR is irrelevant here. Anyway, HDR workflows moved to OCIO/ACES.

All I can say is ICC v2 is supported everywhere, many devs & projects didn't bother with v4, and ICCmax is supported nowhere and not planned for adoption for apps that need HDR. So, just stick to good old ICC v2, the future of ICC is 30 years ago.

---

**Massimo** — 2025-01-10

My understanding was that with the adoption of cicpTag in version 4.4 (2022), that links to ITU or SMPTE specification, ICC profiles would be used for still and video HDR contents on computers.

From your reply, I'm learning that this would probably not be the case.

