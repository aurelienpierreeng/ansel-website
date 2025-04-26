---
title: Color theory readings
date: 2023-03-20
draft: false
weight: 10
authors:
    - Aurélien Pierre
---

What resources can be found online and in libraries to help understand _some_ color theory ?

<!--more-->

## Preamble

### What is color theory ?

Color theory has 2 aspects :

* a __scientific__ one, historically linked to light physics, but now related more closely to psychology, trying to link physical signals with perceptual stimuli,
* an __artistic__ one, studying color semantics (which are mostly cultural) and how they play in creating believable shadows in paintings or moody ambiance into photographs and movies.

It is worth noting that the scientific side has been studied by artists too (like [Munsell](https://en.wikipedia.org/wiki/Munsell_color_system)). The field mixes notions of :

* physics (light spectrum, where everything begins),
* biology and medicine (retina cells, optical nerve and brain, that is the human sensor),
* psychology (color memory and afterimages),
* art history (color harmonies),
* ethnology (cultural meaning of color).

Every author being typically an expert in only one of those fields, but still needing the others, it is often useful to know beforehand from what vantage point he will treat the subject, and at which point he might not be at home anymore.

### Pitfalls

Most color talk focuses on tri-dimensional models of color appearance : the hue-chroma-lightness, or the hue-saturation-brightness. That is basically color split into 3 absolute properties that would ideally be completely independent from each other, because it would be mathematically practical for real-world applications.

Problem is, vision is not absolute but subjected to the interference of the background and surrounding. The same color patch displayed on different backgrounds (varying color and illumination) will appear differently. But vision is also very sensitive to local contrast and patterns, and scientific evidence suggests that it is actually much more about color opponency (that is, subtractive stimuli) than about intensities (additive stimuli).[^2]

[^2]: To convince yourself, visit [this website](https://www.echalk.co.uk/amusements/OpticalIllusions/colourPerception/colourPerception.html), showcasing optical illusions where grey patches put in a blue surround appear yellow, and vice versa.

When we talk about the hue-chroma-lightness model, for instance, we imply that colors are evaluated against a white background, as in the [Munsell book](https://fr.wikipedia.org/wiki/Nuancier_de_Munsell#/media/Fichier:Munsell_Books.jpg). This model becomes fairly wrong in any other context, in particular because chroma contributes to the perception of brightness ([Helmholtz-Kohlrausch effect](https://en.wikipedia.org/wiki/Helmholtz%E2%80%93Kohlrausch_effect)), which is discarded by the lightness.

This is why, in the printing and media industries, color assessment is realized in standardized conditions : D50 or D65 lighting, middle-grey background and surround, 100 to 300 Cd/m² of incident light luminance. The problem is this still doesn't account for the effect of the image content itself, because the same red dress may appear quite different against a blue sky, a grey wall, or a green foliage, even when you have discarded the possible effects of the surround lighting.

As the color appearance models try to discard many parameters to try to find truly independent color dimensions, we need to keep in mind that their base assumptions are rarely found in real settings, and that their real-life useability is limited. In any case, models are mathematical reductions of much more complex realities for the sake of being computable. And the 3 color dimensions are actually not fully independent.

### How useful is color theory ?

Image retouchers, digital artists and other pixels pushers deal with images encoded as RGB signals. Those are additive signals that make sense in imaging pipeline starting with sensors gathering photons and ending with LED panels emitting photons. But none of that is directly linked to the actual mechanics of human color vision : it is actually much closer to basic light physics.

For most of art history, painters have worked with pigments, which are subtractive in nature. Centuries before Newton observed light diffraction (rainbow colors) through prisms, they were able to mix pigments as to render human skin and flesh with incredible mastership, without nearly as much knowledge as we have now, and using a color mixing scheme that has nothing to do with actual vision.

Color theory is thus not a requirement to make art, let alone to make good art. But…

Color theory provides names to put on phenomena we experience daily and that are for the most part deeply counter-intuitive. If you have ever met people who suffer great pain for months and years while the medical staff is unable to diagnose precisely what disease they have, you know how important it is to them to simply have a name to put on that disease, no matter if there is a cure or not.

Image retouchers suffer from using color manipulation tools that simply don't behave according to color vision. You can add lights, you can add pigments, but you can't add hues because hues are entirely a product of the human cognitive system. Mixing lights and pigments of a certain original hue will not produce an easily-predictable hue at the end. Color theory provides concepts to understand those deviations and to better handle them, that is, to make sense of what you see beyond what you do when pushing GUI sliders.

### Colorimetry or color sciences ?

Colorimetry is a special branch of color sciences, which aims at _measuring_ color, and this is short from being a contradiction in terms, because color is a perception and we can't really measure perceptions without violating the ethical rules of research on living patients.

We call [colorimeter](https://en.wikipedia.org/wiki/Tristimulus_colorimeter) a sensor that satisfies the Maxwell-Luther-Ives condition, meaning its "primaries" allow to express any light spectrum as a linear combination. I will spare you the maths details, just remember that any random photographic sensor is not automatically a colorimeter, and therefore introduces measuring errors called [metamerism](https://en.wikipedia.org/wiki/Metamerism_(color)#Metameric_failure), which will be very annoying when trying to accurately reproduce colors. In practice, only sensors used for calibration of the graphic chain will be close to the Maxwell-Luther-Ives condition.[^1]

[^1]: From the paper [_What is the space of spectral sensitivity functions for digital cameras_](http://www.gujinwei.org/research/camspec/camspec.pdf), by Jun Jiang, Dengyu Liu, Jinwei Gu and Sabine Süsstrunk (2013), the Canon cameras are the closest from the Maxwell-Luther-Ives condition (twice as good as the Hasselblad), but a cross-search on [DXOMark](https://www.dxomark.fr/Cameras/) indicates that this improved colorimetry is done at the expense of low-light noise. The current ISO beasts have most likely sacrificed a lot of color accuracy to win on sensitivity.

The final goal of colorimetry is not to study human vision, nor to understand its behaviour, but to provide optical and mathematical tools, as well as error metrics (like the delta E) allowing to profile and to correct color rendering on display and image reproduction systems, but also to perform quality control and management. Colorimetry is therefore an engineering field, with all the practical compromises it implies, not a science.

The _colorimetry_ term is improperly used by all sorts of scammers to designate unrelated things, because it sounds scientific while still containing the artsy-connotated "color" keyword.

## References

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
