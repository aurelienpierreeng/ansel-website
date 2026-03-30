#!/usr/bin/env bash
# Requires po4a version 0.58 or higher.

# Resolve the real repository root once, then expose it through a temporary
# symlink without spaces for po4a. po4a internally shells out to diff when
# updating .pot/.po files, and that path handling breaks in this repo because
# the checkout lives under "Sites web".
PROJECT_ROOT="$(cd "$(dirname "$0")/.."; pwd -P)"
PO4A_WORKDIR="$PROJECT_ROOT"
PO4A_TMPDIR=""
PO4A_RUN_CONF="po/po4a.conf"

if [[ "$PROJECT_ROOT" == *" "* ]]; then
    PO4A_TMPDIR="$(mktemp -d /tmp/ansel-po4a.XXXXXX)"
    ln -s "$PROJECT_ROOT" "$PO4A_TMPDIR/repo"
    PO4A_WORKDIR="$PO4A_TMPDIR/repo"
    trap 'rm -rf "$PO4A_TMPDIR"' EXIT
    PO4A_RUN_CONF="$PO4A_TMPDIR/po4a.conf"
fi

cd "$PO4A_WORKDIR"

set -e

# Is po4a installed?
if ! which po4a; then
    echo "ERROR: Install po4a from your package manager."
    exit 1
fi

# Aggregate available .po files
for lang in `find po -name '*.po' | cut -d . -f 2 | sort -u`; do
    languages="$languages $lang"
done

# Create a blank conf file
po4a_conf="po/po4a.conf"
touch $po4a_conf
> $po4a_conf

# Populate languages with what we found in po/ folder
echo "[po4a_langs] $languages" >> $po4a_conf
echo "[po4a_paths] po/content.pot \$lang:po/content.\$lang.po" >> $po4a_conf

# Parsing options
# opt:"--option neverwrap" and opt:"--option nobullets" ensure Markdown bullet lists don't get separated by an extra newline that would break them
cat >> $po4a_conf <<EOF

[options] opt:"--addendum-charset=UTF-8" opt:"--localized-charset=UTF-8" opt:"--master-charset=UTF-8" opt:"--msgmerge-opt='--no-wrap'" opt:"--porefs=full" opt:"--wrap-po=newlines" opt:"--master-language=en_US"

[po4a_alias:markdown] text opt:"--option markdown" opt:"--option yfm_keys=title,thumbnail,tags,aliases"  opt:"--addendum-charset=UTF-8" opt:"--localized-charset=UTF-8" opt:"--master-charset=UTF-8" opt:"--option neverwrap" opt:"--option nobullets"

EOF

for f in  $(find content -type f -name '*.md'); do

    # Enqueue the translations only for Git-tracked files.
    # When building translations, the .LANG.md files are added to the content/ folder.
    # Hugo could manage translations using content/LANG/ subfolders, but that would prevent
    # sharing untranslated image assets between languages as of Hugo 0.146
    # (aka duplicate images and bloat the website for no reason - remember Github Pages limit storage to 1 GB).
    # If user generated the translation files and forgot to remove them before running this script,
    # content/ has the English original .md and generated .LANG.md translations.
    # We obviously don't wont to re-add the translations to the translatable content...

    filename=$(basename $f .md)

    # Add only Git-tracked, non-translated, .md files as translation source,
    # assuming auto-generated translations will never be commited to Git.
    # That is: we exclude files like filename.LANG.md
    if [ "${f##*.*.}" != "md" ] && [ "$(git ls-files $f)" = "$f" ]; then
        line="[type: markdown] $f"
        for lang in $languages; do
            translated="$(dirname $f)/$filename.$lang.md"

            # po4a will only create translations that are not already tracked by Git
            if [ "$(git ls-files $translated)" != "$translated" ]; then
                line="$line $lang:$translated"

                if [ "$(basename "$f")" != "_index.md" ]; then
                    # Create the footer addendum containing contributors for that lang for that file
                    footer="po/footers/${f//\//.}.$lang.add"
                    ./tools/build_page_contributors.sh "$f" "$footer" "po/content.$lang.po"
                    if test -f "$footer"; then
                        line="$line add_$lang:$footer"
                    fi
                fi
            fi
        done

        if [ "$line" != "[type: markdown] $f" ]; then
          echo $line >> $po4a_conf
        fi
    fi

done

# Update .pot and .po content with fresh .md files
if [ "$PO4A_RUN_CONF" != "$po4a_conf" ]; then
    PO4A_WORKDIR="$PO4A_WORKDIR" perl -pe '
        s{(^\[po4a_paths\]\s+)(po/\S+)}{$1 . $ENV{PO4A_WORKDIR} . "/" . $2}e;
        s{(^\[type:\s+\w+\]\s+)(content/\S+|po/\S+)}{$1 . $ENV{PO4A_WORKDIR} . "/" . $2}e;
        s{((?:\$lang|[a-z_]+|add_[a-z_]+):)(content/\S+|po/\S+)}{$1 . $ENV{PO4A_WORKDIR} . "/" . $2}ge;
    ' "$po4a_conf" > "$PO4A_RUN_CONF"
fi

po4a --verbose --previous --no-translations --rm-translations "$PO4A_RUN_CONF"

if [ "$PO4A_RUN_CONF" != "$po4a_conf" ]; then
    for file in po/content.pot po/content.*.po; do
        sed -i "s#${PO4A_WORKDIR}/##g" "$file"
    done
fi
