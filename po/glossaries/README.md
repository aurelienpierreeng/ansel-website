# Translation glossaries

Per-language style guides and terminology for translating the site content in `po/content.<lang>.po`.
One file per language: `glossary.<lang>.md` (fr, de, es, it, nl, pl, pt_br).

Each glossary defines:
- **Fidelity rules** — what must be preserved byte-for-byte when translating a `.po` msgstr:
  LaTeX/math, `code spans`, URLs and `#anchors`, footnote markers/ids, markdown structure,
  Hugo `{{< >}}` shortcodes, HTML, numbers/units, brand/camera names, bibliographic citations.
- **Address & typography** — formal vs. informal address and quotation marks for that language
  (e.g. fr «…» vous, de „…" Sie, es "…" tú, it «…» tu, pt_br "…" você).
- **Terminology** — the canonical translation of recurring photo/darktable terms (raw, demosaic,
  highlights, white balance, denoiser, lighttable, module, gamut, …) so wording stays consistent
  across articles and across successive translation passes.

**Source of truth for UI terms:** the Ansel application's own translations (`po/<lang>.po` in the
ansel app repo). Terms marked "(app UI)" were aligned to what the application shows, so the website
and the program agree (e.g. de thumbnail → *Vorschaubild*, nl highlights → *hooglichten*, es/pt_br
demosaic → *interpolación/interpolação cromática*, pt_br highlights → *realces*). When in doubt,
check the app `.po` and prefer its wording.

Feed the relevant glossary to whoever (human or AI) updates a language, so new strings match the
terminology already in the `.po`. Only human-readable prose is translated; code/math/link targets
stay verbatim. The translated `content/**/*.<lang>.md` files are generated from the `.po` by po4a
at build time and are not tracked in git.
