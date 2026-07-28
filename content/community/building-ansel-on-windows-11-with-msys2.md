---
title: "Building Ansel on Windows 11 with msys2 and with Bitdefender "
date: 2024-03-28
slug: "building-ansel-on-windows-11-with-msys2"
tags:
  - Community archive
forum_author: "PhG44"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/building-ansel-on-windows-11-with-msys2"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/building-ansel-on-windows-11-with-msys2`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **PhG44** on 2024-03-28.*

Bonjour,

Depuis les dernières mises à jour, mon antivirus "Bitdefender Total Security" considère un fichier comme infecté et me le bloque, résultat je n'arrive plus à compiler Ansel . (remarque je n'ai pas ce souci sur mon ordinateur portable sous Ubuntu)

Sources obtenues depuis:

-  git clone --depth 1 https://github.com/aurelienpierreeng/ansel.git
- cd ansel
-  git submodule init
-  git submodule update

Puis mise à jour:

- *cd ~/ansel/ ;git checkout ;git fetch -v ; git pull -v*
- * cd ~/ansel/ ; rm -rf ./build; mkdir ./build ; cd ./build ; cmake -G Ninja -DCMAKE_BUILD_TYPE=Release -DBINARY_PACKAGE_BUILD=OFF -DCMAKE_INSTALL_PREFIX=/opt/ansel ../. ; cmake --build . && cmake --install . && cmake --build . --target package*

Le fichier C:\msys64\home\phg\ansel\build\CMakeFiles\CMakeScratch\TryCompile-c96dm8\cmTC_a8369.exe a été infecté par Gen:Variant.Tedy.532521. La menace a été bloquée avec succès et votre appareil est sain

Et suite à ce bloquage de l'anti-virus :

*-- Configuring incomplete, errors occurred!*

*ninja: error: loading 'build.ninja': Le fichier spÚcifiÚ est introuvable.*

Est-ce juste un excès de zèle de l'anti-virus, ou autre chose ?

A l'avance merci de votre aide

Bonne journée

Philippe

## Replies

**Aurélien Pierre** — 2024-03-29

Bonjour, c'est un faux positif.

---

**PhG44** — 2024-05-17

Merci, réponse tardive, désolé, cela confirme mes doutes, effectivement depuis que j'ai écarté le répertoire Ansel (la zone où je clone le dépôt git et compile), je n'ai plus de problème.

