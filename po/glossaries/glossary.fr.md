# French translation glossary & rules for Ansel website

Ansel is a fork of darktable (photo editor). Author writes in a precise, technical,
sometimes opinionated register. Match that register in French: clear, technical, no fluff.

## Absolute rules (fidelity)
- Translate ONLY human-readable prose. Preserve EXACTLY, byte-for-byte:
  - Inline math and LaTeX: `$...$`, `$$...$$`, `\text{}`, `\nabla`, `\times`, etc.
  - Code spans in backticks: `rawdenoiseai`, `dev_pixelpipe`, file names, flags, commands.
  - URLs and link targets: `[texte](https://...)`, anchors like `[résultats](#results)`
    — translate the visible link TEXT, NEVER the URL or the `#anchor`.
  - Footnote markers `[^forum]`, `[^1]`, and footnote definition IDs `[^1]:` (keep the id).
  - Markdown emphasis/structure: `**bold**`, `*italic*`, `#` headings level, `- ` bullets,
    `>` quotes, tables, Hugo shortcodes `{{< ... >}}` / `{{</ ... >}}`, HTML tags.
  - Numbers, units, image dimensions (256×256), camera/brand names, ISO values.
- Bibliographic citations (author names, article/book titles, journal, DOI, PMID): keep VERBATIM.
  Only translate a leading explanatory clause if the footnote is prose, not a citation.
- Keep the source's line-break structure: preserve blank lines and list-item line breaks.
  Ordinary hard-wrapped prose may be rewrapped or kept as one line — both are fine.
- Do NOT add or remove content. Do not add a trailing newline (handled downstream).

## Terminology (use consistently)
- raw → raw (invariant, masc.: « un fichier raw », « les raw »)
- to demosaic / demosaicing → dématricer / dématriçage
- denoiser / denoising → débruiteur / débruitage
- highlights → hautes lumières ; shadows → ombres ; midtones → tons moyens
- highlight reconstruction → reconstruction des hautes lumières
- white balance → balance des blancs
- chromatic aberration → aberration chromatique
- sensor → capteur ; photosite → photosite ; well capacity → capacité du puits
- colour filter array (CFA) → matrice de filtres colorés (CFA)
- clipping / clipped / blown → écrêtage / écrêté / brûlé (surexposé)
- base ISO → ISO natif
- pipeline → pipeline (invariant) ; downstream → en aval ; upstream → en amont
- wavelet(s) → ondelette(s) ; guided filter → filtre guidé
- "guided laplacians" (method name) → garder « guided laplacians »
- harmonic transposition → transposition harmonique
- scene-referred → scene-referred (garder) ; display-referred → display-referred (garder)
- gamut → gamut ; color space → espace colorimétrique ; color management → gestion des couleurs
- tile → tuile ; shard → fragment ; thumbnail → vignette ; mipmap → mipmap (invariant)
- lighttable → table lumineuse ; darkroom → chambre noire
- module → module ; blending → fusion (des modules) ; mask → masque
- feature → fonctionnalité ; release → version ; changelog → journal des modifications
- maintainer → mainteneur ; contributor → contributeur/contributrice
- pull request → pull request (garder) ; issue → ticket ; commit → commit (garder)
- ground truth → vérité terrain

## Style
- Use French typographic conventions: « guillemets » with regular spaces, — em dashes,
  non-breaking space is not required (ASCII space is fine, matching the existing file).
- Straight apostrophes ' (not curly), matching the existing .po file.
- Vouvoiement when addressing the reader (« vous »).
