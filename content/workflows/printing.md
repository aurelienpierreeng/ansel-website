---
title: "Printing"
date: 2023-10-30
draft: false
toc: true
tags: ['']
authors: ["Aurélien Pierre"]
thumbnail: '/workflows/img/charte-noirs.jpg'
---

The [scene-referred](./scene-referred.md) workflow promises an editing independent from the output medium. It will typically produce an image encoded in sRGB colorspace with 8 bits, that is code values between 0 and 255. To simplify, we will consider here only the 8 bits case. Concepts are the same in 16 bits, only the coding range goes from 0 to 65535, which is anecdotal.

Unfortunately, nothing guarantees that the printer is able to use the whole encoding range. The minimum density (_Dmin_ in analog) is reached with naked paper, and matches an RGB code value 255. The maximum density (_Dmax_ in analog) is reached with 100% ink coverage.[^1] Problem is, if Dmin matches an RGB code value of 255, Dmax never matches an RGB value of 0.

[^1]: Printers reach deeper blacks by mixing pure black ink with all of CYM inks.

To understand the problem, I generated a synthetic chart of sRGB code values from 0 to 59 (over 255) and printed it on regular office paper, with an old photo printer, then scanned it. The grid in-between the patches is pure black (RGB = 0).

{{<compare before="/en/workflows/img/charte-noirs.jpg" after="/en/workflows/img/chartes-scan.jpg" />}}

The printed blacks are muted, compared to the digital original, but it's not the worst part : the patches below 0.12 % are completely blended into the 0 % grid, which means that all code values below 5 / 255 end up in the same black blob.

Said otherwise, our printer black saturates at 5 / 255 and we will not be able to resolve details in deep shadows without proper correction. Let's see the difference it makes on a real image having a lot of content in deep shadows (_before_ : no black correction, _after_ : correction) :

{{<compare before="/en/workflows/img/Shooting Minh Ly-0155-_DSC0155-Minh-Ly-no-bpc.jpg" after="/en/workflows/img/Shooting Minh Ly-0155-_DSC0155-Minh-Ly-bpc.jpg" />}}

Black must be fixed to retain details in the hair, even though it is done at the expense of contrast in the neck.

## Understanding black point compensation

The [black point compensation](https://www.color.org/WP40-Black_Point_Compensation_2010-07-27.pdf) has been invented by Adobe and standardized by the ICC later. It is a simple black offset meant to raise (brighten) all RGB values above the black saturation threshold, such that we recover gradients in deep shadows, acknowledging that blacks will remain more muted than the original no matter what we do.

Unfortunately, the black point compensation by offsetting does not preserve hues and may shift colors. For this reason, [Capture One simply does not support it](https://support.captureone.com/hc/en-us/articles/360002654477-Black-point-compensation).

It should be noted that the black point compensation is the last resort, for when the [perceptual intent](https://www.color.org/v2profiles_v4.pdf) is not available in your output color profile (that is, when the `AtoB` and `BtoA` LUTs are not defined in the profile). This is the most common case when dealing with open-source printer drivers, because those LUTs have to be manually set by someone who understands this, and not by a mere calibration software.

In the absence of defined perceptual intent, the color manager can fallback to the relative colorimetric intent and can use the black point compensation if the profile has some tone curve (the `TRC`).

If you miss both the perceptual LUTs and the TRC, that is if you didn't calibrate your printer yourself, then tough luck.

## Adjusting black point without profiling the printer

1. <a href="/en/workflows/img/charte-noirs.jpg" download>Download the chart of blacks</a>
2. print it directly as an sRGB image, with no editing and no correction,
3. on the print, note the darkest patch that you can visually tell apart from the pure black grid, and record its percent value,
4. open the chart image in Ansel, and in Filmic module do the following :
   1. in _scene_ tab, click on the auto-tuner button,
   2. in _look_ tab, set the contrast to the minimum value (0.5),
   3. in _display_ tab, input the black luminance value you read on the patch previously,
   4. in _options_ tab, set the _contrast in shadows_ parameter to _safe_.
5. export the corrected chart and print again to validate the settings.


This is the result from the example here:

{{< compare before="/en/workflows/img/chartes-scan.jpg" after="/en/workflows/img/chartes-scan-bpc.jpg">}}
Before, the display black point is set at 0 % (no compensation). Patches from 0% to 0.09 % are fully blended in the grid. After, the display black point is set to 0.12 %. All patches stand out of the grid, but the grid itself lost some density. 0.9 % is would be a better setting.
{{< / compare >}}

{{< note >}}
The patches have all integer RGB code values in 8 bits, from 0 to 49 over 255, with the sRGB OETF on, which is what the printer driver will get when printing. The percents translate those values in linear Rec2020 RGB, for Ansel pipeline. It is useless to try and use intermediate percent values for black compensation, since the picture is ultimately converted to 8 bits sRGB by most drivers.
{{</ note >}}


## Applying the settings to real images

When editing your picture, proceed as usual, without black point compensation. Filmic has a default black point compensation meant to deal with quantization errors when going to 8 bits, it is not linked to any particular medium, but only to 8 bits sRGB.

Before printing, change the Filmic _display black_ to the value measured on the chart above and export.

{{< note >}}
A global _display black_ override will be offered in the GUI for temporary changes at export time, without having to change the image parameters, as well as a way to directly extract the black point compensation from a printing ICC profile, if available.
{{</ note >}}


## White point compensation

Users of Fuji Instax pocket printers have reported a similar issue, but with white. Fuji Instax, using a photochemical printing process, seems to add a lot of contrast in highlights, resulting in clipping above 75 % luminance, or so.

You can reproduce the steps above for white, using <a href="/en/workflows/img/charte-blancs.jpg" download>the charts of whites</a>. Note the darkest patch that starts blending into the white grid, and use the corresponding percent value for Filmic _display white_.

{{< note >}}
This post illustrates why the new _Sigmoid_ module, introduced in Darktable 4.0 as a worse duplicate of Filmic for tonemapping, is a no-go in Ansel : there is no way to specify target black and white points while retaining contrast in midtones and middle-grey unchanged.
{{</ note >}}
