---
title: Contribute images to the AI denoiser
date: 2026-07-18
weight: 10
---

Ansel ships a neural raw denoiser (the `rawdenoiseai` module) that is unlike
general-purpose AI denoisers: it is trained on **non-demosaiced sensor data,
as close to the actual sensor reading as a raw file allows**, and it runs at
the exact same point of the pipeline — before white balance,
chromatic-aberration correction and demosaicing — so every downstream stage
inherits clean data. One set of weights covers every camera Ansel has a
noise profile for, Bayer and X-Trans alike.

What limits its quality is the **training corpus**: a public collection of
clean, base-ISO raw tiles that the training synthetically corrupts with
noise, computed exactly from Ansel's measured camera noise profiles. More
scenes, more textures and more camera models directly translate into a
better denoiser for everyone — and this is where you can help, in about ten
minutes, without knowing anything about machine learning or git.

The whole pipeline is scripted; **your only real work is choosing the
images**. Technical deep dives live in the
[ansel-denoise repository](https://github.com/aurelienpierreeng/ansel-denoise)
(training code, [network architecture](https://github.com/aurelienpierreeng/ansel-denoise/blob/master/docs/architecture.md),
[design documentation](https://github.com/aurelienpierreeng/ansel/blob/master/doc/rawdenoiseai.md)).

## What leaves your machine — read this first

Your photographs are **not** uploaded. A harvester decodes each selected raw
file locally and extracts up to 16 tiles of 256×256 **raw sensor pixels**
(mosaic data, before demosaicing), packed with the sensor calibration data
(CFA layout, black/white levels — white balance coefficients are recorded
as metadata but never applied), the camera model, the ISO, and the bare
filename. Shards contain **no** GPS coordinates, no timestamps, no serial
numbers, no author metadata, and no file paths from your machine.

{{< note >}}
The tiles themselves are viewable fragments of your photographs: 256×256
crops are large enough to recognize faces, license plates, documents or
screens. They are published in the public training corpus. Treat a
contribution exactly like publishing crops of the photos — <b>the selection
step in the lighttable is your consent boundary</b>: nothing you did not
explicitly select is ever touched.
{{</ note >}}

### License: locked to denoiser training

You keep the copyright on your photographs. Contributed tiles are published
under the [Ansel Training Data License](https://github.com/aurelienpierreeng/ansel-denoise/blob/master/LICENSE-DATA.md)
(ATDL-1.1). What it allows: **anyone** may use the tiles with the
ansel-denoise training stack (GPL-3.0) to **audit, review, reproduce and
benchmark** the Ansel denoiser — scientific and academic use is welcome —
or to **train their own denoising models**, whose weights are theirs
without restriction, including in other open-source or commercial
applications. The bright line is what the training stack can learn: the
tiles must never feed a stack able to learn anything else than separating
noise from signal — **"style" learning and generative AI are explicitly
forbidden**, as are dataset redistribution and identifying depicted people
or places. You can request removal at any time by opening an issue: your
shards are deleted from the corpus and excluded from all future trainings.

Every contribution is recorded in a
[public registry](https://github.com/aurelienpierreeng/ansel-denoise/blob/master/contrib/registry.jsonl)
— who contributed what, when, from where — so the provenance of the whole
corpus is auditable, forever.

## What makes a good candidate image

The harvester wants **clean** signal — the noise is added synthetically
later, so it must not already be in your files.

Good:

- **Base ISO** (ISO ≤ 200 is enforced; ISO 64–100 is even better), correctly
  exposed or slightly bright — shadows carry noise even at base ISO,
  highlights are clean.
- **Sharp and textured**: foliage, fabric, hair, gravel, brick, grass — fine
  detail is exactly what the network must learn to preserve.
- **Diverse content**: landscapes, architecture, still life, macro...
- **Rare cameras**: anything beyond the usual Canon/Nikon/Sony full-frame
  bodies is disproportionately valuable — Fuji X-Trans, Olympus/OM, Pentax,
  compacts, phones shooting DNG, old CCD bodies. If your gear is unusual,
  your contribution matters twice.

Not useful (the harvester rejects most of these on its own): high-ISO,
underexposed or blurred images; long-exposure night shots (hot pixels are
not "clean"); bursts and near-duplicates — pick one; flat frames (clear
skies, walls, defocused backgrounds).

**Volume policy: up to ~1000 raw images per person.** The corpus needs
content and camera variability, not bulk — a thousand images from one
photographer already share one eye, one gear bag and one processing habit.
Fifty varied, sharp, base-ISO images beat five hundred near-duplicates.

## How to contribute, step by step

Requirements: Linux, macOS or Windows, Python ≥ 3.10, an Ansel library,
about ten minutes. Monochrome-sensor cameras (Leica M Monochrom, Pentax
Monochrome) are not usable — the network needs a color mosaic. Each step
shows the Linux/macOS command first, then the Windows one.

{{< note >}}
<b>Windows first-timers — two one-time preparations.</b><br/>
<b>1. Install Python:</b> open PowerShell (press <code>Win+X</code>, choose
<i>Terminal</i>) and type <code>py --version</code>. If Python is missing,
install it with <code>winget install Python.Python.3.12</code>, or download
it from <a href="https://www.python.org/downloads/">python.org</a> and
<b>tick "Add python.exe to PATH"</b> on the installer's first screen — then
close and reopen PowerShell.<br/>
<b>2. Running scripts:</b> PowerShell refuses script files by default. Every
script command below therefore starts with
<code>powershell -ExecutionPolicy Bypass -File ...</code>, which allows just
that one script for just that one run — you never need to change a system
setting. Paste commands into PowerShell with a right-click.
{{</ note >}}

**0. Install the tooling** — one script, installs the two Python
dependencies (`numpy`, `rawpy`):

```sh
git clone https://github.com/aurelienpierreeng/ansel-denoise.git
cd ansel-denoise
sh scripts/setup_contributor.sh
```

On Windows, in PowerShell, from the folder where you want the tools (e.g.
`cd $HOME\Documents`) — no git needed, the script downloads the repository
as a ZIP for you:

```powershell
Invoke-WebRequest https://raw.githubusercontent.com/aurelienpierreeng/ansel-denoise/master/scripts/setup_contributor.ps1 -OutFile setup_contributor.ps1
powershell -ExecutionPolicy Bypass -File setup_contributor.ps1
cd ansel-denoise
```

**1. Curate in Ansel.** In the lighttable, select the images you are willing
to make public tiles of (filter by ISO to be quick), then
**File ▸ Export image list... ▸ Save as file...** and keep the proposed
`ansel-image-files.txt` name.

**2. Harvest.** Reads your Ansel library database (read-only), gates on ISO,
decodes each file in a crash-isolated process, writes the shards. Nothing is
uploaded:

```sh
python3 -m ansel_denoise.harvest_library --paths-file ansel-image-files.txt --out shards/mine
```

On Windows (`py` comes with Python; your Ansel library is found
automatically under `%LOCALAPPDATA%\ansel` — save the exported
`ansel-image-files.txt` into the `ansel-denoise` folder first, or give its
full path):

```powershell
py -m ansel_denoise.harvest_library --paths-file ansel-image-files.txt --out shards\mine
```

**3. Pack.** Validates every shard, prefixes them with your handle, writes a
manifest with checksums and your license grant, bundles the license text
with the data, produces one tarball:

```sh
python3 scripts/pack_contribution.py shards/mine --handle your-github-name
```

On Windows:

```powershell
py scripts\pack_contribution.py shards\mine --handle your-github-name
```

**4. Upload** the printed `.tar.gz` to any file host the maintainer can
download from — Google Drive, Dropbox, WeTransfer, Proton Drive, your own
server — and copy the download link.

**5. Submit — no git knowledge needed.** One script opens the contribution
pull request for you through the [GitHub CLI](https://cli.github.com)
(`apt install gh` / `brew install gh`, on Windows
`winget install Git.Git GitHub.cli`; it signs you into GitHub through your
browser and does the rest):

```sh
sh scripts/submit_contribution.sh ansel-denoise-contrib-<you>-<date>.tar.gz --url <your-link>
```

On Windows:

```powershell
powershell -ExecutionPolicy Bypass -File scripts\submit_contribution.ps1 -Bundle ansel-denoise-contrib-<you>-<date>.tar.gz -Url <your-link>
```

The pull request contains only a small metadata file — handle, link,
checksum, statistics, license grant — never the images. If you'd rather not
install `gh`, open a
[Shard contribution issue](https://github.com/aurelienpierreeng/ansel-denoise/issues/new/choose)
with the link and the checksum instead.

That's it. You can delete `shards/mine` and the bundle afterwards.

## What happens next

The maintainer reviews your pull request, then a collection script downloads
your bundle, verifies every checksum, re-validates every shard (shards are
loaded so that a bundle cannot execute code), merges the new tiles into the
corpus, and records the contribution in the public registry. Your tiles ride
the next training — and your camera earns its place in the next model
version's changelog.

You can also train the model yourself — on your own machine or a free GPU
tier — with a [single notebook](https://github.com/aurelienpierreeng/ansel-denoise/blob/master/notebooks/train.ipynb)
that runs locally, on Google Colab and on Kaggle: that is precisely the
"reproducing the training workflow" the data license protects.
