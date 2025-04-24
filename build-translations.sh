#!/bin/bash

# Get the documentation module
hugo mod get -u

# Write it to disk locally (=vendor)
hugo mod vendor

# Auto-gen doc translations from module disk cache
./_vendor/github.com/aurelienpierreeng/ansel-doc/tools/generate-translations.sh --no-update

# Auto-gen website translations
./tools/generate-translations.sh --no-update
