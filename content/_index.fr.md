---
title: "Ansel"
date: 2022-11-27T22:36:34+01:00
draft: false
description: "Ansel est un éditeur de photos brutes pour artistes"
thumbnail: "https://user-images.githubusercontent.com/45535283/"
---

<div class="pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold">Votre chambre noire numérique</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4"><em>Ansel</em> est un logiciel libre de traitement photo pour artistes digitaux, conçu pour vous aider à obtenir votre propre interprétation de photos numériques brutes.</p>
  </div>
  <div class="overflow-hidden" style="max-height: 65vh;">
    <div class="container my-5">
      <img src="/main-screenshot-fr.jpg" class="img-fluid shadow-lg mb-4" alt="Ansel screenshot" width="1000" loading="lazy">
    </div>
  </div>
</div>

{{% container %}}

{{% row %}}
{{% column %}}
Il s'inscrit dans la lignée de <a href="https://wikipedia.org/wiki/Ansel_Adams">Ansel Adams</a>, pianiste et photographe, qui a poussé l'artisanat de la chambre noire comme jamais pour servir sa vision photographique.
{{% /column %}}
{{% column %}}
<figure class="text-left">
<blockquote class="blockquote">
  <p>Le négatif est la partition, le tirage est l'interprétation.</p>
</blockquote>
<figcaption class="blockquote-footer">
  <cite title="Ansel Adams">Ansel Adams</cite>
</figcaption>
</figure>
{{% /column %}}
{{% /row %}}
{{< divider >}}

## Installer

<hr>

{{% row %}}
{{% card icon="linux fab" title="Linux" %}}
Exécutable indépendant de la distribution
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/lin-nightly/master/ansel.stable.AppImage.zip" label="Télécharger ansel.appimage" icon="download" >}}
{{% /card %}}

{{% card icon="windows fab" title="Windows" %}}
Installeur Windows 10 & 11
{{< button url="https://nightly.link/aurelienpierreeng/ansel/workflows/win-nightly/master/ansel.stable.win64.zip" label="Télécharger ansel.exe" icon="download" >}}
{{% /card %}}

{{% card icon="terminal" title="Build from source" %}}
Les meilleurs performances pour votre matériel
{{< button url="/fr/doc/install" label="Instructions de compilation" icon="wrench" >}}
{{% /card %}}
{{% /row %}}

<strong>Configuration minimale recommandée</strong> : Processeur Intel i5 (4 cores) / RAM 8 Go / Carte graphique Nvidia GTX 850.

{{< divider >}}

## Pourquoi Ansel ?
<hr>

{{% row %}}
{{% column p=true %}}
De nombreuses solutions existent pour produire des photographies prêtes à consommer pour les masses, des filtres de smartphones aux JPEG produits par les appareils photo, suivis récemment par la magie des IA appliquant des filtres jouets ~~caricaturaux~~ dramatiques. Tout ça rend la photographie plus facile que jamais, mais les images produites sont-elles réellement __vos__ images et, dans les cas, les images que __vous__ attendiez ?
{{% /column %}}
{{% column p=true %}}
Appuyer sur le déclencheur de l'appareil photo a seulement démarré un processus se terminant quand l'image à l'écran ressemble à celle que vous aviez à l'esprit. _Ansel_ propose de remettre les artistes au centre du processus créatif et leur fournit une interface pour manipuler des images avec précision et nuance, en utilisant une science de la couleur à la pointe et des contrôles de couleur indépendants.
{{% /column %}}

{{% /row %}}
<hr>


{{% row %}}
<p class="no-hyphenation lead text-left mx-auto my-3 col-10"><em>Ansel</em> vous permet d'interpréter vos photos brutes comme un instrument de musique, là où la plupart des logiciels essaient de jouer la partition automatiquement à votre place, mais mécaniquement et sans âme.</p>
{{% /row %}}
{{< divider >}}

## Que peut Ansel pour vous ?
<hr>

Ansel vous permet de gérer vos collections d'images, de traiter vos fichiers numériques bruts de capteur et vos pellicules numérisées, et d'exporter le résultat vers les formats de fichiers courants. Il stocke votre historique de traitement sous forme de texte et vous permet de remonter dans le temps à n'importe quelle étape de votre traitement, à tout moment.

### Travail sur la couleur

Ansel embarque une science de la couleur récente et compatible HDR : l'adaptation chromatique CIE CAT 2016, l'espace de couleur HDR JzAzBz (2017) et l'espace de couleur perceptuel darktable UCS 2021, développé spécialement pour manipuler la saturation des couleurs en évitant l'effet fluo.

{{% row %}}
{{% column %}}
 ##### Calibration des couleurs
{{< compare after="/calibration-after.jpg" before="/calibration-before.jpg" >}}
Corrigez la balance des blancs et obtenez des couleurs haute fidélité en seulement quelques clics, en étalonnant les couleurs avec un Color Checker directement en chambre noire.
{{</ compare >}}
{{% /column %}}

{{% column %}}
 ##### Gradation des couleurs
{{< compare after="/grading-after.jpg" before="/grading-before.jpg" >}}
Donnez ambiance et caractère à vos photos en polissant leur palette de couleur avec des contrôles nuancés et détaillés, dans les espaces de couleur RVB, Ych ou HSB, à des fins créatives ou correctives.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

{{% row %}}
{{% column %}}
##### Correspondance de couleur
{{< compare after="/matching-after.jpg" before="/matching-before.jpg" >}}
Forcez l'adaptation chromatique de sorte que n'importe quel objet sélectionné corresponde à une couleur prédéterminée, saisie à partir de ses coordonées CIE Lab (pour les logos ou les couleurs de marques commerciales), ou en échantillonnant la couleur du même objet dans une autre photo, pour obtenir un rendu des couleur uniforme sur une série.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Qualificateurs de teinte et fusion
{{< compare after="/masking-after.jpg" before="/masking-before.jpg" >}}
Utilisez les qualificateurs de teinte, chroma et luminosité pour définir rapidement des masques, et appliquer des effets sélectifs. Combinez les masques paramétriques avec des masques dessinés avec des opérations booléennes. Raffinez et détaillez les bords des masques par floutage ou détection de bords intelligente.
{{</ compare >}}
{{% /column %}}
{{% /row %}}


### Travail sur les tonalités

Les méthodes de travail sur les tonalités sont conçues pour manipuler la luminance sans affecter la teinte ni la saturation, afin de respecter le travail sur la couleur, effectué à part.

{{% row %}}
{{% column %}}
##### Mappage de ton HDR
{{< compare after="/filmic-after.jpg" before="/filmic-before.jpg" >}}
Récupérez les ombres denses et compressez la plage dynamique tout en gardant la saturation et la teinte d'origine, avec un mappage de gamut pour garantir que les couleurs tiennent dans l'espace de couleur de sortie. _(Photo : Andreas Schneider)_
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Traitement basé sur le _zone system_
{{< compare after="/toneeq-after.jpg" before="/toneeq-before.jpg" >}}
Équilibrez les densités par zone de lumination, en préservant le contraste local grâce à un algorithme de détection des bords, et sélectionnez les zones de lumination à affecter directement dans l'image via le curseur interactif. _(Photo : Andreas Schneider)_
{{</ compare >}}
{{% /column %}}
{{% /row %}}

### Reconstruction d'image

{{% row %}}
{{% column %}}
##### Défloutage d'objectif
{{< compare after="/sharpen-after.jpg" before="/sharpen-before.jpg" >}}
Libérez le pouvoir de l'apprentissage machine basée sur l'analyse de gradients multi-échelle pour rajeunir les vieux objectifs, récupérer les erreurs de mise au point ou renforcer votre sujet, mais sans les artefacts de bord typiques, les bizarreries de sur-accentuation ou le bruit additionnel.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Désembuage
{{< compare after="/dehaze-after.jpg" before="/dehaze-before.jpg" >}}
Restaurez une certaine profondeur dans les clichés brumeux et flous en ramenant des textures et de la saturation dans les couleurs, sans pour autant sur-accentuer les détails déjà nets.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

{{% row %}}
{{% column %}}
##### Débruitage
{{< compare after="/denoise-after.jpg" before="/denoise-before.jpg" >}}
Supprimez le bruit chromatique, adoucissez et fusionnez le bruit de luminance.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Reconstruction des hautes lumières
{{< compare after="/highlights-after.jpg" before="/highlights-before.jpg" >}}
Sauvez à la fois la couleur et la texture dans les hautes lumières, récupérez les zones brûlées en propageant les gradients pendant que le gamut-mapping surveille vos arrières en garantissant que les hautes lumières saturées peuvent toujours être imprimées à leur teinte d'origine. Vous n'êtes plus obligé de délaver les hautes lumières pour cacher les problèmes.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

### Fonctions spécialisées

{{% row %}}
{{% column %}}
##### Correction automatique de la perspective
{{< compare after="/perspective-after.jpg" before="/perspective-before.jpg" >}}
Laissez l'apprentissage machine détecter automatiquement les lignes verticales et horizontales et calculer la meilleure correction géométrique pour pivoter, redresser et recadrer l'image, en tenant optionnellement compte du type d'objectif utilisé.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Censurer
{{< compare after="/censorize-after.jpg" before="/censorize-before.jpg" >}}
Anonymisez facilement des gens, plaques d'immatriculation, etc. et jouez avec les conditions d'utilisation des réseaux socialement prudes sans trop défigurer vos images.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

## Compatibilité

{{% row %}}
{{% card title="Edits" icon="desktop" %}}
Ansel est basé sur darktable 4.0 et est entièrement compatible avec les XMP de traitement et la base de données de darktable 2.x à 4.0. Vous venez de darktable ?
{{< button url="/fr/doc/special-topics/from-darktable/" label="Découvrez ce qui a changé" icon="sync" >}}
{{% /card %}}
{{% card title="Appareils photos" icon="camera" %}}
Les nouveaux appareils peuvent demander jusqu'à 24 mois après leur mise sur le marché pour être entièrement supportés.
{{< button url="https://rawspeed.org/CameraSupport.html" label="Appareils pris en charge" icon="wrench" >}}
{{% /card %}}
{{% /row %}}



{{% /container %}}
