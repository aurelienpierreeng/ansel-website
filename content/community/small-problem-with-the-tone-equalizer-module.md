---
title: "Small problem with the tone equalizer module"
date: 2025-01-16
slug: "small-problem-with-the-tone-equalizer-module"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/small-problem-with-the-tone-equalizer-module"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/small-problem-with-the-tone-equalizer-module`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-01-16.*

The tone equalizer module provides a method to build a mask for advanced dodging and burning. To optimize the mask, I used to alternate clicking the rightmost symbols in "Mask exposure compensation" and "Mask contrast compensation" until the "Mask post-processing" indicator was maximized w/o orange borders. This indicator would usually change with every click, as would the values associated with these compensations. But presently, still in version 39ca7b3, the clicks have hardly any effect. Only activating the display of the exposure mask updates the indicator and the values for the compensation. Further clicking to improve those values again does not change the indicator and the values, until the exposure mask display is switched off again. This makes it much harder to find the desired setting.

## Replies

**koslowj** — 2025-01-17

Fixed in version 117e3ca, thanks!

