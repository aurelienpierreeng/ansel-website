---
title: "Film scanning"
date: 2025-04-18
draft: false
toc: true
tags: ['film', 'negative']
authors: ["Aurélien Pierre"]
thumbnail: "film-scan.jpg"
---

Alain Oguse learned photographic printing with [Claudine](https://www.musee-orsay.fr/fr/ressources/repertoire-artistes-personnalites/claudine-sudre-211535) and [Jean-Pierre Sudre](https://en.wikipedia.org/wiki/Jean-Pierre_Sudre) in the late 1960's, and spent his early career in commercial photography. After retiring, he started to investigate how to bring back the photographic (silver halide) grain in digital scans of film negatives, finding the same sharpness and quality he had with near-point light enlargers in the 1970's.

The point light printing technique uses a very tiny source of light that gives a very precise and detailed reproduction of B&W film negatives, as opposed to diffuse lighting. It is very demanding, as its unforgiving sharpness and contrast do not hide scratches and dust on the film surface. Prints done this way would often need manual (painted) corrections on paper, inducing more work and more costs. By the end of the 1970's, it was usually replaced by diffuse light… better at hiding manipulation mistakes and at maximizing print labs profits.

But cleaning up negatives is no issue once they are digitized, and on this topic, Alain and I share the same values : digital imaging should augment the possibilities offered to photographers, building on top of the analog legacy, instead of settling down for what is easy and fast while trying to re-invent photography as if it was born digital.

As an early Ansel user, Alain contacted me to get help on tuning the [_Diffuse or sharpen_](../doc/modules/processing-modules/diffuse/) module to dial up or down the photographic grain in a way that closely reproduces the impact of the enlarger light source quality (point or diffused) on the final print, starting with a DSLR scan. After all, light diffusion is what happens here.[^1]

[^1]: Though it should be mentionned that _diffuse or sharpen_ uses thermal diffusion models ([Fourier heat equation](https://en.wikipedia.org/wiki/Heat_equation)) in [wavelets space](https://en.wikipedia.org/wiki/Wavelet). This equation can also model particle diffusion, and its fundamental solution can be identified as a convolution with a Gaussian function (aka producing here a very computationnaly-expensive Gaussian blur with the right settings). But since we apply it in wavelets space and we don't do it at the photon level, I cannot in good faith claim physical accuracy here, with regard to light diffusion. It's rather _physically-inspired_ generalized diffusion.

But he also built a complete apparatus to achieve the initial film scan and was kind enough to document and illustrate all of his process, from preparation to post-processing, translate it into English and allow me to publish it here. You get for free the very finest of what open-source has to give you:

- 50 years of experience from Alain,
- real-life examples and results,
- optical explanations of what's going on,
- complete schematics of the scanning apparatus in point light setting,
- physically-accurate modules from Ansel/Darktable pixel pipeline, and presets for _demosaicing_, _input color profile_ and _diffuse or sharpen_ modules to dial the grain up or down at post-processing,
- thoughts on the work and responsibility of a print lab technician, regarding heritage conservancy and exhibition quality.

_Please note that Alain is a French speaker and this book was mostly translated using machine translation. If you understand French enough, you might want to read the original version._

<object data="https://static.ansel.photos/article-lumiere-ponctuelle-en-compress.pdf" type="application/pdf" width="100%" height="900px">
  <p>Unable to display PDF file. <a href="https://static.ansel.photos/article-lumiere-ponctuelle-en-compress.pdf">Download</a> instead.</p>
</object>

<div class="text-center">
{{< button url="https://static.ansel.photos/article-lumiere-ponctuelle-en-compress.pdf" label="Download the eBook (PDF)" icon="download fas" class="">}}
</div>
