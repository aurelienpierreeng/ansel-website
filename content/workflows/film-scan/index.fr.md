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
