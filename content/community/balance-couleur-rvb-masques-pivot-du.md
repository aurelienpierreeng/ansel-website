---
title: "Balance couleur RVB - Masques - Pivot du gris du contraste"
date: 2024-01-19
slug: "balance-couleur-rvb-masques-pivot-du"
tags:
  - Community archive
forum_author: "Dom"
forum_category: "Feedback & use cases"
forum_url: "https://community.ansel.photos/view-discussion/balance-couleur-rvb-masques-pivot-du"
wayback_url: "https://web.archive.org/web/20241109184258/https://community.ansel.photos/view-discussion/balance-couleur-rvb-masques-pivot-du"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/balance-couleur-rvb-masques-pivot-du`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20241109184258/https://community.ansel.photos/view-discussion/balance-couleur-rvb-masques-pivot-du).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Dom** on 2024-01-19.*

Bonjour,

Que représente la valeur en % du pivot du gris du contraste ?

L'image présentée avec le fichier joint est un panorama HDR.

Workflow utilisé : Dématriçage des RAW avec Balance des blancs, correction objectifs, dématriçage

sans calibration couleur, filmique, balance couleur

Création d'un panorama par exposition (Autopano)

Panorama HDR 32 bits avec Photomatix

Traitement sans Balance des blancs, correction objectifs, dématriçage

avec exposition, calibration couleur, filmique, balance couleur

Avec l'exposition à 0 EV, le pivot du gris du contraste indique 100 %. 100 % de quoi ?

  

Cdlt

## Replies

**Aurélien Pierre** — 2024-01-19

L'algo de contraste ajoute de la luminosité pour toutes les valeurs RGB supérieures à la valeur du pivot, et en retire pour toutes les valeurs RGB inférieures à la valeur du pivot (en supposant un réglage de contraste positif, sinon c'est le contraire). La valeur du pivot est donc inchangée, et les tonalités pivotent autour d'elles.

En respectant le workflow relatif à la scène, la première étape est la correction générale de l'exposition pour la luminosité générale. Cette correction peut s'interpréter comme un ancrage de ce qu'on considère « gris moyen » dans la scène à la valeur RGB typique de 18 % (dans un espace RGB linéaire). La valeur 18 % nous sert donc de pivot de contraste, autant pour le module balance couleur que pour filmique plus tard dans le pipeline.

La valeur 18 % fait référence au blanc diffus SDR (100 Cd/m^2 dans les conditions d'épreuvage standard), autrement dit une feuille de papier blanc qui serait posée à côté du sujet dans la scène. Un ajustement "techniquement parfait" (idéalisé, ce qui ne veut pas dire que c'est une règle ou une consigne) de l'exposition globale ancrerait le blanc diffus à 100 % (soit des valeurs RGB à 1 dans un pipeline en virgule flottante) en même temps que le gris moyen à 18 %. Les valeurs considérées HDR (plus lumineuses que le blanc diffus) seraient alors supérieures à 1 ou 100 % (et comprimées plus tard par filmique pour être imprimables et affichables).

La pipette de sélection auto du pivot de contraste calcule la moyenne des valeurs RGB sur la zone sélectionnée, qui devrait arriver proche de 20 % si l'exposition a été bien réglée et si la zone ne sélectionne que des zones réfléchissantes (pas de source de lumière, de miroir, et le ciel est un cas bizarre assimilable à une source de lumière secondaire… utiliser son jugement).

