---
title: "Documentation utilisateur"
date: 2024-03-20
slug: "documentation-utilisateur"
tags:
  - Community archive
forum_author: "Alphonse PHILIPPE"
forum_category: "Developers talk"
forum_url: "https://community.ansel.photos/view-discussion/documentation-utilisateur"
wayback_url: "https://web.archive.org/web/20240530214734/https://community.ansel.photos/view-discussion/documentation-utilisateur"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/documentation-utilisateur`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240530214734/https://community.ansel.photos/view-discussion/documentation-utilisateur).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Alphonse PHILIPPE** on 2024-03-20.*

Bonjour,

Ansel ne comporte pas une documentation utilisateur complète. Pour les fonctions non documentées, il est demandé de se référer à Darktable.

De mon point de vue d'*utilisateur*, les fonctions d'Ansel peuvent être classées comme suit :

- fonctions existantes dans à Darktable et identiques ;
- fonctions existantes dans à Darktable et différentes;
- fonctions nouvelles dans Ansel.

Chaque fonction devant être décrite, la solution pourrait être, respectivement :

- reprendre telle que la description de Darktable ;
- reprendre la description de Darktable et la modifier, soit en enlevant un partie du texte, soit en réécrivant une partie ;
- décrire la nouvelle fonction.

Les deux premiers cas pourraient être traités par des utilisateurs non développeurs volontaires. La description complète ou partielle d'une nouvelle fonction ne peut être faite que par le développeur.

Q1 : Est-il possible de récupérer la documentation de Darktable, comme pour le code ?

Q2 : Quelle est la part relative des trois catégories, en pourcentage, en nombre de pages et en taille ?

Q3 : Quelle est votre estimation de temps nécessaire pour les trois catégories ?

Q finale : Cela vous parait-il réaliste et possible ?

Cette analyse et proposition vous est faite par auditeur qualité logiciel ayant audité des fournisseurs de progiciels, petites ou grandes entreprises.

Je suis prêt à en discuter avec vous, sur ce forum ou en privé

Cordialement

A. Philippe

## Replies

**Aurélien Pierre** — 2024-03-22

La documentation de Ansel est à peu près complète, mais pas forcément à jour, et pas traduite en français. Le renvoi à la documentation de Darktable est fait seulement pour les modules dépréciés, pour lesquels j'ai supprimé les pages correspondantes.

Le code source du site web et de la partie documentation sont publiés sur Github, voir les liens en pas de page, sur la page d'accueil https://ansel.photos/fr/#code.

Concernant la traduction, il est possible de récupérer les clés traduites de Darktable, c'est un travail à scripter que je dois faire un jour.

Je ne pense pas pertinent de continuer à se baser sur Darktable pour l'avenir de la doc. L'interface est de plus en plus différente et garder la traçabilité de ce qui a changé avec DT va juste alourdir le texte. De plus, ça n'intéressera pas les nouveaux utilisateurs. Enfin, une grande partie de la documentation de DT sert à expliquer les bizarreries de conception d'interface, la solution n'est donc pas d'écrire plus de doc (que personne ne lira) mais de concevoir une interface qui demande moins de lecture.

Concernant le travail à faire pour mettre à jour, je n'ai pas la moindre idée du volume. Ce qui est certain, c'est qu'elle ne peut s'écrire qu'en lisant le code, car même dans DT, de nombreuses fonctions ne sont pas documentées (et donc parfois ré-implémentées plusieurs fois dans le code…). De plus, c'est régulièrement en rédigeant la doc que je me rends compte de ce qui est mal conçu dans l'interface (quand on en est à 3 paragraphes pour expliquer un bouton, en général c'est un signe).

---

**Alphonse PHILIPPE** — 2024-03-23

Merci pour votre réponse.

Je participerai donc au soutien du projet d'une manière plus traditionnelle quand j'aurai décidé de ne pas renouveler ma licence du produit que j'utilise actuellement.

D'ici là je développerai en parallèle mes photos avec Ansel.

---

**Alphonse PHILIPPE** — 2024-04-07

Bonsoir,

En attendant, vous est-il possible de traduire en priorité, avant la traduction du texte, les titres et sous-titres des différentes rubriques et commandes. Il n'est pas toujours évident de connaitre la traduction anglaise d'une commande ou d'un outil.

Merci

A. Philippe

