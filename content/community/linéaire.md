---
title: "Linéaire"
date: 2024-03-17
slug: "linéaire"
tags:
  - Community archive
forum_author: "Alphonse PHILIPPE"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/linéaire"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/linéaire`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Alphonse PHILIPPE** on 2024-03-17.*

Bonjour,

Après quelques recherches sur le net, j'ai cru comprendre qu'il y avait un intérêt à démarrer le développement d'un RAW avec un profil d'entrée linéaire.

Cela est-il possible avec Ansel ? Si oui, comment faire ? Avec quels modules ? Des lectures pour mieux comprendre?

Merci

A. Philippe

## Replies

**Jiyone** — 2024-03-17

bonjour,

il n’y a rien à faire, Ansel est par défaut en linéaire pour les raw en entrée.

---

**Aurélien Pierre** — 2024-03-17

"Linéaire" signifie que les valeurs RGB contenues dans le fichier sont codées proportionnellement à l'énergie lumineuse captée. Tous les fichiers RAW sont codés de cette manière, et doivent être décodés en conséquence. Ça n'est pas un choix ou une option, c'est une contrainte technique, et c'est bien évidemment la méthode employée par Ansel.

---

**Alphonse PHILIPPE** — 2024-03-18

Bonjour,

Les profils d'entrée associés à l'appareil peuvent avoir une courbe de transfert linéaire, cad sortie proportionnelle à l'entrée , ou en forme gamma.

Dans d'autres logiciels que j'ai utilisé j'avais le choix entre les deux possibilités.

Avec une courbe linéaire il faut forcément retravailler l'image, tandis qu'en non linéaire l'image est tout de suite plus plaisante mais ne correspond peut-être pas à ce qui est souhaité.

Merci

A. Philippe

---

**Alphonse PHILIPPE** — 2024-03-18

Bonjour,

Tout d'abord je ne pose pas ici en tant qu'expert, seulement en amateur qui essaye de comprendre.

Si dans votre réponse vous vouliez dire que Ansel lit les données sans apporter de modification par une courbe, cad de façon linéaire, je vous ai mal compris. Je n'ai donc pas à me préoccuper de cela.

Ci dessous le lien d'une page, qui peut servir à ceux qui lisent ce forum, apportant toute l'information nécessaire à un utilisateur et qui permet de télécharger des profils linéaires.

[https://goodlight.us/linear-profiles.html](https://goodlight.us/linear-profiles.html#Fujifilm)

D'autres logiciels n'offrent pas cette possibilité de base et il faut télécharger les profils et les installer.

Merci

A. Philippe

---

**Aurélien Pierre** — 2024-03-18

Je pense qu'on est en train de confondre gamma, courbe de base et profil. En préambule, lire https://ansel.photos/fr/workflows/scene-referred/.

Le "gamma" est un terme dont l'usage est découragé car il peut signifier trop de choses différentes, suivant le contexte. En particulier, il peut s'appliquer à un encodage non-linéaire des valeurs de bits (obligatoire pour éviter la postérisation dans les images encodées sur 8 bits), et dans ce cas là on l'appelle aujourd'hui OETF (opto-electrical transfer function). Il peut aussi désigner la correction de luminosité qu'on trouve dans la plupart des logiciels de traitement. Cette correction éclaircit les tons moyens sans toucher au blanc et au noir (par une propriété de la fonction mathématique puissance sur le domaine \[0 ; 1\]). La "correction gamma" disponible dans les réglages des écrans est également une adaptation (grossière) de la luminosité de l'image pour compenser l'effet de la luminosité ambiante sur la perception des couleurs (effet Hunt) et des tonalités (effet Stevens, effet Bartleson-Breneman).

Dans tous les cas, le gamma se calcule par une fonction puissance, ce qui fait que toute correction basée sur une puissance a fini par être négligemment appelée gamma, peu importe ce qu'elle **représente.**

Un profil est un fichier de méta-données qui caractérise un espace de couleur RGB. L'utilisation d'un profil permet de convertir le signal RGB d'un espace à un autre, notamment pour en corriger la déviation colorimétrique. Dans l'article ci-dessus, le graphe montre en effet que le RGB capteur est très éloigné du RGB écran, ou même de la réponse électrique des cellules de la rétine. Le profil permet de définir la traduction des données du capteur, avant d'injecter le signal dans le pipeline de traitement.

Une courbe de base est une transformation esthétique, qui accomplit la même tâche que le "gamma luminosité", c'est à dire éclaircir les tons moyens, mais ajoute en plus du contraste. Un telle courbe a typiquement une forme "en S" plus ou moins prononcée. L'origine de la courbe de base est la réponse sensitométrique de la pellicule argentique, qui a la même forme en S.

La confusion vient de ce que Adobe Lightroom intègre cette courbe de base dans ses profils, ce qui impose que la retouche subséquente se fasse dans un espace non-linéaire, relatif à l'affichage. Dans Ansel, la notion de courbe de base a été éliminée : l'éclaircissement (global) se fait par une correction d'exposition (linéaire), le contraste et la compression des hautes lumières se gèrent via le module filmique. Le profil d'entrée est donc purement linéaire, sans avoir besoin d'action particulière. Le signal est relatif à l'affichage (et non-linéaire) après filmique.

---

**Alphonse PHILIPPE** — 2024-03-18

La phrase essentielle : *Dans Ansel, la notion de courbe de base a été éliminée *

C'est ce que j'avais compris. Mais ça va mieux en le disant explicitement.

Je vais continuer à découvrir Ansel.

Merci pour cette précision

