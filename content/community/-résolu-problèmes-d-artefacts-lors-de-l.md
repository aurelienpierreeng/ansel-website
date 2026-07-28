---
title: "[Résolu] Problèmes d'artefacts lors de l'export en JPEG ou TIFF avec le module \"Réduction bruit (profil)\""
date: 2024-11-23
slug: "-résolu-problèmes-d-artefacts-lors-de-l"
tags:
  - Community archive
forum_author: "libresurf"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/-résolu-problèmes-d-artefacts-lors-de-l"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/-résolu-problèmes-d-artefacts-lors-de-l`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **libresurf** on 2024-11-23.*

Version d'Ansel : 4ea986a (d'après le menu "À propos")

Bonjour à tous,

J'observe des artefacts disgracieux lors de l'export, aussi bien au format JPEG que TIFF (non compressé), lorsque j'utilise le module "Réduction bruit (profil)".

Voici le réglage du module "Réduction bruit (profil)" : seul le dernier curseur a été remonté pour travailler sur les détails.

*\[attachment lost: image was hosted on the retired forum\]*

Suite à l'export (ici au format JPEG), l'image présente des dégradés très marqués (franges) dans le ciel.

*\[attachment lost: image was hosted on the retired forum\]*

Est-ce normal ? L'artefact est d'autant plus visible que l'export est de grande dimension (par exemple 5152x7728 pixels).

Pour information, je n'ai aucun problème d'artefacts si je désactive le module "Réduction bruit (profil)" avant l'export.

  

\[Par contre, le rendu des couleurs sur le forum (voir dernière photo) n'a rien à voir avec l'affichage de mes autres logiciels (voir la capture d'Ansel ci-dessus).\]

## Replies

**Jiyone** — 2024-11-23

Quel est le profil choisit à l’export ?

---

**libresurf** — 2024-11-24

Bonjour ﻿@Jiyone﻿ ,

Dans le module "Réduction bruit (profil)", le profil est "*distribution générique*".

Dans le modules "Export images", le profil est "*similaire à l'original*".

*\[attachment lost: image was hosted on the retired forum\]*

---

**libresurf** — 2024-11-24

Si vous voulez faire des essais, le fichier RAW est disponible ici : [http://cedric.leullier.free.fr/divers/DSCF3776.RAF](http://cedric.leullier.free.fr/divers/DSCF3776.RAF)

Il est sous licence Creative Commons CC-BY-SA, donc faites-vous plaisir. ﻿😉﻿

---

**libresurf** — 2024-11-24

Ah, j'oubliais le fichier compagnon .xmp : [http://cedric.leullier.free.fr/divers/DSCF3776.RAF.xmp](http://cedric.leullier.free.fr/divers/DSCF3776.RAF.xmp)

---

**Jiyone** — 2024-11-24

> Dans le modules "Export images", le profil est "*similaire à l'original*".

Voilà le problème. Il faut mettre sRGB et le rendu sur Perceptuel :)

---

**libresurf** — 2024-11-24

Merci ﻿@Jiyone﻿ ,

C'est effectivement ça !

Voici le rendu avec ces nouveaux paramètres :

*\[attachment lost: image was hosted on the retired forum\]*

