---
title: Ansel target audience
date: 2024-07-14
weight: 2
---

As knowing the audience is the first step of design, it is useful to define it.

[The Darktable survey](https://eng.aurelienpierre.com/2023/01/who-are-the-darktable-users/) of 2020 showed an abnormal bias among users, favouring highly-educated men coming from technical and scientific background, and with higher programming skills than the average population. This is problematic because it does not overlap with the sociology of photographers at large (regarding computer skills as well as men/women ratio), but is a filtered subset of that social group.

Ansel expects its users to have

- an intermediate to advanced knowledge of __color theory__ (brightness vs. lightness vs. luminance, chroma vs. saturation, additive models, delta E, etc.), [^1]
- an intermediate to advanced knowledge of __cameras__ (ISO, dynamic range, exposure bias, etc.),[^2]
- an intermediate to advanced knowledge of __stage lighting__ (illuminant, CRI, cast shadows, inverse square law of lighting, etc.)

[^1]: See [Chris Brejon's website](https://chrisbrejon.com/) for the scope of this knowledge,

[^2]: See [DxO Mark website](https://dxomark.com) for the scope of this knowledge,

As such, Ansel does not target beginners and will be more (photography-wise) technical than proprietary competitors, which are frustrating to use for advanced users. That increased technical rootedness is meant to unlock more accurate and fine-grained control over image (especially color) manipulations, it is by no mean technics for the sake of it.

However, Ansel expects average computer-savvy users, with no scripting or programming skills. As such, tasks achieved through the command line interface or direct editing of configuration files should remain exceptionnal, alternative to GUI ways, and limited to advanced tasks.

Ansel does not aim at competing against commercial alternatives like Adobe Lightroom or Capture One. First of all, it would be pointless to compete against million-dollars companies with current resources. But then, those have made technical choices to be appealing to masses, only to ensure a large market share : they are actually quite limited, when you know what you are doing. Which is fine, because the users who are the most willing to pay high price don't.

## Values

### Users should not have to read the manual

_(Some restrictions apply)_

Image processing is hard. It uses notions of optics and color "science". No matter if you shoot digital or analog, _illuminant_, _dynamic range_, _gamut_ and _chroma_ will affect your process, in ways you may not have foreseen, and it might be a good idea to understand what they mean and where they come at play. Digital has its own lot of issues, from _color spaces & management_ to _alpha compositing_. Not much we can do here, except providing documentation : you need the skills. But that is, at least, the core basics of everything we do, no matter the software used.

Managing files and navigating in a graphical interface are things computer users have been doing for decades, using well-known paradigms that converged to pretty unified semantics. Users should not have to read a manual to discover why mouse scrolling is blocked, for example, or how to increase the opacity of a mask, or even what all those silly custom-drawn icons mean.

Users should not have to read the manual because, anyway, they won't. Instead, they will annoy developers with questions already answered somewhere on the extensive docs, which are too long to read because they have to explain why too much standard stuff is not handled in a standard way.

Acknowleging that, bad design loses the time of both users and developers, and it's time to cut the losses, for everybody's sake.

Now, trying to follow typical desktop GUI paradigms is fine for ubiquitous tasks, until you get into the core specifics of your particular application. There, trying to blindly follow paradigms enforced by industry-leading software working on different assumptions and in a different context is just a [cargo cult](https://en.wikipedia.org/wiki/Cargo_cult#As_a_metaphor) that will get in the way of actual productivity. This is no license to stupidly reproduce existing design without understanding the assumptions on which it is grounded.

### Simplifying is not making things easier

A violin is a simple instrument : 4 strings, some wood and a design that has barely changed since the 18th century. A piano is a complicated instrument and got recent innovations : 88 keys, 230 strings, a cast-iron frame on top of a wood table, wool felt everywhere, 3 pedals. Now, your first years of learning the piano will be much easier than your first decade of learning how to play a violin. Until you get to the point where Bach's fugues have 4 voices to play at the same time, or Chopin's studies will have you play chords over 3 octaves at 120 BPM, and you still have only 2 hands and one keyboard, but anyway…

The point is : the apparent simplicity of your instrument (aka the number of organs to interact with) has little to do with the actual easiness of playing it. And a picture-editing software is very much like a music instrument : it lets you manipulate technically a "material" medium for artistic purposes. Emphasis on the dichotomy between using technics to achieve art on a stupid medium that constantly gets in the way of your intents and abilities.

So, simplifying without stupidifying aims at reducing the number of steps needed to achieve a predetermined task. Or the depth of the clutter putting you in cognitive overload during said task. It has nothing to do with allowing you to skip class and use the instrument without prior knowledge.

Allowing users to use the instrument without knowledge nor training is turning a tool into a toy: remove everything possibly harmful or frightening, reduce features to the bare minimum, and put playfulness above the ability to solve problems. You do that when you want to sell many copies of your software, by enlarging your market shares to everybody willing to pose as a photographer without having the slightest idea of what they are doing. ~~Later on, you will force them to host their pictures on the cloud, only to fetch them to train your AI automagic, and sell them canned editings under the label "professional results"~~.

### The ability to learn is more important than being beginner-friendly

Technical names, such as methods or algorithms, are kept as they are published by their authors in the technical and scientific litterature. This allows to use any search engine to learn more about those methods, for example their strong and weak points, or the other competing methods available. It also allows to learn image editing tricks from books written on other software, provided those software abide by the same rule of using original names.

This is an unpopular design choice, as Adobe Lightroom has deliberately chosen to hide technical names, hereby locking users from further understanding… but also preventing any reverse-engineering attempt. Advanced Lightroom users will often try to infer what controls and settings actually do, often incorrectly from the visual feedback and limited theoritical knowledge they have, only to teach, preach and diffuse wrong knowledge.

I believe that keeping doors open to deepen user's understanding of image processing matters is a virtuous and empowering circle, even though it has a cognitive price to pay. Therefore, technics will not be hidden or renamed in GUI for the sake of being less frightening.
