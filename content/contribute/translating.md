---
title: Translating
date: 2024-07-15
weight: 6
---

## Update the po template file (`.pot`)

This step is optional as you may directly use the `po/ansel.pot` file provided on the repository.

You need first to build the project because the files `data/anselconfig.dtd` and `data/anselconfig.xml.in` are not properly defined for `intltool` to extract strings, so we will fetch them directly from `build/bin/conf_gen.h` and `build/bin/preferences_gen.h`. That's an ugly workaround inherited from upstream darktable.

To find out if any source file (`.c`, `.h`, `.sh`) might be missing to the list of translatable files, run :

```sh
$ cd po
$ intltool-update -m
```

This outputs some false-positives, so no need to care about files that have been there for a long time. It's only new files that will need to be added to `po/POTFILES.in`.

To update strings from the source code changes into the `.pot` file, run:

```sh
$ cd po # optional, only if you didn't run the previous command
$ intltool-update -pot
```

It will create a new `untitled.pot` file that you may rename `ansel.pot` if you like, in the `po/` folder.

## Translate the missing strings

Open the `.po` file corresponding to your language in Poedit. In Poedit interface, go to "Translation -> Update from a POT file" and select either the `po/ansel.pot` file already on the repository or the `.pot` that you optionally generated at the previous step.

Update the missing or fuzzy translations, save and send me the resulting `.po` file doing a pull request on Github or by email if you don't know how to Git.

## Notes to translators

### Policy on capitals

The darktable project made a priority to put everything in lower case, which makes the GUI difficult to read, especially for tooltips having several sentences. Capitals anchor visually the beginning of sentences and other important text, like buttons, controls etc. It's no accident if all languages converged to using them (though German has its particular way of putting them everywhere), they help legibility whether you like their aesthetic or not.

Ansel source code reuses most of darktable's labels and adds an initial capital in most places where they are needed (module headers, buttons). This is done by a bit of code using the C function `g_unichar_toupper()` from Gtk Glib, such that the original English text stays in lower case to keep compatibility with translations.

This programmatic fix works for non-accented characters, no matter the language used (default strings in English, or translations). However, it does not work for initial accented characters, which will not be capitalized. In this case, translators are asked to force their translation to use initial capitalized accented characters whenever they are grammatically correct in their language.

New labels or old labels recently changed (which would break translations anyway) will get initial capitals from now on, in the source code (English version), so this should progressively be fixed.

### Translating technical terms

Technical terms related to color theory and colorimetry need to be translated exactly from English, with extra care because these terms can exist also in common language (aka non-technical) but with a different meaning. The [International Electrotechnical Commission](https://www.electropedia.org/iev/iev.nsf/welcome) provides a search-engine where you can search for the English technical terms and get the accurate translations in different languages, including the main European ones as well as Arabian and Chinese.

### Notes aux traducteurs francophones

La traduction de darktable comporte des bizarreries incompréhensibles pour quiconque utilise un ordinateur de bureau depuis plus de 10 ans. Voici une liste rapide des erreurs à corriger:

* "set" est traduit "positionné" mais sa traduction correcte est "réglé". C'est illogique car "settings" est correctement traduit "réglages". Dans Ansel, on ne positionne que des masques (ou leurs nœuds de contrôle) dans le plan 2D. Le reste, ce sont des réglages.
* "reset" est traduit "repositionné" mais sa traduction correcte est "réinitialiser".
* En anglais, un grand nombre de verbes ont la même graphie pour leur infinitif et leur participe-passé, voire même existent comme substantif ("set", dans l'exemple ci-dessus, peut être traduit "réglé" ou "régler" ou comme "ensemble" sous sa forme substantivée). Si une action (pas encore effectuée) est requise, l'infinitif doit être utilisé en français. Si une action est déjà effectuée, c'est le participe-passé qui doit être employé. Les choses se corsent pour les substantifs car l'anglais ne requiert pas toujours de déterminant devant, il faut donc le déduire du contexte. À surveiller : "click" (cliquer ou clic), "type" (type ou entrer/taper), etc.
