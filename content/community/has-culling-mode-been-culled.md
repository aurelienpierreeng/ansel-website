---
title: "Has \"culling mode\" been culled?"
date: 2023-05-27
slug: "has-culling-mode-been-culled"
tags:
  - Community archive
forum_author: "Damon"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/has-culling-mode-been-culled"
wayback_url: "https://web.archive.org/web/20231001125223/https://community.ansel.photos/view-discussion/has-culling-mode-been-culled"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/has-culling-mode-been-culled`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001125223/https://community.ansel.photos/view-discussion/has-culling-mode-been-culled).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Damon** on 2023-05-27.*

As I'm familiarizing myself with Ansel, I tried to enter [culling mode](https://ansel.photos/en/doc/views/lighttable/lighttable-modes/culling/). But when I hit X or Control-X in the lighttable view, a message says "X is not assigned."

I tried to get into culling mode it in DT 4.2 and it worked OK.

I'm using the 0.0.0+285~g0c37799cc appimage.

## Replies

**ariznaf** — 2023-05-28

I think culling and rating is being reworked in Ansel, there is another thread about.

/archive/culling-rating-images-workflow/

---

**Aurélien Pierre** — 2023-05-28

yes

---

**Aurélien Pierre** — 2023-06-10

Culling mode is replaced by something much more simple.

When you think about it, the culling mode is merely a reduction of the current picture collection to a set of selected pictures.

So the culling view is replaced by a "selected" filter in lighttable top toolbar. Select the thumbnails you want to get, click on the "selected" button in top toolbar, do what you need to do, and when you are done, click again on the "selected" button and you shall get back your original collection.

---

**Lukas** — 2023-06-13

I really like the "selected" filter as a nice and simple version of culling mode. One thing struck me though: When I enable the "selected" filter, I enter a new level of collection. In the screenshots below there are 10 images selected, once I activate the "selected" filter, it only displays those 10 images (as expected), but it also reads "0 images of 17 images in current collection selected".

*\[attachment lost: image was hosted on the retired forum\]*

*\[attachment lost: image was hosted on the retired forum\]*

  

I would have expected that the selection stays the same, which would in turn make it possible to cull images by simple deselecting them. In other words: I select all candidates, enter selected filter, deselect until I have reduced down to "keepers", then apply star rating/color label/tag to the remaining and still selected images.

Nice touch on the automatically adjusting zoom level in the selected filter.

---

**Aurélien Pierre** — 2023-06-15

The culling mode turns the current selection into a collection, while saving the previous collection and selection. When you exit the culling mode, previous selection and collection are restored as before. But the collection is not dynamic, so it's initialized when you hit the "selected" button.

The reason for the current design is to keep the behaviour of filters and rating unchanged, which expects you to deal with keepers using star rating (then filter out images using usual star filter). Having a dynamic collection following selection in real time would prevent individual editing.

---

**cyberspeck** — 2023-06-17

What I liked about the culling view in darktable is that it handles the images in one line (instead of a 2-dimensional layout). So when I zoom-in in Ansel to view only 2 images next to each other, I usually end up seeing the top part of the next two images below the currently shown 2 images. I find this rather distracting. However, what bothers me even more in Ansel is that when I press the "right-arrow" key to view the next image, the view actually jumps to the row. In culling mode (darkatable) it would only shift the currently shown pictures by one, basically moving the previously right image to the left side and show the next image in line on the right side. I prefer this behavior because it allows to compare any image directly with their neighbors. Is there a way to reproduce this in Ansel?

