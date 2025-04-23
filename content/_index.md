---
title: "Ansel"
date: 2022-11-27T22:36:34+01:00
draft: false
description: "Ansel is an open-source raw photo editor for artists"
tags: ["darktable", "ansel", "photo editing"]
---

<div class="pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold">Your digital darkroom</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4"><em>Ansel</em> is an open-source photo-editing software for digital artists, designed to help you achieve your own interpretation of raw digital photographs.</p>
  </div>
<div class="my-5">
{{< slideshow images="lighttable.jpg,darkroom.jpg" >}}
</div>
</div>

<div class="container">

{{< quote author="Ansel Adams" >}}
The negative is the score, and the print is the performance.
{{< /quote >}}

<div class="lead">

Pressing the camera shutter merely started a process ending when the on-screen picture looks like the one you had in mind. _Ansel_ proposes to put the artists back at the center of the creative process and enables them with an interface to manipulate images with precision and nuance, using state-of-the-art color science and independent color controls.

</div>


{{< divider >}}

## Install

{{% row %}}
{{% card icon="linux fab" title="Linux" %}}
Distribution-agnostic executable
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/lin-nightly/master/ansel.stable.AppImage.zip" label="Download ansel.appimage" icon="download" >}}
{{% /card %}}

{{% card icon="windows fab" title="Windows" %}}
Windows 7 to 11 installer
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/win-nightly/master/ansel.stable.win64.zip" label="Download ansel.exe" icon="download" >}}
{{% /card %}}

{{% card icon="terminal" title="Build from source" %}}
Best performance for your hardware
{{< button url="/en/doc/install" label="Building instructions" icon="wrench" >}}
{{% /card %}}
{{% /row %}}

{{% row %}}
{{% column %}}

{{< warning >}}
__Ansel is in alpha version__. The GUI is susceptible to change and the application may crash under some circumstances.
{{< /warning >}}


{{% /column %}}
{{% column %}}
The links above always point to the latest nightly build of the "fairly stable" branch. If you want a particular version or need to roll back, [you can find all intermediate versions on Github](https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0).
{{% /column %}}
{{% /row %}}

{{< divider >}}

## Why Ansel ?

{{% row %}}
{{% column %}}

Many solutions already exist to produce ready-to-consume photographs for masses, from smartphones filters to out-of-cameras JPEGs, followed recently by AI-driven automagic toy filters. These make photography easier than ever, but are the produced images really __your__ images and, in any case, the images __you__ expected ?

{{% /column %}}
{{% column %}}

_Ansel_ lets you interpret your raw photographs much like a music instrument, when most software tries to automatically play the score for you. It aims at being an underwhelming, boring, tool that just does what you ask of it, without getting in your way.

{{% /column %}}
{{% /row %}}

<div class="text-center my-5">
<span class="display-5">Get excited by your results</span><br />
<span class="fs-4">Not by your toys</span>
</div>

{{% row %}}
{{% column %}}

When you like music, you can choose between learning how to play or buying recordings. It's easier to buy, but more satisfying to play. Photo editing applications have lied to users for decades, pretending they could play without learning, because the software would deal with technical complexities for them, and entirely hide them.

{{% /column %}}
{{% column %}}

It turns out that users have only been fighting applications they understand less and less, for control over their results, and to recover those tricky cases where automation fails. As time will go by, expect to lose more and more time fighting AIs to get natural-looking results… manually. Why not simply cut the middle-man ?

{{% /column %}}
{{% /row %}}

{{< divider >}}

## What can Ansel do for you ?

Ansel allows you to manage your collections of pictures, to edit your raw digital photographs and film scans non-destructively and to export the result to common file formats. It stores your editing histories as text and lets you go back in time at any editing step you like, anytime.

### Color work

Ansel ships a recent color science, compatible with HDR : the chromatic adaptation CIE CAT 2016, the HDR color space JzAzBz (2017) and the perceptual color space darktable UCS 2022, developed specifically to manipulate color saturation without the fluorescent effect.

<div class="row">
{{% column %}}
<h5>Color calibration</h5>
{{% compare after="calibration-after.jpg" before="calibration-before.jpg" cols="2" %}}
Fix white balance and get __high-fidelity__ colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{% /compare %}}
{{% /column %}}

{{% column %}}
<h5>Color-grading</h5>
{{< compare after="grading-after.jpg" before="grading-before.jpg" cols="2" >}}
Give ambiance and character to your pictures by polishing their color palette with nuanced and fine-grained controls, in RGB, Ych or HSB color spaces, for creative and corrective purposes.
{{</ compare >}}
{{% /column %}}
</div>

<div class="row">
{{% column %}}
<h5>Color matching</h5>
{{< compare after="matching-after.jpg" before="matching-before.jpg" cols="2">}}
Force the chromatic adaptation such that any selected object matches a predetermined color, input from CIE Lab coordinates (for logos and brand colors), or by sampling the color of the same object in another shot, as to even the color rendition over the series.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Hue qualifying and keying</h5>
{{% compare after="masking-after.jpg" before="masking-before.jpg" cols="2" %}}
Use the hue, chroma and lightness qualifiers to quickly define masks and apply selective effects. Combine parametric masks with drawn masks and boolean operations. Refine and feather the edges of masks by blurring or using clever edges detection.
{{% /compare %}}
{{% /column %}}
</div>


### Tonal work

The tonal working methods are designed to manipulate luminance without affecting hue nor saturation, in order to respect the color work, done apart.

<div class="row">
{{% column %}}
<h5>HDR tone mapping</h5>
{{% compare after="filmic-after.jpg" before="filmic-before.jpg" cols="2" %}}
Recover deep shadows and compress the dynamic range while retaining original saturation and hue, with gamut mapping to ensure the colors fit in the output color space. _(Photo : Andreas Schneider)_
{{% /compare %}}
{{% /column %}}

{{% column %}}
<h5>Zone-system editing</h5>
{{% compare after="toneeq-after.jpg" before="toneeq-before.jpg" cols="2" %}}
Balance densities based on exposure zones, by preserving local contrast thanks to an edge detection algorithm, and select the exposure zones to affect directly from the picture, through the interactive cursor. _(Photo : Andreas Schneider)_
{{% /compare %}}
{{% /column %}}
</div>

### Image reconstruction

<div class="row">
{{% column %}}
<h5>Lens deblurring</h5>
{{% compare after="sharpen-after.jpg" before="sharpen-before.jpg" cols="2" %}}
Unleash the power of multiscale, gradient-based machine learning to rejuvenate old lenses, recover focusing mistakes or add emphasis on your subject, but without the typical edge artifacts, over-sharpening oddities or added noise.
{{% /compare %}}
{{% /column %}}

{{% column %}}
<h5>Dehazing</h5>
{{% compare after="dehaze-after.jpg" before="dehaze-before.jpg" cols="2" %}}
Restore some depth in foggy and hazy shots by bringing back textures and saturation in colors, without overaccentuating already sharp details.
{{% /compare %}}
{{% /column %}}
</div>

<div class="row">
{{% column %}}
<h5>Denoising</h5>
{{< compare after="denoise-after.jpg" before="denoise-before.jpg" cols="2">}}
Remove chromatic noise, soften and blend luminance noise.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Highlights reconstruction</h5>
{{< compare after="highlights-after.jpg" before="highlights-before.jpg" cols="2" >}}
Salvage both color and texture in highlights, recover blown areas by propagating gradients while the gamut-mapping watches your back to ensure colorful highlights can still be printed at their proper hue. You don't have to bleach highlights to hide problems anymore.
{{</ compare >}}
{{% /column %}}
</div>

### Specialized features

<div class="row">
{{% column %}}
<h5>Automatic perspective correction</h5>
{{< compare after="perspective-after.jpg" before="perspective-before.jpg" cols="2" >}}
Let the machine learning detect automatically vertical and horizontal lines and compute the best geometric correction to rotate, straighten and crop the picture, optionaly taking into account the kind of lens used.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Censoring</h5>
{{< compare after="censorize-after.jpg" before="censorize-before.jpg" ols="2" >}}
Anonymize people, license plates, etc. and play with use conditions of socially prude network without defiling your pictures too much.
{{</ compare >}}
{{% /column %}}
</div>

{{< divider >}}


## Compatibility

{{% row %}}
{{% card title="Edits" icon="desktop" %}}
Ansel is based on darktable 4.0 and is fully compatible with darktable 2.x up to 4.0 database and XMP files. Coming from darktable ?
{{< button url="/en/doc/special-topics/from-darktable/" label="Find out what is changed" icon="sync" >}}
{{% /card %}}
{{% card title="Cameras" icon="camera" %}}
Ansel uses Rawspeed and Libraw to decode raw photographs. New cameras may need up to 24 months to be fully supported after their commercial release.
{{< button url="/en/resources/supported-cameras" label="Supported cameras" icon="wrench" >}}
{{% /card %}}
{{% card title="Languages" icon="language" %}}
The software is integrally translated in English, French, Italian and simplified Chinese. Partial translations are available in German, Spanish, Portugese, Ukranian, etc.
{{< button url="https://github.com/aurelienpierreeng/ansel/wiki/Translations" label="Improve translations" icon="comment" >}}
{{% /card %}}
{{% /row %}}

{{< divider >}}

## Darktable, but better

{{% row %}}

{{% column %}}

<div class="no-hyphenation lead">

Ansel is what Darktable 4.0 could have been if it didn't die of [feature creep](https://en.wikipedia.org/wiki/Feature_creep).

</div>

Between 2020 and 2023, Darktable has suffered [massive code additions of peripheral features](./news/darktable-dans-le-mur-au-ralenti/), often ill-coded, poorly designed and penalizing usability, performance and maintenance. Too many workarounds failed to fix bugs, but layered new problems on top of legacy code : welcome in maintenance nightmare.

In fairness, without project management or feature planning, this was bound to happen. Darktable has always struggled to be more than a pack of individual plugins.

{{% /column %}}
{{% column %}}

The result is a weird, frustrating, app trying to reinvent GUI paradigms on its own, trying to do everything for everyone, slower and less stable than before, and absolutely terrible to debug.

With a scene-referred-centric user interface, many modules merged into a global menu, rewritten import tool and sparing image pipeline recomputations, Ansel is a Darktable 4.0 variant where 30.000 lines of poorly-written code and half-broken features have been removed, and 11.000 lines rewritten : __it runs faster, smoother, uses less power and requires less configuration__.

With a decreased code complexity, its maintenance should be easier in the future too.

{{% /column %}}
{{% /row %}}

{{< divider >}}

## Beyond documentation

{{% row %}}
{{% column %}}

The typical, recurring painpoint of open-source software projects is documentation. When there is none, users complain about it. When there is one, they complain it is too long, not complete enough, or it doesn't include use cases. Developers expect users to have a linear reading of the project documentation. It will simply not happen and developers will serve as parrots. That only builds up frustration on both ends. __Documentation is not enough__.

{{% /column %}}
{{% column %}}

Chantal is a bilingual (French-English) language model trained specifically for image processing, color theory and photography, that understands technical slang, synonyms and some translations. __Its web interface allows search queries through a central index__ of open-source software documentation, bug reports, user forums, YouTube channels, scientific publications and standards organizations (CIE, ICC, ACES).

{{% /column %}}
{{% /row %}}

<div class="text-center my-5">
<span class="display-5">Meet <a href="https://chantal.aurelienpierre.com" target="_blank">Chantal</a></span><br />
<span class="fs-4">your image processing AI librarian</span>
</div>

{{% row %}}
{{% column %}}

<div class="no-hyphenation lead mx-auto">

Chantal is Ansel's knowledge infrastructure :

- quickly find relevant information among trusted sources,
- avoid asking questions already answered.

</div>

{{% /column %}}
{{% column %}}

<span class="no-hyphenation lead mx-auto">Designed to make users cleverer, instead of making the software dumber.</span> The artificial intelligence feeds you learning material on topics of your choice. Let's invest in natural intelligence.

{{% /column %}}
{{% /row %}}



{{< divider >}}

## There is a full-time designer here

{{% row %}}
{{% column%}}

<div class="d-grid float-start me-4">
{{<figure src="Auto-portrait-0088-MLM_0774_01.jpg" style="width: 200px"/>}}
{{< button url="https://photo.aurelienpierre.com/portfolio" label="Photography portfolio" icon="image" class="text-center w-100 mt-3">}}
{{< button url="https://eng.aurelienpierre.com" label="Engineering blog" icon="code" class="text-center w-100">}}
</div>

<div class="no-hyphenation lead">

Wouldn't it be great if open-source software had full-time designers, able to take the necessary time to understand issues and to find simple solutions, instead of piling up quick hacks and workarounds, in an ever-growing codebase ?

</div>

Designing is not jumping on a code editor to write as much as possible in as little time as possible. It's actually thinking a lot to write as little code as possible, because more code means more bugs.

On my photographs, I make the styling, the make-up, the lighting, the shot, the editing, the retouching, the software color filters, the documentation to use them, the website to talk about them in 2 languages, and even the colorspace used for saturation adjustment. You will find _very_ few people with this kind of full-stack understanding of light and color able to also write efficient computer programs and read academic research papers on applied mathematics. For some reason, there are _lots_ of guys trying to write imaging applications in their spare time. Make your own conclusions here.

{{% /column %}}
{{% column %}}

I have given 4 years of my life to the Darktable project, only to see it destroyed by clueless geeks playing code stashing on week-ends, everyone pushing his own agenda with no sense of design, in a project where nobody is responsible for anything and where we work too fast on everything at the same time.

Ansel development is done at a pace that ensures quality of both the code (backend) and the design (frontend). Design is based on the user feedback I gathered from giving individual editing/retouching lessons with Darktable over the past 3 years, and on the 2 user surveys I ran in 2020 and 2022. Priorities are managed considering the software is meant to export RAW images, meaning R&D is done on image matters and everything else should just follow common computer GUI paradigms and not get in the way.

<div class="bg-white rounded border border-light p-3 lead shadow-sm">

Developing Ansel takes an average of 45 h/week for not even minimal wage. Open-source needs better imaging applications, which requires someone with the right skills and enough time. __Ansel needs manpower and manpower needs to pay bills__.

{{< button url="https://community.ansel.photos/donations-make" label="Support the development" icon="donate" class="d-block text-center mx-auto btn">}}

</div>

{{% /column %}}

{{% /row %}}

{{< divider >}}

## Source code

Ansel software and documentation are released under the GNU/GPL v3 license and versionned with Git. The website is copyrighted but publicly readable. The work repositories are hosted on Github and are mirrored on Gitlab for backup.

{{% row %}}

{{% card title="Software" icon="desktop" %}}
GNU/GPL v3 license.
{{< button url="https://github.com/aurelienpierreeng/ansel" label="Github (original)" icon="github fab">}}
{{< button url="https://gitlab.com/aurelienpierreeng/ansel" label="Gitlab (mirror)" icon="gitlab fab">}}
{{% /card %}}

{{% card title="Documentation" icon="book" %}}
GNU/GPL v3 license.
{{< button url="https://github.com/aurelienpierreeng/ansel-doc" label="Github (original)" icon="github fab">}}
{{< button url="https://gitlab.com/aurelienpierreeng/ansel-doc" label="Gitlab (mirror)" icon="gitlab fab">}}
{{% /card %}}

{{% card title="Website" icon="globe" %}}
Copyright.
{{< button url="https://github.com/aurelienpierreeng/ansel-website" label="Github (original)" icon="github fab">}}
{{< button url="https://gitlab.com/aurelienpierreeng/ansel-website" label="Gitlab (mirror)" icon="gitlab fab">}}
{{% /card %}}

{{% /row %}}

</div>
