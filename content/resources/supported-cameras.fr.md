---
title: Appareils photos et formats pris en charges
date: 2025-04-22
---

Cette page liste tous les appareils photo connus et l'état de la prise en charge de leurs fichiers bruts par Ansel. Certains appareils peuvent utiliser différents formats d'encodage (12 bits, 14 bits, sRAW, compressé ou non) et rapports d'image (4:3, 16:9, 3:2). Le fait que l'un ou plus de ces formats soient pris en charge n'implique pas automatiquement que tous le soient. Des appareils photos différents peuvent partager le même capteur et la même électronique, bien que leur nom commercial soit différent : ils seront trouvés dans la colonne _aliases_.

Les profils de bruits sont utilisés par le module [_débruitage (profilé)_](../../doc/modules/processing-modules/denoise-profiled). Si votre appareil photo n'en a pas, pouvez [en générer un vous-même](https://pixls.us/articles/how-to-create-camera-noise-profiles-for-darktable/) et le soumettre, sinon des statistiques de bruit génériques seront utilisées en repli.

Ansel utilise la librairie [Rawspeed](https://darktable-org.github.io/rawspeed/) pour décoder la plupart des fichiers bruts. Des solutions de repli vers Libraw ont été introduites car Rawspeed ne prend toujours pas en charge les fichiers `.CR3` Canon (format ISOBMFF). Libraw peut être [configuré manuellement](../../doc/preferences-settings/processing/#libraw) pour toujours charger certains fichiers, par appareil photo ou par extension. Le support de Rawspeed dans Ansel est natif et complet, alors que Libraw n'est pas complètement câblé à l'application.

Légende de la prise en charge :

- <span class='badge rounded-circle text-bg-success square-badge'>✓</span> Appareil et format supportés par Rawspeed. En cas de problème, soumettre un [rapport de bug](https://github.com/darktable-org/rawspeed/issues).
- <span class='badge rounded-circle text-bg-danger square-badge'>✗</span> Appareil et format non supportés par Rawspeed et Libraw,
- <span class='badge rounded-circle text-bg-warning square-badge'>?</span> État du support inconnu parce que des échantillons bruts sont manquants. Envisagez d'envoyer des images sur <https://raw.pixls.us>
- <span class='badge rounded-circle text-bg-info square-badge'>+</span> Appareil et format supporté par le repli sur Libraw.

_Ce tableau est généré automatiquement par analyse syntaxique du code source de Rawspeed et Libraw. Aucune vérification humaine n'est effectuée._

{{< rawspeed >}}
