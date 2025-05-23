---
title: Translating
date: 2024-07-15
weight: 6
---

Ansel uses [Gettext](https://www.gnu.org/software/gettext/) to translate all parts of the project:

- The software application (written in C),
- The website (Hugo templates and Markdown content),
- The documentation/user manual, inserted into the website as a module (Hugo templates and Markdown content too).

This ensures the same workflow can be used to translate all files, but also that some translated strings can be shared (for example, the translated GUI controls from the applications can be inserted directly into the documentation).

## Organization of translation files

The source code of the website, documentation and software all contain an immediate `po/` subfolder, containing:

- one `.pot` file that holds all the available, translatable strings in their original language (in English),
- many `.po` files matching translatable strings in their original language with their translation (in one language per file).

Translations files are all named following the convention `language-code.po`. For example:

- for German,
  - the software translation is `de.po`,
  - the website translation is `content.de.po`,
  - the documentation translation is `content.de.po`,
- for Brazilian Portuguese,
  - the software translation is `pt_BR.po`,
  - the website translation is `content.pt_br.po`,
  - the documentation translation is `content.pt_br.po`.

## Translating when you can't use CLI/Git

You will need to locate the relevant `.po` file for your language for the part of the project you want to translate:

- the software : <https://github.com/aurelienpierreeng/ansel/tree/master/po>
- the website : <https://github.com/aurelienpierreeng/ansel-website/tree/master/po>
- the documentation : <https://github.com/aurelienpierreeng/ansel-doc/tree/master/po>

1. Download this file and open it with [Poedit](https://poedit.net/),
2. Make the corrections and editions you need,
3. Add your name in a comment for the strings you translate if you want to be credited on the page :
    - Automatically-translated strings will have `TRANSLATOR ChatGPT` there, once you verify those strings, please remove this line,
    - Then add a comment containing `TRANSLATOR Your Name` on a new line. Keep other (non-ChatGPT) contributors there, if any.
4. Save the file and:
    - __Alternative 1__ _(easier for contributor, more steps for maintainer)_: drop it [on my private cloud](https://cloud.apmlt.net/s/YAdfYajPkE5nLyW),
    - __Aternative 2__ _(more steps for contributor, easier for maintainer)_: commit it with Git and open a pull request against the proper Github repository.

## Translating for power users

This will update the `.pot` file using the source code of the project. You will need to have `Git` installed, and [Hugo 0.146](https://github.com/gohugoio/hugo/releases/tag/v0.146.7) installed on your computer.

1. Clone the source code of the relevant project:
    - the software :
      ```bash
      $ git clone --depth 1 \
        https://github.com/aurelienpierreeng/ansel.git
      $ cd ansel
      ```
    - the website :
      ```bash
      $ git clone --depth 1 \
        https://github.com/aurelienpierreeng/ansel-website.git
      $ cd ansel-website
      ```
    - the documentation :
      ```bash
      $ git clone --depth 1 \
        https://github.com/aurelienpierreeng/ansel-doc.git
      $ cd ansel-doc
      ```
    Later, you will update the repository using :
    ```bash
    $ git pull
    ```
2. Update the `.pot` and all `.po` files from the source code (this step works the same for all 3 projects):
    ```bash
    $ sh tools/update-translations.sh
    ```
3. Translate the relevant `.po` file using Poedit or directly in a text editor (see [_Translating when you can't use CLI/Git_](#translating-when-you-cant-use-cligit)),
4. Test & review your translation :
    - For the software, you will need to build Ansel on your OS. Please see [the documentation](../doc/install/_index.md).
    - For the website and the documentation, you can run :
      ```bash
      sh build-modules.sh
      hugo
      ```
    Watch out for any critical error from po4a, especially for mismatching `\n` characters, and errors from Hugo, especially regarding shortcodes syntax.
5. For the website and documentation, cleanup the translated Markdown files (automatically-generated by po4a using the `.po` file) before commiting, using :
    ```bash
    sh tools/build-translations.sh --remove
    ```
6. Commit all `.pot` and `.po` files and open a pull request against the relevant Github repository. Never commit translated `.md` (Markdown) files.


## Translating images

_The following applies to the website and documentation only._

Images can be translated too, for example application screenshots. Images are stored in the `assets/` folder if they are re-used on several pages (global assets), otherwise they are stored in the same folder as the Mardown file using them (local assets). Whether global or local, the translation process is the same, only the base folder changes.

If, for example, you want to translate the `assets/screenshot.jpg` for the language `LANG` (which is the ISO code of the language, like `de`, `nl`, `pt_br`, `zn_cn`, etc.):

1. add and commit a new `assets/screenshot.LANG.jpg` image file to the documentation or website Git repository,
2. in the `content.LANG.po`, locate the entry containing the Markdown tag for the original image, which will be something like `![alt text](screenshot.jpg)`,
3. translate the Markdown tag by replacing the URL of the image, like `![translated alt text](screenshot.LANG.jpg`,
4. save and commit the `content.LANG.po` file,
5. create a pull request against Ansel website or Ansel docs repository.

## Auto-tools and helper scripts

### Init documentation translation with software one

Because the documentation and the software share the same strings for the GUI controls, you can lazily init the documentation strings from the software ones if they exactly match (including casing). This needs a Python interpeter and the `regex` package (install with `pip install -U regex`). From the source code of the documentation, you can call :

```bash
$ python tools/merge-translations.py path/to/software path/to/doc
```

### Auto-translate documentation and website with ChatGPT

ChatGPT-4o does a very fair job at translating Markdown-formatted text from English, although not in every language. You will need a private API key to store in the folder of the documentation or website in a `.chatgpt.api_key` file. Then, calls to the ChatGPT API are not free, and the minimal payment of 5 US$ will roughly get you the website fully translated into 4 languages.

The all-in-one script can be called using :

```bash
$ sh auto-translate.sh LANG
```

where `LANG` is the target language code (de, fr, pt_br, etc.). This will process the translation in batches of 90 to 120 strings to comply with ChatGPT API limitations and thresholding. This will :

- parse the original `po/content.LANG.po` file and export the batch to translate into a temporary `po/content.LANG.txt` file,
- send `po/content.LANG.txt` file to ChatGPT and get the response in `po/content.LANG.generated.txt`
- fix most common formatting inconsistencies that ChatGPT can introduce and inject the translations back into `po/content.LANG.po`,
- build translated Markdown files (following the `page.LANG.md` naming convention),
- build the website with Hugo.

If all these steps complete without error, then you are good to run the script again to process the next batch until completion. If errors are shown, you will need to fix them. We run only one batch at each call to let user the opportunity to find errors while there are not too many changes to inspect.

__Common errors__:

- nothing will be translated : check ChatGPT answer within `po/content.LANG.generated.txt`, sometimes it is unable to understand its mission. You can try again, sometimes it works on the 3rd call. But often, there is nothing to do and some languages/strings can't be translated at all.
- when building the website with Hugo, some shortcode can't be found. This is because shortcodes are declared like so : `{{</* shortcode_name */>}}`. Sometimes, ChatGPT will try to translate `shortcode_name` and the shortcode won't work again. The solution is to bring back the English name for the shortcode and its attributes,
- same with [Mermaid](https://mermaid.js.org/) graphs, ChatGPT can try to translate commands and properties that shouldn't be translated,
- original strings end with the newline character `\n` and the translated strings don't (or the other way around). The script tries to sanitize that, but some corner cases are not handled. Original strings `msgid` and their translation `msgstr` in the `.po` file should have the same number of `\n` characters at the same place,
- improperly escaped double quotes : the `msgid` and `msgstr` Gettext strings should be delimited by unescaped double quotes `"` at each extremity of the string. Any other double quote, within the Gettext string, should be escaped using `\"`.

The best way to fix errors is to open the relevant `.po` file in a text editor. If you can't find the error and solve it, you can try opening the file into Poedit, but when saving, it will usually completly erase the faulty strings without fixing them, so translation will need to be started again from scratch.

### Build translated Markdown files

For the website and documentation, [Hugo](https://gohugo.io/) handles the translations of any given page `new_page.md` using the naming convention `new_page.LANG.md`, where `LANG` is the language code. Hugo natively supports manually writing these translated files in the same folder as their original, however, here we generate them using the `.po` translation file and the program `po4a`. The `build-modules.sh` and `tools/auto-translate.sh` scripts handle this internally, but you may want to generate those file manually :

1. Update the `.pot` and `.po` files with the source code :
    ```bash
    $ sh tools/update-translations.sh
    ```
2. Create the translated `.md` files :
    ```bash
    $ sh tools/build-translations.sh --add
    ```
2. Cleanup the translated `.md` files :
    ```bash
    $ sh tools/build-translations.sh --remove
    ```

It is important to never commit the translated `.md` files with Git, as they are regenerated only from that script when building the website. This is only for repositiory hygiene, there is no technical drawback. Cleaning up the translated `.md` before committing ensures no mistakes.

## Lost in translation ?

If you have issues or questions, feel free to ask on the dedicated [Matrix translators channel](https://matrix.to/#/#ansel-translators:matrix.org).

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
