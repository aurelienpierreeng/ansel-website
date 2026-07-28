---
title: "Chambre noire - Image HDR Photomatix.exr"
date: 2023-12-01
slug: "chambre-noire-image-hdr-photomatix-exr"
tags:
  - Community archive
forum_author: "Unknown"
forum_category: "Recovered from web archive"
forum_url: "https://community.ansel.photos/view-discussion/chambre-noire-image-hdr-photomatix-exr"
wayback_url: "https://web.archive.org/web/20241109202414/https://community.ansel.photos/view-discussion/chambre-noire-image-hdr-photomatix-exr"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/chambre-noire-image-hdr-photomatix-exr`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20241109202414/https://community.ansel.photos/view-discussion/chambre-noire-image-hdr-photomatix-exr).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Unknown** on 2023-12-01.*

*\[attachment lost: image was hosted on the retired forum\]*

Bonjour,

Sur une zone d'une image, alerte "un canal RVB".

Pipette Gimp : R 255 - V 200 - B 173 Cohérent

Pipette Ansel : R 176 - V 125 - B 101 Je ne comprend pas.

Avec Ansel-6daff28-x86_64.AppImage sous Kubuntu 22.04

## Replies

**Aurélien Pierre** — 2023-12-01

Ansel utilise un pipeline dans lequel se produisent différentes transformations d'espaces de couleurs, et échantillonne la couleur à la fin.

Gimp utilise un calque et échantillonne dessus.

Les valeurs ne peuvent pas être comparées puisqu'elles représentent des choses totalement différentes, et sont probablement affichées dans des espaces RGB différents.

C'est comme comparer une température en Celsius à la sortie du frigo avec un température en Farenheit 30 minutes plus tard.

---

**Aurélien Pierre** — 2023-12-01

[See more...](javascript:void(0))

