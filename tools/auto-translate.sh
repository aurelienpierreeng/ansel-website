#!/bin/bash

# Update translations from .md file, translate through ChatGPT, validate translations and build .md files, all in one.
# Call with LANG code, like `sh tools/auto-translate.sh de` from repository folder

# Refresh .pot and .po from English .md
./tools/update-translations.sh

# Auto-translate .po
python ./tools/chatgpt-translate.py $1

# Validate auto-translated .po
./tools/update-translations.sh

# Build the translated .md
./tools/build-translations.sh --add

# Check that hugo has proper syntax in translated .md
hugo
