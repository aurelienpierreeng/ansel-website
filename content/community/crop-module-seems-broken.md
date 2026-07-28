---
title: "Crop module seems broken"
date: 2023-12-10
slug: "crop-module-seems-broken"
tags:
  - Community archive
forum_author: "Maurizio Paglia"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/crop-module-seems-broken"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/crop-module-seems-broken`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Maurizio Paglia** on 2023-12-10.*

Last recompilation of Ansel (test+185~g55d8a7ad8) seems to have a strange behaviour in Crop module.

Module does not work at all: if I select - for example - SQUARE the module does nothing.

If I click Apply button the square is applied but histogram (top right) and the reference image (top left) disappear.

Than I cannot drag the square selection. I can only modify margins and position sliders but central image is rendered with strange fuzzy colors...

Other modules seems to work right...

## Replies

**migmoq** — 2023-12-10

Yes. Aurelien fixed some important bugs with the cache and with the pipeline computation on changes that invalidated some expectations made by this module. He works currently on this module to fix that.

---

**Maurizio Paglia** — 2023-12-11

OK, thanks!

