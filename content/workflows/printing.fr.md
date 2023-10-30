---
title: "Impression"
date: 2023-10-30
draft: false
toc: true
tags: ['']
authors: ["Aurélien Pierre"]
thumbnail: '/workflows/img/charte-noirs.jpg'
---

Le flux de travail [relatif à la scène](scene-referred.fr.md) promet une retouche indépendante du medium de sortie. Il va typiquement produire une image encodée en sRGB sur 8 bits, c'est à dire des valeurs codées entre 0 et 255. Pour simplifier, nous allons nous limiter au cas 8 bits dans la suite. Les concepts demeurent en 16 bits, la différence est que la plage d'encodage va de 0 à 65535, ce qui est un détail.

Malheureusement, rien ne garantit que l'imprimante soit capable d'utiliser toute la plage d'encodage. Le minimum de densité (_Dmin_ en argentique) est obtenu avec le papier nu, et correspond à la valeur RGB codée 255. Le maximum de densité (_Dmax_ en argentique), est obtenu avec une couverture de 100% d'encre.[^1] Le problème, c'est que si le Dmin correspond à une valeur RGB de 255, le Dmax ne correspond jamais à une valeur RGB de 0.

[^1]: Les imprimantes atteignent des noirs plus denses en mélangeant de l'encre noire pure avec toutes les encres CJM.

Pour comprendre le problème, j'ai généré une charte synthétique de valeurs sRGB de 0 à 59 (sur 255), que j'ai imprimée sur du papier de bureau classique, avec une vieille imprimante photo, puis j'ai scanné le résultat. La grille entre les patchs est noir pur (RGB = 0).

{{<compare before="/en/workflows/img/charte-noirs.jpg" after="/en/workflows/img/chartes-scan.jpg" />}}

Le noirs imprimés sont atténués, comparés à l'original numérique, mais ce n'est pas le pire : les patchs sous 0.12 %  sont complètement fondus dans la grille à 0 %, ce qui veut dire que toutes les valeurs codées sous 5 / 255 finissent dans le mềme pâté noir.

Dit autrement, notre noir d'imprimante sature à 5 / 255 et nous ne serons pas en mesure de résoudre les détails dans les ombres denses sans une correction adaptée. Voyons ce que ça change sur une image réelle ayant beaucoup de contenu dans les ombres denses (_avant_ : pas de correction du noir, _après_ : correction)

{{<compare before="/en/workflows/img/Shooting Minh Ly-0155-_DSC0155-Minh-Ly-no-bpc.jpg" after="/en/workflows/img/Shooting Minh Ly-0155-_DSC0155-Minh-Ly-bpc.jpg" />}}

Le noir doit être corrigé pour garder les détails dans les cheveux, même si cela se fait au prix d'un peu de contraste dans le cou.

## Comprendre la compensation du point noir

La [compensation du point noir](https://www.color.org/WP40-Black_Point_Compensation_2010-07-27.pdf) a été inventée par Adobe et standardisée par l'ICC plus tard. Il s'agit d'un simple décalage du noir destiné à relever (éclaircir) toutes les valeurs RGB au dessus du seuil de saturation du noir, de façon à retrouver les dégradés dans les ombres denses, en acceptant que les noirs resteront atténués par rapport à l'original peu importe ce qu'on fait.

Malheureusement, la compensation du point noir par décalage ne préserve pas les teintes et peut faire virer les couleurs. Pour cette raison, [Capture One ne supporte simplement pas](https://support.captureone.com/hc/en-us/articles/360002654477-Black-point-compensation) cette option.

Il faut noter que la compensation du point noir est le dernier ressort, quand [l'intention perceptuelle](https://www.color.org/v2profiles_v4.pdf)
n'est pas disponible dans le profil de couleur de sortie (c'est à dire, quand les LUTs `AtoB` et `BtoA` ne sont pas renseignées dans le profil). Ceci est le cas le plus courant lorsqu'on travaille avec des pilotes d'imprimante open-source, car ces LUTs doivent être créées par quelqu'un qui comprend tout cela, et pas par un simple logiciel d'étalonnage.

En l'absence d'intention perceptuelle définie, le gestionnaire de couleur se rabat sur l'intention colorimétrie relative et peut utiliser la compensation du point noir si le profil contient une courbe de tonalité (la `TRC`).

Si vous n'avez ni les LUTs perceptuelles, ni la TRC, c'est à dire si vous n'avez pas étalonné votre imprimante vous-mêmes, alors pas de chance.

## Ajuster le point noir sans profiler l'imprimante

1. <a href="/en/workflows/img/charte-noirs.jpg" download>Téléchargez la charte des noirs</a>,
2. imprimez la comme une image sRGB, sans retouche ni correction,
3. sur le tirage, notez le patch le plus sombre que vous pouvez distinguer de la grille noir pur, et relevez sa valeur en pourcentage,
4. ouvrez l'image de la charte dans Ansel, et dans le module Filmique, effectuez les réglages suivants :
   1. dans l'onglet _scène_, cliquez sur le bouton d'auto-réglage,
   2. dans l'onglet _look_, réglez le contraste à la valeur minimum (0.5),
   3. dans l'onglet _affichage_, saisissez la luminance du noir que vous avez relevée sur le patch précédemment,
   4. dans l'onglet _options_, réglez le _contraste des basses lumières_ à _sûr_.
5. exportez la charte corrigée et imprimez la à nouveau pour valider les réglages.

Voici le résultat obtenu ici:

{{< compare before="/en/workflows/img/chartes-scan.jpg" after="/en/workflows/img/chartes-scan-bpc.jpg">}}
Avant, le point noir de l'affichage est réglé à 0 % (pas de compensation). Les patchs de 0 % à 0.09 % sont totalement fondus dans la grille. Après, le point noir affichage est réglé à 0.12 %. Tous les patchs ressortent de la grille, mais la grille elle-même a perdu de la densité. 0.09 % serait un meilleur réglage.
{{< / compare >}}

{{< note >}}
Les patches ont tous des valeurs entières de RGB sur 8 bits, de 0 à 49 sur 255, avec l'OETF sRGB, ce qui est ce que le pilote de l'imprimante recevra à l'impression. Les pourcentages traduisent ces valeurs en RGB linéaire Rec2020 pour le pipeline d'Ansel. Il est inutile d'essayer d'utiliser des valeurs de pourcentages intermédiaires, puisque l'image est finalement converties en 8 bits sRGB par la plupart des pilotes.
{{</ note >}}

## Appliquer le réglage à des images réelles

Pendant le traitement de l'image, procédez comme d'habitude, sans compensation du point noir. Filmique a par défaut une compensation du point noir destinée à gérer les erreurs de quantization inévitables pendant la conversion 8 bits, elle n'est pas liée à un medium particulier, seulement au sRGB 8 bits.

Avant d'imprimer, changez le _noir affichage_ de Filmique à la valeur mesurée sur la charte ci-dessus, et exportez.

{{<note >}}
Un réglage de contournement global du _noir affichage_ sera proposé dans l'interface dans le futur, pour des changements temporaires à l'exportation, sans devoir changer les paramètres de l'image, de même qu'une méthode d'extraction du point noir depuis le profil ICC d'imprimante, si disponible.
{{</note >}}

## Compensation du point blanc

Les utilisateurs d'imprimantes de poche Fuji Instax ont rapporté un problème similaire, mais avec le blanc. La Fuji Instax, utilisant une impression photochimique, semble ajouter beaucoup de contraste dans les hautes lumières, résultant en écrêtage au dessus de 75 % de luminance environ.

Vous pouvez reproduire les étapes ci-dessus pour le blanc, un utilisant <a href="/en/workflows/img/charte-blancs.jpg" download>la charte des blancs</a>. Notez le patch le plus sombre qui commence à se fondre dans la grille blanche, et utilisez le pourcentage correspondant dans le _blanc affichage_ de Filmique.

{{< note >}}
Cet article illustre pourquoi le nouveau module _Sigmoide_, introduit dans Darktable 4.0 comme un mauvais doublon à Filmique dans le mappage de tons, est une voie sans issue dans Ansel : il n'y a aucun moyen de spécifier des points blanc et noir cibles en conservant le contraste dans les tons moyens et le gris moyen inchangés.
{{</ note >}}
