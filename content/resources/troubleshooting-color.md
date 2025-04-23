---
title: Troubleshooting color issues
date: 2024-07-15
authors:
    - Aurélien Pierre
---

This will apply to upstream Darktable as to Ansel since they share most of their color pipeline. The following procedure will help you troubleshoot your color issues, whether it is inconsistent appearance between export vs. preview, or between screen vs. print, or between 2 apps.

## Setup your desktop properly

The inherent problem of color is it exists only as a perception, and that perception is highly contextual and fluid. If I take any color patch and display it over a white, middle-grey or black background, it will not appear the same even though a colorimeter would confirm it's the exact same color. I have built a little web animation to showcase this effect, displaying sRGB gamut slices at constant hue, over user-defined background lightness : [the sRGB book of color](https://eng.aurelienpierre.com/2021/04/the-srgb-book-of-color/).

Now, if you add on top the lighting discrepancy, it will also look different lit by a powerful 120 W halogen bulb or by a weak nightstand lamp. Finally, the color temperature of the light will also come into play : of course, a "cold white" D50 (5000 K) bulb or a "warm" 3200 K bulb will shift hues in a print, but the cold white will also make colors in the blue-violet region appear more colorful (compared to the others), as the warm white bulb will make colors in the red-orange region appear more colorful.

In all this, your physiological perceptual system will adapt real-time, because it's great piece of biology, but it's specifically what makes our retoucher's like miserable: the perceptual system has no standard (reference) perception. Instead, and because of that, we need to work in standard viewing conditions.

The lighting in your editing room should be as constant as possible across the day. Pick a room with a window exposed to the North (in the Northern hemisphere) so the light doesn't change much over the day, and cover it with cold white opaque sheets to diffuse it (yes, that will be cotton bleached with nasty chemicals to be white, natural cotton is beige-ish).

You should never edit in the dark or in a dim room (even if that makes the screen more legible — it's a trap). For night editing, try to find high quality D65 bulbs (or, next best option : D55 – this is more available and mainstream) having a Color Rendering Index (CRI) of at least 92, ideally more than 95 (if you find more than 98, it's probably a scam – in any case, the theoritical max is 100). I don't recommend editing in full artificial lighting because natural light has a built-in 100 CRI (since it's actually the reference for all CRI). Stay away from the energy-saving fluorescent bulbs, they have terrible CRI and need a variable heating time to reach their full potential (which is not much).

{{< warning >}}
Editing late at night under D55 or D65 light will deeply mess-up your sleep pattern, you should turn those lights off at very least 2h before going to bed, otherwise you won't sleep.
{{< /warning >}}

Keep in mind that everything in your visual field will have an impact on your color perception. The wall behind your screen should be painted matte white. Some people recommend middle-grey, but "middle-grey" paint is not easy to find, and still… it will need a proper lighting to appear actually at 20% of the luminance of a white sheet displayed under your lighting. Since nobody cares about lighting their wall, a white paint poorly lit will be closer to middle-grey and anyway, brighter will cause fewer issues than darker.

The backlighting of your screen should be set such that a 100% white frame displayed on your screen appears at the same brightness as a white sheet of paper next to your screen (that is, lit by your room lighting). You may have heard to set your screen white luminance to 90 Cd/m², but that's only to compare the screen rendering with a physical print displayed in a (standard) proofing booth, and not really for general editing. In any case, it is more important that your screen backlighting matches your actual room surround lighting than some arbitrary value, since human vision reacts only to contrast (so, basically, even the room surround with your screen, both in color temperature and in brightness, to avoid creating any artificial contrast).

Only use middle-grey GUI in all your editing software. Yes, the darker GUI look slicker, but they will tamper with your perceptions and you will get bad surprises when printing.

The general idea behind all these pieces of advice is your screen should look as close as possible as a print displayed next to it : whites should have the same brightness and temperature, and then… for blacks, it's a bit more complicated.

## Undo your manual color management
### Context

The vast majority of photographers don't understand how color management work. As a result, they believe in the magic of the "ICC profile", they will buy a calibration device (Datacolor Spyder or Xrite), bake a custom color profile and hope think that it magically fixed all their problems. It didn't.

Color profiles can be good or bad, and you need to check their quality by doing another step of characterization after the calibration/profiling.

Strictly speaking, calibration is an hardware operation by which you set the backlighting, contrast and brightness settings of your monitor by using the knobs (so it doesn't apply to laptops). Then, profiling is achieved by recording the color deviation (error) of the display device by measuring how standard (previously-known) color patches render on the device, then computing the corrections that should annihilate such deviations. Finally, the characterization will compute the residual error that remains **after** the profile is applied, because unfortunately, that profile will not make color perfectly accurate. That residual error is expressed as a delta E, typically using the CIE 2000 dE formula, and the average delta E should absolutely be below 2, with a max delta E ideally below 2.3.

{{< warning >}}
If the profile characterization shows an average delta E higher than 2, your custom profile might actually be worse than using no profile at all. Quality control matters. Custom profile doesn't automatically imply higher quality.
{{< /warning >}}

### Reset everything to sRGB

In your OS/desktop environment color manager (aka **not** in Ansel), set the global color profile to generic sRGB. In Ansel, set the display color profile to sRGB too. Then, export your files as sRGB. If that fixes issues, then you have a faulty ICC profile somewhere in the pipeline. "Faulty" can either be a profile meant for some device and improperly used for another device (profiles are **not** portable, reusable, or else), or a bad profile (wrong profiling options when doing it, or old profile that doesn't match the screen rendering anymore).

## Profiling the right way

**Never use LUT profiles**. Yes, they are theoretically more accurate, but they are also a lot less forgiving to user mistakes, and it would require a solid 4h course to teach you everything you need to know to use LUT-based profiles without harming yourself. Also, LUT-based profiles can generally not be inverted, so they come with technical limitations too. Just forget about them.

In 99% of the use cases, for your screen, you need to use a matrix + 1D curve kind of profile. The 1D curve is essentially a tone curve that will linearize the brightness of your screen and will be applied to the 3 RGB channels the same. Even though LED and LCD screens are *mostly* linear already, they might need some local corrections near black, so the 1D curve deals with that. White point will be set to "native" (aka as-is), with D65 color temperature, and black point will be set to "native" too. If available, use the "Bradford" chromatic adaptation and avoid the CAM02. Use ICC v2 profiles instead of v4, the v4 brings no improvement for us here and is not as widely supported.

If, and only if, the matrix + 1D curve does not yield proper results, you may try matrix + 3D curves (aka one curve per RGB channel). However, DisplayCal has a hardtime ensuring white-balance consistency across the black-to-white range in this setting, and you should check that shadows will not be significatively colder or warmer (in color temperature) than highlights. This is a last-resort attempt. If you need to go that way, I recommend you build your profile with proprietary Xrite or Spyder software, because DisplayCal has issues there.

Keep in mind that the 1D curve is generally not linear, this means that it will not scale with your backlighting setting. You need to check the kind of curve it yields (Display Cal can generate a full HTML report that is very useful if you know how to read it), and if it is far from a straight "identity" line, which means you are in for problems. In that case, you may want to produce display color profiles at 100% and 50% backlighting intensity, and switch between those depending on your screen setting. (Yes, it is tedious).

If you absolutely need to compare physical prints next to your screen (though I have no idea why you would want to do that unless you own a photo lab), you will need to calibrate for D50 white at 90 Cd/m² and for a contrast (white luminance / black luminance) of 250:1 (that's black at 0.36 Cd/m²). Note that D50 is not the native white point of LED screen and, except for the expensive Eizo displays, distorting the white point by that much will result in a substantial loss of gamut.

If you profile a printer, keep in mind that any color profile is valid **only** for a particular triplet { printer driver + paper + ink cartridges }. In any case, I personally think that printing at home is a not worth the trouble and way too expensive for an amateur, unless you print at least several times a week. Indeed, when you start your printer again after some time unused, it will clean its nozzles first, and will do so with good ink from the cardridges – not only will it not be available for the next 15 min, but half or more of your expensive ink will actually end up being used as detergent.

## Remove local contrast modifiers

There **is** an expected discrepancy though, between full resolution exports, and lower resolutions/cropped image exports : the local contrast modifiers. Those are the modules : *local contrast*, *contrast equalizer*, *blurs*, *low-pass*, *diffuse or sharpen*, *sharpen*, *highlights reconstruction* (in *guided laplacian* mode), the *tone equalizer* if used with the internal guided filter for local contrast preservation, and the *details mask* (in parametric masks options).

### Context

All those filters rely on some amount of neighbouring pixels for their output. So, if you crop the image, you change the neighbourhood. But if you downsize it, first of all you remove sharp details (so, for example, sharpening will act on the coarser details instead of the finer), and then there might be rounding errors (say your filter does stuff by grabbing all pixels within a 3 px distance when zoomed 1:1 — zoom at 1:2, that makes it a 1.5 px distance, but there is no such thing as an half pixel, so that will be rounded to either 1 px or 2 px, and that's a 33% error).

There are tricks and mitigating solutions that try to make the output of these filters visually consistent from afar, no matter the zooming level you are using, but they work until they don't, precisely because of the integer nature of pixels that will necessarily introduce rounding errors.

### Export and preview at 1:1

Exporting can be done using 2 strategies : process the full-resolution image, then downsize last (if needed), or downsize first, then process the low-resolution image. The first option will be slower and may introduce aliasing artifacts (due to the fact that we interpolate non-linear RGB with high-frequencies), but neighbourhood filters will behave as expected. The second option will be faster, but neighbourhood filters can show significantly different output. Choose your poison.

In darkroom, you can also preview at 1:1 but it has one more shortcoming : any guided filter (either in *tone equalizer* or in the masking *feathering*) will only see the currently displayed region (possibly cropped to fit in the screen), instead of the full image. This is of course faster to process, but may generate some discrepancies for very large filters.

## Don't upgrade your OpenCL drivers

OpenCL drivers are notoriously bad, and it has nothing to do with any particular OS/platform or vendor (though AMD tends to be consistently shitty in the 2020's). It happens regularly that some driver update makes OpenCL entirely or subtly broken.

Check **when** your drivers are updated, and don't hesitate to roll back to the previously working version if anything breaks. If you don't have time to deal with that nonsense, simply avoid any driver upgrade once you found the one that worked for you.

## Is your image viewer color-managed ?

Ansel is properly color-managed. This part of the code has been consistently working and tested for the past 10 years, and I have checked it myself several times. Problem is, many image viewers and web browsers are not. So, in case of a disagreement between Ansel's internal color and whatever you see in another image viewer, try to assess first if that app is doing the right thing.

Also, note that the default Windows 10 image viewer has "image enhancements" enabled by default, and you need to find that option to disable it, because it will sharpen and resaturate your picture without asking you.

Similarly, pictures exported to Instagram and some other websites from Mozilla Firefox are re-encoded in a weird way (color will look less saturated), compared to exports through Chromium/Google Chrome (which will look as in Ansel).

There is a common belief that images for the web should be only exported in sRGB, and that's partly wrong. Ansel will put the color profile used to export the image in its metadata, such that any color-managed app can use it and convert the color to whatever display space is being used. So you can technically export pictures in whatever color space you choose. However, there is a common practice that consists in stripping the metadata of the pictures entirely, in websites and CMS, to save some bandwidth. If the image file doesn't provide its color space, then any color management system is supposed to assume it is sRGB (as per ICC recommendations), so if the metadata stripping was done without pre-converting the colors to sRGB, then your picture will be wrongly taken as sRGB all the time. So exporting to sRGB for web is the safe thing to do, but if the images are posted under your control and you know metadata are kept, then do as you please.

## Softproofing may not be what you think it is

Softproofing is a process that tries to emulate on screen the final appearance of a print. It's full of challenges and not great, because the screen is emissive and the print is reflective, so that doesn't start well. But there is worse.

Typical screens have a contrast ratio (white luminance / black luminance) of at least 300:1, and sometimes much more. Inkjet prints on matte paper have a contrast ratio of 50:1, and on glossy paper, maybe 100:1. That's a third to a sixth of what you see on a typical screen.

To emulate the print contrast, the ICC way is to anchor whites (the screen white and the paper white) to the same luminance value (typically, 90 Cd/m²). The adjustment variable will then be black, which means that the softproofing will brighten the blacks on screen as to reproduce the same contrast ratio as the print. This gives a "veiled", "washed" and "milky" black that most people don't expect and call an "artifact", but it is absolutely what should be seen. You can read more on that in the [Printing](../workflows/printing/) workflow page.

Note that reduced (global) contrast (that is, the contrast ratio) will result in a reduced perceived sharpness, because we don't perceive sharpness at all, but it is the local contrast that we associate with sharpness. Changes in global contrast affect local contrast too, and therefore trick us into thinking optical the sharpness is better/worse while it didn't change, and it is, again, just an illusion.

## Colorimetric intents don't work

They simply don't. Try loading any ICC profile and changing those intents, the outcome will not change one bit. I'm not sure what LittleCMS2 does with these, but consider them broken.
