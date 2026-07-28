---
title: "Muted contrast and filmic "
date: 2023-04-13
slug: "muted-contrast-and-filmic"
tags:
  - Community archive
forum_author: "Pedro Rodríguez"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/muted-contrast-and-filmic"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/muted-contrast-and-filmic`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Pedro Rodríguez** on 2023-04-13.*

This is a question for @Aurélien Pierre.

At some point in the chat you told me that artificially extending the DR of filmic puts stress on the interpolation and may produce inverted curves. Also, that filmic will be mapped to black point compensation at some point. I understood from this that filmic should just be treated as a more technical module, the display transform, and for artistic choices we should use tone eq and color balance RGB.

After your recommendation, I'm reading the "Color correction handbook", and after going through the chapter on contrast, I was a bit unsure how to best create a lower contrast, muted look. Talking about highlights, the author says that they can generally be anywhere between 60-100%. If say I want my hl around the 70% mark (i know scopes are broken, I'm using my eyes, but just as a reference) what's the best way to achieve this?

I've tried pushing and pulling the luminance sliders in color balance, but such big shifts tend to reduce contrast quite a bit. Doing it via tone eq also hasn't yielded the best results. So far the best look comes from raising the white relative exposure in filmic carefully until the highlights are where i want them, then using tone equalizer and/or color balance RGB.

What is your take?

## Replies

**Aurélien Pierre** — 2023-04-13

I will need a RAW file and a picture of the target look here.

---

**Pedro Rodríguez** — 2023-04-13

Let's take this example of an indoor shot. One version is your typical exposure adjustment and filmic auto levels. It works great for me.

The other is the same in terms of exposure (+1.970 EV), but went crazy with white relative exposure in filmic (+16EV). So that the curve wouldn't break, I reduced contrast in the look tab to 0.800. Then, following the recommendations of the Color correction handbook, I lowered the power in color balance RGB to -13.37% and raised my shadows by 100%.

Here is the raw file:

https://drive.google.com/file/d/1s2_6y5ErnIH--9sKqmxo-tqpaTNcqEcq/view?usp=share_link

---

**Pedro Rodríguez** — 2023-04-14

Found the better solution, I think. Reduce contrast in color balance RGB and bring shadows down with offset and shadows luminance sliders. It also has the added bonus of being able to control the contrast fulcrum in the masking tab.

