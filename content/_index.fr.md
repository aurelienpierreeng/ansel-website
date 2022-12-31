---
title: "Ansel"
date: 2022-11-27T22:36:34+01:00
draft: false
description: "Ansel est un éditeur de photos brutes pour artistes"
thumbnail: "https://user-images.githubusercontent.com/45535283/"
---

<div class="px-4 pt-5 my-5 text-center">
  <h1 class="display-4 fw-bold">Votre chambre noire numérique</h1>
  <div class="col-lg-6 mx-auto">
    <p class="lead mb-4"><em>Ansel</em> est un logiciel libre de traitement photo pour artistes digitaux, conçu pour vous aider à obtenir votre propre interprétation de photos numériques brutes.</p>
  </div>
  <div class="overflow-hidden" style="max-height: 65vh;">
    <div class="container px-5 my-5">
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
{{< button url="/" label="Instructions de compilation" icon="wrench" >}}
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

## What can Ansel for you ?
<hr>

### Color work

{{% row %}}
{{% column %}}
 ##### Color calibration
{{< compare after="/calibration-after.jpg" before="/calibration-before.jpg" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
 ##### Color-grading
{{< compare after="/grading-after.jpg" before="/grading-before.jpg" >}}
Donnez ambiance et caractère à vos photos en polissant leur palette de couleur avec des contrôles nuancés et détaillés, dans les espaces de couleur RVB, Ych ou HSB, à des fins créatives ou correctives.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

{{% row %}}
{{% column %}}
##### Color matching
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Hue qualifying and keying
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}
{{% /row %}}


### Tonal work

{{% row %}}
{{% column %}}
##### HDR tone mapping
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Zone-system editing
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
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

### Advanced features

{{% row %}}
{{% column %}}
##### Masking and blending
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Censoring
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
{{</ compare >}}
{{% /column %}}
{{% /row %}}
### Printing

{{% row %}}
{{% column %}}
##### Printer profiles
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}

{{% column %}}
##### Gamut mapping
{{< compare after="https://www.dropbox.com/s/h8rds5ozk0u3s2f/coder.jpg?raw=1" before="https://www.dropbox.com/s/pem8kaorr488apn/universe.jpg?raw=1" >}}
Fix white balance and get high-fidelity colors in just a few clicks, by calibrating colors with a Color Checker directly in the darkroom.
{{</ compare >}}
{{% /column %}}
{{% /row %}}

## Compatibility

{{% row %}}
{{% card title="Edits" icon="desktop" %}}
Ansel is based on darktable 4.0 and is fully compatible with XMP edits and database darktable 2.x up to 4.0 database and XMP files.
{{% /card %}}
{{% card title="Cameras" icon="camera" %}}
New cameras may need up to 24 months to be fully supported after their commercial release.
{{% /card %}}
{{% /row %}}

{{% /container %}}
