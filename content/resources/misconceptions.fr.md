---
title: "Idées fausses répandues"
date: 2023-01-19
draft: false
weight: 10
authors: ["Aurélien Pierre"]
---

Cette page regroupe la plupart des erreurs et des idées fausses sur Ansel que l'on peut trouver sur internet.

<!--more-->

## Je dois être un expert / ingénieur pour utiliser Ansel

Mes [vidéos](https://www.youtube.com/channel/UCmsSn3fujI81EKEr4NLxrcg)
et mes articles contiennent à la fois la partie "quoi faire" et la partie "pourquoi/comment". Le "pourquoi/comment" est typiquement technique ou même théorique, et sert à justifier le "quoi faire". Il y a plusieurs raisons pour lesquelles je donne les deux :

1. Les explications techniques précises sont très difficiles à trouver sur internet, et je suis à peu près le seul à lier la théorie et la pratique en vidéo. Autrement, il est très facile de trouver des informations fausses en photographie, venant de gens juste au dessus de la moyenne qui essaient d'aider, mais induisent les autres en erreur.
1. Je déteste personnellement les gourous qui lancent des consignes sans prendre la peine de les justifier. Les règles ont toujours une raison et doivent être violées dès que cette raison cesse d'être valide. On trouve beaucoup de gens qui continuent à suivre de vieilles règles parce que « les anciens savaient ce qu'ils faisaient » — mais ils ne se souviennent pas pourquoi ils le faisaient — alors que les circonstances ont changé.
1. Comprendre comment les outils se comportent vous permet de prédire à quelle moment ils vont échouer (parce qu'il vont tous échouer à un certain point), ce qui vous permet de régler les problèmes avant même qu'ils apparaissent, et de préparer un plan B quand ça arrive,
1. La plupart des conseils que je donne sont contextuels au résultat désiré et au type d'image travaillée. Supprimer le contexte les rend faux en général.

À cause de tout ça, beaucoup de gens ont conçu l'idée qu'ils devaient comprendre 100 % du contenu technique avant d'être capable d'utiliser le logiciel. C'est simplement faux. À la fin, Ansel est seulement un logiciel avec une interface graphique, vous pouvez pousser les curseurs ou utiliser les préréglages fournis jusqu'à ce que l'image paraisse bien. Tout ce que vous ne comprenez pas peut être ignoré pour le moment, et peut-être réessayé plus tard.

D'un autre côté, si vous commencez à mélanger les media, comme imprimer des photos sur papier et fournir des images numériques à partir de la même retouche, ou réinjecter vos exports d'Ansel dans un autre logiciel pour des manipulations plus avancées, avoir au moins une compréhension basique de comment un pipeline graphique fonctionne va vous aider grandement.

Comme tout objet technologique, plus vous le comprenez et mieux vous le contrôlez, et moins vous vous battez avec. Mais Ansel est fourni avec un pack de préréglages par défaut et un pipeline préconfiguré qui devraient vous donner une base de traitement correcte dans la plupart des cas.

Il est vrai cependant que les contrôles de traitement d'image dans l'interface graphique ont tendance à être plus ancrés dans les sciences de la couleur et dans l'optique que d'autres applications. La raison en est que traiter des HDR sans artefacts demande des modèles de couleur plus précis, qui prennent plus de paramètres en entrée pour s'adapter à la plage dynamique des images. La raison pour laquelle la plupart des applications peuvent se permettre d'avoir l'air plus simple est que leurs modèles de couleur sont moins performants et reposent sur des approximations qui ne suivent plus quand la plage dynamique augmente. Tout a un prix…

## Ansel traite mes images brutes d'une façon qui les rend plus sombres et plus fades

La réalite est en fait le contraire.

Les photos brutes (raw) ont typiquement un fichier JPEG intégré qui sert de miniature basse résolution. Cette miniature est ce que vous voyez dans la table lumineuse d'Ansel mais aussi sur l'écran à l'arrière de votre appareil photo. Vous ne verrez jamais une image brute sans aucune correction, c'est tout simplement impossible de l'afficher.

Cette miniature a été traitée et améliorée par le logiciel interne de l'appareil photo, d'une manière qui l'éclaircit en général beaucoup, ajoute du contraste, de la saturation, et très souvent la teinte pour un rendu plus chaud.

Ce que vous voyez en ouvrant l'image dans la chambre noire d'Ansel est une image beaucoup moins traitée, plus proche du fichier brut et plus neutre, prévue pour être une base à votre traitement personnel.

Mais souvenez vous que ce rendu par défaut en ouvrant la chambre noire n'est que ça : une base de travail, un point de départ. À la fin, même les réglages par défaut peuvent être ajustés à votre convenance, ce qui est tout l'intérêt du logiciel.


## Les modules dépréciés ne fonctionnent plus

Ansel est basé sur darktable 4.0. darktable 4.0 a déprécié de nombreux
modules. Ansel en  a déprécié encore plus. Les  modules sont dépréciés
quand une meilleure alternative est disponible.

Mais « déprécié » est un mot un peu fort pour dire « le widget du module est cachée dans l'interface graphique ». Le code d'interface graphique et le code de traitement de pixels sont toujours dans le logiciel, et seront toujours exécutés pour les anciens traitement utilisant ce module. Pour ces traitements, le module sera visible dans l'interface.

Pour de nouveaux traitements, le module sera caché de l'interface. La dépréciation est seulement un nettoyage de l'espace écran pour limiter la prolifération des modules.
