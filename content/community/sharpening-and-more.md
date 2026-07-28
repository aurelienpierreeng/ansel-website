---
title: "Sharpening and more"
date: 2025-01-23
slug: "sharpening-and-more"
tags:
  - Community archive
forum_author: "Annabel"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/sharpening-and-more"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/sharpening-and-more`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Annabel** on 2025-01-23.*

Firstly, I was editing yesterday and it all went very well. It seems to me Ansel has improved a lot over recent weeks. Thank you Aurelien and the team. There's Darktable of course but Ansel is the way to go for me.

Re. sharpening, I was reading about final resampling here - https://ansel.photos/en/doc/modules/processing-modules/finalscale/ and moving the module to before Filmic. I don't obsess about sharpening but it makes sense to me to do it at the final resolution. So how does the module know what dimensions to go down to? Presumably those in the Output module, yes? And if you've just typed them in and so not yet exported with them, are they nevertheless used for the "early" resampling. I always use the "bounding box" option.

I had a quick try using a raster mask after final resampling which was defined before f.r. Is this recommended / supported? I can imagine it's quite a complication for the pipe to change resolution part way through.

Re. upscaling, which I generally don't do, Darktable gives you the option to stop any upscaling regardless of the target pixel dimensions you have set at the time. I can't see anything equivalent in Ansel, what does it do pls?

## Replies

**Aurélien Pierre** — 2025-01-24

All sharpening and blurring modules use the resolution of the pipeline at the stage where they are put. Those modules are highly scale-dependent and trying to account for resizing (for example, setting the pixel size with regard to raw resolution and correcting it for actual resolution when applying the module) will be at best inaccurate. There are 2 reasons for that :

1.  pixels are integer numbers, so rescaling a 3 px diameter by 50% leads to either 1 px or 2 px. 1 px is basically equivalent to doing no blurring or sharpening at all, and 2 px is a 17 % error.
2.  some internal parameters (like edge-avoidance) have a 2D dependency to the image features in the region used for blurring/sharpening, which can't be reduced to a simple correction factor to apply on user input to account for image scale.

That said, we still try to perform these inaccurate corrections in darkroom previews, for the sake of having something to preview. But for robustness of exports, we avoid them in this context. In the same spirit, the option to export with early downscaling (after demosaicing), for the sake of speed, has been removed recently, so the downscaling will always happen within the "final rescaling" module, at the end.

Ansel prevents export size from being larger than the input raw size, without option, because it's the safe thing to do. Properly increasing resolution requires "super resolution" algorithms that use machine learning/AI to infer the content to dilate.

Now, you need to decide what you want to sharpen, and that's mostly deciding what kind of blur you want to undo. Lens blurs or demosaicing low-pass (aka blur…) are defined optically, in scene-referred space and in sensor coordinates. These need to be undone on scene-linear RGB, using pixel coordinates relative to sensor coordinates, so there is no need to move the modules achieving that past final resolution module.

There has been a trend, among digital photographers, to sharpen after downscaling images. I have personally never done that, both because I find oversharpened pictures way more disturbing than slightly soft ones, but also because uploading pictures to web services may resize thumbnails on the server (typically, to support [responsive image sizes](https://developer.mozilla.org/en-US/docs/Web/HTML/Responsive_images#resolution_switching_same_size_different_resolutions) and please Google), and those services usually don't resharpen thumbnails (except for [Flickr](https://www.flickr.com/help/forum/en-us/72157710116798327/) - who is still using it in 2025 ?). In that case, the look of your images may be inconsistent depending on viewing scale (which may load a different image file, if using responsive images sizes), so it's better to just do nothing.

Now, if you still wanted to sharpen post-downscaling, you should probably do so with a small radius (1 to 2 px, so that's a diameter of 3 to 5 px), and those are pixels relative to the coordinates of the final size, which any module in Ansel will use when placed in the pipeline after the final rescaling.

Be aware, though, that sharpening may create negative RGB values in the darkest areas. Filmic has some tricks to recover them as to avoid creating chroma noise, but later modules don't, and anyway, you might end up crushing shadows, depending on image content. All in all, sharpening late in the pipe is more like a ticking bomb.

---

**Annabel** — 2025-01-26

Thanks for that, very informative. Ha, nothing is as simple as you might like! I think I'll pretty much leave the pipe order to itself going forward.

