---
title: "Problème avec le module de retouche pour effacer une tâche - Problem with the retouch module to erase a spot"
date: 2024-04-10
slug: "problème-avec-le-module-de-retouche-pour"
tags:
  - Community archive
forum_author: "Bild"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/problème-avec-le-module-de-retouche-pour"
wayback_url: "https://web.archive.org/web/20250120201437/https://community.ansel.photos/view-discussion/probl%C3%A8me-avec-le-module-de-retouche-pour"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/problème-avec-le-module-de-retouche-pour`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250120201437/https://community.ansel.photos/view-discussion/probl%C3%A8me-avec-le-module-de-retouche-pour).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Bild** on 2024-04-10.*

Bonjour à tous, 

Je constate un comportement étrange (peut être un bug). 

J'essaie d'enlever une tâche avec le module retouche sur une photo RAW (RW2).

Pour cela, je sélectionne un cercle de retouche que je positionne sur la tâche, ensuite je repositionne un cercle sur la source, puis j'effectue une retouche en copiant /collant la source vers la cible (J'ai aussi essayé avec l'outil de correction.)

Dans Ansel (1ière capture d'écran), je constate que la tâche n'est pas systématiquement retouchée et parfois oui après plusieurs tentatives de retouche qui se superposent.

*\[attachment lost: image was hosted on the retired forum\]*

Dans Darkatble (2ième capture d'écran), je constate que la retouche se fait correctement et de manière plus fluide.

*\[attachment lost: image was hosted on the retired forum\]*

Que pouvez vous faire pour m'aider? 

Au delà de ce constat, quelles sont les données (des logs) qui vous permettrait de comprendre ce qu'il se passe ? 

Bien cordialement

------------------------------------------------------------

Hello everyone,

I'm seeing strange behavior (maybe a bug).

I'm trying to remove a spot with the retouching module on a RAW photo (RW2).

To do this, I select a retouching circle that I position on the spot, then I reposition a circle on the source, then I perform a retouch by copying/pasting the source to the target (I also tried with the fix tool.)

In Ansel (1st screenshot), I notice that the spot is not systematically erased and sometimes it's erased after several overlapping retouching attempts.

*\[attachment lost: image was hosted on the retired forum\]*

In Darkatble (2nd screenshot), I see that the editing is done correctly and more fluidly.

*\[attachment lost: image was hosted on the retired forum\]*

What can you do to help me?

Beyond this observation, what data (logs) would allow you to understand what is happening?

Best regards

## Replies

**JVO** — 2024-04-21

Bonjour,

Je constate le même problème. La correction de tâches avec le module Retouche de ma version applmage d'Ansel est sans effet. Sommes nous seuls à galérer. Quelle peut être la solution?

D'avance merci

---

**Aurélien Pierre** — 2024-06-04

Ce sont les effets de bord d'un travail en cours qui vise à utiliser correctement le cache du pixelpipeline. Darktable s'en tire en purgeant le cache intégralement, ce qui le rend en grande partie inutile. Les soucis sont réglés module par module, du plus général au plus particulier, et le module retouche est très particulier dans sa conception.

Déjà rapporté ici : https://github.com/aurelienpierreeng/ansel/issues/310

---

**Bild** — 2024-06-04

Merci Aurélien pour ce retour. Je vais m'y remettre et tester la nouvelle version.

---

**Aurélien Pierre** — 2024-06-04

Pour être clair, ce n'est pas encore réglé dans retouche parce que c'est le dernier (avec liquify) que je regarderai.

---

**Bild** — 2024-06-05

C'est pas grave. Je teste qd meme

---

**Dom** — 2024-06-06

En solution de contournement : GIMP

- Outils - Outils de peinture - Clonage (Maj+C)
- Filtres - Carte - Resynthesizer
- Filtres - G'MIC - Repair - Inpaint (5 modules)

Gimp est bien documenté sur le web.

---

**Bild** — 2024-09-09

Hello Aurélien,

Est ce que vous avez pu avancer sur ce bug ? Quel est le statut de ce bug ?

par avance merci

Bien cordialement

