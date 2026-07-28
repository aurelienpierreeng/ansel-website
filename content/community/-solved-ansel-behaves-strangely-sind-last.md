---
title: "[Solved] Ansel behaves strangely sind last weekend's update"
date: 2023-06-14
slug: "-solved-ansel-behaves-strangely-sind-last"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/-solved-ansel-behaves-strangely-sind-last"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/-solved-ansel-behaves-strangely-sind-last`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2023-06-14.*

Since an update last weekend Ansel behaves very strangely. The top part of the usual window is missing, including the logo and the selection tool (how many stars, or the color labels). I also cannot toggle the filmstrip. Moreover, the only files shown in the lighttable are the tiffs I've created using a separate HDR program, I don't see any of my Canon raw files (.CR3) of of the dng-files produced by PureRaw3, even though the tree-view on the left lists the correct number of pictures in the various folders. When I try to add the pictures again, they are listed as already registered. I'm including a screen-shot to illustrate the phenomenon.

This is happening under gentoo linux, kernel 6.1.31. Up to last weekend the versions I compiled worked perfectly fine. I've tried to remove the source directory and the ansel directory from the opt directory and start from scratch, without any effect. I removed an old darktable version as well.

## Replies

**Aurélien Pierre** — 2023-06-15

Hit Ctrl+H, what's happening is the header panel is collapsed.

Regarding CR3 not showing, beside user error, the most probable cause is your Exiv2 library was built without ISOBMFF support, please see https://ansel.photos/en/doc/install/linux/#caveats-1

---

**koslowj** — 2023-06-16

Thanks, that fixed it.

