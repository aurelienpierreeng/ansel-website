---
title: "Versions - Install or Appimage?"
date: 2024-03-16
slug: "versions-install-or-appimage"
tags:
  - Community archive
forum_author: "gomi"
forum_category: "Installing help"
forum_url: "https://community.ansel.photos/view-discussion/versions-install-or-appimage"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/versions-install-or-appimage`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **gomi** on 2024-03-16.*

I'm currently running Ansel on an Appimage. The last update was early January. Is it felt that the pace of updates has slowed sufficiently for a full installation to be more appropriate? I'm on Arch Linux so it would be the AUR repository version, which is currently carrying the same date as the Appimage.

I have three questions but not sure which context to ask them in, Appimage or full install. I'll mention them here but await pointers:

1.  Imported a newly downloaded folder of images and began processing in Ansel. One image is now a single black rectangle in Lighttable view. It starts off as a totally black image in Darkroom but the image returns if I scroll in slightly. is this a known problem? {Edit: the exported Jpeg is perfect, so the 'problem' only exists visually in Ansel}
2.  I can't see a way to import a new watermark in either PNG or SVG format. There is no directory .config/Ansel/, only the .config/ansel/
3.  There are several folders already imported and images processed in my old darktable config files .config/darktable/ but they are mostly DT 4.2 or later. Is it better to import them into Ansel as raw files and re-process them or are my efforts likely to persist if I pull the DT DB files into .config/ansel/?

TIA,

Mike

## Replies

**Aurélien Pierre** — 2024-03-16

> Imported a newly downloaded folder of images and began processing in Ansel. One image is now a single black rectangle in Lighttable view. It starts off as a totally black image in Darkroom but the image returns if I scroll in slightly. is this a known problem? {Edit: the exported Jpeg is perfect, so the 'problem' only exists visually in Ansel}

It's a known issue. To mitigate it until it's fixed, hit global menu -\> Run -\> clear pipeline caches when it appears.

> I can't see a way to import a new watermark in either PNG or SVG format. There is no directory .config/Ansel/, only the .config/ansel/

Just create that directory and add your watermarks if it's not created automatically.

> There are several folders already imported and images processed in my old darktable config files .config/darktable/ but they are mostly DT 4.2 or later. Is it better to import them into Ansel as raw files and re-process them or are my efforts likely to persist if I pull the DT DB files into .config/ansel/?

Ansel is compatible with Darktable up to 4.0. For editings made with Darktable 4.2, you may loose your settings for filmic and highlights reconstruction modules.

**Ansel is still not considered stable as of now.**

---

**gomi** — 2024-03-16

Thanks Aurelien (and apologies for not finding how to type the accent on the e). That's all a lot easier than I'd imagined.

