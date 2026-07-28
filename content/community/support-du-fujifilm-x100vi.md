---
title: "Support du Fujifilm X100VI"
date: 2024-10-19
slug: "support-du-fujifilm-x100vi"
tags:
  - Community archive
forum_author: "libresurf"
forum_category: "Developers talk"
forum_url: "https://community.ansel.photos/view-discussion/support-du-fujifilm-x100vi"
wayback_url: "https://web.archive.org/web/20250519020348/https://community.ansel.photos/view-discussion/support-du-fujifilm-x100vi"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/support-du-fujifilm-x100vi`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250519020348/https://community.ansel.photos/view-discussion/support-du-fujifilm-x100vi).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **libresurf** on 2024-10-19.*

Bonjour à tous et particulièrement aux développeurs.

Serait-il possible de rajouter le support des fichiers RAF issus des capteurs X-Trans V de Fujifilm et particulièrement celui du X100VI ?

La dernière version de *darktable* le supporte. J'ai donc recompilé les sources de *ansel* en mettant à jour le dépôt git de *rawspeed* à sa version "stable" et même "develop" dans *ansel/src/external/rawspeed* espérant obtenir le support des fichiers RAF issus du X100VI, mais cela génère des erreurs lors de la compilation.

``` ql-syntax
[...]
[123/853] Checking validity of cameras.xml
/mnt/leullier/Systeme/Packages/sources/ansel/src/external/rawspeed/data/cameras.xml validates
[130/853] Building CXX object src/CMakeFiles/lib_ansel_imageio_rawspeed.dir/common/imageio_rawspeed.cc.o
FAILED: src/CMakeFiles/lib_ansel_imageio_rawspeed.dir/common/imageio_rawspeed.cc.o  
/usr/bin/c++ -DDT_HAVE_SIGNAL_TRACE -DGDK_DISABLE_DEPRECATED -DGDK_VERSION_MIN_REQUIRED=GDK_VERSION_3_22 -DGLIB_VERSION_MAX_ALLOWED=GLIB_VERSION_MIN_REQUIRED -DGLIB_VER
SION_MIN_REQUIRED=GLIB_VERSION_2_56 -DGTK_DISABLE_DEPRECATED -DGTK_DISABLE_SINGLE_INCLUDES -DHAVE_BUILTIN_CPU_SUPPORTS=1 -DHAVE_CONFIG_H=1 -DHAVE_GMIC=1 -DHAVE_GRAPHICS
MAGICK=1 -DHAVE_HTTP_SERVER=1 -DHAVE_ICU=1 -DHAVE_ISO_CODES=1 -DHAVE_KWALLET=1 -DHAVE_LENSFUN=1 -DHAVE_LIBEXIV2_WITH_ISOBMFF=1 -DHAVE_LIBHEIF=1 -DHAVE_LIBRAW=1 -DHAVE_L
IBSECRET=1 -DHAVE_MAP=1 -DHAVE_OPENCL=1 -DHAVE_OPENEXR=1 -DHAVE_OPENJPEG=1 -DHAVE_OSMGPSMAP_110_OR_NEWER=1 -DHAVE_OSMGPSMAP_NEWER_THAN_110=1 -DHAVE_PRINT=1 -DHAVE_SQLIT
E_324_OR_NEWER=1 -DHAVE_WEBP=1 -DNATIVE_ARCH -DSQLITE_CORE -DSQLITE_ENABLE_ICU -DUSE_COLORDGTK -D_XOPEN_SOURCE=700 -D__GDK_KEYSYMS_COMPAT_H__ -I/mnt/leullier/Systeme/Pa
ckages/sources/ansel/build/src -I/mnt/leullier/Systeme/Packages/sources/ansel/src -I/mnt/leullier/Systeme/Packages/sources/ansel/build/src/external/rawspeed/src -I/mnt/
leullier/Systeme/Packages/sources/ansel/src/external/rawspeed/src/librawspeed -isystem /mnt/leullier/Systeme/Packages/sources/ansel/src/external -isystem /mnt/leullier/
Systeme/Packages/sources/ansel/src/external/OpenCL -isystem /mnt/leullier/Systeme/Packages/sources/ansel/src/external/rawspeed/src/external -isystem /usr/include/glib-2
.0 -isystem /usr/lib/x86_64-linux-gnu/glib-2.0/include -isystem /usr/include/gtk-3.0 -isystem /usr/include/pango-1.0 -isystem /usr/include/harfbuzz -isystem /usr/includ
e/freetype2 -isystem /usr/include/libpng16 -isystem /usr/include/libmount -isystem /usr/include/blkid -isystem /usr/include/fribidi -isystem /usr/include/cairo -isystem
/usr/include/pixman-1 -isystem /usr/include/gdk-pixbuf-2.0 -isystem /usr/include/gio-unix-2.0 -isystem /usr/include/atk-1.0 -isystem /usr/include/at-spi2-atk/2.0 -isys
tem /usr/include/at-spi-2.0 -isystem /usr/include/dbus-1.0 -isystem /usr/lib/x86_64-linux-gnu/dbus-1.0/include -isystem /usr/include/libxml2 -isystem /usr/include/libso
up-2.4 -isystem /usr/include/lensfun -isystem /usr/include/librsvg-2.0 -isystem /usr/include/json-glib-1.0 -isystem /usr/include/openjpeg-2.5 -isystem /usr/include/libs
ecret-1 -isystem /usr/include/GraphicsMagick -isystem /usr/include/osmgpsmap-1.0 -isystem /usr/include/colord-1 -Wall -Wformat -Wformat-security -Wshadow -Wtype-limits
-Wvla -Wno-unknown-pragmas -Wno-error=varargs -Wno-format-truncation -Wno-error=address-of-packed-member -std=c++14 -fopenmp -O3 -DNDEBUG -fPIC -fdiagnostics-color=alwa
ys -fopenmp -std=c++20 -MD -MT src/CMakeFiles/lib_ansel_imageio_rawspeed.dir/common/imageio_rawspeed.cc.o -MF src/CMakeFiles/lib_ansel_imageio_rawspeed.dir/common/image
io_rawspeed.cc.o.d -o src/CMakeFiles/lib_ansel_imageio_rawspeed.dir/common/imageio_rawspeed.cc.o -c /mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_raws
peed.cc
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc: In function ‘dt_imageio_retval_t dt_imageio_open_rawspeed(dt_image_t*, const char*, dt_mipm
ap_buffer_t*)’:
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:218:31: error: cannot convert ‘rawspeed::Optional<int>’ to ‘uint32_t’ {aka ‘unsigned int’} i
n assignment
 218 |     img->raw_white_point = r->whitePoint;
     |                            ~~~^~~~~~~~~~
     |                               |
     |                               rawspeed::Optional<int>
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:220:29: error: no match for ‘operator[]’ (operand types are ‘rawspeed::Optional<rawspeed::Ar
ray2DRef<int> >’ and ‘int’)
 220 |     if(r->blackLevelSeparate[0] == -1
     |                             ^
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:221:32: error: no match for ‘operator[]’ (operand types are ‘rawspeed::Optional<rawspeed::Ar
ray2DRef<int> >’ and ‘int’)
 221 |        || r->blackLevelSeparate[1] == -1
     |                                ^
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:222:32: error: no match for ‘operator[]’ (operand types are ‘rawspeed::Optional<rawspeed::Ar
ray2DRef<int> >’ and ‘int’)
 222 |        || r->blackLevelSeparate[2] == -1
     |                                ^
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:223:32: error: no match for ‘operator[]’ (operand types are ‘rawspeed::Optional<rawspeed::Ar
ray2DRef<int> >’ and ‘int’)
 223 |        || r->blackLevelSeparate[3] == -1)
     |                                ^
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:229:63: error: no match for ‘operator[]’ (operand types are ‘rawspeed::Optional<rawspeed::Ar
ray2DRef<int> >’ and ‘uint8_t’ {aka ‘unsigned char’})
 229 |       img->raw_black_level_separate[i] = r->blackLevelSeparate[i];
     |                                                               ^
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:402:60: error: ‘NoSamples’ is not a member of ‘rawspeed::Camera::SupportStatus’
 402 |     if(cam && cam->supportStatus == Camera::SupportStatus::NoSamples)
     |                                                            ^~~~~~~~~
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc: In function ‘dt_imageio_retval_t dt_imageio_open_rawspeed_sraw(dt_image_t*, rawspeed::RawIm
age, dt_mipmap_buffer_t*)’:
/mnt/leullier/Systeme/Packages/sources/ansel/src/common/imageio_rawspeed.cc:558:58: error: ‘NoSamples’ is not a member of ‘rawspeed::Camera::SupportStatus’
 558 |   if(cam && cam->supportStatus == Camera::SupportStatus::NoSamples)
     |                                                          ^~~~~~~~~
[135/853] Building CXX object src/external/LibRaw-cmake/CMakeFiles/raw.dir/__/LibRaw/src/decoders/crx.cpp.o
ninja: build stopped: subcommand failed.


```

Visiblement *ansel* utilise une version particulière de *RawSpeed* qui ne génère pas ces erreurs. Malheureusement pour moi, cette version ne contient pas le support du X100VI.

Ne sachant pas comment aller plus loin dans la démarche, je m'adresse donc à vous, développeurs.

Est-il compliqué d'utiliser la dernière version de *RawSpeed* avec *ansel* pour pouvoir profiter des appareils récents ?

## Replies

**libresurf** — 2024-10-20

Il y a un truc que je ne comprends pas...

Quand je regarde dans le fichier *ansel/.gitmodule* :

``` ql-syntax
[submodule "src/external/rawspeed"]
       path = src/external/rawspeed
       url = https://github.com/darktable-org/rawspeed.git
       branch = stable
```

c'est bien la branche "stable" du projet *rawspeed* qui est utilisée.

Or cette branche supporte le Fuji X100VI : voir [https://github.com/darktable-org/rawspeed/blob/stable/data/cameras.xml#L15735](https://github.com/darktable-org/rawspeed/blob/stable/data/cameras.xml#L15735)

``` ql-syntax
    <Camera make="FUJIFILM" model="X100VI">
        <ID make="Fujifilm" model="X100VI">Fujifilm X100VI</ID>
        <CFA2 width="6" height="6">
            <ColorRow y="0">GGRGGB</ColorRow>
            <ColorRow y="1">GGBGGR</ColorRow>
            <ColorRow y="2">BRGRBG</ColorRow>
            <ColorRow y="3">GGBGGR</ColorRow>
            <ColorRow y="4">GGRGGB</ColorRow>
            <ColorRow y="5">RBGBRG</ColorRow>
        </CFA2>
        <Sensor black="1023" white="16383"/>
        <ColorMatrices>
            <ColorMatrix planes="3">
                <ColorMatrixRow plane="0">11809 -5358 -1141</ColorMatrixRow>
                <ColorMatrixRow plane="1">-4248 12164 2343</ColorMatrixRow>
                <ColorMatrixRow plane="2">-514 1097 5848</ColorMatrixRow>
            </ColorMatrix>
        </ColorMatrices>
    </Camera>
    <Camera make="FUJIFILM" model="X100VI" mode="compressed">
        <ID make="Fujifilm" model="X100VI">Fujifilm X100VI</ID>
        <CFA2 width="6" height="6">
            <ColorRow y="0">GGRGGB</ColorRow>
            <ColorRow y="1">GGBGGR</ColorRow>
            <ColorRow y="2">BRGRBG</ColorRow>
            <ColorRow y="3">GGBGGR</ColorRow>
            <ColorRow y="4">GGRGGB</ColorRow>
            <ColorRow y="5">RBGBRG</ColorRow>
        </CFA2>
        <Sensor black="1023" white="16383"/>
        <ColorMatrices>
            <ColorMatrix planes="3">
                <ColorMatrixRow plane="0">11809 -5358 -1141</ColorMatrixRow>
                <ColorMatrixRow plane="1">-4248 12164 2343</ColorMatrixRow>
                <ColorMatrixRow plane="2">-514 1097 5848</ColorMatrixRow>
            </ColorMatrix>
        </ColorMatrices>
    </Camera>
```

Une fois les commandes **git submodule init** et **git submodule update** exécutées, nous devrions donc retrouver ces informations dans le fichier *ansel/src/external/rawspeed/data/cameras.xml*.

Or il n'en est rien !

``` ql-syntax
$ grep X100VI ansel/src/external/rawspeed/data/cameras.xml
$
```

La commande ne retourne rien car ne trouve pas l'occurence "X100VI" dans le fichier *cameras.xml*.

J'ai loupé un truc ? Ce n'est pas la branche "stable" de *rawspeed* qui a été récupérée ?

---

**Aurélien Pierre** — 2024-10-21

Git et configuré pour suivre la branche Rawspeed "stable" et est réglé au commit 6e0d1e8d6fffcb6b0af787b6f7ad6bd99c1bb6b2.

Il faut lancer la commande :

``` ql-syntax
git submodule update --recursive
```

pour récupérer le dernier commit (e3f16a78ebabfe5f1167d7bcc960c37515094d05). Ce commit introduit probablement un changement d'API qui rend le module Ansel responsable du décodage des photos raw incompatible. Il est donc nécessaire de modifier le code d'Ansel en conséquence, en plus de mettre à jour Rawspeed.

Bienvenue dans l'enfer des dépendances tierces.﻿

---

**Aurélien Pierre** — 2024-10-21

Je viens de mettre à jour le sous-module Rawspeed ainsi que le code qui interface la librairie dans Ansel, pour répercuter les changements d'API. Ça devrait marcher, à confirmer.

---

**libresurf** — 2024-10-21

Bonjour ﻿@Aurélien Pierre﻿ ,

Un "très... très grand... MERCI !!!" ﻿😃﻿﻿😃﻿﻿😃﻿

Ça marche effectivement très bien ! ﻿👏﻿﻿👍﻿

Crois moi, tu fais vraiment un heureux. Quel plaisir de pouvoir utiliser un logiciel de développement photo cohérent et efficace sous Linux.

Et je comprends ta difficulté à sans cesse devoir mettre à jour le code pour suivre les changements d'API dans les dépendances tierces. Merci d'avoir été si réactif ! ﻿🎩﻿

