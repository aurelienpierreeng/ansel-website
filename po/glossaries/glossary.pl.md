# Polish (Polski) translation glossary & rules for the Ansel website

Ansel is a fork of darktable (photo editor). Author's register is precise, technical, opinionated.
No prior translations — establish a clean, consistent style.

## Absolute rules (fidelity) — identical to all languages
- Translate ONLY human-readable prose. Preserve EXACTLY, byte-for-byte: inline math/LaTeX
  (`$...$`, `\text{}`, `\times`…), `code spans`, URLs and #anchors (translate only visible link
  text), footnote markers/ids (`[^x]`, `[^1]:`), markdown structure (`**pogrubienie**`, headings,
  `- ` bullets), Hugo `{{< >}}` shortcodes, HTML tags, numbers/units (256×256, ISO 100),
  brand/camera names. Keep bibliographic citations verbatim. Preserve blank lines and list breaks.
- Do NOT add/remove content. Do not add a trailing newline (handled downstream).

## Address & typography
- Address the reader directly and informally (2nd person, "ty" form: możesz, Twój). Use Polish
  „…" quotation marks (dolny–górny). Em dash — ok. Follow Polish grammar/declension carefully.

## Terminology
- raw → raw (plik raw) ; demosaic → demozaikowanie / demozaikować
- denoiser → odszumiacz ; AI denoiser → odszumiacz AI ; denoising → odszumianie
- highlights → światła ; highlight reconstruction → rekonstrukcja świateł
- shadows → cienie ; midtones → tony średnie
- clipping → przycięcie ; clipped → przycięty ; blown highlight → wypalone światło
- white balance → balans bieli ; chromatic aberration → aberracja chromatyczna
- sensor → matryca ; photosite → element światłoczuły (photosite) ; well capacity → pojemność studni
- colour filter array (CFA) → matryca filtrów barwnych (CFA) ; base ISO → bazowe ISO
- pipeline → potok (pipeline) ; downstream → dalej w potoku ; upstream → wcześniej w potoku
- wavelet(s) → falki ; guided filter → filtr sterowany ; "guided laplacians" → zachować
- harmonic transposition → transpozycja harmoniczna
- scene-referred → odniesiony do sceny (scene-referred) ; display-referred → odniesiony do wyświetlacza
- gamut → gamut ; color space → przestrzeń barwna ; color management → zarządzanie kolorami
- tile → kafelek ; shard → fragment ; thumbnail → miniaturka (app UI) ; mipmap → mipmapa
- sharpen → wyostrzenie ; exposure → ekspozycja
- lighttable → stół podświetlany ; darkroom → ciemnia
- module → moduł ; blending → mieszanie ; mask → maska
- feature → funkcja ; release → wersja ; changelog → lista zmian
- maintainer → opiekun ; contributor → współtwórca
- pull request → pull request ; issue → zgłoszenie ; commit → commit ; ground truth → prawda podstawowa (ground truth)
