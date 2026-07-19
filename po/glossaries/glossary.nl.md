# Dutch (Nederlands) translation glossary & rules for the Ansel website

Ansel is a fork of darktable (photo editor). Author's register is precise, technical, opinionated.
No prior translations — establish a clean, consistent style.

## Absolute rules (fidelity) — identical to all languages
- Translate ONLY human-readable prose. Preserve EXACTLY, byte-for-byte: inline math/LaTeX
  (`$...$`, `\text{}`, `\times`…), `code spans`, URLs and #anchors (translate only visible link
  text), footnote markers/ids (`[^x]`, `[^1]:`), markdown structure (`**vet**`, headings, `- `
  bullets), Hugo `{{< >}}` shortcodes, HTML tags, numbers/units (256×256, ISO 100), brand/camera
  names. Keep bibliographic citations verbatim. Preserve blank lines and list-item line breaks.
- Do NOT add/remove content. Do not add a trailing newline (handled downstream).

## Address & typography
- Address the reader informally with **je/jij** (jouw). Use „…" (low-high) quotation marks. Em dash — ok.

## Terminology
- raw → raw (raw-bestand) ; demosaic → demosaic (app UI behoudt de Engelse term)
- denoiser → ruisonderdrukker ; AI denoiser → AI-ruisonderdrukker ; denoising → ruisonderdrukking
- highlights → hooglichten (app UI, één woord) ; highlight reconstruction → reconstructie van hooglichten
- sharpen → verscherpen ; exposure → belichting
- shadows → schaduwen ; midtones → middentonen
- clipping → clipping ; clipped → geklipt ; blown highlight → uitgebrand hoog licht
- white balance → witbalans ; chromatic aberration → chromatische aberratie
- sensor → sensor ; photosite → fotosite ; well capacity → putcapaciteit
- colour filter array (CFA) → kleurenfilterarray (CFA) ; base ISO → basis-ISO
- pipeline → pipeline ; downstream → verderop/stroomafwaarts ; upstream → stroomopwaarts
- wavelet(s) → wavelet(s) ; guided filter → geleid filter ; "guided laplacians" → behouden
- harmonic transposition → harmonische transpositie
- scene-referred → scènegerefereerd (scene-referred) ; display-referred → schermgerefereerd
- gamut → gamut ; color space → kleurruimte ; color management → kleurbeheer
- tile → tegel ; shard → fragment ; thumbnail → miniatuur ; mipmap → mipmap
- lighttable → bibliotheek (app UI) ; darkroom → ontwikkelen (app UI)
- module → module ; blending → mengen ; mask → masker
- feature → functie ; release → versie ; changelog → wijzigingslogboek
- maintainer → beheerder ; contributor → bijdrager
- pull request → pull request ; issue → issue ; commit → commit ; ground truth → ground truth
