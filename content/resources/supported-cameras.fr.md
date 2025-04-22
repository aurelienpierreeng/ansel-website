---
title: Appareils photos et formats pris en charges
date: 2025-04-22
---

Cette page liste tous les appareils photo connus et l'état de la prise en charge de leurs fichiers bruts par Ansel. Certains appareils peuvent utiliser différents formats d'encodage (12 bits, 14 bits, sRAW, compressé ou non) et rapports d'image (4:3, 16:9, 3:2). Le fait que l'un ou plus de ces formats soient pris en charge n'implique pas automatiquement que tous le soient. Des appareils photos différents peuvent partager le même capteur et la même électronique, bien que leur nom commercial soit différent : ils seront trouvés dans la colonne _aliases_.

Ansel utilise la librairie [Rawspeed](https://darktable-org.github.io/rawspeed/) pour décoder la plupart des fichiers bruts. Des solutions de repli vers Libraw ont été introduites car Rawspeed ne prend toujours pas en charge les fichiers `.CR3` Canon (format ISOBMFF). Le support de Rawspeed dans Ansel est natif et sera meilleur que lire les images avec Libraw.

Légende de la prise en charge :

- <span class='badge rounded-circle text-bg-success square-badge'>✓</span> Appareil et format supportés par Rawspeed. En cas de problème, soumettre un [rapport de bug](https://github.com/darktable-org/rawspeed/issues).
- <span class='badge rounded-circle text-bg-danger square-badge'>✗</span> Appareil et format non supportés par Rawspeed et Libraw,
- <span class='badge rounded-circle text-bg-warning square-badge'>?</span> État du support inconnu parce que des échantillons bruts sont manquants. Envisagez d'envoyer des images sur <https://raw.pixls.us>
- <span class='badge rounded-circle text-bg-info square-badge'>+</span> Appareil et format supporté par le repli sur Libraw.

{{< rawspeed >}}
