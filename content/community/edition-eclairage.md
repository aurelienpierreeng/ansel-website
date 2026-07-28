---
title: "Edition  - Eclairage"
date: 2024-08-07
slug: "edition-eclairage"
tags:
  - Community archive
forum_author: "Dom"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/edition-eclairage"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/edition-eclairage`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Dom** on 2024-08-07.*

Bonjour,

[https://ansel.photos/en/resources/troubleshooting-color/](https://ansel.photos/en/resources/troubleshooting-color/)

Aurélien à écrit :

> Vous ne devez jamais éditer dans le noir ou dans une pièce sombre (même si cela rend l'écran plus lisible – c'est un piège). Pour le montage de nuit, essayez de trouver des ampoules D65 de haute qualité (ou, meilleure option suivante : D55 – c'est plus disponible et courant) ayant un indice de rendu des couleurs (IRC) d'au moins 92, idéalement supérieur à 95 (si vous en trouvez plus de 98, c'est probablement une arnaque – de toute façon, le max théorique est de 100). Je ne recommande pas le montage sous un éclairage entièrement artificiel car la lumière naturelle a un CRI intégré de 100 (puisque c'est en fait la référence pour tous les CRI). Éloignez-vous des ampoules fluorescentes à économie d'énergie, elles ont un IRC épouvantable et ont besoin d'un temps de chauffage variable pour atteindre leur plein potentiel (ce qui n'est pas grand-chose).

Une lampe de bureau peut-elle le faire ? La position de l'éclairage est-elle importante ? Son intensité ?

Qqs pistes :

[https://www.guide-gestion-des-couleurs.com/test-lampe-ilford-ilfolux.html](https://www.guide-gestion-des-couleurs.com/test-lampe-ilford-ilfolux.html)

https://www.amazon.ca/-/fr/lumineuse-rétroéclairage-éblouissement-électronique-dordinateur/dp/B08SC71QR1?th=1

[https://www.ledaqua.fr/Barre-led-haute-performance-lumiere-du-jour-6500-kelvin-p-525-c-2.html](https://www.ledaqua.fr/Barre-led-haute-performance-lumiere-du-jour-6500-kelvin-p-525-c-2.html)

https://www.truelight.fr/ampoules-fluocompactes-a-vis-e27/23w-ampoule-lumiere-du-jour-true-light-a-vis-e27.html

https://www.truelight.fr/ampoules-et-tubes-led/true-light-led-gu10-65-watt-irc98.html

  

J'édite sur un écran Asus ProArt PA248QV, convient-il de le calibrer ?

[https://www.guide-gestion-des-couleurs.com/test-ecran-asus-pa248qv.html](https://www.guide-gestion-des-couleurs.com/test-ecran-asus-pa248qv.html)

Cordialement

## Replies

**Aurélien Pierre** — 2024-08-13

> Une lampe de bureau peut-elle le faire ? La position de l'éclairage est-elle importante ? Son intensité ?

Lampe de bureau ou lampe de n'importe quoi, c'est surtout la nature de l'ampoule utilisée qui est importante :

1.  les lampes de bureau utilisent traditionnellement des ampoules halogènes, autour de 4500 K, donc trop oranges pour nous,
2.  les lampes de bureau utilisent traditionnellement des ampoules spot, qui vont créer un éclairage localement dur et donc un fort gradient de luminance sur le bureau et le mur. Or l'idée générale est d'éviter au maximum les éléments contrastants dans l'environnement visuel.

L'objectif est d'obtenir un fond (mur et bureau) le plus neutre possible, c'est à dire (idéalement) 6500 K et uniformément gris, sans reflets ni gradients. Donc, effectivement, privilégier les barres de LED plutôt que les spots, utiliser des diffuseurs (non teintés), etc. sont des pré-requis. Tout cela est le cas idéal, dans la pratique, on fait comme on peut en fonction du budget et des conditions réelles.

> J'édite sur un écran Asus ProArt PA248QV, convient-il de le calibrer ?

Les tests d'Arnaud Frich semblent indiquer qu'il n'est pas critique de calibrer cet écran, étant données ses performances natives. Cependant, dans une production industrielle, on a toujours de la variabilité sur la qualité des produits, et le fait qu'un échantillon tiré au hasard passe le test ne garantit en rien que tous les échantillons le passeront. Moi je réalise toujours au moins une caractérisation, pour mesurer si la température du point blanc natif et le delta E maximum sont dans les limites tolérables.

De plus, à mesure que l'écran va vieillir, il peut devenir crucial de le calibrer puisque le vieillissement s'accompagne d'une dérive.

