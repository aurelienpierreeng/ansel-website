---
title: "Diffusion et Netteté - Proposition d'interface alternative"
date: 2023-08-28
slug: "diffusion-et-netteté-proposition"
tags:
  - Community archive
forum_author: "Balistic"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/diffusion-et-netteté-proposition"
wayback_url: "https://web.archive.org/web/20250129091508/https://community.ansel.photos/view-discussion/diffusion-et-nettet%C3%A9-proposition"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/diffusion-et-netteté-proposition`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250129091508/https://community.ansel.photos/view-discussion/diffusion-et-nettet%C3%A9-proposition).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Balistic** on 2023-08-28.*

Bonjour tout le monde,  

Je propose ici une piste de réflexion pour une interface alternative simplifiée au module Diffusion ou netteté. 

1\) Ce n'est PAS une demande d'ajout. C'est juste **un début de discussion** dont beaucoup d'éléments sont encore à retravailler. Si des développeurs sont intéressés pour implémenter un truc semblable, tant mieux pour les autres. Sinon tant pis, moi je m'en sors très bien avec l'interface actuelle. 

2\) Ce n'est PAS un remplacement d'interface, mais un AJOUT d'une interface "simplifiée" qui vient se superposer au-dessus de l'interface actuelle (avancée). Exactement comme le module **Réduction de bruit** propose les interfaces **Moyennes non locales** et **Ondelettes**, auxquelles viennent se superposer les interfaces simplifiées **Moyennes non locales auto** et **Ondelettes auto**, dont les curseurs "Auto" vont juste modifier les paramètres des deux premières interfaces. 

3\) Les utilisateurs auraient donc le choix via menu déroulant (semblable à la réduction de bruit) entre les interfaces "**Simple**" et "**Avancé**". **Avancé** étant l'interface actuelle. **Simple** étant une interface plus "compréhensible" pour le non mathématicien, *mais qui ne permet PAS toute la finesse des réglages du mode Avancé* (c’est-à-dire que certaines combinaisons du mode Avancé ne seront pas possible en mode Simple).  

  

# **Utilisation**

1\) On choisit la taille des éléments (en pixels) sur lesquels on agit.

2\) On choisit si on **diffuse** ou si on **accentue**.

3\) On choisit la **force** de l'effet. Voilà, c'est le minimum syndical.

4\) Eventuellement, on affine ses réglages en augmentant le **temps de traitement**, en altérant la **direction** (= anisotropie) ou en choisissant une "**optimisation**" (j'ai pas encore trouvé de meilleur terme, voir plus bas).

  

# 

*\[attachment lost: image was hosted on the retired forum\]*

Description

Voici les éléments de l'interface Simple : 

### ** \[Interface\] :** Simple ou Avancé 

**Inferface** : Menu déroulant (semblable au choix de la réduction du bruit) (PAS des onglets, car les paramètres ne sont pas équivalents).  

**Choix : ** 

• **Avancé** = Interface actuelle de diffusion ou netteté. L'interface Avancé pilote directement le module tel qu'actuellement. 

• **Simple** = Interface "simplifiée" dont les réglages modifient les paramètres du mode Avancé. Le mode Simple ne pilote PAS directement l'algorithme du module, il modifie juste les paramètres du mode avancé (tout comme les réductions de bruit "auto" pilotent les moyennes non locales et ondelettes). Ce n'est pas bijectif : le mode Simple ne permet pas de récréer toutes les possibilités que le mode Avancé permet. Le mode Simple est également une bonne base pour qu'un débutant puisse choisir ses réglages, puis bascule sur le mode Avancé pour voir comment ses réglages ont été modifiés.  

  

### \* Taille des éléments à influer : de \[radius_min\] à \[radius_max\] pixels. radius_min et radius_max sont des entiers ≥ 0 avec radius_max ≥ radius_min 

**Interface** : Menu déroulants proposant par défaut les choix 0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024 et 2048. On peut effectuer un clic gauche ou droit pour entrer directement d'autres valeurs (comme dans le module Recadrer). C'est plus logique pour le débutant de comprendre "je vais influer les éléments de 128 à 896 pixels" plutôt que je vais influer les éléments de "512 ± 384 pixels" (et encore, ça c'est quand on a compris ce qu'étaient radius_center et radius. J'ai proposé menu déroulant, mais ça peut aussi être 2 barres avec curseurs, ou une barre avec 2 curseurs (ça dépend comment vous préférez gérer ça). 

**Calculs internes** : Modifie les paramètres radius_center et radius du mode avancé. 

Si **radius_min** = 0, alors : 

**radius_center** = 0 

**radius** = radius_max 

Si **radius_min** \> 0, alors : 

**radius_center** = (radius_max + radius_min)/2 

**radius** = (radius_max – radius_min)/2   

  

### \[Mode\] : Diffuser ou Accentuer

** Interface** : Menu déroulant  

**Commentaire** : Permet de choisir entre diffuser ou accentuer (netteté). D'après le dico, accentuer est bien l'antonyme de diffuser (plus juste que le terme netteté, car on peut accentuer la netteté ou le contraste local, on ne peut pas "netteter le contraste local"). Ce sera là l'une des limites du mode Basique ne permettra en effet que l'un ou l'autre (qui sont les cas les plus généraux) (enfin presque, voir plus bas). Pour des réglages différents (par exemple V3 en netteté et V4 en diffusion, se mettre en mode Avancé).  

**Choix** :  

• Diffuser : \[Mode\] = 1 

• Accentuer : \[Mode\] = -1   

### \[Force\] : Nombre à virgule, de 0 à l'infini. 

**Interface** : barre avec curseur. La valeur peut éventuellement être présentée en % (à discuter). 

**Commentaire** : détermine la force de l'effet. Plus on augmente, plus on diffuse ou accentue. Ce seul curseur Force va influer à la fois les vitesses (V1 à V4) et le nb d'itérations. C'est plus simple à comprendre pour le débutant  (ne demandez pas à un débutant de choisir entre vitesse et itérations, il veut juste que son effet soit plus fort ou moins fort).   

### \[Time\] Allonger le temps de traitement : Nombre à virgule, de 1 à l'infini 

**Interface** : barre avec curseur. La valeur peut éventuellement être présentée en % (à discuter). 

**Commentaire** : permet de déterminer si l'on souhaite privilégier la vitesse d'exécution (vitesses maximales, nb d'itérations minimales) ou laisser plus de temps (réduire la vitesse et augmenter le nb d'itérations) pour que l'effet soit éventuellement plus propre avec moins de divergences. Pour \[Time\] = 1, le module attribue la vitesse maximale possible et le nb minimal d'itérations possibles . En mettant des valeurs supérieures à 1, les vitesses sont alors réduites et le nb d'itérations est augmenté proportionnellement à \[Time\].  On part du principe que la vitesse et le nb d'itérations sont équivalents ( Vitesse \* Itérations = Force), ce qui est vrai dans une certaine mesure pour des petites valeurs mais faux quand on pousse les curseurs loin. Ce curseur \[Time\] est justement là pour réduire la vitesse au profit du nb d'itérations. 

Par exemple, pour une \[Force\] de valeur 5 (ou 500%) : 

• Time = 1 (ou 100%) : on aura 5 itérations avec une vitesse de 100% 

• Time = 1.2 (ou 120%) : on aura 6 itérations avec une vitesse de 83,3% 

• Time = 4 (ou 400%) : on aura 20 itérations avec une vitesse de 25% (on quadruple le temps de traitement mais on garde la même "force" globale).   

### \[Anisotropy_global\] Priorité : Nombre à virgule positif ou négatif de –10 à 10 (ou -1000% à +1000%) 

**Interface** : barre avec curseur.

J'hésite entre les dénominations : 

•  Affecter les bords \<=\> Affecter les surfaces (à l'intérieur des bords) ? 

• Affecter les bords \<=\> Affecter les dégradés ? 

• Prioriser les bords \<=\> Prioriser les surfaces ? 

• Prioriser les bords \<=\> Prioriser les dégradés ? 

**Commentaire** : Rien de spécial, il s'agit juste du même curseur Anisotropie que le mode Avancé, avec des dénominations plus claires. A ceci près qu'il n'y a qu'un seul curseur et qu'il affecte les 4 curseurs du mode avancé (dans la majorité des cas, ces 4 curseurs sont très souvent égaux. Si quelqu'un veut affiner les réglages, il basculera en mode Avancé. J'ai beau réfléchir dans tous les sens, décrire le curseur "anisotropie" au débutant reste tout de même difficile. Si quelqu'un a des meilleures idées... 

Autre remarque : certains pré-réglages (présets) de diffusion ou netteté utilisent des anisotropies différentes (défloutage par exemple qui utilse +100% pour V1 et V3 et 0% pour V2 et V4). Bah tant pis, on perdra un peu en exactitude en mode Simple en imposant la même anisotropie à toutes les vitesses mais on gagnera en simplicité. De toute façon, celui qui veut plus de finesse ira en mode Avancé. 

**Calculs internes** : Modifie les paramètres anisotropie du mode avancé : 

Anisotropy_first = anisotropy_second = anisotropy_third = anisotropy_fourth = anisotropy_global

### \[Optimisation\] : Menu déroulant à choix multiple

** Interface** : menu déroulant à choix multiple

**Commentaire** : C'est un paramètre qui permet de choisir entre différentes matrices de facteurs pour les vitesses V1 à V4 (pour ne pas forcément travailler sur les mêmes vitesses). Ca permet d'éviter de travailler tout le temps sur les mêmes vitesses et d'apporter un peu plus de finesse au mode Simple. J'hésite beaucoup pour le nom à donner à ce réglage et aux différents choix. Actuellement, ce qui m'a paru le plus simple à comprendre (pour le débutant) est de parler de différentes "optimisations", certaines pour le contraste local, d'autres pour la netteté ou le débruitage. Le débutant pourra choisir "l'optimisation" qui semble la plus adaptée à sa situation sans se poser plus de questions. S'il veut affiner ses réglagles =\> go mode Avancé. 

**Choix** : les matrices sont données dans l'ordre des facteurs V1 à V4. On respecte également le fait que V1+V2 et V3+V4 ne doivent pas dépasser 100%. De même, on permet ici la vitesse maximale possible (les vitesses sont ensuite réduites avec le curseur \[Time\] si besoin. Ce qui fait que qu'une même Force peut avoir plus ou moins d'effet selon l'optimisation choisie (d'un facteur 1 à 0.5) 

• Général : Optimisation = \[ 0.5  0.5  0.5  0.5 \]  

• Pour contraste local : Optimisation = \[ 1  0  0  1 \] 

• Pour netteté : Optimisation = \[ 0  1  1  1 \] 

• Pour Débruitage : Optimisation = \[ 1  0  1  0 \] 

• Pour effets rapides (Netteté ou contraste local) : Optimisation =  \[ 0  0  1  0\] 

• Pour suppression de la brume : Optimisation = \[ 1  -0.5  1  -0.5 \] 

• Pour défloutage : Optimisation = \[ 0.5  -0.25  1  -0.5 \] 

• Agir sur les détails fins : Optimisation = \[ 0  0  0.5  0.5 \] 

• Agir sur les détails grossiers : Optimisation = \[ 0.5  0.5  0  0 \] 

**Remarque :** j'espère beaucoup de commentaires et de retours de vous sur cette partie-là. Elle doit encore être peaufinée, voire complètement retravaillée.   

  

### \[Sharpness\] :

à retirer de l'interface Simple (de toute façon, ce n'est pas utilisé dans les pré-réglages). Elle sera disponible uniquement en mode "Avancé"  

### Edge sensitivity \[regularization\]

=\> à garder en renommant en **Protéger les bords **

###  Edge treshold  \[variance_treshold\]

=\> à garder en renommant en **Ignorer les surfaces lisses **  (si j'ai bien compris l'effet de ce paramètre ?)

### Luminance masking treshold \[treshold\]

=\> A retirer ou à garder ? Je pencherai pour le supprimer du mode Simple mais c'est à discuter (est-ce des gens s'en servent souvent ?)   

  

### Calculs internes supplémentaires :  

Le nombre d'itérations **\[iterations\]** est déterminé à partir des variables **\[Force\]** et **\[Time\]** (Allonger le temps de traitement) 

**• \[iterations\] = arrondi( Time \* Force )  **

(arrondi au plus proche tel que arrondi(1.49) = 1 et arrondi(1.5) = 2) 

Par exemple une force de 4 (400%) donne 4 itérations pour Time = 1 et 8 itérations pour Time = 2. 

Les vitesses V1, V2, V3 et V4 sont ensuite calculées en fonction du nb **\[iterations\]**, du signe de **\[Mode\]** (diffuser ou accentuer), de la **\[Force\]** voulue et du facteur d'**\[optimisation\]** (on comprendra que optimisation\[V1\] est le premier terme de la matrice opitmisation, etc.) 

• V1 : first = mode \* Force \* optimisation\[V1\] / iterations 

• V2 : second = mode \* Force \* optimisation\[V2\] / iterations 

• V3 : third = mode \* Force \* optimisation\[V3\] / iterations 

• V4 : fourth = mode \* Force \* optimisation\[V4\] / iterations 

  

# Exemples :

Voici ce que donneraient quelques présets existants en mode Simple. Je ne précise pas les paramètres Regularization et variance_treshold qui seront identiques au mode Avancé.  

**Le préset Contraste local donnerait ceci** :   

Interface = Simple 

Taille des éléments à influer = de 128 à 896 pixels 

Mode = Accentuer 

Force = 5 (ou 500%) 

Allonger le temps de traitement = 2 (ou 200%) 

Priorité = -250% (prioriser les bords) 

Optimisation = pour contraste local (matrice \[ 1  0  0  1 \] )  

  

** Le préset Netteté filtre AA donnerait ceci** :   

Interface = Simple 

Taille des éléments à influer = de 0 à 8 pixels 

Mode = Accentuer 

Force = 0.5 (ou 50%) 

Allonger le temps de traitement = 1 (ou 100%) 

Priorité = 100% (prioriser les surfaces/dégradés) 

Optimisation = Général (matrice \[ 0.5  0.5  0.5  0.5 \] )  

Commentaire : On doit mettre une force de 0.5 (et pas 0.25) car l'optimisation Général divise par 2 les vitesses.  

  

**Le préset Débruitage (Fort) donnerait ceci :  **

 Interface = Simple 

Taille des éléments à influer = de 2 à 14 pixels 

Mode = Diffuser Force = 1.6 (ou 160%) 

Allonger le temps de traitement = 20 (ou 2 000 %) 

Priorité = 200% (prioriser les surfaces/dégradés) 

Optimisation = Pour débruitage (matrice \[ 1  0  1  0 \] )  

Commentaire :  Iterations = arrondi(1.6 \* 20) = 32  V1 = 1 \* 1.6 \* 1 / 20 = 0.05 = 5% On retombe bien sur nos pattes. D'ailleurs, on voit qu'on pourrait réduire le temps de traitement à 1 (au lieu de 20) et avoir 2 itérations à V1 = 80% (donc on irait bien plus vite mais le résultat risque d'être beaucoup moins propre).

## Replies

**Balistic** — 2023-09-02

Quelques remarques supplémentaires :

# Interface

Le curseur "**Allonger le temps de traitement**" pourrait éventuellement être décalé plus bas dans les paramètres. A discuter. (Pour rappel, "Allonger le temps de traitement" va réduire les **vitesses d'ordre 1, 2 3 et 4** et augmenter en proportion le **nb d'itérations**, pour conserver une "**Force**" globale équivalente). Le but est d'augmenter le temps de calcul pour un effet plus propre.

*\[attachment lost: image was hosted on the retired forum\]*

  

  

# Calcul de radius et radius_center (correctif)

Je me suis rendu compte d'une erreur dans mes calculs de **radius** et **radius_center** : ceux-ci doivent être entiers !

Si par exemple l'utilisateur choisit d'influer les détails de 1px à 2px (radius_min = 1 px, radius_max = 2 px),on se retrouve avec :

- radius_center = (2 + 1)/2 = 1.5\[
- radius = (2 - 1)/2 = 0.5

Ce qui ne marche pas !

La valeur critique qui doit être respectée, c'est le radius_min (car plus petit, et si l'utilisateur sélectionne 1px, il veut 1px, pas 0px ou 2px !). On peut tolérer une marge d'erreur sur le radius_max (c'est bien moins grave, et l'erreur est proportionnellement inférieure à celle de radius_min.

Il faut donc plutôt utiliser les formules suivantes :

**Si radius_min = 0, alors** :

- radius_center = 0
- radius = radius_max

**Si radius_min \> 0, alors :**

- radius_center = arrondi.sup( (radius_max + radius_min)/2 )
- radius = arrondi.sup( (radius_max – radius_min)/2 )
- où l'on comprendra que arrondi.sup est l'arrondi à la valeur supérieure.

  

*Exemple : l'utilisateur choisit d'influer sur les détails de* ***3 à 8 pixels.***

*radius_center = arrondi.sup( (8+3)/2) = arrondi.sup( 5.5 ) = 6*

*radius = arrondi.sup( (8-3)/2 ) = arrondi.sup( 2.5 ) = 3*

*Le module diffusion et netteté influera donc en réalité sur les détails de* ***3 à 9 pixels.***

En gros, **on autorise (selon les valeurs choisies) une majoration de 1px sur le radius_max**. ça ne devrait pas fondamentalement changer le résultat (de toute façon, il est impossible de sélectionner exactement de 3 à 8 pixels en mode avancé).

---

**migmoq** — 2023-10-03

En effet, une interface simple pour les non matheux serait, de mon point de vue, intéressant. En tout cas, ce serait un bon moyen de poser le pied dans ce module.

Ce serait intéressant d'avoir l'avis d'﻿@Aurélien Pierre﻿ là dessus.

---

**Aurélien Pierre** — 2023-10-04

L'interface est jolie mais les maths ne pourront pas marcher comme ça.

Concernant les vitesses et directions, on est sur des effets non-linéaires dont les interactions ne peuvent pas être factorisées comme présenté ici et sont difficiles à prévoir.

Ensuite, la réécriture du filtre passe-bande de type gaussien en type "porte" ne marchera pas bien avec les mises à l'échelle de la prévisualisation, c'est la raison pour laquelle on utilise actuellement un filtre de type gaussien avec des coefficients ajustés pour le niveau de zoom.

De façon beaucoup plus pragmatique, avant de parler interface, j'aimerais d'abord faire une étude paramétrique d'apprentissage machine pour créer des profils. Le protocole serait le suivant :

1.  prendre une photo nette de référence à f/11,
2.  prendre des photos floues de la même scène, avec un flou de mise au point, un flou de mouvement, un flou de diaphragme,
3.  faire varier tous les paramètres du module à l'aveugle (brute-force) et enregistrer la sortie du module,
4.  mesurer l'erreur en norme L2, pixel à pixel, entre la photo nette de référence et chaque tentative de correction (ie chaque set de paramètres) par diffusion & netteté.

À partir de là :

1.  les réglages qui donnent la plus petite erreur pourront être enregistrés comme profil en pré-réglage,
2.  on pourra effectuer une [analyse de composantes principales](https://fr.wikipedia.org/wiki/Analyse_en_composantes_principales) permettant d'identifier les réglages dont l'effet est le plus significatif sur le résultat. À partir de là, on pourra peut-être réduire le problème actuel qui a une dizaine de dimensions à 2 ou 3 dimensions, et réduire l'interface à ces 3 réglages.

Mais attaquer le problème sous l'angle UI, c'est commencer par la fin. Dans tous les cas, je n'ai pas le temps pour ça en ce moment.

Pour info, l'analyse en composantes principales est utilisée dans [Chantal](https://chantal.aurelienpierre.com/?s=contraste&github=False&forums=False&method=1#search-form) pour produire le graphe en 2D des mots clés. Ils sont auparavant représentés dans un espace à 300D.

---

**migmoq** — 2023-10-05

Heu ... je serai assez intéressé de savoir quels outils tu vas utiliser pour faire un tel apprentissage non supervisé. Si je comprend bien, ton système d'apprentissage machine va devoir, à partir d'une matrice représentant une image floue donnée, faire varier les différents paramètres en jeu dans le module Diffusion et Netteté jusqu'à obtenir de lui même la plus petite différence d'avec la référence (la matrice de l'image nette) ; ce calcul d'erreur ressemble en fait à un calcul de similitude, non ?

---

**Aurélien Pierre** — 2023-10-06

Oui c'est un calcul de similitude si on veut, en fait il y a plein de métrique de similitude possible.

Je ne parle pas d'apprentissage machine ici, simplement de faire un balayage où l'on fait varier tous les paramètres de -1 à +1 par incrément de 0.1 (par exemple) et où on mesure la similitude en sortie. À la suite de quoi, on obtient erreur = f(paramètres), où paramètres est un vecteur de dimension 12 ou 15.

À partir de là, par analyse, on peut savoir s'il y a des paramètres dépendants (± une certaine erreur), donc redondants, donc les virer de l'interface allégée sans trop dégrader le résultat visuel. Et si on est chanceux, on peut essayer de réduire la dimensionnalité du problème pour réduire l'interface. Mais là, je suis seulement à l'étape "comprendre l'influence des paramètres" pour voir si des comportements répétables se produisent.

Le problème de la suggestion de notre ami @Balistic, c'est de postuler a priori des dépendances linéaires, alors qu'on en sait rien, et que des dépendances linéaires en 1D peuvent très bien devenir quadratiques en 2D (cf. l'interpolation bilinéaire : https://fr.wikipedia.org/wiki/Interpolation_bilin%C3%A9aire#:~:text=Contrairement%20%C3%A0%20ce%20que%20son%20nom%20sugg%C3%A8re%2C%20la%20fonction%20d%27interpolation%20n%27est%20pas%20bilin%C3%A9aire%20mais%20quadratique%2C%20qui%20peut%20se%20mettre%20sous%20la%20forme%C2%A0%3A). Sans parler qu'on est sur un problème inverse mal posé au sens de Hadamard (https://en.wikipedia.org/wiki/Well-posed_problem), puisqu'on cherche à inverser un processus de diffusion thermique.

Concernant l'outil en lui même, j'utile Scikit-learn : https://scikit-learn.org/stable/modules/generated/sklearn.decomposition.PCA.html

---

**migmoq** — 2023-10-06

Ha oui sklearn ... c'est un outil phare en IA avec Python. Je l'ai vue utilisé aussi en clustering de flux de données (CluStream, DenStream, etc.)

