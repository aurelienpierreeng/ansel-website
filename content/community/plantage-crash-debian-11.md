---
title: "Plantage/Crash Debian 11"
date: 2024-05-30
slug: "plantage-crash-debian-11"
tags:
  - Community archive
forum_author: "photux"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/plantage-crash-debian-11"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/plantage-crash-debian-11`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **photux** on 2024-05-30.*

Bonjour,

la version \`Ansel-0.0.0+748.g61eb388-x86_64.AppImage\` téléchargée ce matin plante sous Debian 11 Bullseye.

Lancée dans un Terminal, j'obtiens de nombreuses lignes d'erreur dont le point commun est l'absence de la GLIBC_2.3x.

Est-ce dû à ma distribution ou à d'autres causes ?

Merci

*Hello,*

*version \`Ansel-0.0.0+748.g61eb388-x86_64.AppImage\` downloaded this morning crashes under Debian 11 Bullseye.*

*When I run it in a Terminal, I get numerous error lines, all of which have GLIBC_2.3x missing.*

*Is this due to my distribution or to other causes?*

*Thanks*

## Replies

**Timothy White** — 2024-05-31

I had the same problem, and had to upgrade to Debian 12.

---

**photux** — 2024-05-31

> I had the same problem, and had to upgrade to Debian 12.

Hi,

thanks for the information. Upgrading my PC is actually a hard task for me, I'm a recent Linux user.

---

**Aurélien Pierre** — 2024-06-04

Les paquets AppImage n'ont aucune dépendance tierce… sauf une : Glibc, qui ne peut pas être incluse pour des raisons de compatibilité. Notre AppImage est compilé sur Ubuntu 22.04, qui utilise Glibc 2.35. L'AppImage ne fonctionnera que sur des systèmes qui ont au moins cette version.

Debian 11 date de 2021, c'est une distribution axée sur la stabilité, donc essayer d'y exécuter des logiciels récents est une contradiction dans les termes.

---

**photux** — 2024-06-04

Bonjour,

merci Aurélien pour les précisions. La version 2.31 de glibc est la seule proposée pour cette version de Debian. Je ferai le nécessaire avec Debian 12. Je comprends la cohérence de ce système, je n'ai en effet aucune raison de me précipiter.

