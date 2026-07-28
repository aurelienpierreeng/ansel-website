---
title: "Diffusion ou Netteté - Fonctionnement"
date: 2023-07-29
slug: "diffusion-ou-netteté-fonctionnement"
tags:
  - Community archive
forum_author: "Balistic"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/diffusion-ou-netteté-fonctionnement"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/diffusion-ou-netteté-fonctionnement`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Balistic** on 2023-07-29.*

Bonjour,

Questions vis-à-vis du module Diffusion et Netteté. J'ai regardé la vidéo d'@Aurélien Pierre à ce sujet. Il reste quelques points que j'ai mal compris :

- Dans la vidéo est expliqué que le contraste local est représenté par dy/dx. On peut améliorer la netteté *perçue* en augmentant le dy, ou améliorer la netteté *réelle* en réduisant le dx. Plus tard dans la vidéo, le préset *Contraste local rapide* est présenté comme augmentant le dy. En revanche, je n'ai pas réussi à comprendre si l'autre préset *Contraste local* joue lui aussi sur le dy ou sur le dx. **Quels sont les paramètres qui permettent de différencier si l'on veut jouer sur le dy ou le dx ? Est-ce que ce sont les ordres des vitesses ? (par exemple ordre 3 qui jouerait sur le dy et ordre 4 qui jouerait sur le dx ?)**

  

- D'après la doc : on a d'une part :

Ordre 1 = basses fréquences selon la direction basse fréquences.

Ordre 2 = basses fréquences selon gradients hautes fréquences.

Ordre 3 = hautes fréquences selon la direction des basses fréquences.

Ordre 4 = hautes fréquences selon la direction des hautes fréquences.

**Comment sont déterminées ces hautes et basses fréquences ?** S'agit-il des détails **Central radius - Radius span** pour les hautes fréquences et **Central radius + Radius span** pour les basses fréquences ?

La même doc indique ensuite qu'ordre 1 = gradients, ordre 2 = laplacien, ordre 3 = gradient du laplacien et ordre 4 = laplacien du laplacien.

Cela signifierait que ordre 2 = dérivée de l'ordre 1 ; ordre 3 = dérivée seconde de l'ordre 1 ; ordre 4 = dérivée troisième de l'ordre 1 ? **Ce qui signifierait que les hautes fréquences sont en fait tirées des dérivées des basses fréquences ?﻿**

  

- Pour finir, **est-ce que le nb d'itérations et la vitesses sont interchangeables ?** C'est-à-dire, tous autres paramètres fixés, est-ce qu'avoir 20 itérations à vitesse 25% donne le même résultat qu'en avoir 5 itérations à vitesse 100% ? (j'ai fait quelques essais, mais je n'ai pas été capable de noter une différence significative).

  

Merci d'avance

## Replies

**Aurélien Pierre** — 2023-07-29

> Quels sont les paramètres qui permettent de différencier si l'on veut jouer sur le dy ou le dx ? Est-ce que ce sont les ordres des vitesses ? (par exemple ordre 3 qui jouerait sur le dy et ordre 4 qui jouerait sur le dx ?)

Aucun. Le module travaille sur le rapport des 2, soit dy/dx, de manière non différenciée (parce que ce n'est pas mathématiquement différentiable dans l'image). C'est par une succession d'effets secondaires de l'ensemble les réglages qu'on voit à la fin si on a affiné la transition entre les éléments (et réduit le dx) à dy grossièrement constant, ou au contraire augmenté le dy (en réduisant généralement le dx en même temps).

L'explication que je donne dans la vidéo est une explication de principe. À la louche, pour affecter le dx sans trop modifier le dy, il faut opérer sur des détails à petite échelle (central radius à 0 et radius span entre 2 et ~12 px max). Dès qu'on augmente le span pour aller chercher des détails plus larges, on affecte dy de manière plus marquée.

> Comment sont déterminées ces hautes et basses fréquences ? 

Il s'agit d'une décomposition en ondelettes. À chaque étape n, on applique un flou proche d'un flou gaussien de rayon 2^n pixels. C'est notre couche basse fréquence pour l'étape n. Puis on calcule la différence entre cette couche basse fréquence et l'image d'origine (pour la première étape), ou entre cette couche basse fréquence et la couche basse fréquence de l'étape précédente, et ça nous donne les hautes fréquences pour cette étape. On applique autant d'étapes que nécessaire pour que la dernière couche corresponde à un rayon central radius + radius span, tels que définis par l'utilisateur.

> Cela signifierait que ordre 2 = dérivée de l'ordre 1 ; ordre 3 = dérivée seconde de l'ordre 1 ; ordre 4 = dérivée troisième de l'ordre 1 ? Ce qui signifierait que les hautes fréquences sont en fait tirées des dérivées des basses fréquences ?﻿

À l'ordre 1 et 2, on résout l'équation différentielle de diffusion laplacien(basses fréquences) = 0. Le laplacien est normalement isotrope et orienté dans les directions principales du maillage différentiel (horizontal/vertical), ce qui suppose un maillage "infiniment petit". Ici, le laplacien est généralisé pour travailler dans une direction arbitraire qui suit la direction du gradient (autrement dit, la direction de la pente la plus raide), afin de tenir compte des limites numériques posées par la discrétisation d'un champ de lumière en pixels. À l'ordre 1, on échantillonne la direction du gradient sur la couche basse fréquence, alors qu'à l'ordre 2, on échantillonne sur la couche haute fréquence. À l'ordre 3 et 4, on résout l'équation différentielle de diffusion laplacien(hautes fréquences) = 0. À nouveau, l'ordre 3 échantillonne le gradient sur la couche basses fréquences, et l'ordre 4 sur la couche hautes fréquences.

À noter que la différence entre l'image source et son flou gaussien (donc le calque hautes fréquences) est un approximation numérique du laplacien (impliquant des dérivées secondes), donc laplacien(hautes fréquences) est un bi-laplacien, donc un ordre 4.

> Pour finir, est-ce que le nb d'itérations et la vitesses sont interchangeables ?

Oui pour un petit nombre d'itérations et une faible vitesse. Mais quand les réglages deviennent plus drastiques, augmenter les itérations et réduire la vitesse limite la dégénérescence de la solution et d'autres artefacts numériques caractéristiques des méthodes de reconstruction inverses (dépassements, oscillations, etc.).

---

**Balistic** — 2023-07-30

Ok merci beaucoup

