---
title: "Develop photo with flames"
date: 2024-01-15
slug: "develop-photo-with-flames"
tags:
  - Community archive
forum_author: "cendalc"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/develop-photo-with-flames"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/develop-photo-with-flames`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **cendalc** on 2024-01-15.*

Hi, I'd like to get some tips how to develop photo with flames (e.g. candle). I am not able to create vibrant yellow flames. The best I could have done is this:

*\[attachment lost: image was hosted on the retired forum\]*

Source RAW with my edits is on https://1drv.ms/f/s!AtyecmjANN7wna4lzFcpFDC4z_50eA?e=Jj9Bk7

Any tips/help is much appreciated!

## Replies

**cendalc** — 2024-01-15

For another picture, as soon as I enable Filmic, the flames are red and I don't know what to do to fix it. Here is a snapshot between enabled/disabled Filmic.

*\[attachment lost: image was hosted on the retired forum\]*

Source RAW also posted to [https://1drv.ms/f/s!AtyecmjANN7wna4lzFcpFDC4z_50eA?e=Jj9Bk7](https://1drv.ms/f/s!AtyecmjANN7wna4lzFcpFDC4z_50eA?e=Jj9Bk7)

---

**Aurélien Pierre** — 2024-01-16

Red is actually radiometrically-accurate for flames, as in : it's consistent with the lightspectrum the camera recorded. Indeed, the color temperature of flames is actually… its own burning temperature (gas burns at high temperature with blue flame, coal and candles burn lower with red flames that you don't actually see red…). See here the "theoritical" color of illuminants in relation with temperature (in kelvin):

*\[attachment lost: image was hosted on the retired forum\]*

Filmic honors that and apply gamut mapping (aka desaturation) to fit colors into the display color space.

Now, what you perceptually expect here is the [Bezold-Brücke shift](https://en.wikipedia.org/wiki/Bezold%E2%80%93Br%C3%BCcke_shift), aka a yellow shift of very bright red lights, but the camera is not subjected to it because it's a product of human retina.

What you see without filmic is the product of gamut clipping, where green clips earlier than red, producing a yellow shift by accident (along with ugly flat areas).

The solution is a mix :

1.  in filmic options, go for "color science" v7,
2.  in color balance RGB, manually push highlights to yellow with the highlights gain setting (in 4 ways tab).

More details:

https://www.youtube.com/watch?v=34iZotlYBBs

---

**Aurélien Pierre** — 2024-01-16

Another note : you will not be able to get a lot of saturation on colors that are very bright. That is a limitation of RGB color spaces. This is the sRGB gamut on a lightness, chroma graph at constant hue :

*\[attachment lost: image was hosted on the retired forum\]*

You see that at 100% lightness (top tip), you can only have white. The pure yellow tip is probably at 80 % lightness. So if you want saturation in flames, you will need to darken them so they don't end up at the white end of the dynamic range, because there is no room for saturation in there.

