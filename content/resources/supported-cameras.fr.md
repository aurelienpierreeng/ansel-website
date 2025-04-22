---
title: Appareils photos et formats pris en charges
date: 2025-04-22
---

Cette page liste tous les appareils photo connus et l'état de la prise en charge de leurs fichiers bruts par Ansel, ainsi que tous les types de fichiers supportés en entrée et en sortie.

## Appareils photos

### Introduction

Certains appareils peuvent utiliser différents formats d'encodage (12 bits, 14 bits, sRAW, compressé ou non) et rapports d'image (4:3, 16:9, 3:2). Le fait que l'un ou plus de ces formats soient pris en charge n'implique pas automatiquement que tous le soient. Des appareils photos différents peuvent partager le même capteur et la même électronique, bien que leur nom commercial soit différent : ils seront trouvés dans la colonne _alias_.

Ansel utilise la librairie [Rawspeed](https://darktable-org.github.io/rawspeed/) pour décoder la plupart des fichiers bruts. Des solutions de repli vers Libraw ont été introduites car Rawspeed ne prend toujours pas en charge les fichiers `.CR3` Canon (format ISOBMFF). Libraw peut être [configuré manuellement](../../doc/preferences-settings/processing/#libraw) pour toujours charger certains fichiers, par appareil photo ou par extension. Le support de Rawspeed dans Ansel est natif et complet, alors que Libraw n'est pas complètement câblé à l'application.

__Le projet Ansel n'a aucun contrôle sur la liste d'appareils photos et de formats de fichiers pris en charge, par Rawspeed ou par Libraw.__ L'application Ansel gère les pixels après qu'ils ont été décodés par Rawspeed ou Libraw, et les métadonnées (EXIF, IPTC, XMP) après qu'elles ont été décodés par [Exiv2](https://exiv2.org/). Les problèmes de décodage doivent être rapportés aux projets Rawspeed, Libraw ou Exiv2, suivant leur nature.

Les profils de bruits sont utilisés par le module [_débruitage (profilé)_](../../doc/modules/processing-modules/denoise-profiled). Les appareils qui n'ont pas de profil de bruit seront tout de même utilisables, seul le débruitage à hauts ISO peut être de qualité inférieure car il utilisera des statistiques de bruit génériques.

### Tableau de prise en charge

Légende de la prise en charge :

- <span class='badge rounded-circle text-bg-success square-badge'>✓</span> Appareil et format supportés par Rawspeed. En cas de problème, soumettre un [rapport de bug](https://github.com/darktable-org/rawspeed/issues).
- <span class='badge rounded-circle text-bg-danger square-badge'>✗</span> Appareil et format non supportés par Rawspeed et Libraw,
- <span class='badge rounded-circle text-bg-warning square-badge'>?</span> État du support inconnu parce que des échantillons bruts sont manquants (voir [faire prendre en charge votre appareil](#faire-prendre-en-charge-votre-appareil))
- <span class='badge rounded-circle text-bg-info square-badge'>-</span> Appareil et format supporté via le repli sur Libraw. Ce repli peut être de plus ou moins bonne qualité.

Légende de la qualité du support :

- 🏆 appareil entièrement supporté
- 🥈 appareil partiellement supporté, utilisable avec compromis mineurs,
- 🥉 appareil partiellement supporté, utilisable avec compromis,
- ⁉️ appareil partiellement supporté, utilisabilité réelle impossible à estimer,
- 💩 appareil non supporté.

_Ce tableau est généré automatiquement par analyse syntaxique du code source de Rawspeed, Libraw et Ansel. Aucune vérification humaine n'est effectuée._

{{< rawspeed >}}


### Faire prendre en charge votre appareil

Les utilisateurs incapables d'effectuer des opérations en ligne de commande dans un terminal ne seront pas capables d'aider au support de leur appareil photo. Ils doivent acheter des appareils pris en charge dès maintenant ou utiliser un logiciel commercial. Il n'existe aucune garantie qu'un nouvel appareil sera un jour pris en charge, et aucune indication sur quand il le sera. La prise en charge des appareils repose entièrement sur un travail communautaire bénévole, limité par les disponibilités de chacun.

#### Le cas des fichiers Canon CR3 / ISOBMFF

Les fichiers Canon `.CR3` appartiennent à un nouveau type de conteneurs ISOBMFF. Ceux-ci requièrent des décodeurs spécifiques, dans Rawspeed, Libraw et Exiv2. Ce décodeur spécifique n'est pas disponible dans Rawspeed, de sorte qu'un support partiel et _temporaire_ de Libraw a été introduit dans Rawspeed autour de 2020. Ansel en hérite, mais en 2025, Rawspeed ne prend toujours pas en charge `.CR3`.

Mais Ansel requiert d'avantage que Libraw pour effectivement prendre en charge `.CR3` : il a besoin de Exiv2 compilé avec le support de ISOBMFF, pour les métadonnées. La prise en charge de ISOBMFF dans Exiv2 est optionnelle pour des raisons (principalement inventées) légales & de droit d'auteur, et certaines distributions Linux (Fedora) empaquètent cette librairie sans le support ISOBMFF. Les utilisateurs qui utilisent des paquets Ansel pré-compilés provenant de telles distributions, ou qui compilent eux-mêmes en utilisant la librairie Exiv2 venant des dépôts de leur distribution, n'auront jamais une prise en charge complète des `.CR3`.

#### Aider la prise en charge

Si votre appareil photo est partiellement ou non pris en charge :

- téléversez des fichiers bruts de test sur <https://raw.pixls.us>,
- ouvrez un rapport de bug sur [le tracker Rawspeed](https://github.com/darktable-org/rawspeed/issues) et sur [le tracker Libraw](https://github.com/LibRaw/LibRaw/issues/608).

Si votre appareil photo n'a pas de profil de bruit, vous pouvez [en générer un vous-même](https://pixls.us/articles/how-to-create-camera-noise-profiles-for-darktable/) et le soumettre sur le trackeur de bugs d'Ansel.


## Codecs non bruts

Ansel prend en charge les formats de fichiers et extensions suivant (en lecture et en écriture) :

- JPEG: `.jpg`, `.jpeg` (obligatoire),
- PNG: `.png` (obligatoire),
- PFM: `.pfm` (obligatoire),
- TIFF: `.tif`, `.tiff` (obligatoire),
- OpenEXR: `.exr` (optionnel),
- WebP: `.wepb` (optionnel),
- AVIF: `.avif` (optionnel),
- HEIF: `.heif`, `.heic`, `.hif` (optionnel),
- JPEG2000: `.j2c`, `.j2k`, `.jp2`, `.jpc` (optionnel),
- Via GraphicsMagick/ImageMagick: `.gif`, `.bmp`, `.dcm`, `.jng`, `.miff`, `.mng`, `.pbm`, `.ppm`, `.pgm` (optionnel)

Notez que les formats optionnels sont activés seulement si Ansel est compilé avec les options correspondantes et si les librairies fournissant les codecs sont trouvées sur le système. Les binaires pré-compilés fournis par le projet Ansel ont toutes les options activées mais les packagers tiers peuvent en décider autrement.
