---
title: Introduction
date: 2024-07-14
weight: 1
---

## Context

Digital photography has widely spread in the 2000's as it allowed faster workflows and made possible to get immediate results, compared to the traditional film & darkroom workflow. But this introduced many new problems.

Firstly, analogue photographers were not necessarily accomplished lab and printing technicians, but could rely on local photo labs to get their developments and prints done. Digital photography added the burden of processing the "digital negatives" (raw files) on the shoulders of the photographers, by means of software. But those photographers didn't usually got the appropriate training, both in digital color management and in general computer use. That pushed many of them in the hands of over-simplified software, verging on the toy side, which defined the mainstream expectation of what a digital photo editing software should be. Video editing software took another approach, being used by heavily-trained professionals in a billion-dollars industry.

Secondly, the analogue printing is a hands-on process, where the lab tech interacted directly with the finished product : the print. Digital processing makes a virtual master edit, because the monitor used to preview the result will generally not have the same visual properties as the printing medium or as the consumer display. This introduces complexity in the imaging pipeline, because what you are interacting with is neither what you will see, nor what you actually manipulate. For example, when you push an Lch slider, that should make a change to HDR pipeline RGB, but what you will see is the effect on SDR display RGB after gamut and tone mapping. The proper way to handle this is through the [model-view-controller paradigm](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller), but many software did not get it right[^1]. Display profiling workflows, like the ICC framework, have tried to automatize and hide most of the complexity of color management, but they mostly managed to confuse users even more by abstracting too much things that can actually be written as a couple of equations using only domestic-accounting-level maths (sums and products).

[^1]: And most software still use broken [alpha compositing](https://hg2dc.com/2020/08/26/question-25/) in sRGB, as well as unassociated alpha, so even the color models are butchered.

Thirdly, the analogue lab tech could directly (physically) access the paper and the negative to perform all kinds of adjustments and even distortions (dodging & burning, masking, split-toning, cross-processing, bleach bypass, solarization, etc.). This direct physical access enabled artists to hack the printing process in ways sometimes unplanned by vendors, to match their targeted visual outcome. Digital imaging has cast away the techs and artists alike from the medium, and they are confined to the functionality provided in the GUI of their software. The actual image lives in the computer as pure data, and only engineers know how to access it and what happens to it.

Finally, digital imaging has been driven by computer scientists rather than by color scientists, let alone by actual photographers or photo lab technicians. They developed a digital language incompatible with the legacy of analogue photography and collections of editing tools making use of anonymous unit-less parameters that didn't care for optics and exposure values, thus confusing the analogue-trained photographers (used to drive brightness through light exposure or chemical developing times…). Their constant reliance on "barely working" color spaces (HSL, non-linearly encoded RGB) to handle color changes impregnated many an user with bad habits which soon became expectations, then requirements. The color pipelines developed by the coding monkeys later needed a completely different workflow to handle HDR images, because their hacky logic didn't scale with dynamic range and "worked" only as long as camera sensors and computer displays had mostly the same dynamic range as paper prints, with no future-proofing intended.

## High-level goal of Ansel

Ansel aims at being an instrument of visual expression letting artists develop their own interpretation of the raw material by allowing a large expressive range of color effects, much like a musical instrument lets musicians interpret the score by allowing a large expressive range of sound effects. This is achieved by putting back the retoucher in the center of the image processing, by allowing a transparent and as-direct-as-possible access to the image data, and by providing color manipulations making sense either on an optical level or on a psycho-perceptual level.

Although film and the analogue legacy is often used as an inspiration and as a starting point/first base, making digital image processing a 1:1 virtual translation of analogue printing is not the goal. Let us not forget that film was engineered within the technical limitations of dyes and chemicals, and that many of its beloved properties are actually limitations of its technology (which is not to say that don't have expressive merits, but let's not fall into backward-looking for the sake of it), and were not actually desired in the first place.

However, much like music, it is expected from users to complete at least a basic theoretical and practical training to be able to use this imaging instrument, and Ansel will not give up visual quality for the sake of smoothing the learning curve.

## User-level goal of Ansel

1. Allow to efficiently cull the photographs coming out of the camera/memory card, in order to pick only the ones worthy of being fully post-processed,
2. Allow to edit/retouch the culled photographs in the most direct way, with a minimal number of steps, using unit image controls that affect only one perceptual or optical property at a time,
3. Allow indexing and later retrieval of the processed photographs for archival purposes.

## Supported workflows

Any tool can only be made optimal for a single and definite use case. Supporting too many uses cases will prevent optimization at all. This is where upstream darktable miserably failed. The workflows presented below are the intended uses for Ansel. Any use that deviates from these may be possible but is not recommended and nothing will be made to actively support it.


### Culling workflow

1. The user will mount the file system of the camera or the memory card using the OS tools (MTP/PTP protocols, FAT/exFAT file systems),
2. The user will import the pictures in individual directories named like `YEAR-MONTH-DAY-Job name`. The pictures will use unique names like `Job name-ID number.extension`. Those directories will be used in Ansel as the parent path for "filmrolls" and opened in lighttable once pictures are imported. Filmrolls may or may not contain the whole content of their associated directory.
3. The user will proceed to the culling part. Images are imported with a rating of 0 star. Obviously bad pictures will be rejected (shortcut : <kbd>R</kbd>). 2 methods can then be used :
   1. negative : assign an high star-rating to all pictures, and gradually downgrade bad pictures, so only the keepers keep their high rating,
   2. positive : assign a 1-star-rating to all the seemingly-good pictures, then assign a 2-star rating only to the best of the 1-star-rated, and carry-on until reaching 5 stars or any rating where an appropriate amount of keepers is left,
4. From there, the highest-rated images are considered keepers and may be edited. [Batch-editing features](https://docs.darktable.org/usermanual/4.0/en/guides-tutorials/batch-editing/) that may speed-up this step for series are presented on upstream darktable's manual.
5. Tracking the state of pictures in the workflow can be made through the darktable internal tags `darktable|changed`, `darktable|exported`, `darktable|printed`, which are set automatically when these operations are done. Users needing more states, like those who edit in several steps (one step of basic editing, for better preview during culling, another step of full editing), may add more children tags to the `darktable` parent tag, like `darktable|edited` for pictures that are finished and ready to export.
6. The user may set color labels, tags and metadata in light table, after editing and before exporting, for better archiving.
7. The user may export and print the pictures. It is advised to keep a 16 bits TIFF export in Adobe RGB or ProPhotoRGB color spaces for archival purposes as soon as the edit is finished, to prevent any data loss that may incur with future versions of Ansel or upstream darktable (although everything is done to ensure future compatibility of the software with old edits, mistakes happened and will happen again).

### Notes and Comments

The proposed culling and storing method is the best as it allows to efficiently search and access the pictures from any external software, including other cataloguing software and file browsers. Directories containing dates and job names can be easily searched from any file browser, and each directory is a consistent collection on its own that can be re-imported as a whole, with no further internal sorting.

Users are advised against ditching all pictures in a yearly directory and relying too heavily on Ansel/darktable's filtering features to browse them. If you need to send pictures to a website or to print via internet (through a web browser calling the file browser), this method is clearly inefficient. It is probably the origin of the filtering over-engineered GUI introduced in darktable 4.0.

Users are warned against the "mad librarian syndrom", which consists in hugely overdoing the tagging and sorting. Photo stack agencies may heavily rely on tags to structure their image database of images because they need to deliver pictures of matching content for illustrative purposes quickly, but individuals should not spend more time tagging than taking pictures. Tags are meant to bind similar pictures together, if you find yourself using tags applied to only 1 or 2 pictures, you are defeating their binding purpose, your tagging method is too restrictive and you may want to use image title instead (which can also be searched later). Restrictive and specialized tags should be made hierarchical, so the parent tag can be fetched instead of cooking complex queries fetching multiple children to get your images.

Although color labels may be used as implicit status tag, the recommended way of documenting the status of an image is through the `darktable` tag children, which is explicit. Such status tags may get a dedicated GUI at some point.

In darktable, the tags have been customarily misunderstood as mere keywords, but they are actually hierarchical taxonomies that can be used to declare categories or arbitrary collections. If your pictures are properly stored in directories containing meaningful names, then those names can be used directly in searches, in place of tags. Many users, including myself, manage databases of more then 30.000 images through only directories (filmroll) names.

In any case, if you find yourself needing a complex GUI to sort and access your pictures, your method needs to be simplified. A good software allows to achieve simple tasks simply, and I refuse to make the simple tasks complicated just to account for insane workflows.

## Processing workflow

The scene-referred workflow is the standard in Ansel, as it proved to be faster and more reliable for users who allocated some time to understand it, and allows an unified treatment for HDR and SDR scenes alike. It relies on manipulating the image in a framework where pixel RGB is treated as a light emission for as long as possible, allowing accurate (de-)blurring, (de-)noising, illuminant correction and color-preserving brightening/darkening based on exposure compensations. When the last optically-bound image filter is applied, it then shifts to a perceptual framework where the pixel RGB is converted and handled as a 3D color object (hue, chroma or saturation, lightness or brightness) using color appearance models.

1. The user will setup the global exposure as to match the overall picture brightness to the desired level, in exposure module. This will usually consist into matching the average brightness or the brightness of the picture's subject to the brightness of the GUI background color (middle-grey by design),
2. The user will ensure the bounds of the scene dynamic range are properly remapped to the bounds of the display dynamic range, in filmic module. For typical SDR monitors, the default display settings will not need to be changed, but the scene white and black relative exposures will need to be adjusted for each image, either automatically (use the "Auto tune levels" button) or manually. Then, adjust the contrast (in "look" tab) to taste.
3. The user will ensure the white balance is neutral (reminder : it's not an artistic choice) by setting the "CAT" tab properly, in color calibration module. The user may calibrate the colors directly from a color checker test shot too.
4. Any artistic color deviation, in hue or in saturation, may be applied in color balance module.
5. Any other artistic change can then be made.
