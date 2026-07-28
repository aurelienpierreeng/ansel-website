---
title: "Two problems with the mask icon"
date: 2025-01-14
slug: "two-problems-with-the-mask-icon"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/two-problems-with-the-mask-icon"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/two-problems-with-the-mask-icon`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-01-14.*

Modules that utilized a mask used to show a mask-icon to the left of the three ordinary icons, so one could display the mask even if the module was collapsed. These extra icons seem to have disappeared in the recent self-compiled versions: b811815, cf52835, and also 7027d2f.

For B&W pictures I noticed another oddity: I usually have a second color calibration module moved on top of the filmic module. Sometimes, when clicking on the mask-display icon in some expanded module, the mask is displayed in yellow as usual, but when I cllick again to switch off the display of the mask, a darker color picture instead of the B&W picture is displayed. In case that the development stack can be collapsed, doing so restores the B&W picture. But if the development stack is already minimal, I have to open a different image and the return to the first one to get it displayed properly in B&W. I'm sure this is just a phenomenon of a somewhat deeper problem, no wonder at the current pace of development and easy to get around so far.

## Replies

**koslowj** — 2025-01-15

Already fixed, wow! Thank you!

