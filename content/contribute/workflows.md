---
title: Automated workflows
date: 2025-05-01
---

Because Ansel is mostly a one-person operation, everything that could be automated was automated. This page keeps track of everything that should be maintained in the future, and where.

## Software

### Nightly builds

Nightly builds prepare a compiled and packaged version of the software, every night at 6am UTC, for:

- [Linux](https://github.com/aurelienpierreeng/ansel/blob/master/.github/workflows/lin-nightly.yml),
- [Windows](https://github.com/aurelienpierreeng/ansel/blob/master/.github/workflows/win-nightly.yml),
- MacOS is currently disabled.

The newest binary files are automatically added to the [pre-release](https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0) assets, are posted on a [Matrix channel](https://matrix.to/#/#ansel-builds:matrix.org) so users can subscribe to updates, and can be downloaded through (constantly up-to-date) permalinks at:

- <https://nightly.link/aurelienpierreeng/ansel/workflows/lin-nightly/master/ansel.stable.AppImage.zip> for the Linux AppImage,
- <https://nightly.link/aurelienpierreeng/ansel/workflows/win-nightly/master/ansel.stable.win64.zip> for the Windows AppImage.

### Developer documentation

The dev docs are [automatically built](https://github.com/aurelienpierreeng/ansel/blob/master/.github/workflows/docs.yml) from the source code with Doxygen, every Sunday at 00:00 UTC, then uploaded to <https://dev.ansel.photos>, which is hosted on Github Pages attached to the Ansel (software) repository.

### Commits and issues

Github new commits and issues are [automatically posted](https://github.com/aurelienpierreeng/ansel/blob/master/.github/workflows/matrix.yml) to a [Matrix channel](https://matrix.to/#/#ansel-dev:matrix.org) for updates.

## Website

The Hugo static website is [automatically built](https://github.com/aurelienpierreeng/ansel-website/blob/master/.github/workflows/hugo.yml) on every new commit to the source code and ever Sunday at 00:00 UTC. This auto-update is intended for [camera support](https://github.com/aurelienpierreeng/ansel-website/blob/master/themes/ansel/layouts/shortcodes/rawspeed.html) which re-parses Libraw, Rawspeed and Ansel source code straight from Github, and dynamically generates the camera support table. It is uploaded to <https://ansel.photos>, which is hosted on Github Pages attached te the Ansel Website repository.

## Documentation

The documentation is imported into the website as a Go/Git module ([see _website_](./website/index.md)). Every new commit to the documentation [fires a workflow dispatch](https://github.com/aurelienpierreeng/ansel-doc/blob/master/.github/workflows/hugo.yml) to the main website to rebuild and update it.

## Forum

New posts on the forum are posted through an RSS bot to the [Matrix channel](https://matrix.to/#/#ansel-dev:matrix.org) for updates.

## Chantal

The page crawler for Chantal search engine database does not yet run automated and needs manual updating.

Converting web pages to their vector representation, through the language model, will probably remain too heavy for any public server and will need to be done on a powerful private server.

## Ansel GPT

The [custom ChatGPT model for Ansel](https://chatgpt.com/g/g-680d2f861a608191a0f7549eadd40f2e-ansel-gpt) is meant to assist users who have questions on Ansel software (installation, compilation, usage) or color theory. It is trained with Ansel website, documentation, Github issues, Matrix chats, and other resources. It also uses Chantal AI JSON API as backend, from where it can tap into the database of 68.800+ imaging-related pages indexed there.

It is configured to automatically recrawl and cache, once a week, all the following resources for all languages:

- [the main website sitemap](https://ansel.photos/sitemap.xml),
- each [language-centric sitemap](https://ansel.photos/en/sitemap.xml),
- the [one-page aggregated website](https://ansel.photos/en/index.md) content for each language,
- Github RSS feed of new commits,
- Github issues,
- the main Community forum RSS feed.

Users can request to see the last update log by asking "show me the last update log" to GPT.
