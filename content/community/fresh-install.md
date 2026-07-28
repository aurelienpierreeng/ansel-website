---
title: "Fresh install"
date: 2023-04-24
slug: "fresh-install"
tags:
  - Community archive
forum_author: "James Roberts"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/fresh-install"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/fresh-install`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **James Roberts** on 2023-04-24.*

I've noticed a couple of strange behaviours since installing this evening. Please let me know if these would be better split into two different posts.

Firstly, I discovered too late that dt4.2.1 wasn't compatible with 0.0.0, so have used the 'data.db.pre-4.2.1' and 'library.db.pre-4.2.1' db files when copying over the config.

1\) I can't select any images in lighttable - whether that's clicking on one to select, or double clicking to open in darkroom, or Ctrl+ A to select all - nothing will select.

2\) Starting with a clean 'C:\\LOCALAPPDATA%\ansel' folder, I'm able to select images, but I get a number of black thumbnails (and corresponding images in darkroom) for anything worked on in darktable which used the filmic module - I get a warning about "version 6 != 5" - presumably this is picked up from the .xmp file - I can work around this by identifying images, switching off the filmic module in dt, exiting and re-importing the file.

Hope this helps, and apologies if these are know issues with me too late and upgrading to dt4.2.1 :\|

Thanks

James

## Replies

**Aurélien Pierre** — 2023-04-24

Please see https://ansel.photos/en/doc/install/darktable/

Regarding selection, it's WIP.

---

**Scorpion078** — 2023-04-25

The black images comes most likely from the highlight reconstruction module.

It was probably set to inpaint oppesed which is not in ansel. Change it to clip highlights or any of the other options.

