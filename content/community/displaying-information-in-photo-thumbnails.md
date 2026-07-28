---
title: "Displaying information in photo thumbnails in Lighttable - Affichage d'informations dans les vignettes de photo dans Lighttable - Captures pour illustrer"
date: 2024-01-24
slug: "displaying-information-in-photo-thumbnails"
tags:
  - Community archive
forum_author: "Bild"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/displaying-information-in-photo-thumbnails"
wayback_url: "https://web.archive.org/web/20240530215113/https://community.ansel.photos/view-discussion/displaying-information-in-photo-thumbnails"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/displaying-information-in-photo-thumbnails`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240530215113/https://community.ansel.photos/view-discussion/displaying-information-in-photo-thumbnails).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Bild** on 2024-01-24.*

Hello

Photo thumbnails in Darkroom display informations relating to ISO, speed, focal length, etc.

*\[attachment lost: image was hosted on the retired forum\]*

In Ansel, photo thumbnails do not display these informations into the lighttable.

*\[attachment lost: image was hosted on the retired forum\]*

Would it be possible to display these informations in photo thumbnails into ligthtable in Ansel ?

Furthermore, is it possible to carry out enhanced search/selection based on these informations ?

*\[attachment lost: image was hosted on the retired forum\]*

Thank you in advance

Best regards

---------------------------------------------------------------------

Hello

  

Les vignettes des photos dans Darkroom affichent des informations relatives à l'ISO, la vitesse, la focale...(paramétrable)

*\[attachment lost: image was hosted on the retired forum\]*

Dans Ansel, les vignettes des photos n'affichent pas ces informations dans la table lumineuse.

*\[attachment lost: image was hosted on the retired forum\]*

Serait il possible de faire afficher ces informations dans les vignettes dans Ansel ?

Par ailleurs, est il possible d'effectuer des recherche / sélection poussées sur la base de ces informations?

*\[attachment lost: image was hosted on the retired forum\]*

Par avance merci

Bien cordialement

## Replies

**Alphonse PHILIPPE** — 2024-03-17

Bonjour,

J'ai posté une question sur la même demande. Je m'associe donc à cette demande.

Merci

A. Philippe

---

**Aurélien Pierre** — 2024-03-17

EXIF infos **on thumbnails** in the lighttable have been removed :

- the static display was removed because the code was tangled and unmanageable,
- the hover display was removed for performance reasons because it would trigger a new SQL request everytime the cursor hovered a different thumbnail.

There is an EXIF module in the left sidepanel, showing the metadata of the currently selected thumbnail. Info will update when selection changes, and the fields to display are fully configurable.

*\[attachment lost: image was hosted on the retired forum\]*

Now, as usual, the real question is : why do you need those metadata **in each thumbnail ?**

Thumbnail width is flexible while text width is fairly constant, the problem is what happens when text spans too wide for the thumbnail ? That triggers all sorts of exceptions to manage it, that I would rather avoid.

> Furthermore, is it possible to carry out enhanced search/selection based on these informations ?

Of course. In lighttable -\> Library module -\> Queries tab, you can select images based on anything and mix constraints :

*\[attachment lost: image was hosted on the retired forum\]*

---

**Bild** — 2024-03-18

Thanks for the response, Thanks for this great work

---

**Bild** — 2024-03-18

Exif Panel ==\> it meets my needs,

lighttable -\> Library Module -\> Queries Tab ==\>it meets my needs

Everything is fine. It's better to have something functional than something cosmetic and complicated.

I appreciate your desire for simplification.

---

**Alphonse PHILIPPE** — 2024-04-07

Bonjour,

Dans ce monde chaque être ou chose a un nom. Donc le minimum serait de faire apparaitre le nom de la photo au dessus ou en dessous de celle-ci.

-----

In this world every being or thing has a name. So the minimum would be to make the name of the photo appear above or below it.

Thanks

---

**Aurélien Pierre** — 2024-04-07

Chaque être ou chose a aussi une date de naissance. Une taille. Un poids. Pour autant, on ne se fait pas tatouer notre carte d'identité sur le front, et on ne met pas des étiquettes partout. D'abord parce que ça ne servirait généralement à rien, ensuite parce que trop d'information tue l'information. L'argument "ça existe donc ça doit être affiché" est fallacieux.

On est là pour traiter des images dans un espace écran limité, ce qui implique de choisir attentivement quelles étiquettes on veut afficher pour utiliser judicieusement l'espace disponible. La question est donc : pourquoi on a besoin du nom de l'image ? Quel est l'intérêt dans le workflow ? En particulier, quel est l'intérêt de savoir qu'on est sur IMG_8965.ext ou sur IMG_9656.ext en dessous de chaque miniature ?

---

**Jiyone** — 2024-04-07

> En particulier, quel est l'intérêt de savoir qu'on est sur IMG_8965.ext ou sur IMG_9656.ext en dessous de chaque miniature ?

Pour ne pas les confondre si l’image est semblable ? 🤷‍♂️

---

**Aurélien Pierre** — 2024-04-07

Confondre quoi ? Si l'image est semblable, qu'est-ce que ça change qu'on prenne l'une ou l'autre ?

---

**Jiyone** — 2024-04-07

Tu arrives à voir des différences de details fins dans la table lumineuse ? 🤣

On aurait besoin d’ouvrir l’image en grand pour les différencier.

de toute façon je suis sûr qu’on trouvera plus tard une solution pour ré-afficher des données dans les vignettes sans ralentissement.

---

**Aurélien Pierre** — 2024-04-08

Mais… encore une fois… voir des détails fins dans quel but ?

On manipule des images. Si on a besoin des méta-données pour différencier deux images, c'est qu'elles sont visuellement identiques. Et si elles sont visuellement identiques, pourquoi on a besoin de les différencier ? Qu'on prenne l'une ou l'autre, c'est pareil. On est pas en train de manipuler des fichiers clients ou des sauvegardes ou n'importe quoi d'unique et identifié.

Le seul cas d'utilisation que je peux voir, c'est pour retrouver le fichier sur le système de fichiers, et vu que ça arrive rarement, le module d'affichage des méta-données me paraît suffisant.

D'ailleurs, si le but est de voir des détails fins, on aurait plutôt intérêt à maximiser la surface des vignettes au lieu de charger l'UI avec du texte.

---

**Jiyone** — 2024-04-08

> Mais… encore une fois… voir des détails fins dans quel but ?

Dans le but de les comparer et faire la différence entre deux images 🤣

---

**Aurélien Pierre** — 2024-04-08

Et une fois qu'on a fait la différence, on a résolu quel problème ? C'est quoi l'action suivante ?

---

**Alphonse PHILIPPE** — 2024-04-08

Bonjour,

La façon la plus simple de parler d’‘une photo est de décrire son contenu. Mais il est plus commode de lui associer un nom. Pour les photos argentiques, un numéro figure toujours sur le côté de la bande du négatif ou un numéro est imprimé sur le cache d’une diapositive. En numérique c’est le nom du fichier qui est utilisé

Je comprends votre souci de simplifier l'interface utilisateur. Mais comme vous le dites :

> « Les années 2020 sont 40 ans trop tard pour ré-inventer les paradigmes d’interaction entre l’utilisateur et son ordinateur, que ce soit la façon dont on utilise son clavier et sa souris pour piloter une interface ou le comportement d’un navigateur de fichiers. Depuis les années 1980, toute l’informatique grand public a convergé vers une sémantique plus ou moins unifiée, ...»

 il faut garder ce qui est devenu une pratique courante. Le nom du fichier de la photo figure toujours en dessus ou en dessous des photos dans toutes les visionneuses de photos que je connais.

Si on utilise que Ansel pour sélectionner et traiter une photo, il est acceptable de ne pas avoir le nom de la photo dessus ou dessous de celle-ci, puisque c’est le contenu de la photo qui nous intéresse.

Mais si on utilise un autre logiciel, une visionneuse permettant de voir finement les détails ou permettant d’analyser le raw, RawDigger ou FastRawViewer, par exemple, pour choisir la photo à traiter, la référence de la photo retenue sera, en principe, son nom de fichier. Pour la retrouver dans Ansel il faut balayer toutes les photos dans la table lumineuse et regarder dans le panneau des EXIF, à gauche, pour la retrouver. Cela n’est pas très commode.

Certaines visionneuses permettent de faire un lien avec le logiciel de traitement pour l’ouvrir directement. Mais toutes le ne permettent pas forcément.

Et il y certainement d'autres façons d'insérer Ansel dans un flux de travail.

Pour conclure je propose que le nom de photo figure au dessus ou en dessous de celle-ci. Et aucun autre paramétrage ne doit permettre d’ajouter d’autres informations. L’absence de cette information peut un handicap pour certains utilisateurs.

A Philippe

---

**Aurélien Pierre** — 2024-04-08

> Mais si on utilise un autre logiciel, une visionneuse permettant de voir finement les détails ou permettant d’analyser le raw, RawDigger ou FastRawViewer, par exemple, pour choisir la photo à traiter, la référence de la photo retenue sera, en principe, son nom de fichier. Pour la retrouver dans Ansel il faut balayer toutes les photos dans la table lumineuse et regarder dans le panneau des EXIF, à gauche, pour la retrouver. Cela n’est pas très commode.

Du coup, l'objectif c'est d'avoir une vue agrandie de l'image. Le passage par le nom de fichier est une solution de contournement utilisant un autre logiciel. La vraie solution serait d'avoir la vue agrandie directement en table lumineuse.

> Pour conclure je propose que le nom de photo figure au dessus ou en dessous de celle-ci. Et aucun autre paramétrage ne doit permettre d’ajouter d’autres informations. L’absence de cette information peut un handicap pour certains utilisateurs.

Avoir une séquence de "Shoot dim...23.NEF" (texte tronqué) quand la taille de miniature ne permet pas de rentrer le nom de fichier complet va être tout aussi handicapant.

Je rappelle que pour trouver un nom de fichier, il y a aussi une fonction recherche (Ctrl+F) en table lumineuse.

---

**Alphonse PHILIPPE** — 2024-04-08

Bonjour,

Autre visionneuse : pas uniquement pour avoir une vue agrandie, mais des fonctions qu'une visionneuse standard n'offre pas : [*FastRawViewer*](https://www.fastrawviewer.com) permet de voir et d'analyser le contenu d'un fichier raw.

Nom de fichier : si c'est clairement indiqué qu'un nom trop long sera tronqué, à chacun d'en tenir compte.

Quoi de plus simple que d'avoir un nom associé à une photo. Toute autre solution, fonction recherche, données EXIF, ... est une solution de contournement de la simplicité. Un nom est vu au premier coup d'œil et ne demande aucune action supplémentaire, même pas tourner la tête pour regarder à gauche.

A. Philippe

---

**cendalc** — 2024-04-08

I agree with Alphonse here - name is great identifier for cooperation with other software tools - it would be nice to see names even if they can be trimmed.

---

**binoyte** — 2024-08-18

> Avoir une séquence de "Shoot dim...23.NEF" (texte tronqué) quand la taille de miniature ne permet pas de rentrer le nom de fichier complet va être tout aussi handicapant.

Afficher l'ID de la photo est peut-être une solution. Ou alors une renumérotation volatile c'est à dire l'index de la photo dans la collection affichée. On l'a en haut de la table lumineuse. On pourrait peut-être le faire apparaître à côté de chaque miniature.

Au moins en réunion / projection on peut rapidement dire de laquelle des versions très similaires on parle. C'est ce que fait Lightroom. Je ne dis pas ça pas pour donner du poids à mon argument, loin de là, mais au moins les capture d’écran ne manque pas pour se faire une idée.

Personnellement le nom exact de la photo ne me sert qu'exceptionnellement, et aller le lire dans le panneau EXIF & IPTC ne me pose pas de problème. L'afficher sur chaque miniature ne me semble pas pertinent.

Benoît

