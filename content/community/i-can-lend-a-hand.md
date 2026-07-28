---
title: "I can lend a hand."
date: 2023-12-22
slug: "i-can-lend-a-hand"
tags:
  - Community archive
forum_author: "jjw"
forum_category: "Developers talk"
forum_url: "https://community.ansel.photos/view-discussion/i-can-lend-a-hand"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/i-can-lend-a-hand`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **jjw** on 2023-12-22.*

Somehow Ansel wasn't on my radar at all. Just found it yesterday. Old time programmer here, I did Gnome Wave Cleaner back in the day (way back...):

http://gwc.sourceforge.net/

More recently an application to fill the top of ragged edged panoramas matching the sky color, modeling the sky color from left to right, and horizon to zenith:

https://github.com/weltyj/SkyFill

For darktable, I have a modified dehaze module, which I call "Enhanced Dehaze", that I add to darktable every time a new release comes out. I tried to get some interest from the dev's on darktable but they were always too busy to look at it. I did download the source for Ansel today and was able to merge enhanced dehaze into the source. Key thing it does is allow the user to adjust the lightness and color of the haze estimate, as well as changing the window size for detecting the haze, and change the guided filter window size. Really helps with eliminating halos. I have both the ".c" and opencl ".cl" versions done, but the user interface is not acceptable (I needed "integer" sliders but didn't know how to do it right with bauhaus)

For an experiment I also implemented the guided filter sharpening approach, which looks pretty good. Not as powerful as the diffusion-sharpen module, but it's likely far less cpu intensive for sharpening and may provide equivalent results (within a limit).

First, though one of the things I'd like to have (and thus am offering to do right away), is a little script to copy styles and presets from the darktable data.db to ansel's data.db If the tables and what is stored in them have not changed from darktable to ansel it should be relatively easy.

I am fluent in C, Perl. Mostly fluent in C++, can modify python code, but it really isn't my thing. I understand how databases work and can write SQL like code/commands...

Also my complements on the images I'm seeing from Ansel. They look very natural. Since I take a lot of outdoor panoramas that is a very nice result for me ;-)

