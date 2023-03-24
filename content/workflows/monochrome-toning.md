---
title: "Monochrome toning"
date: 2023-03-24
draft: false
toc: true
tags: ['film', 'monochrome']
authors: ["Aurélien Pierre"]
---

This article will demonstrate how to perform monochrome toning on digital images in Ansel, to emulate the color rendition of cyanotypes, platinotypes, sepia and split-toning developments.

## Step 0 : global preparation

Set the global exposure and filmic scene white and scene black, as in any other editing. See [basic editing steps](./basic-editing.md). This is our base image, by Glenn Butcher :

![](/posts/toning-workflow-base.jpg)

If you start from a color image, you need to turn it into black and white : the recommended way is through the [color calibration](../doc/modules/processing-modules/color-calibration.md) module, using the B&W presets. Here is what we get :

![](/posts/toning-workflow-monochrome.jpg)

## Variant 1 : cyanotype

The cyanotype is a development where "black" is replaced by blue, because the typical silver halide (that develop black) are replaced by ferric ferrocyanide, which develops blue.

### Step 1 : switch black and blue

In the [color balance](../doc/modules/processing-modules/color-balance-rgb.md) module, go to the _4 ways_ tab, and in the _Global offset_ section, define a hue of 259° at a chroma of 1.50%. You will need to right-click on the chroma slider, then input the `1.5` value on the keyboard, because the range of the slider goes as high as 0.75%, which fits typical color-grading uses.

If you just do that, you will note that blacks stay neutral, and don't get tinted to blue. This is because of the internal gamut mapping in the module, that prevents negative RGB values, which would create later problems in the pipeline. To force blacks to be colored, you will need to raise the luminance of the _Global offset_ by the same amount as the chroma, that is 1.50% in this example.

This is the result:

![](/posts/toning-workflow-cyanotype-1.jpg)

From there, you can fine-tune the _Global offset_ settings to your taste.

### Step 2 : adjust contrast

The luminance increase of the black point, mandatory to be able to tint black, reduces the contrast and flattens the image. To overcome this, you will need to come back to filmic and to raise the scene black exposure until the density of the darkest parts seems acceptable to you. Here is the result:

![](/posts/toning-workflow-cyanotype-2.jpg)

### Step 3 : fine-tune midtones

The _Global offset_ that we adjusted at the step 1 will mostly affect blacks and deep shadows. You may want to drive the fall-off of the tinting toward white, as to get more or less tinted mid-tones.

You will have to go the _mask_ tab of the color balance module, and set the white fulcrum with the color picker on the right of the slider. This is important for the _Power_ setting next. In a display-referred, where white is known beforehand to be at 100%, this wouldn't be necessary, but since we are in a [scene-referred workflow](./scene-referred.md) where white can have any value, we need to define it explicitly.

Then, in the _4 ways_ tab, move to the bottom, at the _Power_ section. In here, use the same hue as before (259°) and a chroma more or less intense depending on how blue you want your midtones to be. This is what we get:

![](/posts/toning-workflow-cyanotype-3.jpg)

Once you raised the blueing in the midtones, you may want to soften it slightly in the deep shadows by reducing a bit the chroma of the _Global offset_. Adjust everything to taste and watch out for flat blue surfaces that might indicate over-saturation.

### Conclusion

That's it. The look is pretty consistent with analog cyanotypes. You having nothing to do with whites and highlights, which are defined by the paper tone for analog cyanotypes. For a more vintage look, you can choose a slightly greener hue, that is around 257° or even less, and even delicately shift the highlights gain toward yellow to simulate paper aging.

For a believable look, you absolutely need to watch out for any neutral blacks: you should not have any. Increase the chroma and luminance of the _Global offset_ until they are fully tinted.

## Variant 2 : platinotype

The platinotype uses palladium and platinum in variable proportions, instead of silver halide. Depending on the proportions of each, blacks will be warmer or colder, but will be less dense than with silver halide. We will go here for the warmer look.

It works very much the same as the cyanotype emulation, we only change the hue, so refer to the previous section for the full explanations.

### Step 1 : warm up black

We will use much gentler settings than before, that is hue set at 55°, chroma at 0.20% and luminance at 0.20% in _Global offset_.

![](/posts/toning-workflow-platinotype-1.jpg)


### Step 2 : fine-tune midtones

Again, I barely touched the _Power_ settings, with a 0.10% chroma at hue 55°.

![](/posts/toning-workflow-platinotype-2.jpg)

### Conclusion

There is not one definite platinotype look because the final tint depends on the proportions of the mix between platinum and palladium in the photo-sensible emulsion. The result presented here is more opinionated than most actual platinotypes I have seen, for educating purposes. You may want to dial it down a notch for a more believable result (reduce chroma).
