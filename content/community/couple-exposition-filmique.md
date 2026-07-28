---
title: "Couple exposition - filmique"
date: 2024-01-03
slug: "couple-exposition-filmique"
tags:
  - Community archive
forum_author: "Dom"
forum_category: "Feedback & use cases"
forum_url: "https://community.ansel.photos/view-discussion/couple-exposition-filmique"
wayback_url: "https://web.archive.org/web/20241109203958/https://community.ansel.photos/view-discussion/couple-exposition-filmique"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/couple-exposition-filmique`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20241109203958/https://community.ansel.photos/view-discussion/couple-exposition-filmique).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Dom** on 2024-01-03.*

Bonjour,

Hormis la luminosité globale de l'image,l'exposition a t-elle une incidence sur le mappage de la plage dynamique, selon que l'on porte attention plutôt sur les hautes ou basses lumières ?

*\[attachment lost: image was hosted on the retired forum\]*

## Replies

**Aurélien Pierre** — 2024-01-16

L'exposition globale définit implicitement la position du point gris (central sur la vue courbe de filmique).

Sur ta version à 0 EV, on voit clairement que la distance entre le gris et le blanc scène (mesurée sur les abscisses) est très supérieure à ce qu'on aurait à -2 EV. Cependant, la distance gris-blanc affichage (mesurée sur les ordonnées) reste constante, par construction.

Sur ce cas précis, la compression des hautes lumières est donc plus agressive dans le cas 0 EV que dans le cas -2 EV, et donc la perte de contraste local dans les hautes lumières est donc plus importante. Par contre, on perd les ombres à -2 EV.

Comme toujours, c'est un compromis qui doit s'ajuster en regardant l'image, pas les chiffres.

La plage dynamique a 2 extrémités, et le compromis se pilote sur les 2 extrémités en même temps. C'est pour ça que je n'aime pas trop qu'on se focalise sur « exposer à droite » (ETTR), parce que c'est juste la moitié du problème.

