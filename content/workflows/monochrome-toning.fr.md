---
title: "Tons monochromes"
date: 2023-03-24
draft: false
toc: true
thumbnail: '/workflows/img/toning-workflow-cyanotype-3.jpg'
tags: ['film', 'monochrome']
authors: ["Aurélien Pierre"]
---
Cet article montre comment effectuer un ton monochrome sur des images numériques dans Ansel, afin d'émuler le rendu des couleurs des développements type cyanotype, platinotype, sépia et virage partiel.

## Etape 0 : préparation globale

Réglez l'exposition globale ainsi que l'exposition relative du blanc et du noir dans filmique RVB comme pour toute autre opération d'édition. Voir [retouche de base](./basic-editing.md). Voici notre image de base de Glenn Butcher :

![](/posts/toning-workflow-base.jpg)

Si vous partez d'une image couleur, vous devez la transformer en noir et blanc : la méthode recommandée est de passer par le module [calibration des couleurs](../doc/modules/processing-modules/color-calibration.md), en utilisant les presets N&B. Voici ce que nous obtenons :

![](/posts/toning-workflow-monochrome.jpg)

## Variante 1 : cyanotype

Le cyanotype est un développement où le "noir" est remplacé par le bleu, car les halogénures d'argent typiques (qui développent le noir) sont remplacés par du ferrocyanure ferrique, qui développe le bleu.

### Etape 1 : échange du noir et bleu

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

Selenium toning can be reproduced exactly the same way, only the hue will need to be changed to purple.

## Variant 3 : sepia

The sepia toning is obtained from a typical silver halide print where the silver halide is turned into sulphide, which is more stable and has better longevity. It results in a brown shift.

The digital reproduction of the toning is very similar in spirit to the platinotype, only the hue will be slightly different (70° instead of 55°) and the shift is more pronounced, which will require to use the _Shadows lift_ as well.

The proposed settings are (all hues set to 70°): 

* _Global offset_:
  * chroma : 0.20%
  * luminance : 0.20%
* _Shadows lift_:
  * chroma: 10%
* _Highlights gain_ : don't touch it (same as previously)
* _Power_: 
  * chroma: 1.50%

This gives us:

![](/posts/toning-workflow-sepia.jpg)


## Variant 4 : split-toning

Split-toning is a process where highlights and shadows get a different color shift, the most common being teal and orange. It is not specific to monochrome toning, and can be used for color work, where it becomes a particular case of color grading (more on that topic in [ressources](../resources/readings.md#color-grading)). For monochrome, the split-toning will need to be very gentle to keep it believable.

Using the color balance module, we only need to use the _Highlights gain_ and the _Shadows lift_. Here is a proposal for teal and orange :

![](/posts/toning-workflow-split-toning.jpg)

The possibilities are limitless, and the typical "teal and orange" should be used carefully because it has been already overused and abused.

## Conclusion

You may have noticed that all the analog-inspired tonings (that is, all except split-toning) don't affect whites. This is because, on an analog print, white is achieved by letting the paper naked, while black and midtones uses photosensitive pigments.

Pure black and pure white are ignored by the _Power_ setting of the color balance module, which is a property of the power function (maths…). However, the more you increase its chroma and the more impact it has on very bright and very dark midtones. If you ever find that it takes too much of highlights once you found a proper setting for midtones, you can always desaturate them in the _Master_ tab, using the _Perceptual saturation grading_ for the _Highlights_ channel (because _perceptual saturation_ is applied after the _4 ways_ settings in the pixel pipeline, while the _linear chroma grading_ is applied before).

The real strength of the color balance module here is to let you fine-tune very precisely how the effects target shadows, midtones or highlights, and how fast the transitions are between them. But with great power comes great responsibilities, and it is certainly a tool that requires some time to master.
