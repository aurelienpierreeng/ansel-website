---
title: "Mask problems in version 0e94264"
date: 2024-10-02
slug: "mask-problems-in-version-0e94264"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/mask-problems-in-version-0e94264"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/mask-problems-in-version-0e94264`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2024-10-02.*

I'm running into a strange new problem with masks in the new version 0e94264 of ansel I just compiled. When applying some operation, eg., change of exposure by one stop, to the whole image, the change usually is easily visible. In the new version, when I then select, say, a drawn mask, e.g., an ellipse, and then click on the image, the exposure reverts to the initial value, the green outline appears, and within the green outline the effect is miniscule compared to before, if present at all. Moreover when I click on the mask refinement symbol (white square with a dark circle inside), the whole picture turns black and white, with the masked region marked very faintly in yellow. This used to be very clear and bright yellow before. The terminal from which I started ansel repeatedly shows the message "\[\_dev_add_history_item_ext\] invalidating history", apparently for any action I take in ansel. I first noticed this problem with the Contrast equalizer module, but the same problems occurs with the exposure module and also with different pictures.

Ansel is self-compiled under Gentoo Linux 6.6.52. How can I revert to the previous version?

## Replies

**koslowj** — 2024-10-06

First of all, sorry for the double posting.

The problem above happened with one specific picture (actually a copy of a picture) and after a while of playing around with versions 916.0e94264 and 913.g85f2b8b15 and getting the problem with both versions, editing the original picture worked fine. And after that the copy which initially displayed the problem also allowed to be edited properly. Strange, so I withdraw the above posting.

I'm also happy to report that now the AppImages work under Gentoo Linux - this was not the case some months ago when I first tried to use them.

