---
title: "Toning images"
date: 2023-03-22
slug: "toning-images"
tags:
  - Community archive
forum_author: "Jofial"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/toning-images"
wayback_url: "https://web.archive.org/web/20230601130543/https://community.ansel.photos/view-discussion/toning-images"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/toning-images`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20230601130543/https://community.ansel.photos/view-discussion/toning-images).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Jofial** on 2023-03-22.*

Hello everyone,

I have a query. My photographic background comes from the days of chemical photography (not digital). We used to make use of toning to preserve prints (Selenium, platinum, sepia, etc.).

In DT I used to use the color correction module. Now obsolete in Ansel. This module had a virtue very appreciated by me because it allowed me to tacked the images without "tinting" the whites. In the current modules I have not been able to do this. They all end up "coloring" the whites. The tacking only attacked exposed and developed silver halides, the whites not having such halides, were not affected.  

  

Any suggestions?

## Replies

**Scorpion078** — 2023-03-23

you can try applying a parametric mask where you protect the whites

---

**Aurélien Pierre** — 2023-03-23

You can tint shadows only in color balance RGB, using the "4 channels tab", and a mix of offset and shadows lift, possibly even the midtones power.

---

**Jofial** — 2023-03-23

But it is not the same in terms of operability. With the "color correction" it was two clicks: set the white in the center and move the black to one of the color/tone boxes.

I will look for a solution and create a preset. I will comment if I find a good solution

---

**Jofial** — 2023-03-23

I will try it and let you know if it works for me.

Thanks

---

**Aurélien Pierre** — 2023-03-23

The problem of color correction is the transition to black to white is done linearly in CIE Lab space, assuming a display-referred (bounded white) image. That assumption is voided in our pipeline.

---

**Jofial** — 2023-03-24

While trying to achieve a tonal shift using 4-way color balance, I noticed the following.

As I have not seen any reference in the Ansel or Darktable documentation, I ask if this is normal and what is the purpose of the percentage being so different between the different vias.

I leave an image

Any ideas or advice?

*\[attachment lost: image was hosted on the retired forum\]*

---

**Jofial** — 2023-03-24

To match the ease of converting my B&W photographs to a tonal tonal shift such as Sepia, Cyanotype, Platinum, Selenium, etc., I have to use a tonal shift to convert my B&W photographs to a tonal shift such as Sepia, Cyanotype, Platinum, Selenium, etc.

I have only found with this tool that it allows to be worked by independent channels and allows the "scene mode".

Would it be acceptable in a scene mode workflow?

*\[attachment lost: image was hosted on the retired forum\]*

---

**Aurélien Pierre** — 2023-03-24

Yes, it's normal. The same number does not have the same effect depending on the setting, so the GUI has been adjusted for consistent visual effect. Numbers are just symbols, they don't mean anything in themselves.

---

**Aurélien Pierre** — 2023-03-24

Again, this is a GUI that expects 100% to sit at the far end of the graph, aka display-referred framework. It can work to some extend in scene-referred, but I don't see why you would want that for toning monochrome.

---

**Aurélien Pierre** — 2023-03-24

I wrote that just for you : https://ansel.photos/en/workflows/monochrome-toning/

It's work in progress, but the fundamentals are there.

---

**Jofial** — 2023-03-24

Thank you. I'm going to try, and check my obsession that the whites are not colored

---

**Aurélien Pierre** — 2023-03-24

They won't if you follow the guide.

---

**Jofial** — 2023-03-24

Yes.

I am very happy and embarrassed.

Happy, because now I have a method very similar to the chemical one without breaking the flow referred to the scene.

Embarrassed that I did not achieve this result by my own means.

Thanks for your help.

This is the result:

*\[attachment lost: image was hosted on the retired forum\]*

---

**Jofial** — 2023-03-24

But, there is always a but...

In photos with speculars or areas with some saturated channel. I have my doubts...

Here is an example:

*\[attachment lost: image was hosted on the retired forum\]*

This is the complete image

*\[attachment lost: image was hosted on the retired forum\]*

---

**Aurélien Pierre** — 2023-03-24

You can increase chroma until you get the amount of tinting you want.

---

**Aurélien Pierre** — 2023-03-24

What is the problem with saturated regions ? B&W conversion will remap them to white, and then it's business as usual. Or it should be.

