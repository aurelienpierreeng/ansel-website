---
title: "May somebody help with the development of this image?"
date: 2023-05-16
slug: "may-somebody-help-with-the-development-of"
tags:
  - Community archive
forum_author: "ariznaf"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/may-somebody-help-with-the-development-of"
wayback_url: "https://web.archive.org/web/20231001112628/https://community.ansel.photos/view-discussion/may-somebody-help-with-the-development-of"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/may-somebody-help-with-the-development-of`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001112628/https://community.ansel.photos/view-discussion/may-somebody-help-with-the-development-of).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **ariznaf** on 2023-05-16.*

I'm having problems editing an image.

I've edited it as I usually do by adjusting exposure, adjusting the filmic module a bit, and fiddling a bit with highlights and shadows with colour balance.

Focus with contrast equalizer and a bit of local contrast.

The thing is that my colleagues tell me that the colours in the houses look strange, dull and that there is little contrast in the lights and those facades (the sky seems to look good to everybody).

And the truth is that I think they are right, I have tried to give it more life and bring out some more detail and contrast in those facades, but I can't achieve a natural look.

If I force too much I get unnatural results with colours that are a little bit steely.

This is the result I have obtained, using the settings I attach in the link I put at the end with the xmp and the raw.

*\[attachment lost: image was hosted on the retired forum\]*

The photo with a neutral development as it comes out of the Ansel after opening it is this one:

Let's see if any of you can tell me what could be wrong with my editing and how to improve it.

*\[attachment lost: image was hosted on the retired forum\]*

The raw and the editing file can be downloaded from the following link (they will be available for a week, the maximum that we transfer allows me):

https://we.tl/t-IEOizuYjjm

  

Translated with www.DeepL.com/Translator (free version)

## Replies

**migmoq** — 2023-05-18

I don't think the colors of the house are strange or unnatural. But their facades can be dull for a lack of local contrast. If, in Filmic RGB the color preservation is set on *max rgb*, then this can explain that. Try to choose another color preservation mode: for example *RGB power norm* or *RGB euclidean norm* (they tend to preserve a bit the local contrast).

Another tips: use both the *contrast* and *latitude* sliders in Filmic RGB to preserve the natural-looking of the image.

(For adding some local contrast, the Local Contrast module is by far too strong in my toast. I usually prefer the *local contrast* preset in the Diffuse and Sharpen module; it is more subtle.)

---

**ariznaf** — 2023-05-19

Thank you I will try it.

But if I did not miss something, the preservation color mode is applied only when there are blown pixels, values above the threshold stablished in reconstruction. None of the pixels in the image is above that threshold or blown in the raw.

I had not thought the norm could affect the pixels that are not blown, but I will try.

I wil try to play with latitude too.

I am not too fan of local contrast either, is usually takes the darks to black.

Will try the diffuse module (but it is not intuitive module, you can only use the presets).

Do you need to move the module to other position? After filmic?

---

**photoscouleurs** — 2023-05-20

Hi !

xmp in zip file below

*\[attachment lost: image was hosted on the retired forum\]*

---

**ariznaf** — 2023-05-20

Thank you, I will study how you have processed it.

---

**migmoq** — 2023-05-22

The preservation color mode isn't for blown pixels but to preserve the colors of the image once the mapping applied (tone mapping alters the colors as the luminance, and hence the lightness, is modified)

For the module Diffuse and Sharpen, indeed it isn't a user friendly module as its interface is technical and requires to know a bit what is hidden under the hood. Simply use the presets. You can also, from a given preset, play with the sliders to observe their effects on the image. Whatever, the module doesn't need to be moved to other position.

---

**ariznaf** — 2023-05-22

Thank you.

I was using the v7 2023 version of filmic, it does not have the option to select the norm to use.

May it be that the problem, that v7 is not ready for production or has changed drastically the way it treats colors?

  

No diffuse module it not intuitive in any way, you play with the mathematical model directly, a model that is able to do such differente things as noise reduction, focusing or local contrast, so it is not easy to play with the parameters in a meaningfull way without knowing the theory in detail.

But the presets give a good result many times.

---

**ariznaf** — 2023-05-22

I could not use the xmp.

  

I tried creating a new virtual copy and importing editing from xmp but the system hangs after that.

May you tell me how to use an xmp edition?

---

**photoscouleurs** — 2023-05-25

Ansel version : Ansel-0.0.0+285~g0c37799cc-x86_64

With your file browser

1a - In the directory containing the RAW image create a directory "xmp-importe

2a - Unzip the file containing the xmp file into a "xmp-importer" directory

With Ansel

1b - Open Ansel containing the RAW image in light table mode.

2b - click on the photo for which you wish to import the proposed xmp file

3b - in the "Act on selection" window on the right of the light table, click on "Clone" to create a clone of the image

4b - Still in the light table, "Menu \> Edit" at the top left, click on "Delete development". The image returns to the default settings.

5b - "Menu \> Edit" click on "Load development from XMP".

6b - Enter the "xmp-importe" directory and click on the proposed xmp file.

7b - You have an additional development of your photo.

8b - the "xmp-importe" directory can be deleted

---

**ariznaf** — 2023-05-25

I will try it that way.

I had made a copy in the darktable and used import development from the xmp but the system hangs for ever.

I will try it again.

---

**ariznaf** — 2023-05-25

Thank you, it worked.

It was basically the same I was doing in the darkroom, but when done in the darkroom it does not work and the system hangs for ever.

May you try it to confirm it is a bug?

In the darkroom select a photo, selec the duplicate manager and check original button.

Then edit/delete development and edit/load development from xmp.

Ansel hangs after that.

I have reported the bug, please if you test it tell there if you can reproduce the bug.

[-load-development-from-xmp-hangs-when](-load-development-from-xmp-hangs-when.md)

