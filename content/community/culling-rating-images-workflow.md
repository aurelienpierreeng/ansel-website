---
title: "Culling/Rating Images Workflow"
date: 2023-04-15
slug: "culling-rating-images-workflow"
tags:
  - Community archive
forum_author: "Joshua"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/culling-rating-images-workflow"
wayback_url: "https://web.archive.org/web/20231001123557/https://community.ansel.photos/view-discussion/culling-rating-images-workflow"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/culling-rating-images-workflow`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001123557/https://community.ansel.photos/view-discussion/culling-rating-images-workflow).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Joshua** on 2023-04-15.*

Hello all!

I was wondering if people wouldn't mind sharing how they assess a collection of new photos for which to work on further? (commonly called culling, but I will omit this term to avoid confusion with the removed "Culling" mode)

  

Personally, the most intuitive approach would be able to view each photo in a full screen, and then with keyboard shortcuts rate/reject photos, and move onto the next.

This almost works out-of-the-box in Ansel, but there's a quirk with photo selection.

The rating/reject shortcuts work on the "Selected" image (shown with a light grey highlight), however arrow keys do not change this "Selected" image they merely move the "cursor" to other images, at which point they can be selected with "Space".

  

This leads me to use this workflow currently:

1\. Adjust Lighttable to view 1 photo per row, press tab to remove panels.

2\. Rate/reject/color the photo

3\. Press Space to unselect it

4\. Move to the next photo with Right

5\. Press Space to select it

6\. Repeat from step 2

  

  

This is fairly cumbersome, and I do not like that if I've made a mistake with my Space select/unselect dance, I can end up with some other photo silently selected in the background and then I am performing invisible rating/rejection edits to it without realising.

  

Please let me know if I'm missing something here, or any alternative approaches people have.

  

Thanks,

Joshua

## Replies

**Aurélien Pierre** — 2023-04-16

The lighttable is currently undergoing cleanup and simplification, which I fear will end up in a complete rewrite, so there are transient annoyances like that for now.

---

**Lukas** — 2023-04-17

This is a similar problem, ﻿@omrihar﻿

---

**cyberspeck** — 2023-05-12

I face the same problem. And I would be interested to know (or contribute to) the future design of the lighttable view. For me, I feel like work in lighttable currently takes 3 times the effort it should take. Cheers, david

---

**ariznaf** — 2023-05-22

Providing feedback in the thumbnails about stars, flags an other info would be great and would help, as you could immediately see the changes to classification.

Lightroom has strong capabilities in that aspect, I think it would be a good model to follow.

---

**Steve** — 2023-06-10

I concur. Ansel really needs a simple browser for viewing/zooming/rating files before import.

---

**cyberspeck** — 2023-10-09

Hi Aurélien,

Any estimate when the lighttable will get its overhaul? Today it accidently marked a big numer of my photos as 'rejected' and I could not undo it without restoring an backup of the xmp files. Honestly, I don't trust Ansel to provide what I need for efficient and reliable culling right now.

---

**Aurélien Pierre** — 2023-10-10

How did you accidentally reject all the pictures ? Using the mouse or the keyboard ? Did Ctrl+Z work ?

---

**cyberspeck** — 2023-10-10

I was marking images using the mouse and pressing "r" to reject the photos which I wanted to delete. At one point Ansel did not longer reject them but a pop up said "r not defined" (or something similar). I don't know what exactly had happened at this point. I tried to get "r" working again by switching into darkroom mode and back, but it still didn't recognise "r". I then closed/restarted Ansel. By that time the undo history was gone, but only then when I continued to mark images I noticed that I had somehow marked more as rejected than I had intended. I'm not sure how it happened, but I the inconsistent behaviour probably led to me doing it without being aware.

---

**Lukas** — 2023-10-11

I had similar problems when rating and rejecting photos. A couple of times I got a hint saying something like "r not defined" or "not initiated", but it sort of went back to working for unclear reasons. Just recently I discovered that having caps lock activated can throw off the shortcuts as well. The main confusion was due to the hint saying "r not assigned". I have written a [bug report](https://github.com/aurelienpierreeng/ansel/issues/211) about that.

