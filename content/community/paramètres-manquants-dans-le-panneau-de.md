---
title: "Paramètres manquants dans le panneau de configuration"
date: 2023-06-17
slug: "paramètres-manquants-dans-le-panneau-de"
tags:
  - Community archive
forum_author: "Balistic"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/paramètres-manquants-dans-le-panneau-de"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/paramètres-manquants-dans-le-panneau-de`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Balistic** on 2023-06-17.*

Bonjour,

Le/Les paramètres suivants sont fonctionnels dans Ansel mais n'apparaissent pas dans le panneau de configuration. Est-il possible de les rajouter ? Merci d'avance

- plugins/darkroom/0/navigation_visible (TRUE/FALSE)

  

  

Accessoirement, s'il est également possible de retrouver la fonctionnalité "Déplier un seul module de développement à la fois", ce serait pratique, merci.

## Replies

**Jiyone** — 2023-07-06

Pour la fenêtre de navigation, sa place serait plutôt dans le menu global. Pourquoi as tu besoin de le masquer ou de l'afficher ?

---

**Balistic** — 2023-07-08

"**navigation_visible**" masque ou affiche la petite prévisualisation située en haut à gauche dans la chambre noire.

Dans Darktable, elle ne pouvait être montrée/masquée que par un raccourci clavier (ctrl+maj+h je crois, je ne suis plus sûr) (donc il faut déjà se souvenir du raccourci clavier lorsqu'on veut réafficher la petite prévisualisation, ce qui n'est pas... ergonomique).

Il n'existait aucune option dans le panneau de configuration pour activer/désactiver cette petite prévisualisation. Le seul moyen autre que le raccourci clavier était d'aller directement éditer le fichier darktablerc.

Dans les dernières version d'Ansel que j'ai testé (il y a quelques semaines), le paramètre **navigation_visible** est toujours présente et fonctionne. Ce serait donc ergonomique d'ajouter l'option correspondant à ce paramètre dans le panneau de configuration d'Ansel.

