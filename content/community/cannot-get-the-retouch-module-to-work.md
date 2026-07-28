---
title: "Cannot get the retouch module to work + missing check-marks for selected presets"
date: 2024-01-19
slug: "cannot-get-the-retouch-module-to-work"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/cannot-get-the-retouch-module-to-work"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/cannot-get-the-retouch-module-to-work`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2024-01-19.*

I compiled version e2c4a0a from git (under amd64 Gentoo linux), and while an old problem (mouse pointer not aligned with active area) is fixed, I'm having a new problem: presently I cannot use the retouch module to heal blemishes. Using the brush and the healing tool, I see a black line while I work; then green lines indicate which path has been shifted from the source to the target, as before. But when I click on the brush again, the green lines disappear and nothing has been fixed :-(

Since I already struggled in other pictures to get horizons straightened (the old method of right-right clicking and drawing a line initially did not have any effect, further activation clicks were required), I'm wondering if the intuitive old method also has been replaced by something more complicated, or if this really is a bug.

Still missing are the check-marks for the selected presets in development modules (e.g., color balance rgb); those used to exist a long time ago. Strangely enough, in the export module, the check-marks are still present (I hope they stay). I cannot compare with the AppImage version, as it requires the libthai library which so far I haven't been able to compile under Gentoo.

## Replies

**koslowj** — 2024-01-21

I've since tried the windows version and can confirm that the same problems persist there.

---

**koslowj** — 2024-01-24

This issue was already brought up by vtyrtov at https://github.com/aurelienpierreeng/ansel/issues/310. I can confirm that after closing ansel, then re-opening it and trying to re-touch the same blemish in the same image, it works. However, I still cannot work on a second blemish afterwards :-(

