---
title: Ansel n'est pas un projet de loisir
date: 2024-03-17
draft: true
authors:
    - Aurélien Pierre
---

*Publié à l'origine sur le forum de la communauté Ansel, fermé en 2026.*

Ansel __n'est pas__ un projet de loisir. C'est un outil de travail conçu pour accomplir des tâches. Quelle est la différence ?

## Corvées

Prévoir la maintenance à long terme, la stabilité et la robustesse implique des corvées, comme refactoriser du code, simplifier la structure du programme, et identifier quelles fonctionnalités doivent être élaguées. En plus d'être laborieuses, ces corvées sont souvent déplaisantes, car elles n'impliquent aucune créativité et ne produisent aucune nouvelle fonctionnalité cool qui va booster le marketing, mais elles demandent souvent de comprendre le code emmêlé et confus écrit au cours d'un "projet du samedi" par quelqu'un d'autre.

C'est juste de la gestion ennuyeuse et responsable, mais chronophage. Sauf que quelqu'un doit le faire.

## Design/Conception

La conception est ce qui se passe quand vous cherchez la solution la plus simple et minimaliste au problème de quelqu'un. La conception impose que le concepteur comprenne le problème du point de vue humain, et connaisse les technologies disponibles suffisamment bien pour identifier la plus adaptée.

L'opposé de la conception est l'ajout aveugle "de la prise en charge/ du support de ...", ce qui implique bourrer l'application avec autant de fonctionnalités que possible, jusqu'à ce qu'on ne puisse plus la maintenir et qu'on passe au projet suivant. En anglais, cela s'appelle [feature creep](https://en.wikipedia.org/wiki/Feature_creep) et son effet sur les gens est appelé [feature fatigue](https://www.jstor.org/stable/30162393). Cela porte préjudice aux projets autant qu'aux gens.

Ici encore, la tâche est chronophage, en plus de requérir un ensemble de compétences particulières (_l'ingénierie_), qui prennent elles-mêmes du temps à maîtriser (_et demandent d'aller en école d'ingénieur_). Tout ça va bien au-delà de la simple capacité d'écrire du code informatique, l'essentiel du travail est d'ailleurs fait avant d'écrire la moindre ligne de code, et s'il est fait correctement, ce travail réduit en fait le volume de code requis, ce qui aide à la maintenabilité.

## Coûts additionnels

Le produit n'est jamais le produit, le produit est toujours le service dans lequel le produit est un composant clé. Livrer un logiciel sous forme d'exécutable installable n'est pas si difficile. Penser que c'est ça qui créée la valeur pour les gens est se fourvoyer. Fournir l'assistance utilisateur dans des délais raisonnables, former/éduquer les utilisateurs, et débugger est la partie la plus difficile car c'est une tâche récurrente et une charge cognitive, mais c'est ce dont l'utilisateur a besoin pour accomplir son travail.

Plus de 500 heures ont été investies dans le développement du moteur de recherche et modèle de langage [Chantal AI](https://chantal.aurelienpierre.com) pour le traitement d'image, ce qui a en fait démarré un autre projet open-source  ([Virtual Secretary](https://github.com/aurelienpierreeng/VirtualSecretary)). Même les logiciels commerciaux n'ont pas d'IA dédiée pour agréger la connaissance des documentations, des forums d'utilisateurs et des publications scientifiques, pour améliorer l'assistance utilisateur.

Par ailleurs, les rapports techniques et scientifiques documentant la théorie sous-jacente aux améliorations logicielles d'Ansel et Darktable sont en accès libre sur le [site d'Aurélien Pierre](https://eng.aurelienpierre.com).

## Vous pouvez être un acteur de tout ça

Les individus qui ont les compétences professionnelles mentionnées ci-dessus ont tendance à trouver des opportunités d'emploi stables et bien payées. S'ils pratiquent déjà leurs compétences professionnellement toute la semaine, il y a de fortes chances pour qu'ils aient envie de faire autre chose dans leur temps libre. 

C'est une _très_ mauvaise nouvelle pour les applications libres/open-source car elle signifie qu'elles devront se contenter de contributions aléatoires provenant d'amateurs, ce qui résulte en un problème connu depuis longtemps : les application libres sont les alternatives bas de gamme et bâclées des équivalents commerciaux, leur caractère ouvert rendant cette réalité tolérable pour la minorité d'utilisateurs qui priorisent la confidentialité sur la capacité à accomplir la tâche correctement.

__Le libre doit suffisamment bien payer pour attirer les ingénieurs compétents, afin de produire des applications de niveau industriel__. Ça n'est pas de l'astrophysique : les gens ont d'abord besoin de payer leurs factures. Ensuite, s'ils le peuvent, de travailler sur des projets cools. Mais pas l'inverse.

__En finançant Ansel, vous donnez à Aurélien Pierre la possibilité d'investir le temps requis pour corriger les choses correctement et pour régler vos problèmes concrets, sans avoir à vivre en stress financier.__ Vous incitez aussi d'autres ingénieurs à faire de même sur d'autres projets, en démontrant que c'est possible. 

__Vous contribuez à créer une culture de la juste rémunération du travail sur des projets libres__, qui ont trop souvent tendance à reposer sur l'exploitation du travail bénévole et le précariat.

Vous pouvez donner via [Liberapay](https://liberapay.com/aurelienpierre/donate) ou directement ici (voir plus bas).

Liberapay permet les dons anonymes via Stripe, ou des dons normaux via Paypal. Les dons faits ici n'utilisent que PayPal pour l'instant. Depuis 2023, les deux services facturent des commissions très similaires.

Merci.

_Note :_ Aurélien Pierre a travaillé sur Darktable depuis fin 2018, étant l'auteur de l'espace de couleur darktable UCS 22,  des modules filmique, égaliseur de ton, balance couleur, diffusion & netteté, flou d'objectif, de la chaîne de travail relative à la scène, etc. en plus d'avoir refactorisé le code d'interface graphique, permettant d'avoir des thèmes graphiques définis par l'utilisateur. 

Ansel a été forké sur Darktable 4.0 depuis que les contributeurs de dt ont perdu la raison et se dispersent sur des fonctionnalités périphériques, coûteuses à tous les niveaux
