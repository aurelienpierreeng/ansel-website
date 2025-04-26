---
title: Common misconceptions
date: 2023-01-19
draft: false
weight: 10
authors:
    - Aurélien Pierre
---

This page addresses most of the mistakes and misconceptions about Ansel that can be found online.

<!--more-->

## I need to be an expert / engineer to use Ansel

My [videos](https://www.youtube.com/channel/UCmsSn3fujI81EKEr4NLxrcg) and my posts typically contain both the "how to" and the "why/how" part. The "why/how" is typically technical or even theoritical, and is there to justify the "how to". There are several reasons for which I give both :

1. The accurate technical explanations are really difficult to find on the internet, and I'm pretty much the only one to link theory and practice on video. On the other hand, it's easy to find wrong information in photography, from people slightly above the average who try to help, but actually mislead others.
2. I personaly hate gurus that drop instructions without bothering to justify them. Rules always have a reason and need to be broken as soon as this reason stops being valid. You see a lot of people continuing to follow old rules because "the elders knew what they were doing" — but don't remember why they did — while circumstances have changed.
3. Understanding how tools behave allows you to predict when they will fail (because they will all fail at some point), which enables you to solve problems even before they appear, and to be ready with a plan B when it happens,
4. Most pieces of advice I give are contextual to the desired result and the type of image being worked. Removing context would make them simply wrong in general.

Because of that, many people have conceived the idea that they need to understand 100 % of the technical content before being able to use the software. That is simply not true. Ultimately, Ansel is just a software with a GUI, you can push cursors or use factory presets until the picture looks good. Whatever you don't understand can be disregarded for now, and perhaps tried again later.

On the other hand, if you start mixing media, like printing pictures on paper and releasing digital pictures from the same edit, or inputing your Ansel exports into another software for further manipulation, having at least a basic understanding of how an imaging pipeline works is going to help you tremendously.

Like any technological object, the more you understand it and the better you control it, the least you fight it. But Ansel comes shipped with a pack of default presets and a pre-configured pipeline that should give you a proper editing base in most cases.

It is true, however, that the image processing controls in the GUI tend to be more grounded into color science and optics than in other applications. The reason is processing HDR without artifacts needs more accurate color models, that take more input parameters to adapt to the dynamic range of images. The reason most applications can afford to look more simple is their color models are less performant and rely on approximations that don't really scale with dynamic range. Everything has a cost…

## Ansel processes my raw pictures in a way that makes them darker and duller

The reality is actually the other way around.

Raw photographs typically have a JPEG file embedded as a low-resolution thumbnail. This thumbnail is what you see in Ansel lighttable as well as on your camera back screen. You will never see a raw photograph without any kind of correction, it's simply not displayable.

This thumbnail has been processed and enhanced by the camera firmware, in a way that usually brightens it a lot, adds contrast, saturation, and very often tints it for a warmer look.

What you see when opening the picture in Ansel darkroom is a much less processed picture than the JPEG, closer to the raw and more neutral, meant to be a base for your personal editing.

But remember that the default look when opening the darkroom is just that : a base look, a starting point. Ultimately, even the default settings can be adjusted to your liking, which is the whole point of the software.

## Deprecated modules don't work anymore

Ansel is based on darktable 4.0. darktable 4.0 has deprecated many modules. Ansel has deprecated even more. Modules get deprecated when they get a better alternative introduced.

But "deprecated" is a strong word to say "the widget of the module is hidden from the GUI". Both the GUI and the pixel code of the module are still in the software, and will still run for old edits using this module. For these edits, the module will show in the GUI.

For new edits, the module will only be hidden from the GUI. Deprecation is only a display clean-up to limit modules proliferation.
