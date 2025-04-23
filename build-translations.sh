#!/usr/bin/env bash

# Get the documentation
hugo mod get -u

# Write it locally (=vendor)
hugo mod vendor

# Auto-gen doc translations
sh _vendor/github.com/aurelienpierreeng/ansel-doc/tools/generate-translations.sh --no-update
