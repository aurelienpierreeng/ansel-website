# Italian (Italiano) translation glossary & rules for the Ansel website

Ansel is a fork of darktable (photo editor). The author writes in a precise, technical,
sometimes opinionated register. Match that register in Italian: clear, technical, no fluff.
(This language has no prior translations — establish a clean, consistent style.)

## Absolute rules (fidelity) — identical to all languages
- Translate ONLY human-readable prose. Preserve EXACTLY, byte-for-byte:
  - Inline math and LaTeX: `$...$`, `$$...$$`, `\text{}`, `\nabla`, `\times`, etc.
  - Code spans in backticks: `rawdenoiseai`, `dev_pixelpipe`, file names, flags, commands.
  - URLs and link targets: `[testo](https://...)`, anchors like `[risultati](#results)`
    — translate the visible link TEXT, NEVER the URL or the `#anchor`.
  - Footnote markers `[^forum]`, `[^1]`, and footnote definition IDs `[^1]:` (keep the id).
  - Markdown emphasis/structure: `**grassetto**`, `*corsivo*`, `__x__`, heading levels `#`, `- ` bullets,
    `>` quotes, tables, Hugo shortcodes `{{< ... >}}` / `{{</ ... >}}`, HTML tags (`<kbd>`, `<em>`…).
  - Numbers, units, image dimensions (256×256), camera/brand names, ISO values.
- Bibliographic citations (author names, article/book titles, journal, DOI, PMID): keep VERBATIM.
- Keep the source's line-break structure: preserve blank lines and list-item line breaks.
- Do NOT add or remove content. Do not add a trailing newline (handled downstream).

## Address & typography
- Address the reader informally with **tu** (modern, direct technical register).
- Use Italian angular quotation marks «…» for quoted prose. Em dash — is fine. Straight apostrophes '.

## Terminology (use consistently; darktable-it style where it exists)
- raw / raw file → raw / file raw (invariante)
- to demosaic / demosaicing → demosaicizzare / demosaicizzazione
- denoiser → riduttore di rumore ; AI denoiser → riduttore di rumore IA ; denoising → riduzione del rumore
- highlights → alte luci ; highlight reconstruction → ricostruzione delle alte luci
- shadows → ombre ; midtones → mezzitoni
- clipping → clipping ; clipped → tagliato ; blown highlight → alta luce bruciata
- white balance → bilanciamento del bianco
- chromatic aberration → aberrazione cromatica
- sensor → sensore ; photosite → fotosito ; well capacity → capacità del pozzo
- colour filter array (CFA) → matrice di filtri colore (CFA)
- base ISO → ISO base
- pipeline → pipeline ; downstream → a valle ; upstream → a monte
- wavelet(s) → wavelet ; guided filter → filtro guidato
- "guided laplacians" (method name) → mantenere «guided laplacians»
- harmonic transposition → trasposizione armonica
- scene-referred → riferito alla scena (scene-referred) ; display-referred → riferito al display
- gamut → gamut ; color space → spazio colore ; color management → gestione del colore
- tile → tassello ; shard → frammento ; thumbnail → anteprima (app UI) ; mipmap → mipmap
- sharpen → nitidezza ; chromatic aberration → aberrazione cromatica ; exposure → esposizione
- lighttable → tavolo luminoso ; darkroom → camera oscura
- module → modulo ; blending → fusione ; mask → maschera
- feature → funzione ; release → versione ; changelog → registro delle modifiche
- maintainer → maintainer ; contributor → collaboratore/collaboratrice
- pull request → pull request ; issue → issue ; commit → commit
- ground truth → ground truth (verità di riferimento)
