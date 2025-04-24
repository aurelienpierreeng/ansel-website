#!/bin/bash

# Get the documentation module
hugo mod get -u

# Write it to disk locally (=vendor)
hugo mod vendor

# Auto-gen doc translations from module disk cache
chmod 744 _vendor/github.com/aurelienpierreeng/ansel-doc/tools/generate-translations.sh
./_vendor/github.com/aurelienpierreeng/ansel-doc/tools/generate-translations.sh --no-update

# Auto-gen website translations
chmod 744 tools/generate-translations.sh
./tools/generate-translations.sh --no-update
