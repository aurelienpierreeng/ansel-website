# Spanish (Español) translation glossary & rules for the Ansel website

Ansel is a fork of darktable (photo editor). The author writes in a precise, technical,
sometimes opinionated register. Match that register in Spanish: clear, technical, no fluff.

## Absolute rules (fidelity) — identical to all languages
- Translate ONLY human-readable prose. Preserve EXACTLY, byte-for-byte:
  - Inline math and LaTeX: `$...$`, `$$...$$`, `\text{}`, `\nabla`, `\times`, etc.
  - Code spans in backticks: `rawdenoiseai`, `dev_pixelpipe`, file names, flags, commands.
  - URLs and link targets: `[texto](https://...)`, anchors like `[resultados](#results)`
    — translate the visible link TEXT, NEVER the URL or the `#anchor`.
  - Footnote markers `[^forum]`, `[^1]`, and footnote definition IDs `[^1]:` (keep the id).
  - Markdown emphasis/structure: `**negrita**`, `*cursiva*`, `__x__`, heading levels `#`, `- ` bullets,
    `>` quotes, tables, Hugo shortcodes `{{< ... >}}` / `{{</ ... >}}`, HTML tags (`<kbd>`, `<em>`…).
  - Numbers, units, image dimensions (256×256), camera/brand names, ISO values.
- Bibliographic citations (author names, article/book titles, journal, DOI, PMID): keep VERBATIM.
- Keep the source's line-break structure: preserve blank lines and list-item line breaks.
- Do NOT add or remove content. Do not add a trailing newline (handled downstream).

## Address & typography
- Address the reader informally with **tú** (the existing Spanish text uses tú, e.g. "conectaste").
- Emphasis is normally done with markdown *italics*, as in the source. If you need quotation
  marks, use straight double quotes "…" to match the existing file (it does not use « » or „ ").
- Use the inverted opening marks ¿ … ? and ¡ … ! for questions/exclamations. Straight apostrophes.

## Terminology (use consistently; darktable-es style where it exists)
- raw / raw file → raw / archivo raw (invariante)
- to demosaic / demosaicing → interpolación cromática (app UI; el módulo demosaico)
- denoiser → reductor de ruido ; AI denoiser → reductor de ruido por IA ; denoising → reducción de ruido
- highlights → luces (app UI) ; highlight reconstruction → reconstrucción de luces
- sharpen → enfoque ; exposure → exposición
- shadows → sombras ; midtones → tonos medios
- clipping → recorte ; clipped → recortado ; blown highlight → alta luz quemada
- white balance → balance de blancos
- chromatic aberration → aberración cromática
- sensor → sensor ; photosite → fotosito ; well capacity → capacidad del pozo
- colour filter array (CFA) → matriz de filtros de color (CFA)
- base ISO → ISO base
- pipeline → pipeline ; downstream → posterior / aguas abajo ; upstream → anterior / aguas arriba
- wavelet(s) → wavelet(s) ; guided filter → filtro guiado
- "guided laplacians" (method name) → mantener «guided laplacians»
- harmonic transposition → transposición armónica
- scene-referred → referido a la escena (scene-referred) ; display-referred → referido a la pantalla
- gamut → gama (gamut) ; color space → espacio de color ; color management → gestión del color
- tile → tesela ; shard → fragmento ; thumbnail → miniatura ; mipmap → mipmap
- lighttable → mesa de luz ; darkroom → cuarto oscuro
- module → módulo ; blending → fusión ; mask → máscara
- feature → función ; release → versión ; changelog → registro de cambios
- maintainer → mantenedor ; contributor → colaborador/colaboradora
- pull request → pull request ; issue → incidencia ; commit → commit
- ground truth → verdad de referencia (ground truth)
