---
title: Color management for Linux users
date: 2026-06-24
authors:
    - Aurélien Pierre
---

Linux is still vastly lagging behind MacOS and even Windows when it comes to ensuring the consistency of colors displayed on the monitor. The widely forced adoption of Wayland graphic server in most Linux distributions has damaged this state even more, since color management has been long refused by Wayland developers. The specification for a CMS in Wayland was finally drafted in 2020 and the code was merged into upstream Wayland in 2025, by external contributors, and after a long battle from the developers of earlier CMS software against the historical developers of Wayland.[^1] Since then, the state of CMS support is very hit-and-miss across desktop environments and distributions. And yet, the preliminary results of Ansel [telemetry](/doc/data-privacy.md) show 67 % of Wayland adoption among Ansel users.

__You should not use Ansel, or any other image editing software, on Wayland.__

{{< note >}}
The Wayland CMS situation varies greatly depending on distribution and desktop environment, and will evolve in the future. Rather than a full (soon outdated) landscape of what works and what doesn't, I will present the checklist that need to be validated to consider using Wayland.
{{< /note >}}

[^1]: Pekka Paalanen, _12 years of incubating Wayland color management_, February 2025. [URL](https://www.collabora.com/news-and-blog/news-and-events/12-years-of-incubating-wayland-color-management.html)

## TL;DR: why not use Wayland on Linux ?

Because the very author of Wayland color management system said it's nowhere near ready for professional photo & video usage.[^1]

For consumer & entertainment use, you can check the state of Wayland CMS support by your desktop compositor on [Wayland documentation](https://wayland.app/protocols/color-management-v1#compositor-support).

## The problem

Most (if not all) laptop screens and many consumer-level monitors have a white point _much_ more blue than the standard 6500 K, anywhere between 6800 K to 7200 K. To correct that, the historical way is to calibrate the screen and write the calibration curves into the [Video Card Gamma Table (VCGT)](https://www.color.org/groups/medical/displays/controllingVCGT.pdf). The VCGT is both:

- [a special data field](https://www.argyllcms.com/doc/iccvcgt.html) inside the ICC profiles,
- a special memory region on your GPU.

When starting your Linux session, some piece of software reads the VCGT from an ICC profile and loads it on the actual video memory. So the whole desktop would have its white point and contrast curve corrected in one lazy step, whether application were "color managed" or not.

Later on, many applets called "night color" or "redshift" hacked the VCGT to shift colors to amber in the evening and at night, because blue(ish) light is known to disturb sleep patterns, and while it is great for your circadian rhythm, it adds a layer of randomness in the color pipeline. Also, the VCGT could be lost without warning when resuming from standby mode, and several applications could race to be the last one overriding it. The rise of dual-GPU systems (discrete + embedded) did nothing to help reliability in the color pipeline, and the proprietary Nvidia driver is still the only one allowing to preview the VCGT.

But the bottom line is: you need some sort of system-wide way of loading a VCGT to normalize the white point,[^2] and Xorg/X11 had `colord` to globally advertise a system display profile that applications could fetch.

[^2]: The contrast/brightness curve is not so much of an issue on LED screens that are, by nature, close to linear.

On top of the VCGT, that holds the _calibration_, comes the _profiling_ which corrects the native color primaries of the display, such that RGB triplets match the light spectrum they are associated with. In short: 

- nailing the display white point at 6500 K and linearizing the brightness response is the first stage (calibration), 
- nailing the display color primaries to reduce hue and saturation deviations is the second stage (profiling). 

The profiling is typically a 3×3 color matrix, sometimes with extra curves or gamma, but it can also be a LUT (not recommended in Ansel).

When a photographer "calibrates" their display, actually both stages are usually silently done and saved into the same ICC profile. There is a way, in particular in Display Cal, to disable the calibration through the VCGT, which then bakes it into the profiling as a pack, but this is generally a very bad idea because then GUI theme colors are excluded from white point adaptation even on Xorg.

{{< note >}}
Contrarily to a common belief, ICC profiles are nothing more than a descriptor (kind of a file of metadata), that actual programs choose to apply (and choose how). They are not a piece of software in themselves.
{{< /note >}}

__At the application level, we can only apply the profiling stage on images__. This has 2 implications :

1. The color validity of the profiling stage relies on the calibration stage being properly performed at the VCGT level. Profiling becomes unpredictable and inaccurate without its twin calibration : it's a pipeline.
2. We cannot color-correct/color-manage GUI colors from the application theme (in particular: background color) declared in CSS stylesheet and passed through to Gtk.

This is a problem in Ansel because we set the whole GUI neutral grey, for color assessment purposes, and we need this grey to be 6500 K, but also consistent with the white point of the image. So we need a full-desktop color management, at least for the calibration, to avoid clashing white points between windows. Which Wayland initial design explicitely makes it none of its business, relying on apps developers to do the right thing (as if…).

And then, last but not least, if you are using several monitors, you need some piece of software mapping an ICC profile to each monitor, such that the CMS can grab the right profile for the monitor where your application window is sitting.[^3] Which is what Wayland explicitely forbids for "security" reasons.

[^3]: And since Xorg as well as Wayland allow application windows to sit on multiple monitors at once, you can only guess which color profile is going to be applied.

## What you need to check if using Wayland

The following assumes that you calibrated and profiled your monitor with a colorimeter, and produced a display ICC profile neutralizing the color deviations of your monitor.

Check that each monitor has its calibration loaded from ICC profile into VCGT when starting a graphic session
: That part seems to be fairly covered as of 2026, at least for the main players Gnome/KDE Plasma. The desktop environment allows to define a system profile that will globally change the white point of all applications.
: If not, the [`dispwin`](https://argyllcms.com/doc/dispwin.html) command of the `argyllcms` software allows to manually load it, like `dispwin -d 1 ~/.local/share/icc/YOUR_DISPLAY_PROFILE.icc`. "Suffice" to script it and have the script started automatically with your session, which excludes any user unfamiliar with scripting.

~~Check that each monitor is tagged with a color profile~~
: This part is explicitely removed from the Wayland protocol, so applications are, by design, forbidden to fetch information about displays. In particular, starting [`ansel-cmstest`](/doc/cli/ansel-cmstest/) in Wayland will return:
    ```bash
    $ /opt/ansel/bin/ansel-cmstest
    ansel-cmstest version 0.0.0+3877~gcfa6648f92
    this executable was built with colord support enabled
    ansel itself was built with colord support enabled

    primary CRTC is at CRTC 0

    eDP-1   the X atom and colord returned the same profile
            X atom: _ICC_PROFILE (0 bytes)
                    description: (none)
            colord: "(none)"
                    description: (file not found)

    Better check your system setup
    - some monitors lacked a profile
    You may experience inconsistent color rendition between color managed applications
    ```
: This practically means that Ansel _system profile (default)_, which is supposed to be automatically detected through `colord` or `xatom` on X11/Xorg, is empty/undefined all the time on Wayland and you will need to:
    1. add your display profile into `~./config/ansel/color/out`,
    2. choose it manually in the global menu __Display__ -> __Monitor color profile__,
    3. manually change it if/when you move the Ansel window to a different monitor.
: Failure to do that will result in Ansel defaulting to sRGB as output colorspace. If your display native gamut is:
    - Adobe RGB, then colors in the green-cyan region will appear more saturated on screen than they are in the file,
    - Display P3, then all colors will appear more saturated on screen than they are in the file, but the orange-green-cyan region will also be the worst offender.
: This problem has no solution within GTK3, that Ansel uses as a graphic toolkit, and even with GTK4, there is still no viable, widely supported solution as of now. Manually handling color profiles in Ansel works until the compositors start actively color-managing application windows themselves : then GTK3 offers no way of tagging a window as "already color-managed", as to prevent the compositor from doing them further harm. It will instead double up on colorspace conversions we already did internally and mess up colors in way that only experts will be able to spot. Luckily for us, as of mid-2026, no compositor is able to color-manage anything.
: In any case, the manual colorspace conversions can be done only on image surfaces that we paint in the Ansel app window. We have zero control over GUI controls colors defined in the theme stylesheet (`ansel.css`), and handled directly by GTK widgets, which are implicitely sRGB (as per CSS standard). Meaning GUI colors will always look oversaturated if your monitor native gamut is larger than sRGB, compared to what they are intended to be.

Check that HDR support is disabled
: Wayland now supports HDR capabilities by tampering with display backlighting. Although Ansel outputs good old 8 bits RGB and should not pull the HDR triggers, HDR is not part of ICC v2 or v4 and there is no telling how this feature would affect the tone response. It may be harmless, but until this is thorougly audited, the safe path is to keep HDR disabled.

Check that you are using Xorg
: Seriously, just don't use Wayland for photography.