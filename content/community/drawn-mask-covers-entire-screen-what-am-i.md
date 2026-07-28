---
title: "Drawn Mask Covers entire Screen What am I missing?"
date: 2023-05-27
slug: "drawn-mask-covers-entire-screen-what-am-i"
tags:
  - Community archive
forum_author: "Damon"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/drawn-mask-covers-entire-screen-what-am-i"
wayback_url: "https://web.archive.org/web/20231001121820/https://community.ansel.photos/view-discussion/drawn-mask-covers-entire-screen-what-am-i"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/drawn-mask-covers-entire-screen-what-am-i`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001121820/https://community.ansel.photos/view-discussion/drawn-mask-covers-entire-screen-what-am-i).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Damon** on 2023-05-27.*

I'm new to Ansel/DT. I am much more used to RawTherapee. I wanted to mess with the color saturation in this photo only on one section of it. I drew a mask with the path tool, but when I change the settings in the color balance RGB module, it applies to the whole picture. Also, if I preview the mask, the whole screen is yellow. I eventually got the mask to behave the way I expected after mashing buttons for 25 minutes, but I don't know how I would reproduce it, so I reverted to a backup of the XMP file so I could learn to do it correctly.

So...question is why do I have a mask drawn, but the module's effect is still applied to the entire image?

Here is a screenshot of my settings...also showing the mask I made with the path tool.

  

*\[attachment lost: image was hosted on the retired forum\]*

And here is what I get with the "mask preview."

*\[attachment lost: image was hosted on the retired forum\]*

## Replies

**ariznaf** — 2023-05-28

You have to have changed something.

May be you changed the mode (exclusive, inclusive,) or the composing of masks (union, intersection...)

Or may be you have created a Ptah independent of the module and have not applied it to a module.

Paths and modules are independent, you can create a path and apply it to several modules.

If you create the path under the module mask (at the right) it is automatically applied to that module, and selects the interior.

Be sure there are selected figures in the module mask.

---

**Damon** — 2023-05-28

I finally figured out how to get the mask to behave the way I want it to. Look at the screenshot...in my browser, I have to right-click --\> "open image in new tab" since this website scales the pictures down so much.

Anyways in the upper left there's a slider for "Mask Opacity" and that is somehow set to ~13%. I just moved the slider to 100% and that took care of it.

I'm pretty sure the "Mask Opacity" in the upper left is totally unrelated to the "Mask Opacity" that's found in "Mask Refinement" section of the module (right sidebar).

---

**ariznaf** — 2023-05-28

Mask opacity affects at the intensity of the selection, if you use 0% everything is un selected and there is no yellow area, as everything is unselected.

  

You have the selection inverted it seems, and everything is yellos, selected so it seems your selection is not selecting anything.

I usuallly do not use the left menu for selections, just when I need to delete a figure or something.

Usually you create the selection in the right menu.

  

But you can create it in the left an select one of the figures created to be applied to a module, they are the same, at the left you see al figures created for any module and grouped for figures used in a module.

It seems a bit confuse, I know.

---

**Aurélien Pierre** — 2023-05-28

> I'm pretty sure the "Mask Opacity" in the upper left is totally unrelated to the "Mask Opacity" that's found in "Mask Refinement" section of the module (right sidebar).

There are several opacities here, the masking logic is really messy.

You have shapes, drawn from several methods (circle, ellipse, path, pen), that get aggregated in groups (possibly using boolean operations) to define masks. Groups can themselves be aggregated in hierarchical groups. The highest level of mask group is the module level, which is targeted by the opacity slider you see in the masking options (refinement) in the module. While the global opacity slider in the header toolbar targets the group to which the currently-selected shape belongs.

The joys and wonders of multi-layered masking code hacked again every 2 years since 2014 to avoid a anxiety-triggering rewrite…

