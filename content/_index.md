---
title: "Ansel"
date: 2022-11-27T22:36:34+01:00
draft: false
description: "Ansel is an open-source raw photo editor for artists"
thumbnail: "https://user-images.githubusercontent.com/45535283/"
---

<div class="px-4 pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold">Your digital darkroom</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4"><em>Ansel</em> is an open-source photo-editing software for digital artists, designed to help you achieve your own interpretation of raw digital photographs.</p>
  </div>
  <div class="overflow-hidden" style="max-height: 65vh;">
    <div class="container px-5 my-5">
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
{{< button url="/" label="Building instructions" icon="wrench" >}}
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

### Color work

{{% row %}}
{{% column %}}
 ##### Color calibration
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
 ##### Color-grading
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

{{% row %}}
{{% column %}}
##### Color matching
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Hue qualifying and keying
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}
{{% /row %}}


### Tonal work

{{% row %}}
{{% column %}}
##### HDR tone mapping
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Zone-system editing
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
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

### Advanced features

{{% row %}}
{{% column %}}
##### Masking and blending
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Censoring
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
{{</ compare >}}
{{% /column %}}
{{% /row %}}
### Printing

{{% row %}}
{{% column %}}
##### Printer profiles
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Gamut mapping
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

## Compatibility

{{% row %}}
{{% card title="Edits" icon="desktop" %}}
Ansel is based on darktable 4.0 and is fully compatible with XMP edits and database darktable 2.x up to 4.0 database and XMP files.
{{% /card %}}
{{% card title="Cameras" icon="camera" %}}
New cameras may need up to 24 months to be fully supported after their commercial release.
{{% /card %}}
{{% /row %}}

{{% /container %}}
