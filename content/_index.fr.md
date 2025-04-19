---
title: "Ansel"
date: 2022-11-27T22:36:34+01:00
draft: false
description: "Ansel est un éditeur de photos brutes pour artistes"
tags: ["darktable", "ansel", "photo editing"]
---

<div class="pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold">Votre chambre noire numérique</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4"><em>Ansel</em> est un logiciel libre de traitement photo pour artistes digitaux, conçu pour vous aider à obtenir votre propre interprétation de photos numériques brutes.</p>
  </div>
<div class="my-5">
{{< slideshow images="lighttable.jpg,darkroom.jpg" >}}
</div>
</div>

<div class="container">

{{< quote author="Ansel Adams" >}}
Le négatif est la partition, le tirage est l'interprétation.
{{< /quote >}}

<div class="lead">

Presser le déclencheur de l'appareil photo démarre à peine un processus qui termine quand l'image à l'écran ressemble à celle que vous aviez en tête. _Ansel_ propose de remettre les artistes au centre du processus créatif en leur offrant une interface pour manipuler les images avec précision et nuance, en utilisant une science de la couleur de pointe et des contrôles de couleur indépendants.

</div>

{{< divider >}}

## Installer

{{% row %}}
{{% card icon="linux fab" title="Linux" %}}
Exécutable indépendant de la distribution
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/lin-nightly/master/ansel.stable.AppImage.zip" label="Télécharger ansel.appimage" icon="download" >}}
{{% /card %}}

{{% card icon="windows fab" title="Windows" %}}
Installeur Windows 7 à 11
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/win-nightly/master/ansel.stable.win64.zip" label="Télécharger ansel.exe" icon="download" >}}
{{% /card %}}

{{% card icon="terminal" title="Compilation depuis les sources" %}}
Les meilleurs performances pour votre matériel
{{< button url="/en/doc/install" label="Instructions de compilation" icon="wrench" >}}
{{% /card %}}
{{% /row %}}

{{% row %}}
{{% column  %}}

{{< warning >}}
__Ansel est en version alpha__. L'interface graphique est susceptible de changer et l'application peut crasher dans certaines circonstances.
{{< /warning >}}

{{% /column %}}
{{% column p=true %}}
Les liens ci-dessus pointent toujours vers la dernière compilation quotidienne de la branche « raisonnablement stable ». Si vous voulez une version particulière ou que vous voulez rétrograder, [vous pouvez trouver toutes les versions intermédiaires sur Github](https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0).
{{% /column %}}
{{% /row %}}

{{< divider >}}

## Pourquoi Ansel ?

{{% row %}}
{{% column %}}

De nombreuses solutions existent pour produire des photographies prêtes à consommer pour les masses, des filtres de smartphones aux JPEG produits par les appareils photo, suivis récemment par la magie automatisée des filtres jouets par IA. Tout ça rend la photographie plus facile que jamais, mais les images produites sont-elles réellement __vos__ images et en tout cas, les images que __vous__ attendiez ?

{{% /column %}}
{{% column %}}

_Ansel_ vous permet d'interpréter vos photos brutes comme un instrument de musique, là où la plupart des logiciels essaient de jouer la partition automatiquement à votre place. Il vise à être un outil peu excitant et ennuyeux, qui fait juste ce que vous lui demandez, sans se mettre en travers de votre chemin.
{{% /column %}}
{{% /row %}}

<div class="text-center my-5">
<span class="display-5">Émerveillez-vous de vos résultats</span><br />
<span class="fs-4">Pas de vos jouets</span>
</div>

{{% row %}}
{{% column %}}

Si vous aimez la musique, vous avez le choix entre apprendre à jouer ou acheter des enregistrements. Acheter est plus facile, mais jouer est plus satisfaisant. Les applications de traitement photo ont menti aux utilisateurs pendant des décennies, en prétendant qu'ils pourraient jouer sans apprendre parce que le logiciel se chargerait des complexités techniques à leur place.

{{% /column %}}
{{% column %}}

Il apparait en fait que les utilisateurs se battent contre des applications qu'ils comprennent de moins en moins, pour le contrôle de leurs résultats et pour récupérer les cas épineux où l'automatisation échoue. À mesure que le temps passe, attendez vous à perdre de plus en plus de temps à vous battre contre des IA pour obtenir des résultats naturels… manuellement. Pourquoi ne pas directement éliminer l'intermédiaire ?

{{% /column %}}
{{% /row %}}


{{< divider >}}

## Que peut Ansel pour vous ?

Ansel vous permet de gérer vos collections d'images, de traiter vos fichiers numériques bruts de capteur et vos pellicules numérisées, et d'exporter le résultat vers les formats de fichiers courants. Il stocke votre historique de traitement sous forme de texte et vous permet de remonter dans le temps à n'importe quelle étape de votre traitement, à tout moment.

### Travail sur la couleur

Ansel embarque une science de la couleur récente et compatible HDR : l'adaptation chromatique CIE CAT 2016, l'espace de couleur HDR JzAzBz (2017) et l'espace de couleur perceptuel darktable UCS 2022, développé spécialement pour manipuler la saturation des couleurs en évitant l'effet fluo.

<div class="row">
{{% column %}}
<h5>Calibration des couleurs</h5>
{{< compare after="calibration-after.jpg" before="calibration-before.jpg" cols="2" >}}
Corrigez la balance des blancs et obtenez des couleurs __haute fidélité__ en seulement quelques clics, en étalonnant les couleurs avec un Color Checker directement en chambre noire.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Gradation des couleurs</h5>
{{< compare after="grading-after.jpg" before="grading-before.jpg" cols="2" >}}
Donnez ambiance et caractère à vos photos en polissant leur palette de couleur avec des contrôles nuancés et détaillés, dans les espaces de couleur RVB, Ych ou HSB, à des fins créatives ou correctives.
{{</ compare >}}
{{% /column %}}
</div>

<div class="row">
{{% column %}}
<h5>Correspondance de couleur</h5>
{{< compare after="matching-after.jpg" before="matching-before.jpg" cols="2" >}}
Forcez l'adaptation chromatique de sorte que n'importe quel objet sélectionné corresponde à une couleur prédéterminée, saisie à partir de ses coordonées CIE Lab (pour les logos ou les couleurs de marques commerciales), ou en échantillonnant la couleur du même objet dans une autre photo, pour obtenir un rendu des couleur uniforme sur une série.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Qualificateurs de teinte et fusion</h5>
{{< compare after="masking-after.jpg" before="masking-before.jpg" cols="2" >}}
Utilisez les qualificateurs de teinte, chroma et luminosité pour définir rapidement des masques, et appliquer des effets sélectifs. Combinez les masques paramétriques avec des masques dessinés avec des opérations booléennes. Raffinez et détaillez les bords des masques par floutage ou détection de bords intelligente.
{{</ compare >}}
{{% /column %}}
</div>

### Travail sur les tonalités

Les méthodes de travail sur les tonalités sont conçues pour manipuler la luminance sans affecter la teinte ni la saturation, afin de respecter le travail sur la couleur, effectué à part.

<div class="row">
{{% column %}}
<h5>Mappage de ton HDR</h5>
{{< compare after="filmic-after.jpg" before="filmic-before.jpg" cols="2" >}}
Récupérez les ombres denses et compressez la plage dynamique tout en gardant la saturation et la teinte d'origine, avec un mappage de gamut pour garantir que les couleurs tiennent dans l'espace de couleur de sortie. _(Photo : Andreas Schneider)_
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Traitement basé sur le zone system</h5>
{{< compare after="toneeq-after.jpg" before="toneeq-before.jpg" cols="2">}}
Équilibrez les densités par zone de lumination, en préservant le contraste local grâce à un algorithme de détection des bords, et sélectionnez les zones de lumination à affecter directement dans l'image via le curseur interactif. _(Photo : Andreas Schneider)_
{{</ compare >}}
{{% /column %}}
</div>

### Reconstruction d'image

<div class="row">
{{% column %}}
<h5>Défloutage d'objectif</h5>
{{< compare after="sharpen-after.jpg" before="sharpen-before.jpg" cols="2" >}}
Libérez le pouvoir de l'apprentissage machine basée sur l'analyse de gradients multi-échelle pour rajeunir les vieux objectifs, récupérer les erreurs de mise au point ou renforcer votre sujet, mais sans les artefacts de bord typiques, les bizarreries de sur-accentuation ou le bruit additionnel.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Désembuage</h5>
{{< compare after="dehaze-after.jpg" before="dehaze-before.jpg" cols="2" >}}
Restaurez une certaine profondeur dans les clichés brumeux et flous en ramenant des textures et de la saturation dans les couleurs, sans pour autant sur-accentuer les détails déjà nets.
{{</ compare >}}
{{% /column %}}
</div>

<div class="row">
{{% column %}}
<h5>Débruitage</h5>
{{< compare after="denoise-after.jpg" before="denoise-before.jpg" cols="2" >}}
Supprimez le bruit chromatique, adoucissez et fusionnez le bruit de luminance.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Reconstruction des hautes lumières</h5>
{{< compare after="highlights-after.jpg" before="highlights-before.jpg" cols="2" >}}
Sauvez à la fois la couleur et la texture dans les hautes lumières, récupérez les zones brûlées en propageant les gradients pendant que le gamut-mapping surveille vos arrières en garantissant que les hautes lumières saturées peuvent toujours être imprimées à leur teinte d'origine. Vous n'êtes plus obligé de délaver les hautes lumières pour cacher les problèmes.
{{</ compare >}}
{{% /column %}}
</div>

### Fonctions spécialisées

<div class="row">
{{% column %}}
<h5>Correction automatique de la perspective</h5>
{{< compare after="perspective-after.jpg" before="perspective-before.jpg" cols="2" >}}
Laissez l'apprentissage machine détecter automatiquement les lignes verticales et horizontales et calculer la meilleure correction géométrique pour pivoter, redresser et recadrer l'image, en tenant optionnellement compte du type d'objectif utilisé.
{{</ compare >}}
{{% /column %}}

{{% column %}}
<h5>Censurer</h5>
{{< compare after="censorize-after.jpg" before="censorize-before.jpg" cols="2" >}}
Anonymisez facilement des gens, plaques d'immatriculation, etc. et jouez avec les conditions d'utilisation des réseaux socialement prudes sans trop défigurer vos images.
{{</ compare >}}
{{% /column %}}
</div>

{{< divider >}}


## Compatibilité

{{% row %}}
{{% card title="Edits" icon="desktop" %}}
Ansel est basé sur darktable 4.0 et est entièrement compatible avec les XMP de traitement et la base de données de darktable 2.x à 4.0. Vous venez de darktable ?
{{< button url="/fr/doc/special-topics/from-darktable/" label="Découvrez ce qui a changé" icon="sync" >}}
{{% /card %}}
{{% card title="Appareils photos" icon="camera" %}}
Ansel utilise Rawspeed et Libraw pour décoder les photos brutes. Les nouveaux appareils peuvent demander jusqu'à 24 mois après leur mise sur le marché pour être entièrement supportés.
{{< button url="https://rawspeed.org/CameraSupport.html" label="Appareils pris en charge" icon="wrench" >}}
{{% /card %}}
{{% card title="Langues" icon="language" %}}
Le logiciel est intégralement traduit en anglais, français et chinois simplifié. Des traductions partielles sont disponibles en allemand, espagnol, portugais, ukrainien, etc.
{{< button url="https://github.com/aurelienpierreeng/ansel/wiki/Translations" label="Améliorez les traductions" icon="comment" >}}
{{% /card %}}
{{% /row %}}

{{< divider >}}

## Darktable, mais en mieux

{{% row %}}

{{% column %}}

<div class="no-hyphenation lead">

Ansel est ce que Darktable 4.0 aurait pu être s'il n'était pas mort de [feature creep](https://en.wikipedia.org/wiki/Feature_creep).

</div>

Entre 2020 et 2023, Darktable a souffert d'[additions massives de code pour des fonctionnalités périphériques](./news/darktable-dans-le-mur-au-ralenti/), souvent mal codées, mal conçues et pénalisant l'utilisabilité, la performance et la maintenance. Trop de solutions de contournement ont échoué à corriger des bugs, mais ont empilé de nouveaux problèmes par dessus du code ancien : bienvenue dans un cauchemar de maintenance.

Sans gestion de projet ni planification des fonctionnalités, ce qui devait arriver a simplement fini par arriver. Darktable a toujours peiné à être plus qu'un pack de plugins individuels.

{{% /column %}}
{{% column %}}

Le résultat est une application bizarre et frustrante, qui essaie de réinventer les paradigmes GUI dans son coin, en essayant de tout faire pour tout le monde, plus lent et moins stable qu'avant, et absolument terrible à débugger.

Avec une interface centrée sur l'orienté scène, de nombreux modules fusionnés dans un menu global, un outil d'import réécrit et des recalculs du pipeline d'image plus économes, Ansel est une variante de Darktable 4.0 où 30 000 lignes de code mal écrit et de fonctionnalités à moité cassées ont été retirées, et 11 000 lignes ont été réécrites : __il s'exécute plus vite, il est plus réactif, utilise moins de puissance et requiert moins de configuration.__

Avec une complexité réduite du code, la maintenance devrait aussi être plus facile à l'avenir.

{{% /column %}}
{{% /row %}}

{{< divider >}}

## Au delà de la documentation

{{% row %}}
{{% column %}}

Le point de blocage typique et récurrent des projets logiciels open-source est la documentation. Quand il n'y a en pas, le utilisateurs s'en plaignent. Quand il y en a une, ils se plaignent qu'elle est trop longue, pas assez complète, ou qu'elle n'inclue pas d'exemples d'utilisation. Les développeurs s'attendent à ce que les utilisateurs fassent une lecture linéaire de la documentation du projet. Ça n'arrivera simplement pas, et les développeurs serviront de perroquets. Cela ne fait qu'alimenter la frustration des deux côtés. __La documentation ne suffit pas__.

{{% /column %}}
{{% column %}}

Chantal est un modèle de langage bilingue (français-anglais) entraîné spécifiquement pour le traitement d'image, la théorie de la couleur et la photographie, qui comprend le jargon technique, les synonymes et certaines traductions. __Son interface web permet de faire des recherches dans un index central__ composé de documentations de logiciels open-source, de rapport de bugs, de forums utilisateurs, de chaînes Youtube, de publications scientifiques et d'instances de standardisation (CIE, ICC, ACES).

{{% /column %}}
{{% /row %}}

<div class="text-center my-5">
<span class="display-5">Découvrez <a href="https://chantal.aurelienpierre.com" target="_blank">Chantal</a></span><br />
<span class="fs-4">votre bibliothécaire IA pour traitement d'image</span>
</div>

{{% row %}}
{{% column %}}

<div class="no-hyphenation lead mx-auto">

Chantal est l'infrastructure de connaissance d'Ansel :

- trouvez rapidement des informations pertinentes parmi des sources fiables,
- évitez de reposer des questions déjà traitées.

</div>

{{% /column %}}
{{% column %}}

<span class="no-hyphenation lead mx-auto">Conçu pour rendre les utilisateurs plus intelligents, au lieu de rendre le logiciel plus stupide.</span> L'intelligence artificielle vous procure du matériel d'apprentissage sur les sujets de votre choix. Investissez dans l'intelligence naturelle.

{{% /column %}}
{{% /row %}}

{{< divider >}}


## Il y a un concepteur à demeure ici

{{% row %}}
{{% column %}}

<div class="d-grid float-start me-4">
{{<figure src="Auto-portrait-0088-MLM_0774_01.jpg" style="width: 200px"/>}}
{{< button url="https://photo.aurelienpierre.com/portfolio" label="Portfolio photographie" icon="image" class="text-center w-100 mt-3">}}
{{< button url="https://eng.aurelienpierre.com" label="Blog d'ingénierie" icon="code" class="text-center w-100">}}
</div>


<div class="no-hyphenation lead">

Ça ne serait pas génial si les logiciels open-source avaient des concepteurs à temps plein, capables de prendre le temps nécessaire pour comprendre les problèmes et trouver des solutions simples, plutôt qu'empiler des bricolages rapides et des stratégies d'évitements, dans une base de code qui ne fait que grossir ?

</div>

La conception n'est pas se jeter sur un éditeur de code et en écrire autant que possible dans le moins de temps possible. En fait, c'est réfléchir beaucoup pour coder aussi peu que possible, parce que plus de code signifie plus de bugs.

Sur mes photos, je réalise le stylisme, le maquillage, l'éclairage, la capture, le traitement, la retouche, les filtres de couleur logiciels, la documentation pour les utiliser, le site web pour en parler en 2 langues, et même l'espace de couleur pour l'ajustement de la saturation. Vous trouverez _très_ peu de gens ayant cette compréhension de la lumière et de la couleur sur toute la chaîne qui sont aussi capables d'écrire des programmes informatiques efficaces et de lire des articles académiques de recherche en mathématiques appliquées. Pour une raison étrange, vous trouverez _beaucoup_ de gars essayant d'écrire des applications d'imagerie dans leur temps libre. Tirez-en vos propres conclusions.

{{% /column %}}
{{% column %}}

J'ai donné 4 ans de ma vie au projet Darktable, juste pour le voir détruit par des geeks désemparés qui jouent à accumuler du code pendant le week-end, chacun poussant ses propres intentions sans aucun sens du design, dans un projet où personne n'est responsable de rien et où on travaille trop vite sur tout en même temps.

Le dévelopment d'Ansel est fait à un rythme permettant d'assurer la qualité du code (backend) et de la conception (fontend). Le design est basé sur les retours utilisateurs que j'ai collecté en donnant des cours particuliers de retouche/traitement avec Darktable ces 3 dernières années, et sur les 2 enquêtes que j'ai menées en 2020 et 2022 sur les utilisateurs. Les priorités sont gérées considérant que le logiciel est un moyen d'exporter des images RAW, ce qui veut dire que la R&D est faite sur les sujets d'imagerie et que tout reste doit suivre les paradigmes courants d'interface graphique, sans se mettre en travers du chemin.


<div class="bg-white rounded border border-light p-3 lead shadow-sm">

Le développement d'Ansel prend une moyenne de 45 h/semaine pour moins que le salaire minimum. L'open-source a besoin de meilleures applications d'imagerie, ce qui requiert que quelqu'un ayant les compétences requises y mette le temps nécessaire. __Ansel a besoin de main d'œuvre et la main d'œuvre a besoin de payer ses factures__.

{{< button url="https://community.ansel.photos/donations-make" label="Soutenir le développement" icon="donate" class="d-block text-center mx-auto btn">}}

</div>

{{% /column %}}
{{% /row %}}

{{< divider >}}

## Code

Le logiciel et la documentation d'Ansel sont publiés sous licence GNU/GPL v3 et versionnés avec Git. Le site web est sous copyright mais le code est visible. Les dépôts de travail sont hébergés sur Github et dupliqués sur des miroirs Gitlab pour sauvegarde.

{{% row %}}

{{% card title="Logiciel" icon="desktop" %}}
Licence GNU/GPL v3.
{{< button url="https://github.com/aurelienpierreeng/ansel" label="Github (original)" icon="github fab">}}
{{< button url="https://gitlab.com/aurelienpierreeng/ansel" label="Gitlab (miroir)" icon="gitlab fab">}}
{{% /card %}}

{{% card title="Documentation" icon="book" %}}
Licence GNU/GPL v3.
{{< button url="https://github.com/aurelienpierreeng/ansel-doc" label="Github (original)" icon="github fab">}}
{{< button url="https://gitlab.com/aurelienpierreeng/ansel-doc" label="Gitlab (miroir)" icon="gitlab fab">}}
{{% /card %}}

{{% card title="Site web" icon="globe" %}}
Copyright.
{{< button url="https://github.com/aurelienpierreeng/ansel-website" label="Github (original)" icon="github fab">}}
{{< button url="https://gitlab.com/aurelienpierreeng/ansel-website" label="Gitlab (miroir)" icon="gitlab fab">}}
{{% /card %}}

{{% /row %}}

</div>
