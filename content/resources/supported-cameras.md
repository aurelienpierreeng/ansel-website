---
title: Supported cameras and formats
date: 2025-04-22
---

This page lists all the known cameras and whether or not their raw files are decoded by Ansel, as well as all file types supported in input and output.

## Cameras

### Introduction

Some cameras may use different encoding formats (12 bits, 14 bits, sRAW, compressed or not) and image ratios (4:3, 16:9, 3:2). Because one or more of these formats is supported doesn't imply they all are. Different cameras may share the same sensor and electronics, even though their commercial name is different: those will be found in the _aliases_ columns.

Ansel uses [Rawspeed](https://darktable-org.github.io/rawspeed/) library to decode most raw files. Libraw fallbacks have been introduced because Rawspeed still does not support `.CR3` Canon files (ISOBMFF format). Libraw can also be [manually configured](../../doc/preferences-settings/processing/#libraw) to always load some files, by camera or by extension. Rawspeed support is native and complete in Ansel, whereas Libraw is not fully wired to the application.

__The Ansel project does not have any control over the list of supported cameras and file formats, by Rawspeed or by Libraw__. The Ansel application handles pixels after they are decoded by Rawspeed or Libraw, and metadata (EXIF, IPTC, XMP) after they are decoded by [Exiv2](https://exiv2.org/). Decoding problems must be reported to Rawspeed, Libraw and Exiv2 projects, depending on their nature.

Noise profiles are used by the [_denoise (profiled)_](../../doc/modules/processing-modules/denoise-profiled) module. Cameras without noise profiles will still be usable, only denoising at high ISO might be of subpar quality because it will use generic noise stats.


### Support table

Support legend:

- <span class='badge rounded-circle text-bg-success square-badge'>✓</span> Camera and format supported by Rawspeed. In case of problems, submit [bug reports](https://github.com/darktable-org/rawspeed/issues).
- <span class='badge rounded-circle text-bg-danger square-badge'>✗</span> Camera and format unsupported by Rawspeed and Libraw,
- <span class='badge rounded-circle text-bg-warning square-badge'>?</span> Support state unknown because raw samples are missing (see [get your camera supported](#get-your-camera-supported))
- <span class='badge rounded-circle text-bg-info square-badge'>-</span> Camera and format supported by Libraw fallback. This fallback can be higher or lower quality.

Support quality legend:

- 🏆 fully-supported camera,
- 🥈 partially-supported camera, usable with minor compromises,
- 🥉 partially-supported camera, usable with compromises,
- ⁉️ partially-supported camera, practical usability impossible to estimate,
- 💩 unsupported camera.

_This table is automatically generated from parsing Rawspeed, Libraw and Ansel source code. No human verification has been made_.

{{< rawspeed >}}

### Get your camera supported

Users who are not able to perform command-line operations in a terminal will be unable to help getting their cameras supported. They should buy cameras currently supported or stick to proprietary software. There is no guaranty that a brand-new camera will one day be supported, and no indication regarding when it will be. Camera support is a entirely based on an unpaid community effort, limited by everyone's availability.

#### The case of Canon CR3 / ISOBMFF files

Canon `.CR3` files belong to a new type of ISOBMFF containers. These require specific decoders, from Rawspeed, Libraw and Exiv2. This specific decoder is not available in Rawspeed, so _temporary_ and partial support for Libraw has been introduced in Darktable circa 2020. Ansel inherit it, but, as of 2025, Rawspeed still does not support `.CR3`.

But Ansel requires more than Libraw to actually handle `.CR3` : it needs Exiv2 built with ISOBMFF support too, for metadata. ISOBMFF support is optional in Exiv2 for (mostly invented) copyright & legal reasons, and some Linux distributions (Fedora) package this library with ISOBMFF disabled. Users that use Ansel pre-built packages from such distributions, or who build it using the Exiv2 library from the distribution repository, will never have complete `.CR3` support.

#### Helping support

If your camera is not or partially supported:

- upload test raw files to <https://raw.pixls.us>,
- open a bug report [on Rawspeed tracker](https://github.com/darktable-org/rawspeed/issues) and [on Libraw tracker](https://github.com/LibRaw/LibRaw/issues/608).


If your camera does not have noise profiles, you can [generate them yourself](https://pixls.us/articles/how-to-create-camera-noise-profiles-for-darktable/) and submit them to Ansel bug tracker.


## Non-raw codecs

Ansel supports the following file formats and extensions (while reading and writing):

- JPEG: `.jpg`, `.jpeg` (mandatory),
- PNG: `.png` (mandatory),
- PFM: `.pfm` (mandatory),
- TIFF: `.tif`, `.tiff` (mandatory),
- OpenEXR: `.exr` (optional),
- WebP: `.wepb` (optional),
- AVIF: `.avif` (optional),
- HEIF: `.heif`, `.heic`, `.hif` (optional),
- JPEG2000: `.j2c`, `.j2k`, `.jp2`, `.jpc` (optional),
- Through GraphicsMagick/ImageMagick: `.gif`, `.bmp`, `.dcm`, `.jng`, `.miff`, `.mng`, `.pbm`, `.ppm`, `.pgm` (optional)

Note that the optional formats are enabled only if Ansel is built with the corresponding options enabled and if the libraries providing the codecs are found on the system building it. Pre-built binaries provided by the Ansel project enable them all but third-party packagers may choose otherwise.
