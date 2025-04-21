---
title: "Numérisation de négatifs"
date: 2025-04-18
draft: false
toc: true
tags: ['film', 'negative']
authors: ["Aurélien Pierre"]
thumbnail: "film-scan.jpg"
---

Alain Oguse a appris le tirage photographique avec [Claudine](https://www.musee-orsay.fr/fr/ressources/repertoire-artistes-personnalites/claudine-sudre-211535) et [Jean-Pierre Sudre](https://fr.wikipedia.org/wiki/Jean-Pierre_Sudre) à la fin des années 1960, et a effectué son début de carrière en photographie commerciale. Après avoir pris sa retraite, il a commencé à chercher des méthodes permettant de retrouver le grain argentique dans les numérisations de négatifs, avec la même netteté et qualité que ce qu'il obtenait en lumière quasi-ponctuelle sous l'agrandisseur, dans les années 1970.

La technique d'impression en lumière ponctuelle utilise une source de lumière très petite, qui donne une reproduction très précise et détaillée des négatifs argentiques N&B, par opposition à la lumière diffusée. C'est une méthode exigeante, car sa netteté et son contraste ne pardonnent pas les rayures et la poussière sur la surface du film. Les tirages effectués ainsi demandaient souvent des corrections manuelles (peintes) sur le papier, impliquant d'avantage de travail et de coûts. À la fin des années 1970, elle était le plus souvent remplacée par la lumière diffusée… meilleure pour cacher les erreurs de manipulation et maximiser les profits des laboratoires photo.

Mais nettoyer les négatifs n'est plus un problème une fois numérisés, et sur ce sujet, Alain et moi partageons les mêmes valeurs : l'imagerie numérique doit augmenter les possibilités offertes aux photographes, en construisant par dessus l'héritage argentique, plutôt que de se contenter de ce qu'on peut obtenir rapidement et facilement pendant qu'on essaie de ré-inventer la photographie comme si elle était née numérique.

En tant qu'utilisateur d'Ansel de la première heure, Alain m'a contacté pour obtenir de l'aide sur l'ajustement du module [_diffusion ou netteté_](../doc/modules/processing-modules/diffuse/) pour renforcer ou atténuer le grain argentique d'une manière qui reproduit fidèlement l'impact de la source lumineuse de l'agrandisseur (ponctuelle ou diffusée) sur le tirage final, en partant d'une numérisation faite au réflex numérique. Après tout, la diffusion est ce qui se produit ici. [^1]

[^1]: Cependant, il doit être mentionné que _diffusion ou netteté_ utilise un modèle de diffusion thermique ([l'équation de transfert thermique de Fourier](https://fr.wikipedia.org/wiki/%C3%89quation_de_la_chaleur)) dans le [domaine des ondelettes](https://fr.wikipedia.org/wiki/Ondelette). Cette équation peut aussi modéliser la diffusion des particules, et sa solution fondamentale peut être identifiée à une convolution avec une fonction de Gauss (i.e. produisant un flou gaussien bien plus lourd en calcul, en utilisant les bons réglages). Mais puisqu'on l'applique dans le domaine des ondelettes, et pas à l'échelle des photons, je ne peux pas, en toute bonne foi, prétendre ici à l'exactitude du modèle physique vis à vis de la diffusion lumineuse. C'est plutôt une diffusion généralisée _inspirée par la physique_.

Mais il a également construit un dispositif complet pour effectuer la numérisation initiale, et a été assez aimable pour documenter et illustrer tout ce processus, de la préparation au post-traitement, et me permettre de le publier ici. Vous avez ici, gratuitement, le meilleur de ce que l'_open-source_ a à vous offrir :

- 50 ans d'expérience d'Alain,
- des exemples et résultats concrets,
- les explications optiques de ce qui se passe,
- des schémas complets du dispositif de lumière ponctuelle,
- les modules physiquement réalistes de pipeline graphique d'Ansel/Darktable, et des pré-réglages pour les modules _dématriçage_, _profil de couleur d'entrée_, _diffusion et netteté_, afin de renforcer ou d'atténuer le grain en post-production,
- une réflexion sur le travail et la responsabilité du tireur photo, concernant la conservation du patrimoine et la qualité d'exposition.

<object data="https://static.ansel.photos/article-lumiere-ponctuelle-32-4.pdf" type="application/pdf" width="100%" height="900px">
  <p>Impossible d'intégrer le PDF. <a href="https://static.ansel.photos/article-lumiere-ponctuelle-32-4.pdf">Télécharger</a> à la place.</p>
</object>

<div class="text-center">
{{< button url="https://static.ansel.photos/article-lumiere-ponctuelle-32-4.pdf" label="Télécharger le livre numérique (PDF)" icon="download fas" class="">}}
</div>


## Résumé des réglages dans Ansel

Ces réglages supposent que vous numérisez des négatifs N&B sous une lumière verte quasi-monochromatique avec un appareil photo numérique.

- Télécharger le profil de couleur [IdentityRGB-elle-V2-g10.icc](https://github.com/ellelstone/elles_icc_profiles/blob/master/profiles/IdentityRGB-elle-V2-g10.icc) :
  - pour Linux/Mac :
    - `~./config/ansel/color/in`
    - `~./config/ansel/color/out`
  - pour Windows :
    - `./AppData/Local/ansel/Color/In`
    - `./AppData/Local/ansel/Color/Out`
- Ouvrir le scan de négatif N&B dans Ansel,
- Régler le module _dématriçage_ en utilisant le mode VNG4,[^2]
- Régler le module _profil de couleur d'entrée_ pour utiliser `IdentityRGB-elle-V2-g10.icc` comme profil d'entrée et comme profil de travail,
- Régler le module _calibration des couleurs_:
  - dans l'onglet _CAT_, régler l'adaptation sur _sans (contourner)_,
  - dans l'onglet _N&B_, régler le canal vert à 1,0 et les canaux rouge/bleu à 0,0.
- Se reporter au livre pour le réglage du module _diffusion ou netteté_.

Ces réglages permettent d'éliminer toute possible diaphonie (_cross-talk_) entre canaux, aussi bien liée au dématriçage (pouvant utiliser des méthodes collaboratives entre canaux, pour les méthodes autres que VNG4) qu'aux conversions d'espace de couleur (dont la diaphonie est intégrée par construction dans le calcul matriciel effectué à l'application du profil). Ainsi, toute aberration chromatique liée à la réfraction optique variable suivant la longueur d'onde lumineuse est éliminée, et en scannant sous une lumière verte quasi-monochromatique, la netteté de la numérisation est maximale car seuls les photo-sites verts de l'appareil photo sont utilisés. En pratique, cela revient à supprimer la trichromie du pipeline graphique.

Bien évidemment, cela ne fonctionnera pas pour des négatifs couleurs et des diapositives, qui demanderont une lumière blanche à spectre complet et une gestion trichromatique.

[^2]: CHANG, Edward, CHEUNG, Shiufun, et PAN, Davis Y. Color filter array recovery using a threshold-based variable number of gradients. In : Sensors, Cameras, and Applications for Digital Photography. SPIE, 1999. p. 36-43. <https://doi.org/10.1117/12.342861>
