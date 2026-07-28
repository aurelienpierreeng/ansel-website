---
title: "Soucis sur rouge vif en développement"
date: 2023-12-10
slug: "soucis-sur-rouge-vif-en-développement"
tags:
  - Community archive
forum_author: "Julien FAUCHER"
forum_category: "Editing help"
forum_url: "https://community.ansel.photos/view-discussion/soucis-sur-rouge-vif-en-développement"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/soucis-sur-rouge-vif-en-développement`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Julien FAUCHER** on 2023-12-10.*

Bonjour tout le monde !

J'ai passé un moment sur la photo ci-dessous et je rencontre quelques soucis plus ou moins récurrents dans le cadre de photos ayant des notes rouges assez vif (penser fleurs très rouges genre roses ou œillets comme ici).

1.  Au moment de l'entrée dans Ansel, le rouge vif vire au magenta.
2.  Dans le cadre de cette image, une frange semble apparaître en bord de pétales.
3.  Dans le cadre de cette image toujours, j'ai du mal à récupérer un beau jaune vif dans les étamines, mais c'est plus un détail.

Conclusion, j'ai tendance à préférer le rendu JPEG du boitier (Canon EOS M50 mk1) malgré des défauts que j'arrive à rattraper en traitement (notamment un manque de contraste dans les pétales les plus saturés et la petite bête un peu claire et désaturée)

J'ai pu remarquer, sur de précédent développements, que supprimer complètement 'Filmique RGB" résout le problème de teinte, mais je suis assez certain que ce n'est pas un flot de travail normal.

Également, désactiver le module "Balance des couleurs RGB" supprime la frange, le paramètre impactant étant surtout la gradation de saturation des ombres qui fait apparaître le soucis très vite.

Auriez-vous des suggestions ? (Je peux fournir le RAW et le XMP si l'on m'indique un moyen de les partager ﻿😊﻿ )

Voici quelques images pour mieux voir les problèmes.

*\[attachment lost: image was hosted on the retired forum\]*

JPEG Sortie de boitier

  

*\[attachment lost: image was hosted on the retired forum\]*

RAW en traitement "par défaut"

A noter la couleur qui vire au violet et la frange sur le haut de la fleur. De plus les pistils ont plus de nuances, ce qui ne m'arrange pas vraiment mais semble correct vis-à-vis de la réalité

*\[attachment lost: image was hosted on the retired forum\]*

Le résultat (à peu près satisfaisant) de mon développement.

La couleur rouge des pétales est globalement correcte, la texture des pétales est restaurée, me semble-t-il. L'ensemble est un peu trop jaune/orangé, un petit ajustement sur la calibration des couleurs ne ferait pas de mal. Par contre, on voit bien la frange rouge du bord du pétale. De même, des franges rouges vif apparaissent sur les pistils bien que ça ne se voie peut-être pas sur l'image.

Mon soucis est que j'ai été obligé de forcer sur le module "zones de couleurs" pour rattraper le violet. Heureusement, je n'ai pas de violet "légitime" dans cette photo mais ça ne me semble pas être un procédé "normal" (peut-être que je me trompe, ceci dit).

*\[attachment lost: image was hosted on the retired forum\]*

Merci d'avance !

## Replies

**Dom** — 2023-12-11

Bonjour,

Il n'est pas possible d'avoir un rouge très saturé et très lumineux simultanément.

Risque de sortie de Gamut et changement de teinte. Ci-après avec la pipette Gimp.

*\[attachment lost: image was hosted on the retired forum\]*

Prendre connaissance de ce document dans un premier temps.

https://eng.aurelienpierre.com/2021/04/the-srgb-book-of-color/

---

**Julien FAUCHER** — 2023-12-11

Bonjour et merci de la réponse !

Donc, pour vérifier ma compréhension.

Ce qu'il se passerait est que mon rouge est "trop" rouge, et par conséquent sort du gamut sRGB d'où effets bizarres (et virage de teinte) ?

Après examen (vérification du gamut \*sans\* utiliser le module filmique RVB qui, si je comprends bien, a pour rôle de s'assurer que toute l'image rentre dans le gamut) :

*\[attachment lost: image was hosted on the retired forum\]*

Donc on peut effectivement confirmer que le rouge est... beaucoup trop rouge. On constate aussi un vilain pic à droite sur le canal rouge dans l'histogramme.

Par contre, je ne vois pas comment rattraper "correctement" ma teinte. Il me semble que filmique devrait "rabattre" ma couleur dans le gamut, en préservant au mieux les teintes. Auquel cas, le module aurait du mal a digérer ce rouge et "le plus proche" tirerai un peu sur le magenta ?

Dans ce cas, y aurait-il un module/un réglage qui permettrait d'améliorer la situation en dehors du remappage "bourrin" des teintes comme je l'ai fait ?

---

**Dom** — 2023-12-15

3 vidéo du développeur à appréhender avant de pratiquer le flux de travail relatif à la scène :

‍

https://www.youtube.com/watch?v=doR50We5FkU

‍Bon visionnage

---

**Dom** — 2023-12-15

‍

https://www.youtube.com/watch?v=luZyu3zj1G4&t=1238s

‍

---

**Dom** — 2023-12-15

‍

https://www.youtube.com/watch?v=t4pghirdXuk

‍

---

**wadouk** — 2023-12-21

Je serais intéressé par le résumé ﻿😂﻿

---

**Julien FAUCHER** — 2023-12-25

Le résumé, dans le cas qui nous concerne et très rapidement, serait de dire qu'il existe des couleurs (dans la réalité vraie) qui ne peuvent tout simplement pas être affichées par un écran.

Ici, potentiellement un rouge très très rouge.

Normalement, les outils de Ansel tentent de travailler avec un espace de couleur plus ou moins perceptuel, bien que ce soit une galère à développer et que, par manque de données scientifiques (et peut-être aussi parce que tout le monde n'a pas les mêmes yeux), un vrai espace de couleurs perceptuel (où l'on peut faire varier la chroma sans changer la teinte ni la luminance) est à peu près illusoire.

Quoi qu'il en soit, il semble qu'ici mon rouge trop rouge soit rabattu dans l'espace de couleur sRGB (le "standard" commun des écrans) avec des inexactitudes. Ce qui peut être dû à pas mal de choses. On peut imaginer un mauvais algo de traitement (mais au vu de la tête des recherches d'Aurelien Pierre sur le sujet, ce n'est pas vraiment là que j'irai chercher) ou d'un mauvais étalonnage de l'appareil / un profil imparfait dans Ansel. Ce qui fait que mon blanc n'est pas blanc et que réduire la luminance ou la chroma (pour retourner dans le sRGB) ne se fait plus à teinte constante. Ce qui donnerait le virage coloré. Vu que je n'ai pas prêté d'attention particulière à la gestion du blanc jusqu'ici, je ne peux pas vraiment utiliser une référence pour rattraper le coup "proprement".

Maintenant, il me faut trouver l'astuce/ruse/paramètre sur lequel jouer pour correctement réaliser le remapping du gamut. Il me semble quand même que l'outil à manipuler reste filmique RGB, mais je n'arrive pas vraiment à en tirer les résultats escomptés.

Je referais des essai un peu plus tard...

---

**Dom** — 2023-12-28

La fonction première de filmique est le re-mappage de tonalité.

[https://www.youtube.com/watch?v=zbPj_TqTF88](https://www.youtube.com/watch?v=zbPj_TqTF88)

*\[attachment lost: image was hosted on the retired forum\]*

Le module pour régler la photo est le module « Balance couleur RVB »

Les 3 modules de base conçus pour fonctionner de concert sont « Calibration des couleurs »

« Filmique RVB » et « Balance couleur RVB »

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Teinte constante = Proportions valeurs RVB constantes

Luminance constante = Somme des valeurs RVB constante.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Correction de la sur-saturation :

\> Filmique – Onglet look – Saturation luminance extrême

\> Calibration des couleurs – Onglets Saturation et/ou Luminosité

\> Balancecouleur RVB

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Pour viser une couleur précise : Le mixage de canaux

[https://www.youtube.com/watch?v=hzoRSNX4594](https://www.youtube.com/watch?v=hzoRSNX4594)

[https://www.youtube.com/watch?v=XPW1EM5rYYk](https://www.youtube.com/watch?v=XPW1EM5rYYk)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Mes sites préférés :

A dabble in photography [https://www.youtube.com/channel/UCxHYygok15XQ6bqu9FK-oCw/videos](https://www.youtube.com/channel/UCxHYygok15XQ6bqu9FK-oCw/videos)

JC TUTOS [https://www.youtube.com/channel/UChkmJoz4r375C6F2eym99YQ/videos](https://www.youtube.com/channel/UChkmJoz4r375C6F2eym99YQ/videos)

Luc VIATOUR - Photographe https://www.youtube.com/c/LucViatour-photographe

Olivier - Carte postale photo [https://www.youtube.com/channel/UCGil9-K90bDUcVwtEMcXA3A](https://www.youtube.com/channel/UCGil9-K90bDUcVwtEMcXA3A)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Généralités : [https://colorandcontrast.com/#/](https://colorandcontrast.com/#/)

[https://www.cambridgeincolour.com/](https://www.cambridgeincolour.com/)

[http://hclwizard.org:3000/hclcolorpicker/](http://hclwizard.org:3000/hclcolorpicker/)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Le flux de travail relatif à la scène de Ansel nécessite effectivement un effort certain en amont pour appréhender qqs notions de la théorie des couleurs mises en pratique avec Ansel.

Maintenant,il existe le logiciel « ART » avec un flux de travail relatif à l’affichage,plus aisé à prendre en main. [https://artherapee.fr/](https://artherapee.fr/)

---

**Dom** — 2024-01-07

Auriez-vous des suggestions ? (Je peux fournir le RAW et le XMP si l'on m'indique un moyen de les partager ﻿😊﻿ )

Tu peux déposer le RAW et le jpeg en utilisant le lien ci-après.

[https://vieuxloup.synology.me:5001/sharing/J15UTrlbN](https://vieuxloup.synology.me:5001/sharing/J15UTrlbN)

Lien opérationnel 1 semaine

---

**Dom** — 2024-01-08

**Explication écart couleur RAW vs JPEG**

***Mesure à droite de la patte avant droite de la sauterelle***

**RAW par défaut**

*\[attachment lost: image was hosted on the retired forum\]*

JPEG

*\[attachment lost: image was hosted on the retired forum\]*

**Luminosité & chroma = JPEG - Teinte = RAW**

*\[attachment lost: image was hosted on the retired forum\]*

**Constat : Échappement de gamut – Décalage de teinte vers la droite pour rentrer dans le gamut**

  

**Lisez-moi**

[**https://ansel-photos.translate.goog/fr/resources/misconceptions/?\_x_tr_sl=en&\_x_tr_tl=fr&\_x_tr_hl=fr**](https://ansel-photos.translate.goog/fr/resources/misconceptions/?_x_tr_sl=en&_x_tr_tl=fr&_x_tr_hl=fr)

## **Ansel traite mes images brutes d'une façon qui les rend plus sombres et plus fades**

La réalité est en fait le contraire. Les photos brutes (raw) ont typiquement un fichier JPEG intégré

qui sert de miniature basse résolution. Cette miniature est ce que vous voyez dans la table lumineuse d'Ansel mais aussi sur l'écran à l'arrière de votre appareil photo. Vous ne verrez jamais une image brute sans correction, c'est tout simplement impossible de l'afficher.

Cette miniature a été traitée et améliorée par le logiciel interne de l'appareil photo, d'une manière qui l'éclaircit en général beaucoup, ajoute du contraste, de la saturation, et très souvent la teinte pour un rendu plus chaud.

Ce que vous voyez en ouvrant l'image dans la chambre noire d'Ansel est une image beaucoup moins traitée, plus proche du fichier brut et plus neutre, prévue pour être une base à votre traitement personnel.

Mais souvenez-vous que ce rendu par défaut en ouvrant la chambre noire n'est que ça : une base de travail, un point de départ. À la fin, même les réglages par défaut peuvent être ajustés à votre convenance, ce qui est tout l'intérêt du logiciel.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

[**https://tomasrosprim.com/fr/lespace-couleur-adobe-rvb-par-rapport-%C3%A0-lespace-couleur-srvb-lequel-devez-vous-choisir/**](https://tomasrosprim.com/fr/lespace-couleur-adobe-rvb-par-rapport-%C3%A0-lespace-couleur-srvb-lequel-devez-vous-choisir/)

---

**Julien FAUCHER** — 2024-01-08

Hello !

J'ai posté le RAW et (normalement) le XMP de mon essai le plus réussi (le troisième) dans le post initial.

---

**Julien FAUCHER** — 2024-01-08

Merci pour cette analyse !

Par contre, il y a un point qui me surprends un peu. D'après la capture d'écran "Mix JPEG+RAW" il me suffirait de réduire la chroma pour retrouver la teinte d'origine. Sauf que dans les faits, lors d'essais, réduire (même très fortement, pour l'exercice) la chroma globale via balance RGB ne semble pas renvoyer la couleur dans le gamut (à teinte égale).

Je me serait attendu à voir la teinte redevenir correcte...

De même, quel serait le module supposé gérer le mapping pour renvoyer la couleur dans le gamut ?

Je m'attendrait à ce que ce soit le module Filmique, mais en farfouillant, je n'ai pas non plus réussi à retomber sur la bonne teinte. Il semble agir sur la teinte déjà remappée. C'est peut-être une erreur d'interprétation de ma part, mais cela me semble louche... En gros, je pense que mon problème dans cette affaire est que je n'arrive pas à trouver le point dans le pipeline sur lequel jouer pour réaliser l'effet souhaité.

*Petit edit : Je viens de me rendre compte en relisant que je confond probablement "tonalité" avec une autre notion qui inclurai la couleur, et pas seulement l'exposition.*

Si j'ai tout suivi, le flux (ou plutôt les modules) sont "relatif à la scène" jusqu'à filmique, puis relatif à l'affichage (on vient modifier les couleurs "à la main", sans correspondance physique) au delà. Donc, on devrait pouvoir obtenir un résultat naturel raisonnable sans utiliser de module de retouche au delà de filmique.

---

**Dom** — 2024-01-09

Fichier RAW reçu

---

**Dom** — 2024-01-09

> Fichiers récupérables avec le lien suivant: [http://gofile.me/2rWS7/z6Of74aVp](http://gofile.me/2rWS7/z6Of74aVp)

Correction L : Module exposition

Correction c : Balance couleur RVB - Maître - Saturation hautes lumières

Correction h : Balance couleur RVB - Maître - Virage de teinte

*\[attachment lost: image was hosted on the retired forum\]*

---

**Dom** — 2024-01-14

Nouveau lien : [http://gofile.me/2rWS7/m5otJNP0j](http://gofile.me/2rWS7/m5otJNP0j)

*\[attachment lost: image was hosted on the retired forum\]*

---

**Julien FAUCHER** — 2024-01-15

Bonjour, j'avais essayé de télécharger via le premier lien il y a quelques jours (dès que j'ai vu le post) et aujourd'hui pour le second, mais il semble que le lien soit mort ou incorrect (ou mal configuré ?)

Dans tous les cas, je reçois un message "Ce lien partagé n'est pas disponible"

---

**Dom** — 2024-01-16

Nouveau lien valide 1 semaine : [http://gofile.me/2rWS7/2mVBUmqXF](http://gofile.me/2rWS7/2mVBUmqXF)

---

**Aurélien Pierre** — 2024-01-16

Bonjour,

problème de sortie de gamut typique. Il est en réalité probable que ce soit le JPEG boîtier qui fasse virer la couleur en teinte, parce qu'Ansel a différents moyens de comprimer le gamut à teinte constante (sans préjuger de l'aspect plus ou moins flatteur du résultat).

Dans le module "calibration couleur", le premier onglet (CAT) dispose d'un curseur de compression du gamut précisément pour corriger ces problèmes en début de pipeline. Le curseur peut aller jusqu'à la valeur 8 en faisant une saisie au clavier (clic droit sur le curseur, puis saisir le chiffre au clavier).

---

**Dom** — 2024-01-21

En pièces jointes les fichiers .xmp

