---
title: "Contrast ajdustment"
date: 2023-04-07
slug: "contrast-ajdustment"
tags:
  - Community archive
forum_author: "migmoq"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/contrast-ajdustment"
wayback_url: "https://web.archive.org/web/20231001124632/https://community.ansel.photos/view-discussion/contrast-ajdustment"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/contrast-ajdustment`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001124632/https://community.ansel.photos/view-discussion/contrast-ajdustment).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **migmoq** on 2023-04-07.*

There are several ways to adjust the global contrast of an image:

- with the contrast slider in Filmic (Look tab),
- by using the Tone Equalizer (either by using one of the contrast preset or by playing a bit with darker and lighter tones),
- by using the contrast slider in Color Balance.

I didn't find any clues about the difference between these three ways and, according to the goal, which one to use.

For instance, what I understood is:

- Use the the contrast slider in Filmic so that each elements in the image can be correctly perceived (for doing, minimize its viewing). Usually, this slider is rarely used. (Prefer to use the latitude slider which improves a little the global contrast and to not desaturate the mid-tones.)
- Use the Tone Equalizer to choose to contrast or not an image (artistic choice).

Is my understanding correct? Are there more details to know? And for what purpose the contrast slider in Color Balance should be used or preferred?

## Replies

**Aurélien Pierre** — 2023-04-07

I think you can find all that scattered in the docs, so let's recap here.

## Filmic contrast

Filmic maps input (scene) dynamic range to output (screen/display/paper) dynamic range. That typically leads to compromises, and the most typical use case is you need to compress dynamic range from scene to display in order to retain smooth gradients over the full range of luminance.

Compressing dynamic range results in losses of local contrast and may make things look awefully flat, so the contrast of filmic is the adjustment variable in this compromise.

**Use this one in priority. It's safe, robust and generic.**

## Tone equalizer

Filmic is a global tone curve, it doesn't care about luminance blobs and continuous areas (for example : sky vs. ground). Also, global contrast is linked to local contrast (aka the feeling of sharpness) in weird ways.

When you need to **balance contiguous areas** against each other in terms of brightness, tone EQ is the way to go. The internal mask ensures you don't mess up the local contrast too much, aiming at having a piece-wise constant exposure correction.

**Use this one for sunsets, landscapes and studio shots where you have a continuous range of luminances that you need to even.** That is, either for adding or removing contrast.

## Masked exposure instance

The tone equalizer is really just an exposure compensation where the exposure correction is made dependent of the original luminance (norm) of the pixel, and with internal masking ensuring an uniform exposure correction over contiguous regions in the image.

When you have a clear separation between foreground and background, for example a **dark subject shot in backlighting situation,** it is actually easier to use a basic exposure module, with a new instance and with a typical drawn mask. This will remove the need of fiddling around with tone EQ masking setting.

From the pixel maths perspective, tone EQ and masked exposure are the exact same operation, the difference is merely the user GUI and sweeteners on top.

## Color balance

People wrongly assume that "color" is the pack of hue and chroma/saturation. Lightness/Brightness is a valid part of it too.

Imagine **you color-graded the subject of your image**, meaning you masked it out of the rest, you may want to selectively increase its contrast to enhance its volume and peceived third dimension. That's where the color balance contrast comes into play.

**The color balance contrast is meant to be used selectively, within masks, because it will change the white point of the picture and will invalidate your filmic white exposure setting. But it's super powerful since you can set its fulcrum.**

From the "mask" tabs in colorbalance, the grey fulcrum can be set with a zone color picker. In practice, luminances above fulcrum will get increased, luminances below fulcrum will be decreased, the fulcrum itself will keep its original luminance. Once you set the fulcrum to the average luminance of your subject, increasing the contrast locally on the subject will get a quick boost of local contrast with none of the side-effects of the typical local contrast operators (fringes and halos around edges).

---

**Steve** — 2023-04-08

Thanks so much for clarifying this for us AP. I too was some what confused.

---

**migmoq** — 2023-04-11

Yes, thank you very much. We have now a better overview of what each of them does and for which purpose.

