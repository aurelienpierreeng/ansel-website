#!/bin/bash

# Get the documentation module
hugo mod get -u

# Write it to disk locally (=vendor)
hugo mod vendor

# Auto-gen doc translations from module disk cache
chmod 700 _vendor/github.com/aurelienpierreeng/ansel-doc/tools/build-translations.sh
./_vendor/github.com/aurelienpierreeng/ansel-doc/tools/build-translations.sh --add

# Auto-gen website translations
chmod 700 tools/build-translations.sh
./tools/build-translations.sh --add
