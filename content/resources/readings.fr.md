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

Il faut mentionner que l'aspect scientifique a été aussi étudié par des artistes (comme [Munsell](https://en.wikipedia.org/wiki/Munsell_color_system)). La discipline mélange des notions de physique (spectre lumineux, là où tout commence), biologie et médecine (cellules rétiniennes, nerf optique et cerveau, c'est à dire le capteur humain), psychologie (mémoire de la couleur et images rémanentes), histoire de l'art (harmonies colorées) et ethnologie (signication culturelle des couleurs).

### Pièges à éviter

L'essentiel du discours sur la couleur se concentre sur des modèles d'apparence des couleurs en 3D : teinte-chroma-clarté ou teinte-saturation-luminosité. Il s'agit simplement de décomposer la couleur en 3 propriétés absolues qui devraient idéalement être totalement indépendantes les unes des autres, car ceci serait pratique pour les applications concrètes dans le monde réel.

Le problème est que la vision n'est pas absolue mais sujette aux interférences avec l'arrière-plan et l'environnement. Le même patch de couleur affiché sur différents fonds (de couleur et d'illumination variables) apparaîtra différent. Mais la vision est également sensible au contraste local et aux motifs répétitifs, et des preuves scientifiques suggèrent qu'elle est bien plus liée à des phénomènes d'opposition des couleurs (c'est à dire à des stimuli soustractifs) qu'à des intensités absolues (stimuli additifs).

C'est la raison pour laquelle, dans les industries des média et de l'imprimerie, l'évaluation des couleurs est réalisé en conditions standard : lumière D50 ou D65, arrière-plan et environnement gris moyen, lumière incidente de luminance 100 à 300 Cd/m². Le problème est que tout cela ne tient toujours pas compte des effets du contenu de l'image elle-même, car la même robe rouge peut paraître très différente vue contre un ciel bleu, un mur gris ou un feuillage vert, même si vous avez éliminé tous les effets possibles de l'éclairage ambiant.

Tandis que les modèles d'apparence des couleurs essaient d'éliminer la contribution de nombreux paramètres pour tenter de trouver des dimensions de la couleur vraiment indépendantes, nous devons garder à l'esprit que leurs hypothèses de base ne peuvent êtres validées dans les conditions réelles, et leur utilisabilité pratique dans le monde réel est limitée. Dans tous les cas, les modèles sont des réductions mathématiques de réalités bien plus complexes afin d'être calculables. Et les 3 dimensions de la couleur ne sont pas réellement indépendantes.

### À quel point la théorie de la couleur est-elle utile ?

Les retoucheurs d'images, artistes digitaux et autres pousseurs de pixels traitent des images encodées en tant que signaux RVB. Celles-ci sont des signaux additifs qui ont du sens dans des pipelines d'imagerie commençant avec des capteurs qui accumulent des photons et finissant avec des panneaux LED qui émettent des photons. Rien de tout ça n'est directement lié à la mécanique réelle de la vision humaine. C'est en réalité beaucoup plus proche de la physique de la lumière.

L'histoire de l'art a été écrite en grande partie par des peintres qui travaillaient avec des pigments, par natures soustractifs. Plusieurs siècles avant que Newton n'observent la diffraction de la lumière par des prismes (les couleurs de l'arc en ciel), ils étaient capables de restituer la peau et la chair humaine avec une incroyable maîtrise, sans avoir les connaissances que nous avons actuellement, et en utilisant un schéma de mélange des pigments qui n'a rien à voir avec la vision humaine.

La théorie de la couleur n'est pas un pré-requis pour faire de l'art, et certainement pas pour faire de l'art de qualité. Mais…

La théorie de la couleur fournit des noms à mettre sur des phénomènes que nous vivons quotidiennement et qui sont pour la plupart profondément contre-intuitifs. Si vous avez déjà rencontré des gens qui ont souffert des mois et des années sans que le personnel médical ne soit capable de diagnostiquer précisément leur maladie, vous savez à quel point il est important de pouvoir nommer la maladie, même si aucun traitement n'est disponible.

Les retoucheurs d'images souffrent d'utiliser des outils de manipulation de la couleur qui ne se comportent pas comme la vision humaine. Vous pouvez additionner des lumières, vous pouvez additionner des pigments, mais vous ne pouvez pas additionner des teintes car elles sont entièrement un produit du système cognitif humain. Mélanger des lumières et des pigments ayant une teinte originale donnée ne produira pas une teinte résultante facile à prévoire à la fin. La théorie de la couleur fournit des concepts pour comprendre ces déviations et pour mieux les gérer, c'est à dire pour donner du sens à ce que vous voyez, au-delà de ce qui se passe en poussant des curseurs dans une interface graphique.

## Références

Malheureusement pour les francophones, l'information de qualité en théorie de la couleur est exclusivement en langue anglaise, qui est également la langue de la recherche scientifique. Les ressources francophones disponibles sont peu nombreuses et le peu qu'il y a est de mauvaise qualité. Le reste de cet article sera donc dans la langue des publications référencées…

### Color science

Color Appearance Models, 3rd Edition. Mark D. Fairchild. 2013.
: Mark Fairchild is professor at the Rochester Institute of Technology (closely tied to Munsell legacy and located in the neighbourhood of the Eastman Kodak company). The  Chapters 1 to 9 list the different aspects of vision and adaptation, along with the parameters affecting it and the color terminology. The 9 central chapters detail the typical industry-ready color appearance models, with implementation details that will only interest engineers. The last 3 chapters treat matters such as color management and color reproduction that may interest any graphic artist. [Publisher website](https://www.wiley.com/en-us/Color+Appearance+Models%2C+3rd+Edition-p-9781119967033)

Colour : sense and measurement. Richard Kirk. 2022.
: Richard Kirk holds a PhD in physics and has worked at Filmlight UK research and development since the 1980's. Filmlight is best known for its film digitization workflow (software and hardware) and its Baselight color grading software, used by most Hollywood movie productions to fine-tune the color look. Kirk is the co-author of the color-grading "tRGB" space used in Ansel [color balance](/en/doc/modules/processing-modules/color-balance-rgb/) module and presented in the book (p. 79). The book itself is made available free of charge, as a PDF, so I will not expand on its content here : have a look for yourself. Just know that it is fairly accessible to non-technical people, well illustrated, and covers both film and digital imaging, with their relationships. [Download the PDF](https://www.filmlight.ltd.uk/support/documents/colourbook/colourbook.php).

The dimensions of color. David Briggs. [Website 1](http://www.huevaluechroma.com/). [Website 2](https://sites.google.com/site/djcbriggs/life-drawings-2).
: David Briggs is a member of the Colour Society of Australia and teacher at the National Art School and University of Technology in Sydney. As a drawer and painter, his publications give an useful insight on the interconnections between color theory and pigments mixing practice.
