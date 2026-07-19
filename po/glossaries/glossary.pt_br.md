# Brazilian Portuguese (Português do Brasil) glossary & rules for the Ansel website

Ansel is a fork of darktable (photo editor). Author's register is precise, technical, opinionated.
No prior translations — establish a clean, consistent style.

## Absolute rules (fidelity) — identical to all languages
- Translate ONLY human-readable prose. Preserve EXACTLY, byte-for-byte: inline math/LaTeX
  (`$...$`, `\text{}`, `\times`…), `code spans`, URLs and #anchors (translate only visible link
  text), footnote markers/ids (`[^x]`, `[^1]:`), markdown structure (`**negrito**`, headings,
  `- ` bullets), Hugo `{{< >}}` shortcodes, HTML tags, numbers/units (256×256, ISO 100),
  brand/camera names. Keep bibliographic citations verbatim. Preserve blank lines and list breaks.
- Do NOT add/remove content. Do not add a trailing newline (handled downstream).

## Address & typography
- Address the reader informally with **você**. Use straight double quotes "…" for quotation.
  Em dash — ok. Straight apostrophes.

## Terminology
- raw → raw (arquivo raw) ; demosaic → interpolação cromática (app UI; o módulo demosaico)
- denoiser → redutor de ruído ; AI denoiser → redutor de ruído por IA ; denoising → redução de ruído
- highlights → realces (app UI) ; highlight reconstruction → reconstrução de realces
- shadows → sombras ; midtones → meios-tons (app UI)
- sharpen → melhorar nitidez ; exposure → exposição
- clipping → clipping ; clipped → recortado ; blown highlight → alta luz estourada
- white balance → balanço de branco ; chromatic aberration → aberração cromática
- sensor → sensor ; photosite → fotossítio ; well capacity → capacidade do poço
- colour filter array (CFA) → matriz de filtros de cor (CFA) ; base ISO → ISO base
- pipeline → pipeline ; downstream → a jusante/adiante ; upstream → a montante
- wavelet(s) → wavelets ; guided filter → filtro guiado ; "guided laplacians" → manter
- harmonic transposition → transposição harmônica
- scene-referred → referente à cena (scene-referred) ; display-referred → referente à tela
- gamut → gamut ; color space → espaço de cor ; color management → gerenciamento de cores
- tile → ladrilho ; shard → fragmento ; thumbnail → miniatura ; mipmap → mipmap
- lighttable → mesa de luz ; darkroom → sala escura (app UI)
- module → módulo ; blending → mesclagem ; mask → máscara
- feature → recurso ; release → versão ; changelog → registro de alterações
- maintainer → mantenedor ; contributor → colaborador/colaboradora
- pull request → pull request ; issue → issue ; commit → commit ; ground truth → verdade de referência (ground truth)
