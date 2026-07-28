---
title: "Vibrant colors and skin tones"
date: 2024-11-12
slug: "vibrant-colors-and-skin-tones"
tags:
  - Community archive
forum_author: "nicorikken"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/vibrant-colors-and-skin-tones"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/vibrant-colors-and-skin-tones`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **nicorikken** on 2024-11-12.*

I've been reading up on Ansel color dimensions to add more color to my event photo's without it looking too unnatural.

I fail to understand why 'basic colorfulness: natural skin' preset in Color balance rgb is defined using saturation instead of chroma. Chroma seems to me more fitting for skin tones. What was the thought process of this preset? (I did watch the videos on this module).

Also Color balance rgb sliders differentiate on luminance (shadows, midtones, highlights) and so doesn't account for skin tones as other software does in a 'vibrance' setting. I did some experiments using a parametric mask on hue, which works but also will take time to get to a good default setting. How do other users deal with this?

## Replies

**Pedro Rodríguez** — 2024-11-12

Saturation is designed to avoid neon colors. If you increase chroma too much, you easily get colors that seem to glow. Saturation alleviates this by slightly darkening as you increase it, and slightly lightening as you decrease it.

Masks are a good option, but skin is often in the midtones, so if you increase saturation in the midtones you often get good results. Also, I've been playing with the shadows and highlights falloff in the masks tab, as well as where both areas overlap.

Once color equalizer is merged, you will be able to target specific hues much quicker, though.

Hope that helps

---

**nicorikken** — 2024-11-12

Thanks. I did some more experimentation and noticed that when I was pushing colors to extremes to exaggerate the effect, I never pushed chroma as much as saturation because the slider of chroma goes to 50% where the slider of saturation goes to 100%. I mistakenly assumed that saturation was resulting in a worse look. Going for a similar result using chroma by manually entering higher numbers results in brighter reds and blues that appear neon-like, as you mentioned. So saturation as implemented in the great color science in Ansel is the better way to go.

Color equalizer would indeed be a great solution to be able to push saturation some more while avoiding the saturation effect on skin tones. Until then I can distinguish on luminance using the sliders or use filters.

Of course the proper color calibration and lighting conditions also have an effect on saturation on skin tones. I have one photo where a few people have a warmer reflected light on them than the main people of interest. When pushing the saturation the warmer lit people become orange rather quickly compare to the ones for which the color correction is set.

If somebody else has tips or suggestions I'm happy to learn them.

