---
title: "Ansel"
date: 2022-11-27T22:36:34+01:00
draft: false
description: "Ansel is an open-source raw photo editor for artists"
thumbnail: "https://user-images.githubusercontent.com/45535283/"
tags: ["darktable", "ansel", "photo editing"]
---

<div class="pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold">Your digital darkroom</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4"><em>Ansel</em> is an open-source photo-editing software for digital artists, designed to help you achieve your own interpretation of raw digital photographs.</p>
  </div>
  <div class="overflow-hidden" style="max-height: 65vh;">
    <div class="container my-5">
      <img src="/main-screenshot.jpg" class="img-fluid shadow-lg mb-4" alt="Ansel screenshot" loading="lazy" width="1000">
    </div>
  </div>
</div>

{{% container %}}

{{% row %}}
{{% column %}}
It is grounded in the legacy of <a href="https://wikipedia.org/wiki/Ansel_Adams">Ansel Adams</a>, pianist and photographer, who pushed darkroom craftsmanship like never before to serve his photographic vision.
{{% /column %}}
{{% column %}}
<figure class="text-left">
<blockquote class="blockquote">
  <p>The negative is the score, and the print is the performance.</p>
</blockquote>
<figcaption class="blockquote-footer">
  <cite title="Ansel Adams">Ansel Adams</cite>
</figcaption>
</figure>
{{% /column %}}
{{% /row %}}
{{< divider >}}

## Install

<hr>

{{% row %}}
{{% card icon="linux fab" title="Linux" %}}
Distribution-agnostic executable
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/lin-nightly/master/ansel.stable.AppImage.zip" label="Download ansel.appimage" icon="download" >}}
{{% /card %}}

{{% card icon="windows fab" title="Windows" %}}
Windows 10 & 11 installer
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/win-nightly/master/ansel.stable.win64.zip" label="Download ansel.exe" icon="download" >}}
{{% /card %}}

{{% card icon="terminal" title="Build from source" %}}
Best performance for your hardware
{{< button url="/en/doc/install" label="Building instructions" icon="wrench" >}}
{{% /card %}}
{{% /row %}}

<strong>Minimal recommended configuration</strong> : CPU Intel i5 (4 cores) / 8 GB RAM / GPU Nvidia GTX 850.

{{< divider >}}

## Why Ansel ?
<hr>

{{% row %}}
{{% column p=true %}}
Many solutions already exist to produce ready-to-consume photographs for masses, from smartphones filters to out-of-cameras JPEGs, followed recently by AI-driven automagic applying  ~~caricatural~~ dramatic toy filters. These make photography easier than ever, but are the produced images really __your__ images and, in any case, the images __you__ expected ?
{{% /column %}}
{{% column p=true %}}
Pressing the camera shutter merely started a process ending when the on-screen picture looks like the one you had in mind. _Ansel_ proposes to put the artists back at the center of the creative process and enables them with an interface to manipulate images with precision and nuance, using state-of-the-art color science and independent color controls.
{{% /column %}}

{{% /row %}}
<hr>


{{% row %}}
<p class="no-hyphenation lead text-left mx-auto my-3 col-10"><em>Ansel</em> lets you interpret your raw photographs much like a music instrument, when most software tries to automatically play the score for you, but mechanically and soullessly.</p>
{{% /row %}}
{{< divider >}}

## What can Ansel for you ?
<hr>

Ansel allows you to manage your collections of pictures, to edit your raw digital photographs and film scans non-destructively and to export the result to common file formats. It stores your editing histories as text and lets you go back in time at any editing step you like, anytime.

### Color work

Ansel ships a recent color science, compatible with HDR : the chromatic adaptation CIE CAT 2016, the HDR color space JzAzBz (2017) and the perceptual color space darktable UCS 2021, developed specifically to manipulate color saturation without the fluorescent effect.

{{% row %}}
{{% column %}}
 ##### Color calibration
{{< compare after="/calibration-after.jpg" before="/calibration-before.jpg" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}

{{% /column %}}

{{% column %}}
 ##### Color-grading
{{< compare after="/grading-after.jpg" before="/grading-before.jpg" >}}
Give ambiance and character to your pictures by polishing their color palette with nuanced and fine-grained controls, in RGB, Ych or HSB color spaces, for creative and corrective purposes.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

{{% row %}}
{{% column %}}
##### Color matching
{{< compare after="/matching-after.jpg" before="/matching-before.jpg" >}}
Force the chromatic adaptation such that any selected object matches a predetermined color, input from CIE Lab coordinates (for logos and brand colors), or by sampling the color of the same object in another shot, as to even the color rendition over the series.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Hue qualifying and keying
{{< compare after="/masking-after.jpg" before="/masking-before.jpg" >}}
Use the hue, chroma and lightness qualifiers to quickly define masks and apply selective effects. Combine parametric masks with drawn masks and boolean operations. Refine and feather the edges of masks by blurring or using clever edges detection.
{{</ compare >}}
{{% /column %}}
{{% /row %}}


### Tonal work

The tonal working methods are designed to manipulate luminance without affecting hue nor saturation, in order to respect the color work, done apart.

{{% row %}}
{{% column %}}
##### HDR tone mapping
{{< compare after="/filmic-after.jpg" before="/filmic-before.jpg" >}}
Recover deep shadows and compress the dynamic range while retaining original saturation and hue, with gamut mapping to ensure the colors fit in the output color space. _(Photo : Andreas Schneider)_
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Zone-system editing
{{< compare after="/toneeq-after.jpg" before="/toneeq-before.jpg" >}}
Balance densities based on exposure zones, by preserving local contrast thanks to an edge detection algorithm, and select the exposure zones to affect directly from the picture, through the interactive cursor. _(Photo : Andreas Schneider)_
{{</ compare >}}
{{% /column %}}
{{% /row %}}

### Image reconstruction

{{% row %}}
{{% column %}}
##### Lens deblurring
{{< compare after="/sharpen-after.jpg" before="/sharpen-before.jpg" >}}
Unleash the power of multiscale, gradient-based machine learning to rejuvenate old lenses, recover focusing mistakes or add emphasis on your subject, but without the typical edge artifacts, over-sharpening oddities or added noise.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Dehazing
{{< compare after="/dehaze-after.jpg" before="/dehaze-before.jpg" >}}
Restore some depth in foggy and hazy shots by bringing back textures and saturation in colors, without overaccentuating already sharp details.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

{{% row %}}
{{% column %}}
##### Denoising
{{< compare after="/denoise-after.jpg" before="/denoise-before.jpg" >}}
Remove chromatic noise, soften and blend lumaninance noise.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Highlights reconstruction
{{< compare after="/highlights-after.jpg" before="/highlights-before.jpg" >}}
Salvage both color and texture in highlights, recover blown areas by propagating gradients while the gamut-mapping watches your back to ensure colorful highlights can still be printed at their proper hue. You don't have to bleach highlights to hide problems anymore.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

### Specialized features

{{% row %}}
{{% column %}}
##### Automatic perspective correction
{{< compare after="/perspective-after.jpg" before="/perspective-before.jpg" >}}
Let the machine learning detect automatically vertical and horizontal lines and compute the best geometric correction to rotate, straighten and crop the picture, optionnaly taking into account the kind of lens used.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Censoring
{{< compare after="/censorize-after.jpg" before="/censorize-before.jpg" >}}
Anonymize people, license plates, etc. and play with use conditions of socially prude network without defiling your pictures too much.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

## Compatibility

{{% row %}}
{{% card title="Edits" icon="desktop" %}}
Ansel is based on darktable 4.0 and is fully compatible with darktable 2.x up to 4.0 database and XMP files. Coming from darktable ?
{{< button url="/en/doc/special-topics/from-darktable/" label="Find out what is changed" icon="sync" >}}
{{% /card %}}
{{% card title="Cameras" icon="camera" %}}
New cameras may need up to 24 months to be fully supported after their commercial release.
{{< button url="https://rawspeed.org/CameraSupport.html" label="Supported cameras" icon="wrench" >}}
{{% /card %}}
{{% /row %}}

{{< divider >}}
## Darktable, but better

{{% row %}}

<p class="no-hyphenation lead text-left mx-auto my-3"><em>Ansel</em> is what Darktable 4.0 could have been if its developers were not so busy turning it into an usability nightmare. Ansel is a Darktable 4.0 variant where 29.000 lines of poorly-written code and half-broken features have been removed, and 10.000 lines rewritten : it runs faster, smoother, uses less power and requires less configuration. Enjoy an app focusing on getting work done and stability.</p>

{{% /row %}}

{{< divider >}}

{{% /container %}}
