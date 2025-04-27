#!/usr/bin/env bash
# build_page_contributors.sh  <master_doc>  <addendum_path>  <po_files...>
#
# Example:
#   ./build_page_contributors.sh docs/about.adoc footers/about.add po/fr.po po/es.po po/de.po
#
# For the *same* source page (about.adoc in this example) you typically have one
# PO file per language.  This helper gathers every
#   "# TRANSLATOR Name <mail>"
# comment across all those POs, deduplicates the names and writes a single
# addendum that po4a can splice into **every** translated output.
#
# ────────────────────────────────────────────────────────────────────────────
# Usage in a Makefile (sketch):
#
#   PAGE   := about.adoc
#   ADDEND := footers/$(basename $(PAGE)).add
#   POFILES:= $(wildcard po/*/$(basename $(PAGE)).po)
#
#   $(ADDEND): $(POFILES) build_page_contributors.sh
#       ./build_page_contributors.sh $(PAGE) $@ $(POFILES)
#
#   [type: asciidoc]
#   docs/$(PAGE) $lang:build/$(PAGE:%.adoc=%).$lang.adoc add_$lang:?@$(ADDEND)
# ---------------------------------------------------------------------------

set -euo pipefail

master_doc=$1   # shown in the comment of the footer
addendum=$2
shift 2 || { echo "Usage: $0 <src> <addendum> <po...>" >&2; exit 1; }
po_files=("$@")

if [ ${#po_files[@]} -eq 0 ]; then
  echo "No .po files supplied" >&2
  exit 1
fi

# Ensure the directory for the addendum exists
mkdir -p "$(dirname "$addendum")"

# ────────────────────────────────────────────────────────────────────────────
# Gather all translator tags, one per array element.
# Using readarray/mapfile avoids word‑splitting on spaces inside a name.
readarray -t contributors < <(
  grep -Eho '^# TRANSLATOR .*$' "${po_files[@]}" \
    | sed 's/^# TRANSLATOR[[:space:]]*//' \
    | sort -u
)

# If no contributors found, still create an empty addendum so po4a finds the
# file, but leave it blank.
if [ ${#contributors[@]} -eq 0 ]; then
  : > "$addendum"   # touch + truncate to 0 bytes
  exit 0
fi

# ────────────────────────────────────────────────────────────────────────────
# Write the footer.  Each translator ends up on its own line (<br/>) so the
# list keeps formatting in HTML, AsciiDoc, Markdown, POD (etc.).
{
  echo "PO4A-HEADER: mode=eof"

  printf '\n\n'
  printf '<!-- Translators of %s -->\n' "$master_doc"
  printf '{{< translators >}}\n'
  printf '%s, ' "${contributors[@]}"
  printf '\n{{</ translators >}}\n'
} > "$addendum"
