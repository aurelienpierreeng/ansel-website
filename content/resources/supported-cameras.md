---
title: Supported cameras and formats
date: 2025-04-22
---

This page lists all the known cameras and whether or not their raw files are decoded by Ansel. Some cameras may use different encoding formats (12 bits, 14 bits, sRAW, compressed or not) and image ratios (4:3, 16:9, 3:2). Because one or more of these formats is supported doesn't imply they all are. Different cameras may share the same sensor and electronics, even though their commercial name is different: those will be found in the _aliases_ columns.

Noise profiles are used by the [_denoise (profiled)_](../../doc/modules/processing-modules/denoise-profiled) module. If your camera does not have one, you can [generate them yourself](https://pixls.us/articles/how-to-create-camera-noise-profiles-for-darktable/) and submit it, or use generic noise statistics as a fallback. Cameras without noise profiles will still be usable, only denoising at high ISO might be of subpar quality.

Ansel uses [Rawspeed](https://darktable-org.github.io/rawspeed/) library to decode most raw files. Libraw fallbacks have been introduced because Rawspeed still does not support `.CR3` Canon files (ISOBMFF format). Libraw can also be [manually configured](../../doc/preferences-settings/processing/#libraw) to always load some files, by camera or by extension. Rawspeed support is native and complete in Ansel, whereas Libraw is not fully wired to the application.

Support legend:

- <span class='badge rounded-circle text-bg-success square-badge'>✓</span> Camera and format supported by Rawspeed. In case of problems, submit [bug reports](https://github.com/darktable-org/rawspeed/issues).
- <span class='badge rounded-circle text-bg-danger square-badge'>✗</span> Camera and format unsupported by Rawspeed and Libraw,
- <span class='badge rounded-circle text-bg-warning square-badge'>?</span> Support state unknown because raw samples are missing. Consider submitting images to <https://raw.pixls.us>
- <span class='badge rounded-circle text-bg-info square-badge'>-</span> Camera and format supported by Libraw fallback. This fallback can be higher or lower quality.

Support quality legend:

- 🏆 fully-supported camera,
- 🥈 partially-supported camera, usable with minor compromises,
- 🥉 partially-supported camera, usable with compromises,
- ⁉️ partially-supported camera, practical usability impossible to estimate,
- 💩 unsupported camera.

_This table is automatically generated from parsing Rawspeed, Libraw and Ansel source code. No human verification has been made_.

{{< rawspeed >}}
