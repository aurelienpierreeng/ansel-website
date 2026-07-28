---
title: "Support Fujifilm X-M5"
date: 2025-01-05
slug: "support-fujifilm-x-m5"
tags:
  - Community archive
forum_author: "nyv3s"
forum_category: "Developers talk"
forum_url: "https://community.ansel.photos/view-discussion/support-fujifilm-x-m5"
wayback_url: "https://web.archive.org/web/20250120201520/https://community.ansel.photos/view-discussion/support-fujifilm-x-m5"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/support-fujifilm-x-m5`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250120201520/https://community.ansel.photos/view-discussion/support-fujifilm-x-m5).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **nyv3s** on 2025-01-05.*

Bonjour,

J'ai fait l'acquisition du fujifilm X-M5, et j'ai un message d'erreur lors de l'ouverture des fichiers raw.

J'ai compilé Ansel sur Manjaro (6.6.65-1-MANJARO).

``` ql-syntax
[image I/O] image `IMAGE.RAF` from camera `X-M5` of maker `FUJIFILM` loaded with Rawspeed
RawSpeed:Unable to find camera in database: 'FUJIFILM' 'X-M5' ''
Please consider providing samples on <https://raw.pixls.us/>, thanks!
[rawspeed] Unsupported camera model for XM5A5473.RAF21.685869 [sql] /var/tmp/pamac-build/ansel-git/src/ansel/src/common/image_cache.c:253, function dt_image_cache_write_release(): prepare "UPDATE main.images SET width = ?1, height = ?2, filename = ?3, maker = ?4, model = ?5,   lens = ?6, exposure = ?7, aperture = ?8, iso = ?9, focal_length = ?10,   focus_distance = ?11, film_id = ?12, datetime_taken = ?13, flags = ?14,   crop = ?15, orientation = ?16, raw_parameters = ?17, group_id = ?18,   longitude = ?19, latitude = ?20, altitude = ?21, color_matrix = ?22,   colorspace = ?23, raw_black = ?24, raw_maximum = ?25,   aspect_ratio = ROUND(?26,1), exposure_bias = ?27,   import_timestamp = ?28, change_timestamp = ?29, export_timestamp = ?30,   print_timestamp = ?31, output_width = ?32, output_height = ?33 WHERE id = ?34"
```

Ce qui est bizarre, c'est que dans la librairie rawspeed (fichier data/cameras.xml), j'ai bien le X-M5.

``` ql-syntax
    <Camera make="FUJIFILM" model="X-M5">
        <ID make="Fujifilm" model="X-M5">Fujifilm X-M5</ID>
        <CFA2 width="6" height="6">
            <ColorRow y="0">GGRGGB</ColorRow>
            <ColorRow y="1">GGBGGR</ColorRow>
            <ColorRow y="2">BRGRBG</ColorRow>
            <ColorRow y="3">GGBGGR</ColorRow>
            <ColorRow y="4">GGRGGB</ColorRow>
            <ColorRow y="5">RBGBRG</ColorRow>
        </CFA2>
        <Sensor black="1022" white="16383"/>
        <ColorMatrices>
            <ColorMatrix planes="3">
                <ColorMatrixRow plane="0">12836 -5909 -1032</ColorMatrixRow>
                <ColorMatrixRow plane="1">-3087 11132 2236</ColorMatrixRow>
                <ColorMatrixRow plane="2">-35 872 5330</ColorMatrixRow>
            </ColorMatrix>
        </ColorMatrices>
    </Camera>
    <Camera make="FUJIFILM" model="X-M5" mode="compressed">
        <ID make="Fujifilm" model="X-M5">Fujifilm X-M5</ID>
        <CFA2 width="6" height="6">
            <ColorRow y="0">GGRGGB</ColorRow>
            <ColorRow y="1">GGBGGR</ColorRow>
            <ColorRow y="2">BRGRBG</ColorRow>
            <ColorRow y="3">GGBGGR</ColorRow>
            <ColorRow y="4">GGRGGB</ColorRow>
            <ColorRow y="5">RBGBRG</ColorRow>
        </CFA2>
        <Sensor black="1022" white="16383"/>
        <ColorMatrices>
            <ColorMatrix planes="3">
                <ColorMatrixRow plane="0">12836 -5909 -1032</ColorMatrixRow>
                <ColorMatrixRow plane="1">-3087 11132 2236</ColorMatrixRow>
                <ColorMatrixRow plane="2">-35 872 5330</ColorMatrixRow>
            </ColorMatrix>
        </ColorMatrices>
    </Camera>
```

  Merci d'avance pour votre aide.

## Replies

**Aurélien Pierre** — 2025-01-05

La version Rawspeed utilisée à la compilation est stockée dans /src/external/rawspeed. La commande suivante met à jour le sous-module (ce qui risque de casser le code existant d'Ansel et de requérir des corrections si l'API de Rawspeed a changé) :

``` ql-syntax
git submodule update --remote
```

Ansel utilise la branche stable du projet Rawspeed, pour des raisons évidentes. Après mis à jour du dépôt, le X-M5 n'est pas dans /src/external/rawspeed/data/cameras.xml﻿ à ce jour. De toute évidence, le fichier data/cameras.xml ci-dessus provient de la branche instable de Rawspeed.

