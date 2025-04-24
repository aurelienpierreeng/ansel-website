#!/bin/bash

# Adapted from https://gitlab.com/fdroid/fdroid-website/-/raw/master/tools/i18n.sh
# Requires po4a version 0.58 or higher.

#go to project root
PROJECT_ROOT="$(cd `dirname $0`/..; pwd)"
cd "$PROJECT_ROOT"

set -e

# Is po4a installed?
if ! which po4a; then
    echo "ERROR: Install po4a from your package manager."
    exit 1
fi

# Is the script argument correct
if [ "$1" = "--no-update" ]; then
    echo "Generating the translated files."
elif [ "$1" = "--no-translations" ]; then
    echo "Generating the POT and PO files."
elif [ "$1" = "--rm-translations" ]; then
    echo "Removing the translated files."
else
    echo "The argument to this script must be one of '--no-update', '--no-translations', or '--rm-translations'."
    exit 1
fi

for lang in `find po -name '*.po' | cut -d . -f 2 | sort -u`
do
   languages="$languages $lang"
done

# Create a temporary po4a config file.
for section in content; do
    po4a_conf=$(mktemp)
    # po4a_conf=po/po_config
    echo "[po4a_langs] $languages" > $po4a_conf
    echo "[po4a_paths] po/${section}.pot \$lang:po/${section}.\$lang.po" >> $po4a_conf
    cat >> $po4a_conf <<EOF

[options] opt:"--addendum-charset=UTF-8" opt:"--localized-charset=UTF-8" opt:"--master-charset=UTF-8" opt:"--msgmerge-opt='--no-wrap'" opt:"--porefs=file" opt:"--wrap-po=newlines" opt:"--master-language=en_US"

[po4a_alias:markdown] text opt:"--option markdown" opt:"--option yfm_keys=title" opt:"--addendum-charset=UTF-8" opt:"--localized-charset=UTF-8" opt:"--master-charset=UTF-8" opt:"--option neverwrap"

EOF
    # for f in $section/*.md; do
    for f in $(find content -type f -name '*.md'); do
        filename=$(basename $f .md)
        # Add only Git-tracked, non-French, .md files as translation source,
        # assuming auto-generated translations will never be commited to Git.
        if [[ $filename != *.fr ]] && [ "$(git ls-files $f)" = "$f" ]; then

            # Because some files are already manually translated in .fr.md, we need
            # to manually unroll which translations will be necessary to discard fr where relevant.
            line="[type: markdown] $f"
            for lang in $languages; do
                translated="$(dirname $f)/$filename.$lang.md"

                # po4a will only create translations that are not already tracked by Git
                if [ "$(git ls-files $translated)" != "$translated" ]; then
	                line="$line $lang:$translated"
                fi
            done
            echo $line >> $po4a_conf
        fi
    done
done

po4a $1 --verbose $po4a_conf --keep 0
