---
title: "Importation des photos depuis un disque USB externe"
date: 2024-07-24
slug: "importation-des-photos-depuis-un-disque"
tags:
  - Community archive
forum_author: "Dom_Ansel"
forum_category: "Configuring help"
forum_url: "https://community.ansel.photos/view-discussion/importation-des-photos-depuis-un-disque"
wayback_url: "https://web.archive.org/web/20241210172136/https://community.ansel.photos/view-discussion/importation-des-photos-depuis-un-disque"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/importation-des-photos-depuis-un-disque`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20241210172136/https://community.ansel.photos/view-discussion/importation-des-photos-depuis-un-disque).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Dom_Ansel** on 2024-07-24.*

Bonjour, je suis sous Ubuntu 24.04 et je n'arrive pas à importer mes photos dans Ansel. Mon disque USB externe n'est pas accessible via Ansel. Il est bien monté, accessible via fichiers et fonctionne normalement via Darktable!

Ansel n'a pas la permission d'y accéder. Message en pièce jointe.

## Replies

**ClaudeJeannaux** — 2024-12-23

Bonjour à tous je suis confronté au même problème. Est-ce que vous avez pu régler celui-ci Je suis avec Ubuntu 22.04.5 LTS. Tous les disques dur connectés ne sont pas accessible avec Ansel.

---

**Aurélien Pierre** — 2025-01-07

Ansel utilise la couche d'abstraction GVFS pour accéder aux stockages externes. Il est nécessaire que les paquets correspondant soient installés sur vos systèmes, incluant les drivers pour les protocoles SMB, WebDAV, FTP, MTP, PTP etc. si les supports de stockage externes les utilisent.

GVFS est installé par défaut sur le bureau Gnome et sur la plupart des bureaux basés sur Gtk, mais pas forcément tous ses drivers. Il faut l'installer manuellement sur les autres bureaux, notamment ceux basés sur Qt.

