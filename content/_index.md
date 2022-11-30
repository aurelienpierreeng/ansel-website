---
title: "Photo-editing software for artists."
date: 2022-11-27T22:36:34+01:00
draft: false
featured_image: '/images/gohugo-default-sample-hero-image.jpg'
---

<div class="px-4 pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold">Your digital darkroom</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4"><em>Ansel</em> is an open-source photo-editing software for digital artists, meant to help you achieve your own interpretation of raw digital photographs.</p>
  </div>
  <div class="overflow-hidden" style="max-height: 50vh;">
    <div class="container px-5">
      <img src="https://user-images.githubusercontent.com/45535283/148689197-e53dd75f-32f1-4297-9a0f-a9547fd4e7c7.jpg" class="img-fluid border rounded-3 shadow-lg mb-4" alt="Example image" width="700" height="500" loading="lazy">
    </div>
  </div>
</div>

<div class="container">
  <div class="row align-items-start">
    <div class="col">
        <p>
          It is grounded in the legacy of <a href="https://wikipedia.org/wiki/Ansel_Adams">Ansel Adams</a>, pianist and photographer, who pushed darkroom craftsmanship like never before to serve his photographic vision.
        </p>
      </div>
      <div class="col">
        <figure class="text-center">
          <blockquote class="blockquote">
            <p>The negative is the score, and the print is the performance.</p>
          </blockquote>
          <figcaption class="blockquote-footer">
            <cite title="Ansel Adams">Ansel Adams</cite>
          </figcaption>
        </figure>
      </div>
    </div>
</div>

<div class="b-example-divider"></div>

<div class="container text-center">

## Downloads

<hr>


</div>

<div class="container text-center">
  <div class="row align-items-start">
    <div class="col">
      <img src="img/Tux.svg" class="col" height="80">
      <h4>Linux</h4>
      <p>
        Distribution-agnostic Appimage
      </p>
      <a role="button" class="btn btn-dark" href="#">
        Download Ansel.appimage
      </a>
    </div>
    <div class="col">
      <img src="img/windows-11-logo_web.png" class="col" height=80>
      <h4>Windows</h4>
      <p>
        Windows 10 & 11 installer
      </p>
      <a role="button" class="btn btn-dark" href="#">
        Download Ansel.exe
      </a>
    </div>
    <div class="col">
      <i data-feather="terminal" height=80 width=80></i>
      <h4>Build from source</h4>
      <p>Best performance for your hardware</p>
      <a role="button" class="btn btn-dark" href="#">
        Go to building instructions
      </a>
    </div>
  </div>
</div>

<div class="container text-center pt-5">
<p><strong>Minimal recommended configuration :</strong> CPU Intel i5 (4 cores) / 8 GB RAM / GPU Nvidia GTX 850.</p>
</div>

<div class="b-example-divider"></div>

<div class="container text-center">

## Why Ansel ?

<hr>

</div>

<div class="container">
<div class="row align-items-start">
<div class="col">

Many solutions already exist to produce ready-to-consume photographs for masses, from smartphones filters to out-of-cameras JPEGs, followed recently by AI-driven automagic applying ~~caricatural~~ dramatic toy filters. These make photography easier than ever, but are the produced images really **your** images and, in any case, the images **you** expected ?

</div>
<div class="col">

Pressing the camera shutter merely started a process ending when the on-screen picture looks like the one you had in mind. _Ansel_ proposes to put the artists back at the center of the creative process and enables them with an interface to manipulate images with precision and nuance, using state-of-the-art color science and independent color controls.

</div>
</div>
<hr>
</div>

<div class="px-4 my-5 text-center">
  <p class="no-hyphenation lead text-left col-lg-7 mx-auto"><em>Ansel</em> lets you interpret your raw photographs much like a music instrument, when most software tries to automatically play the score for you, but mechanically and soullessly.</p>
</div>

<div class="b-example-divider"></div>

<div class="container text-center">

## What can Ansel for you ?

<hr>

</div>

<div class="container">

### Color work

</div>

<div class="container text-center">
  <div class="row align-items-start">
    <div class="col">
      <h4>Color calibration</h4>
      {{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
          Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
      {{</ compare >}}
    </div>
    <div class="col">
      <h4>Color-grading</h4>
      {{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
          Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
      {{</ compare >}}
    </div>
  </div>
  <div class="row align-items-start">
    <div class="col">
      <h4>Color matching</h4>
      {{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
          Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
      {{</ compare >}}
    </div>
  </div>
</div>

### Tonal work

#### HDR images

#### Zone-system editing

### Image reconstruction

#### Deblurring

#### Dehazing

#### Denoising

### Advanced features

#### Masking and blending

#### Censoring

#### Shortcuts

### Film scans

#### Inversion

#### Correction

### Printing

#### Printer profiles

#### Gamut mapping

#### Black point compensation


## Compatibility

### Edits

Ansel is based on darktable 4.0 and is fully compatible with XMP edits and database darktable 2.x up to 4.0 database and XMP files.

### RAW formats

List of supported cameras

New cameras may need up to 24 months to be fully supported after their commercial release.

### Files formats

* TIFF 8/16 bits (integer)[^1], 16/32 bits (floating point)[^1],
* JPEG[^1], JPG2000[^1],
* PNG,
* EXR,
* AVIF/HEIF[^1],
* WebP[^1],
* PDF.

[^1]: Support ICC profile embedding
