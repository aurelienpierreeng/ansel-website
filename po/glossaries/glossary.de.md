# German (Deutsch) translation glossary & rules for the Ansel website

Ansel is a fork of darktable (photo editor). The author writes in a precise, technical,
sometimes opinionated register. Match that register in German: clear, technical, no fluff.

## Absolute rules (fidelity) — identical to all languages
- Translate ONLY human-readable prose. Preserve EXACTLY, byte-for-byte:
  - Inline math and LaTeX: `$...$`, `$$...$$`, `\text{}`, `\nabla`, `\times`, etc.
  - Code spans in backticks: `rawdenoiseai`, `dev_pixelpipe`, file names, flags, commands.
  - URLs and link targets: `[Text](https://...)`, anchors like `[Ergebnisse](#results)`
    — translate the visible link TEXT, NEVER the URL or the `#anchor`.
  - Footnote markers `[^forum]`, `[^1]`, and footnote definition IDs `[^1]:` (keep the id).
  - Markdown emphasis/structure: `**bold**`, `*italic*`, `__x__`, heading levels `#`, `- ` bullets,
    `>` quotes, tables, Hugo shortcodes `{{< ... >}}` / `{{</ ... >}}`, HTML tags (`<kbd>`, `<em>`…).
  - Numbers, units, image dimensions (256×256), camera/brand names, ISO values.
- Bibliographic citations (author names, article/book titles, journal, DOI, PMID): keep VERBATIM.
  Only translate a leading explanatory clause if the footnote is prose, not a citation.
- Keep the source's line-break structure: preserve blank lines and list-item line breaks.
  Ordinary hard-wrapped prose may be rewrapped or kept as one line — both are fine.
- Do NOT add or remove content. Do not add a trailing newline (handled downstream).

## Address & typography
- Address the reader formally with **Sie** / **Ihr** (the existing German text uses Sie).
- Use German quotation marks „…" (low-high) for quoted prose. Em dash — is fine.
- Straight apostrophes. Follow German capitalization (all nouns capitalized).

## Terminology (use consistently; keep darktable-style German where it exists)
- raw / raw file → RAW / RAW-Datei (invariant „RAW")
- to demosaic / demosaicing → entrastern / Entrasterung (app UI; „Demosaicing" nur als Erläuterung)
- denoiser → Entrauscher ; AI denoiser → KI-Entrauscher ; denoising → Entrauschen/Rauschunterdrückung
- highlights → Lichter ; highlight reconstruction → Lichterrekonstruktion
- shadows → Schatten ; midtones → Mitteltöne
- clipping → Clipping ; clipped → beschnitten ; blown highlight → ausgefressenes Licht
- white balance → Weißabgleich
- chromatic aberration → chromatische Aberration
- sensor → Sensor ; photosite → Photosite ; well capacity → Kapazität des Potentialtopfs
- colour filter array (CFA) → Farbfilter-Array (CFA)
- base ISO → Basis-ISO
- pipeline → Pipeline ; downstream → nachgelagert ; upstream → vorgelagert
- wavelet(s) → Wavelet(s) ; guided filter → geführter Filter
- "guided laplacians" (method name) → „guided laplacians" beibehalten
- harmonic transposition → harmonische Transposition
- scene-referred → szenenbezogen (scene-referred) ; display-referred → anzeigebezogen
- gamut → Farbumfang (Gamut) ; color space → Farbraum ; color management → Farbmanagement
- tile → Kachel ; shard → Fragment ; thumbnail → Vorschaubild (app UI) ; mipmap → Mipmap
- sharpen → schärfen ; chromatic aberration → chromatische Aberration ; exposure → Belichtung
- lighttable → Leuchttisch ; darkroom → Dunkelkammer
- module → Modul ; blending → Überblenden ; mask → Maske
- feature → Funktion ; release → Version ; changelog → Änderungsprotokoll
- maintainer → Maintainer ; contributor → Mitwirkende(r)
- pull request → Pull Request ; issue → Issue ; commit → Commit
- ground truth → Ground Truth
- ground-truth study → Ground-Truth-Studie
