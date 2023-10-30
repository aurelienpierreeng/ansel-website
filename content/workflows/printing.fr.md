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

## Le problème de l'impression

Malheureusement, rien ne garantit que l'imprimante soit capable d'utiliser toute la plage d'encodage. Le minimum de densité (_Dmin_ en argentique) est obtenu avec le papier nu, et correspond à la valeur RGB codée 255. Le maximum de densité (_Dmax_ en argentique), est obtenu avec une couverture de 100% d'encre.[^1] Le problème, c'est que si le Dmin correspond à une valeur RGB de 255, le Dmax ne correspond jamais à une valeur RGB de 0.

[^1]: Les imprimantes atteignent des noirs plus denses en mélangeant de l'encre noire pure avec toutes les encres CJM.

Pour comprendre le problème, j'ai généré une charte synthétique de valeurs sRGB de 0 à 59 (sur 255), que j'ai imprimée sur du papier de bureau classique, avec une vieille imprimante photo, puis j'ai scanné le résultat. La grille entre les patchs est noir pur (RGB = 0).

{{<compare before="/en/workflows/img/charte-noirs.jpg" after="/en/workflows/img/chartes-scan.jpg" >}}
Avant : original numérique ; Après : tirage numérisé sans correction.
{{</compare >}}

Les noirs imprimés sont atténués, comparés à l'original numérique, mais ce n'est pas le pire : les patchs sous 0.12 %  sont complètement fondus dans la grille à 0 %, ce qui veut dire que toutes les valeurs RGB codées sous 5 / 255 sont imprimées à la même densité et finissent dans le même pâté noir.

Dit autrement, notre noir d'imprimante sature à 5 / 255 et nous ne serons pas en mesure de résoudre les détails dans les ombres denses sans une correction adaptée. Mais pourquoi ?

Alors que le sRGB 8 bits (avec OETF) peut théoriquement encoder un contraste de 6588:1 (soit une plage dynamique de 12.69 EV), les écrans LED peuvent typiquement restituer un contraste de 300:1 à 1000:1 grâce à des blancs __émissifs__ dont on pilote l'intensité. Sur le papier, les blancs sont __réflectifs__, et la variable d'ajustement du contraste est alors l'encre noire, qui absorbe la lumière incidente. Le contraste restituable sur un tirage papier varie entre 50:1 (Dmax de 1.7) et 200:1 (Dmax de 2.3), soit une plage dynamique variant de 5.6 à 7.6 EV.

À l'impression, on déroule la plage dynamique du fichier dans la plage dynamique du papier en commençant par le blanc. 5.6 EV sous le blanc, on atteint la limite de plage dynamique de l'encre noire sur papier mat, mais on n'est même pas à la moitié de la plage dynamique du fichier numérique. Toutes les tonalités comprises entre -5.6 et -12.7 EV sous le blanc, dans le fichier numérique, sont dont imprimées avec la même densité de noir : l'imprimante est au maximum d'encrage.

{{<table>}}
| Objet | Ratio de contraste | Dmax | Plage dynamique |
|--------|----------------:|------:|---------------:|
| 8 bits sRGB (avec OETF) | 6588:1 | 3.8 | 12.7 EV |
| 8 bits RGB linéaire | 510:1 | 2.7 | 9.0 EV |
| 12 bits RGB linéaire (photos brutes) | 8190:1 | 3.9 | 13 EV |
| 14 bits RGB linéaire (photos brutes) | 32766:1 | 4.5 | 15 EV |
| 16 bits RGB linéaire (photos brutes) | 131070:1 | 5.1 | 17 EV |
| tirage papier mat | 50:1 | 1.7 | 5.6 EV |
| tirage papier brillant | 200:1 | 2.3 | 7.6 EV |
| ICC point noir PCS standard | 287:1 | 2.5 | 8.2 EV |
| Eizo Color Edge CG319X | 1500:1 | 3.2 | 10.6 EV |

_Équivalences d'unités de contraste : toutes représentent le même écart entre les luminances du noir pur et du blanc pur, mais mesuré différemment._
{{</table>}}

Imprimer les tons du fichier numérique compris entre -12.7 et -5.6 EV à la même densité sur le papier implique, en pratique, aplatir les détails et les textures sur une tache noire solide. Pour l'éviter, nous allons devoir remapper la plage dynamique sRGB vers la plage dynamique du papier, ce qui signifie pour notre exemple repousser les valeurs de code RGB entre 5 et 255.

{{<figure src="/en/workflows/img/sRGB-to-printer-zones.png" caption="Le problème de mappage de tons du sRGB numérique vers un papier à contraste 50:1, tel que montré par le graphique zone system de Filmique" />}}


Voyons ce que ça change sur une image réelle ayant beaucoup de contenu dans les ombres denses :

{{<figure src="/en/workflows/img/Shooting Minh Ly-0155-_DSC0155-Minh-Ly-resized.jpg" caption="Original numérique" />}}

{{<compare before="/en/workflows/img/Shooting Minh Ly-0155-_DSC0155-Minh-Ly-no-bpc.jpg" after="/en/workflows/img/Shooting Minh Ly-0155-_DSC0155-Minh-Ly-bpc.jpg">}}
Avant : simulation d'impression à un contraste de 66:1 sans compensation du point noir ; Après : simulation d'impression à un contraste de 66:1 avec compensation.
{{</compare>}}

Le noir doit être corrigé pour garder les détails dans les cheveux, même si cela se fait au prix d'un peu de contraste dans le cou.

## Comprendre la compensation du point noir

La [compensation du point noir](https://www.color.org/WP40-Black_Point_Compensation_2010-07-27.pdf) a été inventée par Adobe et standardisée par l'ICC plus tard. Il s'agit d'un simple décalage du noir destiné à relever (éclaircir) toutes les valeurs RGB au dessus du seuil de saturation du noir, de façon à retrouver les dégradés dans les ombres denses, en acceptant que les noirs resteront atténués par rapport à l'original peu importe ce qu'on fait.

Malheureusement, la compensation du point noir par décalage ne préserve pas les teintes et peut faire virer les couleurs. Pour cette raison, [Capture One ne supporte simplement pas](https://support.captureone.com/hc/en-us/articles/360002654477-Black-point-compensation) cette option.

Il faut noter que la compensation du point noir est le dernier ressort, quand [l'intention perceptuelle](https://www.color.org/v2profiles_v4.pdf)
n'est pas disponible dans le profil de couleur de sortie (c'est à dire, quand les LUTs `AtoB` et `BtoA` ne sont pas renseignées dans le profil). Ceci est le cas le plus courant lorsqu'on travaille avec des pilotes d'imprimante open-source, car ces LUTs doivent être créées par quelqu'un qui comprend tout cela, et pas par un simple logiciel d'étalonnage. En conséquence, les LUTs perceptuelles ne sont typiquement trouvées que dans les profils de couleurs fournis par les fabricants, mais ceux-ci ne seront pas complètement précis pour votre combinaison de cartouches d'encre et de papier.

En l'absence d'intention perceptuelle définie, le gestionnaire de couleur se rabat sur l'intention colorimétrie relative et peut utiliser la compensation du point noir si le profil contient une courbe de tonalité (la `TRC`). Si vous n'avez ni les LUTs perceptuelles, ni la TRC, c'est à dire si vous n'avez pas étalonné votre imprimante vous-même, alors pas de chance : vous ne pourrez pas effectuer de compensation du point noir par les méthodes ICC standard.

Heureusement, Filmique vous permet de ramapper la plage dynamique de la scène vers n'importe quelle plage dynamique cible, via l'onglet _affichage_, en augmentant la _valeur du noir cible_.

{{<figure src="/en/workflows/img/sRGB-to-printer-curve.png" caption="Courbe de compensation du point noir par Filmique (échelle log)" />}}

Puisque le mappage de tons de Filmique est une correspondance générique à 3 points (noir, gris moyen et blanc), il vous permet de remonter le point noir sans changer les valeurs de gris moyen et de blanc, et avec un impact minimal sur le contraste global. Et comme Filmique gère également la teinte et la saturation, sa compensation du point noir n'induit pas de virages de couleur, à la différence de la méthode Adobe. Le problème se résume alors à trouver la valeur cible de noir correcte.

## Ajuster le point noir sans profiler l'imprimante

1. <a href="/en/workflows/img/charte-noirs.jpg" download>Téléchargez la charte des noirs</a>,
2. imprimez la comme une image sRGB, sans retouche ni correction,
3. sur le tirage, notez le patch le plus sombre que vous pouvez distinguer de la grille noir pur, et relevez sa valeur en pourcentage,
4. ouvrez l'image de la charte dans Ansel, et dans le module Filmique, effectuez les réglages suivants :
   1. dans l'onglet _scène_, cliquez sur le bouton d'auto-réglage,
   2. dans l'onglet _look_, réglez le contraste à la valeur minimum (0.5),
   3. dans l'onglet _affichage_, saisissez la valeur du noir cible que vous avez relevée sur le patch précédemment,
   4. dans l'onglet _options_, réglez le _contraste des basses lumières_ à _sûr_.
5. exportez la charte corrigée et imprimez la à nouveau pour valider les réglages.

Voici le résultat obtenu ici:

{{< compare before="/en/workflows/img/chartes-scan.jpg" after="/en/workflows/img/chartes-scan-bpc.jpg">}}
Avant, le point noir de l'affichage est réglé à 0 % (pas de compensation). Les patchs de 0 % à 0.09 % sont totalement fondus dans la grille. Après, le point noir affichage est réglé à 0.12 %. Tous les patchs ressortent de la grille, mais la grille elle-même a perdu de la densité. 0.09 % serait un meilleur réglage.
{{< / compare >}}

{{< note >}}
Les patches ont tous des valeurs entières de RGB sur 8 bits, de 0 à 49 sur 255, avec l'OETF sRGB, ce qui est ce que le pilote de l'imprimante recevra à l'impression. Les pourcentages traduisent ces valeurs en RGB linéaire Rec2020 pour le pipeline d'Ansel. Il est inutile d'essayer d'utiliser des valeurs de pourcentages intermédiaires, puisque l'image est finalement converties en 8 bits sRGB par la plupart des pilotes.
{{</ note >}}

{{<warning>}}
Le niveau de saturation du noir lu sur les patchs n'est pas une métrique du contraste du tirage. Les imprimantes reçoivent les images à travers les pilotes de l'ordinateur et les traitent sur leur électronique embarquée, au moins pour convertir le RGB en CMYK. Les pilotes et l'électronique embarquée appliquent des transformations d'image non documentées qui nous empêchent d'établir des correspondances absolues entre les valeurs de code RGB et la densité d'encre réelle, à moins d'effectuer un étalonnage complet. Ce que nous faisons ici est une forme de rétro-ingéniérie pour estimer la zone de confort du noir de l'imprimante, appliquée par dessus les corrections d'image effectuées nativement par l'imprimante. Retenez vous de tirer des conclusions hâtives de ces lectures.
{{</warning>}}

## Appliquer le réglage à des images réelles

Pendant le traitement de l'image, procédez comme d'habitude, sans compensation du point noir. Filmique a par défaut une compensation du point noir destinée à gérer les erreurs de quantization inévitables pendant la conversion 8 bits, elle n'est pas liée à un medium particulier, seulement au sRGB 8 bits.

Vous devrez juste veiller à la luminosité du rétroéclairage de votre écran, comparée à l'éclairage ambiant de la pièce où vous retouchez. Si votre écran est beaucoup plus lumineux que l'environnement, cela peut vous empêcher de diagnostiquer des images sous-exposées avant de les imprimer. Le rétro-éclairage correct est obtenu quand un rectangle 100% blanc affiché à l'écran paraît avoir la même luminosité qu'une feuille de papier blanc affichée à côté de l'écran.

Avant d'imprimer, changez le _noir affichage_ de Filmique à la valeur mesurée sur la charte ci-dessus, et exportez avec l'intention _colorimétrie relative_.

{{<note >}}
Un réglage de contournement global du _noir affichage_ sera proposé dans l'interface dans le futur, pour des changements temporaires à l'exportation, sans devoir changer les paramètres de l'image, de même qu'une méthode d'extraction du point noir depuis le profil ICC d'imprimante, si disponible.
{{</note >}}

## Compensation du point blanc

Les utilisateurs d'imprimantes de poche Fuji Instax ont rapporté un problème similaire, mais avec le blanc. La Fuji Instax, utilisant une impression photochimique, semble ajouter beaucoup de contraste dans les hautes lumières, résultant en écrêtage au dessus de 75 % de luminance environ.

Vous pouvez reproduire les étapes ci-dessus pour le blanc, un utilisant <a href="/en/workflows/img/charte-blancs.jpg" download>la charte des blancs</a>. Notez le patch le plus sombre qui commence à se fondre dans la grille blanche, et utilisez le pourcentage correspondant dans le _blanc affichage_ de Filmique.

## À propos de l'épreuvage écran

Ansel peut réaliser un [épreuvage écran](/en/doc/module-reference/utility-modules/darkroom/soft-proof/), en utilisant LittleCMS2, si vous lui donnez un profil d'imprimante correct. L'épreuvage écran (_softproofing_) signifie convertir l'image vers l'espace de couleur de l'imprimante, c'est à dire compenser les points noir et blanc, puis remapper le gamut des couleurs, en utilisant les données contenues dans le profil et les méthodes ICC standard. En pratique, cela va enlaidir l'image en la désaturant et en retirant beaucoup de contraste (« noirs laiteux »), dans une tentative de se rapprocher de résultat imprimé. Il y a cependant des pièges.

D'abord, l'épreuvage montre ce que vous obtiendriez d'un pipeline ICC standard si votre imprimante se conformait aux spécifications ICC. L'épreuvage n'est pas écrit dans le fichier exporté, donc l'application des corrections vues à l'écran est la seule responsabilité du pilote de l'imprimante et du technicien de labo photo.

Ensuite, même avec un contraste atténué, un épreuvage écran sur un medium émissif n'est toujours pas proche d'une copie physique sur papier réflectif. L'utilisabilité pratique de l'épreuvage est au mieux anecdotique.

Finallement, il n'y a pas tellement d'informations à tirer d'un épreuvage écran, sinon que les tirages papier sont nuls. Le mieux que vous puissiez faire est vérifier que les conversions de couleur automatiques se comportent correctement, en particulier, vérifier qu'elles préservent des dégradés continus et ne créent pas d'aplats solides là où l'original numérique a des dégradés.

Si vous activez la vérification de gamut, vous verrez presque toujours que les couleurs les plus riches et profondes sont hors du gamut de l'imprimante. Encore une fois, il n'y a pas lieu de s'inquiéter, celles-ci seront remappées par les LUT perceptuelles de l'imprimante ou par le mappage de gamut de Filmique.

Mon expérience avec l'épreuvage écran et la vérification de gamut est qu'ils inquiètent inutilement les utilisateurs semi-compétents, en leur faisant croire qu'ils doivent corriger quelque chose manuellement pour faire disparaître les alertes de dépassement de gamut. J'ai aussi vu des rapports de bugs mentionnant un problème avec l'épreuvage, parce qu'il voilait les noirs, alors que c'est exactement le but. Les graphiques ne sont utiles que si vous savez comment les lire, et les données ne deviennent des informations que si vous savez ce que vous y cherchez.

## Filmique : solution complexe à problème épineux

Le pipeline ICC a pour but d'automatiser les conversions d'espace de couleurs, en définissant des méthodes normalisées utilisant des profils descriptifs. Ce faisant, il place une lourde responsabilité sur les techniciens de laboratoire, chargés de créer et d'opérer ces profils, et l'expérience montre que la majorité d'entre eux naviguent à vue dans la colorimétrie.

Loin d'avoir fiabilisé le pipeline, les standards ICC l'ont simplement rendu plus complexe via des boîtes noires magiques mais incompréhensibles (les _Color Management Systems_), dont la complexité des spécifications pourrait faire oublier qu'on ne fait rien de plus que des mathématiques de niveau BAC+1. L'impression de photos numérique est plus que jamais un jeu d'essai/erreur à base de tirages de test et de corrections empiriques, impliquant des logiciels que seuls leurs développeurs comprennent.

La botte secrète des profils ICC est l'intention perceptuelle, qui passe par des champs `AtoB` et `BtoA` dûment complétés avec des LUTs dans le fichier de profil. Ces champs ne sont guère renseignés que dans les profils des fabricants, et quand ils le sont, les compromis techniques ayant présidé à leur élaboration sont opaques.[^3] Dans tous les cas, l'approche perceptuelle est limitée car les LUT ICC v2 ne sont valides que pour un espace source donné : typiquement, les profils imprimante attendent un espace sRGB ou Adobe RGB en entrée, et tout autre espace d'entrée rend leur LUT perceptuelles invalides. Étant donné que tout logiciel de retouche de photos brutes travaille dans un espace RGB à large gamut, il faut donc 2 étages de mappage de gamut (large gamut vers sRGB, puis sRGB vers imprimante), chacun introduisant des virages de couleur plus ou moins prévisibles.[^2]

[^2]: Pour plus de détails édifiants sur l'horreur des intentions de mappage de gamut dans les profils ICC, voire la documentation de Argyll CMS : <https://www.argyllcms.com/doc/iccgamutmapping.html>

[^3]: On voudrait notamment savoir si le mappage de gamut choisit la couleur la plus proche, ou force une teinte constante, ou une luminance constante, etc.

En l'absence de ces champs, les gestionnaires de couleur se replient silencieusement sur une intention colorimétrique, sans notifier l'utilisateur. Celui-ci n'a donc aucune idée de ce qui se passe et le résultat est imprévisible. Dans la plupart des cas, passer de l'intention perceptuelle à l'intention colorimétrie relative, à l'exportation dans Ansel, ne change pas le résultat final puisque les profils open-source n'ont pas les LUTs perceptuelles.

Filmique est né comme un système de mappage de tonalités, avec la conversion HDR vers SDR en tête. Dès le départ, sa conception a été la plus générale possible, sans présupposer de valeur fixe pour les points blanc et noir du medium de sortie. Il est rapidement apparu que le mappage de gamut ne pouvait être découplé du mappage de tonalités, puisqu'on manipule des signaux RGB dont la modulation pilote à la fois la luminosité, la saturation et la teinte, et le découplage "couleur" vs. luminosité n'est qu'une vue de l'esprit pour mieux comprendre, mais sans réalité technique.

Filmique s'est complexifié au cours des années pour résoudre de façon transparente le problème qu'ICC a échoué à résoudre via l'intention perceptuelle. Au lieu de se reposer sur une LUT dont on n'est pas sûr qu'elle existe, faite on ne sait pas comment et supposant un espace de couleur fixe mais non documenté en entrée, Filmique propose à l'utilisateur de paramétrer lui-même une intention perceptuelle, en définissant :

- les points noir/blanc de l'espace d'entrée (scène) et de sortie (affichage),
- la courbe de contraste pour le mappage de tonalité,
- une normalisation optionnelle des couleurs en normes RGB préservant la saturation d'origine (similaire à l'intention saturation), ou sans normalisation (similaire à l'intention perceptuelle), ou un mélange des deux (depuis la version 7),
- un mappage de gamut vers l'espace de sortie par _soft-clipping_ de la saturation à luminance et teinte constantes (depuis la version 6).

En exportant les images dans l'espace de couleur de l'imprimante (ou à défaut sRGB), en définissant la compensation du point noir dans le _noir cible_ de Filmique et en indiquant l'intention _colorimétrie relative_ dans le fichier exporté, vous pouvez court-circuiter les étapes de correction opaques et non-fiables de la chaîne ICC, et les gérer le redimensionnement de l'espace de couleur en interne.

L'incompréhension et la méconnaissance de ces problèmes a mené Darktable 4.0 à introduire le module _Sigmoïde_ en alternative simplifiée à Filmique, qui peut se permettre d'être considérablement plus simple puisqu'il remplit 25% du contrat et fait reculer le logiciel de 5 ans en arrière.
