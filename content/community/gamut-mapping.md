---
title: "Gamut mapping"
date: 2025-01-06
slug: "gamut-mapping"
tags:
  - Community archive
forum_author: "Massimo"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/gamut-mapping"
wayback_url: "https://web.archive.org/web/20250120180634/https://community.ansel.photos/view-discussion/gamut-mapping"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/gamut-mapping`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250120180634/https://community.ansel.photos/view-discussion/gamut-mapping).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Massimo** on 2025-01-06.*

Using Sony proprietary raw converter (Imaging Edge), but I remember to have seen something similar with Canon DPP, raw files converted to sRGB or AdobeRGB look different (even without out of sRGB gamut colors in the scene). I think this is due to different gamut mapping between native camera color space and sRGB or Adobe RGB.

This behavior made me think about the fact that gamut mapping curves are out of user control.

Back to Ansel, would it make sense to have a module that allows to control gamut compression, much like filmic RGB does with respect to luminance?

## Replies

**Aurélien Pierre** — 2025-01-06

You already have parametric gamut compression in color calibration. This will desaturate colors based on their chroma, using a power function. This was put there because, anyway, chromatic adaptation transform can and will push valid colors outside of gamut, especially the crazy LED blue.

But ultimately, gamut is defined by color spaces which are defined by color profiles, and I believe that should be handled automatically when dealing with color conversions.

---

**Massimo** — 2025-01-06

Thanks, I've found it in the CAT tab.

