---
title: "Lectures en théorie de la couleur"
date: 2023-03-20
draft: false
weight: 10
authors: ["Aurélien Pierre"]
---

Quelles ressources peuvent être trouvées en ligne et dans les bibliothèques pour aider à comprendre _un peu_ de théorie de la couleur ?

<!--more-->

## Préambule

### Qu'est-ce que la théorie de la couleur ?

La théorie de la couleur a 2 aspects :

* __scientifique__, lié historiquement à la physique de la lumière, mais à présent d'avantage apparenté à la psychologie, qui essaie de relier les signaux physiques avec des stimuli sensoriels,
* __artistique__, qui étudie la sémantique de la couleur (essentiellement culturelle) et comment elle agit pour créer des ombrages crédibles en peinture ou des ambiances dans les photographies et le cinéma.

Il faut mentionner que l'aspect scientifique a été aussi étudié par des artistes (comme [Munsell](https://en.wikipedia.org/wiki/Munsell_color_system)). La discipline mélange des notions de :

* physique (spectre lumineux, là où tout commence),
* biologie et médecine (cellules rétiniennes, nerf optique et cerveau, c'est à dire le capteur humain),
* psychologie (mémoire de la couleur et images rémanentes),
* histoire de l'art (harmonies colorées),
* ethnologie (signication culturelle des couleurs).

Chaque auteur n'étant typiquement un expert que dans un seul de ces domaines, bien qu'ayant besoin des autres, il est souvent utile de savoir à l'avance sous quel angle il va traiter le sujet, et à quel moment il risque de sortir de sa spécialité.

### Pièges à éviter

L'essentiel du discours sur la couleur se concentre sur des modèles d'apparence des couleurs tridimensionnels : teinte-chroma-clarté ou teinte-saturation-luminosité. Il s'agit basiquement de décomposer la couleur en 3 propriétés absolues qui devraient idéalement être totalement indépendantes les unes des autres, ce qui serait pratique pour les applications concrètes dans le monde réel.

Le problème est que la vision n'est pas absolue mais sujette aux interférences avec l'arrière-plan et l'environnement. Le même patch de couleur affiché sur différents fonds (de couleur et d'illumination variables) apparaîtra différent. Mais la vision est également sensible au contraste local et aux motifs répétitifs, et des preuves scientifiques suggèrent qu'elle est bien plus liée à des phénomènes d'opposition des couleurs (c'est à dire à des stimuli soustractifs) qu'à des intensités absolues (stimuli additifs).[^2]

[^2]: Pour vous en convaincre, visitez [ce site web](https://www.echalk.co.uk/amusements/OpticalIllusions/colourPerception/colourPerception.html), qui montre des illusions d'optique où des patchs gris placés dans un environnement bleu paraissent jaunes, et réciproquement.

Lorsqu'on parle de modèle teinte-chroma-clarté, par exemple, on implique que les couleurs sont évaluées contre un fond blanc, tel que présenté dans le [nuancier de Munsell](https://fr.wikipedia.org/wiki/Nuancier_de_Munsell#/media/Fichier:Munsell_Books.jpg). Le modèle devient passablement erroné dans tout autre contexte, en particulier parce que la chroma contribue à la perception de luminosité ([effet Helmholtz-Kohlrausch](https://en.wikipedia.org/wiki/Helmholtz%E2%80%93Kohlrausch_effect)), ce dont la clarté ne tient pas compte.

C'est la raison pour laquelle, dans les industries des média et de l'imprimerie, l'évaluation des couleurs est réalisé en conditions standard : lumière D50 ou D65, arrière-plan et environnement gris moyen, lumière incidente de luminance 100 à 300 Cd/m². Le problème est que tout cela ne tient toujours pas compte des effets du contenu de l'image en elle-même, car la même robe rouge peut paraître très différente vue contre un ciel bleu, un mur gris ou un feuillage vert, même si vous avez éliminé tous les effets possibles de l'éclairage ambiant.

Tandis que les modèles d'apparence des couleurs essaient d'éliminer la contribution de nombreux paramètres pour tenter de trouver des dimensions de la couleur vraiment indépendantes, nous devons garder à l'esprit que leurs hypothèses de base sont rarement validées dans les conditions réelles, et leur utilisabilité pratique dans le monde réel est limitée. Dans tous les cas, les modèles sont des réductions mathématiques de réalités bien plus complexes afin d'être calculables. Et les 3 dimensions de la couleur ne sont pas réellement indépendantes.

### À quel point la théorie de la couleur est-elle utile ?

Les retoucheurs d'images, artistes digitaux et autres pousseurs de pixels traitent des images encodées sous forme de signaux RVB. Ceux-ci sont des signaux additifs qui ont du sens dans des pipelines d'imagerie commençant avec des capteurs qui accumulent des photons et finissant avec des panneaux LED qui émettent des photons. Rien de tout ça n'est directement lié à la mécanique réelle de la vision humaine : c'est en réalité beaucoup plus proche de la physique de la lumière.

L'histoire de l'art a été écrite en grande partie par des peintres qui travaillaient avec des pigments, par nature soustractifs. Plusieurs siècles avant que Newton n'observe la diffraction de la lumière par des prismes (les couleurs de l'arc en ciel), ils étaient capables de restituer la peau et la chair humaine avec une incroyable maîtrise, sans avoir le dixième des connaissances que nous avons actuellement, et en utilisant un schéma de mélange des pigments qui n'a rien à voir avec la vision humaine.

La théorie de la couleur n'est donc pas un pré-requis pour faire de l'art, et certainement pas pour faire de l'art de qualité. Mais…

La théorie de la couleur fournit des noms à mettre sur des phénomènes que nous vivons quotidiennement et qui sont pour la plupart profondément contre-intuitifs. Si vous avez déjà rencontré des gens qui ont souffert des mois et des années sans que le personnel médical ne soit capable de diagnostiquer précisément leur maladie, vous savez à quel point il est important de pouvoir nommer la maladie, même si aucun traitement n'est disponible.

Les retoucheurs d'images souffrent d'utiliser des outils de manipulation de la couleur qui ne se comportent pas comme la vision humaine. Vous pouvez additionner des lumières, vous pouvez additionner des pigments, mais vous ne pouvez pas additionner des teintes car elles sont entièrement un produit du système cognitif humain. Mélanger des lumières et des pigments ayant une teinte originale donnée ne produira pas une teinte résultante facile à prévoire à la fin. La théorie de la couleur fournit des concepts pour comprendre ces déviations et pour mieux les gérer, c'est à dire pour donner du sens à ce que vous voyez, au-delà de ce qui se passe en poussant des curseurs dans une interface graphique.

### Colorimétrie ou sciences de la couleur ?

La colorimétrie est une branche à part des sciences de la couleur, qui s'intéresse à _mesurer_ la couleur, ce qui n'est pas loin d'être une contradiction dans les termes, car la couleur est une perception et qu'on ne peut guère mesurer les perceptions sensorielles sans violer les règles d'éthique de la recherche sur patients vivants.

On nomme [colorimètre](https://en.wikipedia.org/wiki/Tristimulus_colorimeter) un capteur trichromatique qui satisfait au critère de Maxwell-Luther-Ives, c'est à dire que ses "couleurs primaires" permettent d'exprimer tout spectre lumineux visible par une combinaison linéaire. Je vous épargne les détails mathématiques, retenez simplement que tout capteur photographique n'est pas automatiquement un colorimétre, et introduit donc des erreurs de mesure qu'on appelle [métamérisme](https://en.wikipedia.org/wiki/Metamerism_(color)#Metameric_failure), qui seront bien embêtantes pour reproduire fidèlement les couleurs. En pratique, seuls les capteurs servant à l'étalonnage de la chaîne graphique se rapprochent du critère de Maxwell-Luther-Ives.[^1]

[^1]: D'après l'article [_What is the space of spectral sensitivity functions for digital cameras_](http://www.gujinwei.org/research/camspec/camspec.pdf), par Jun Jiang, Dengyu Liu, Jinwei Gu and Sabine Süsstrunk (2013), ce sont les appareils Canon qui sont les plus proches des conditions de Maxwell-Luther-Ives (deux fois meilleurs que les Hasselblad), mais une recherche croisée sur [DXOMark](https://www.dxomark.fr/Cameras/) indique que cette colorimétrie améliorée se fait au détriment du bruit en basse lumière. Les monstres d'ISO actuels ont donc vraisembablement sacrifié beaucoup de précision dans la couleur pour gagner en sensibilité.

L'objectif final de la colorimétrie n'est pas d'étudier la vision humaine, ni d'en comprendre le fonctionnement, mais de fournir des outils optiques, mathématiques et des métriques d'erreur (comme le delta E) qui permettent de profiler et de corriger la restitution des couleurs sur des systèmes d'affichage et de reproduction d'images, ou d'en effectuer le contrôle qualité. La colorimétrie est donc une discipline d'ingéniérie, avec tous les compromis pratiques que cela suppose, pas une science.

Le terme _colorimétrie_ est improprement utilisé par toutes sortes de charlatans, pour désigner toutes sortes de choses n'ayant rien à voir, car il sonne scientifique tout en contenant le mot-clé "couleur", connoté artistiquement.

## Références

Malheureusement pour les francophones, l'information de qualité en théorie de la couleur est exclusivement en langue anglaise, qui est également la langue de la recherche scientifique. Les ressources francophones disponibles sont peu nombreuses et le peu qu'il y a est de mauvaise qualité, quand elles ne véhiculent pas carrément des énormités. Le reste de cet article sera donc dans la langue des publications référencées…

### Color science

_Fundamentals, concepts and terminology of colo(u)r._

Color Appearance Models, 3rd Edition. Mark D. Fairchild. 2013.
: Mark Fairchild is professor at the Rochester Institute of Technology (closely tied to Munsell legacy and located in the neighbourhood of the Eastman Kodak company). The  Chapters 1 to 9 list the different aspects of vision and adaptation, along with the parameters affecting it and the color terminology. The 9 central chapters detail the typical industry-ready color appearance models, with implementation details that will only interest engineers. The last 3 chapters treat matters such as color management and color reproduction that may interest any graphic artist. [Publisher website](https://www.wiley.com/en-us/Color+Appearance+Models%2C+3rd+Edition-p-9781119967033)

Colour : sense and measurement. Richard Kirk. 2022.
: Richard Kirk holds a PhD in physics and has worked at Filmlight UK research and development since the 1980's. Filmlight is best known for its film digitization workflow (software and hardware) and its Baselight color grading software, used by most Hollywood movie productions to fine-tune the color look. Kirk is the co-author of the color-grading "tRGB" space used in Ansel [color balance](/en/doc/modules/processing-modules/color-balance-rgb/) module and presented in the book (p. 79). The book itself is made available free of charge, as a PDF, so I will not expand on its content here : have a look for yourself. Just know that it is fairly accessible to non-technical people, well illustrated, and covers both film and digital imaging, with their relationships. [Download the PDF](https://www.filmlight.ltd.uk/support/documents/colourbook/colourbook.php).

The dimensions of color. David Briggs. [Website 1](http://www.huevaluechroma.com/). [Website 2](https://sites.google.com/site/djcbriggs/life-drawings-2).
: David Briggs is a member of the Colour Society of Australia and teacher at the National Art School and University of Technology in Sydney. As a drawer and painter, his publications give an useful insight on the interconnections between color theory and pigments mixing practice.

### Color pipelines

_How digital images are handled in your computer from start to finish_

The Hitchhiker's Guide to Digital colour. Troy Sobotka. [Website](https://hg2dc.com/)
: I have worked with Troy for years — he has basically helped most open-source software projects to unfuck their color pipelines in the past decade (at least the ones who accepted they had a problem whether or not they saw it) — and he is the original author of Filmic for Blender. We share the same passion for calling bullshit bullshit and idiots idiots. The HG2DC website is a step-by-step walk through computer graphics with lots of pictures and video animations explaining where, why and what happens to your RGB pixels.

The Computer Graphics Cinematography Book. Chris Brejon. [Website](https://chrisbrejon.com/cg-cinematography/)
: Chris has worked at 5 of the most prominent movie studios in the world, over the past 13 years, as a lighting and compositing artist. Although the book focuses on cinematography, the chapters on color management, composition, lighting and color theory apply directly to photography as well (though the workflow changes a bit).

### 2D painting and 3D rendering

_Constructing images from scratch_

Marco Bucci's YouTube channel. [Website](https://www.youtube.com/channel/UCsDxB-CSMQ0Vu_hTag7-2UQ)
: Marco Bucci is a painter and shows how he constructs his paintings, most importantly how he shades subjects to give depth to 2D paintings. This is highly interesting because photographers just capture what is there, and can afford to never bother about the "true", "desired" and "believable" colors of a shadow. Since painters (and 3D artists) create everything from scratch, they have to ask themselves what color it should be. Give a good binge to his channel, I promise you will never look at a drop shadow the same way. _(You may need to discard some of his color theory explanations though, they are often inaccurate)_.

### Visual illusions

_Witnessing the gullibility of our own perceptual system is key to anticipating problems in real-world applications_

The illusory staircase Gelb effect. [Website](http://www.psy.ritsumei.ac.jp/~akitaoka/illgelbe.html)
: Repeating the same grey or colored patch over a gradient changes the percieved color of the patch, in addition of the typical Mach banding effect (see below).

Color and Contrast. Nate Baldwin. [Website](https://colorandcontrast.com/)
: Many visual effects and illusions demonstrated, involving local contrast illusions. The website focuses on user interface design and aims at demonstrating the origin of best practices, but the demonstrations are relevant for any audience.

Optical Illusions. R. Beau Lotto. [Website](https://www.echalk.co.uk/amusements/OpticalIllusions/colourPerception/colourPerception.html)
: Witness the impact of different surround brightness and hue on color patches that are exactly similar.


### Color-grading

_Correcting or introducing color shifts to ensure consistent look between pictures and create some ambiance_

Color Correction Handbook (vol. 1) / Color Correction Look Book (vol 2). Alexis Van Hurkman. 2013. [Google Play vol. 1](https://books.google.fr/books?id=kDcdAgAAQBAJ). [Google Play vol. 2](https://books.google.fr/books?id=Hm9VAgAAQBAJ)
: These books have a special place in Darktable/Ansel history because I used them as a reference to redesign the features of the [color balance](/en/doc/modules/processing-modules/color-balance-rgb/) module. While they focus on color grading for movies, they are software-agnostic (showing how to get things done in different applications), and make use of color tools like RGB curves, color balance, channel mixer and 3D LUTs that are all available in Ansel. They contain valuable insight on how to (and why) create color looks in images, to put the form at the service of the content. I recommend you get digital copies of them because they have lots of illustrations that will be rendered on screen better than what printed paper allows.

### News and insights

_Staying up-to-date with color stuff, technical analyses and other myths debunking about color_

Colour science library, blog. [Website](https://www.colour-science.org/blog/)
: The colour-science project provides a Python library with many color models and other numeric tools for engineers and researchers working on color and vision. I use it extensively, in particular to create color sweeps and other graphs on this website. While this will not interest end-users, the blog of the project contains well-documented and useful insights on matters like color calibration and lighting.
