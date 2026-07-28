---
title: "Quelques questions"
date: 2024-07-31
slug: "quelques-questions"
tags:
  - Community archive
forum_author: "fourdogslong"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/quelques-questions"
wayback_url: "https://web.archive.org/web/20240806203339/https://community.ansel.photos/view-discussion/quelques-questions"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/quelques-questions`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240806203339/https://community.ansel.photos/view-discussion/quelques-questions).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **fourdogslong** on 2024-07-31.*

Bonjour, après avoir essayé Ansel sous Windows 11 j'ai installé Linux Fedora et je trouve la performance plus intéressante donc je considère l'utiliser comme programme principal.

Par contre j'ai quelques questions pour lesquelles je n'arrive pas à trouver de réponse. En voici 3, j'ajouterai mes autres questions ici au fur et à mesure que j'en aurai.

1: Est-ce possible de désactiver les ToolTips?

2: Les préférences shortcut ne semblent plus exister, y-a-t'il une liste de shortcut en ligne pour savoir qu'est-ce qui fait quoi?

3: Si je régle le scaling de Linux Fedora à 150% (j'utilise un moniteur 4K), Ansel devient très flou, j'ai essayé de changer le réglage DPI dans Ansel mais je ne trouve pas un réglage qui régle le problème, y-a-t'il un truc pour y arriver? En ce moment j'ai laissé Linux à 100% et mis Ansel à 150% mais tout l'OS est minuscule et difficile à bien voir sauf pour Ansel. Si je fait l'inverse, Ansel à -1 et Linux à 150%, Ansel devient flou.

  

Merci beaucoup, bonne journée.

## Replies

**Aurélien Pierre** — 2024-08-13

Il serait intéressant d'investiguer la raison pour laquelle le programme est plus rapide sous Linux que sous Windows, étant donné que la pile logicielle est la même, mais que ce sont notamment les couches bas niveau qui vont changer (en particulier les drivers). Est-ce que c'est un problème de support OpenCL ?

Sinon, les réponses :

1.  les tooltips ne sont pas désactivables
2.  les préférences shortcuts sont désactivées pour l'instant
3.  le scaling DPI dépend de l'environnement de bureau utilisé (KDE et autres trucs basés sur Qt vs. Gnome et autres trucs basés sur Gtk). Voir mon article sur LXQt : https://dev.aurelienpierre.com/posts/linux/2023-11-03-lxqt-sur-fedora/#g%C3%A9rer-les-hautes-densit%C3%A9s-d%C3%A9cran

