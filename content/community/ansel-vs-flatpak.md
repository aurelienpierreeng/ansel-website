---
title: "Ansel vs. Flatpak"
date: 2024-01-17
slug: "ansel-vs-flatpak"
tags:
  - Community archive
forum_author: "Nicolas Kovacs"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/ansel-vs-flatpak"
wayback_url: "https://web.archive.org/web/20240330042056/https://community.ansel.photos/view-discussion/ansel-vs-flatpak"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/ansel-vs-flatpak`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240330042056/https://community.ansel.photos/view-discussion/ansel-vs-flatpak).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Nicolas Kovacs** on 2024-01-17.*

Bonjour,

J'administre (entre autres choses) le réseau 100 % Linux de notre lycée local. Tous nos postes clients tournent actuellement sous Rocky Linux 8, un clone de Red Hat Enterprise 8. Nous avons choisi cette distribution principalement pour des raisons de pérennité (10 ans de support par version).

Nous aimerions remplacer Darktable par Ansel, mais malheureusement il n'y a pas moyen de faire fonctionner l'AppImage fournie sur le site. Pour l'anecdote, cette AppImage ne fonctionne pas non plus sous Rocky Linux 9.

Nous avons cherché une version Flatpak de l'application, mais en vain. Je me permets donc de vous contacter pour suggérer de mettre à disposition une image Flatpak pour Ansel. Puisque l'application semble pointilleuse sur toute une série de prérequis et de dépendances, c'est probablement un format de distribution plus approprié. Ici, c'est ce qu'on utilise pour les "usines à gaz" avec des dépendances difficiles voire impossibles à satisfaire.

Un gentil bonjour de la garrigue gardoise,

Nicolas

## Replies

**Aurélien Pierre** — 2024-01-17

Bonjour,

je conseille d'attendre la sortie de Ansel 0.1 (première version stable) avant de remplacer Darktable en production, pour l'instant la branche master d'Ansel est encore chaotique. Pas de date de sortie prévue, cependant.

Le support de Flatpak n'est pas prévu non plus, c'est déjà une galère de maintenir l'AppImage et le Exe pour Windows, je n'ai pas le temps de supporter tous les formats, d'autant que Flatpak amène une perte de performance (liée au fait qu'un service additionnel doit tourner en tâche de fond, plus Flatpak utilise ses propres sur-couches pour les pilotes matériels, etc.) et pose des problèmes lié à l'environnement "bac à sable" (par exemple, le dossier .config est planqué à un endroit non standard).

La vraie raison pour laquelle l'AppImage ne fonctionne pas est probablement la version de Libc qui est trop ancienne sur le système, considérant que l'AppImage est compilé sur Ubuntu 22.04 avec GCC 12. Je suis coincé avec cette configuration parce que Rawspeed (la lib qui décode les formats raw) exige GCC 12 depuis peu, et GCC 12 ne fonctionne pas sur Ubuntu 20.04.

Il serait peut-être plus simple de compiler un AppImage direct sur le système Rocky Linux (sous réserve d'avoir accès à GCC 12). Après récupération du dépôt Git en local, et après installation des dépendances, il suffit de lancer le script :

``` ql-syntax
sh .ci/ci-script-appimage.sh
```

Le détail de l'installation des dépendances (sur instances Github utilisant Ubuntu 22.04 server) est également sur le dépôt : https://github.com/aurelienpierreeng/ansel/blob/master/.github/workflows/lin-nightly.yml

---

**Nicolas Kovacs** — 2024-01-18

Merci pour votre réponse prompte et précise.

Sous Rocky Linux 8, l'AppImage d'Ansel m'affiche toute une série d'erreurs liées à GLIBC non trouvé, avec des erreurs liées à 2.29 allant à 2.35. Effectivement, Rocky Linux utilise GLIBC dans la version 2.28.

La tentative avec Rocky Linux 9 a été infructueuse pour une raison similaire, puisque cette version repose sur la GLIBC 2.34. Il y a moins d'erreurs en retour, mais elles sont relatives à la GLIBC 2.35 non trouvée.

J'ai bien peur que toute tentative de compilation sur ces deux systèmes se solde par un échec, étant donné qu'elles sont extrêmement conservatrices dans leur approche et que certains composants risquent d'être trop anciens.

Par curiosité : est-ce qu'il y a une distribution / version que vous préconisez pour faire tourner Ansel ?

Un gentil bonjour de la garrigue gardoise,

Nicolas Kovacs

---

**Aurélien Pierre** — 2024-01-19

Ansel est développé sur Fedora et Suse, et abondamment testé sur Ubuntu et variantes.

Effectivement, c'est probablement une contradiction dans les termes d'essayer d'installer un logiciel même pas stable sur une distro conservatrice.

---

**Nicolas Kovacs** — 2024-01-19

De manière plus pragmatique, Darktable est une forêt de bugs et de régressions, et on nourrit l'espoir de pouvoir le remplacer par quelque chose de plus propre, même si c'est officiellement estampillé bêta ou même alpha.

---

**Aurélien Pierre** — 2024-01-19

On est bien d'accord.

