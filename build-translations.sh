#!/bin/bash

# Get the documentation module
hugo mod get -u

# Write it to disk locally (=vendor)
hugo mod vendor

# Auto-gen doc translations from module disk cache
sh _vendor/github.com/aurelienpierreeng/ansel-doc/tools/generate-translations.sh --no-update

# Auto-gen website translations
sh tools/generate-translations.sh --no-update
