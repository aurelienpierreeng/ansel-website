---
title: "Combien de partitions pour Ansel ?"
date: 2023-12-02
slug: "combien-de-partitions-pour-ansel"
tags:
  - Community archive
forum_author: "Hydrolivee"
forum_category: "Installing help"
forum_url: "https://community.ansel.photos/view-discussion/combien-de-partitions-pour-ansel"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/combien-de-partitions-pour-ansel`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Hydrolivee** on 2023-12-02.*

Bonjour, intéressé par le logiciel Ansel et avant de l'installer sous Linux, pourriez-vous m'indiquer toutes les partitions à créer lors de l'installation du système Linux en plus des partitions racine, home, +/- swap ? J'ai vu en effet qu'Ansel demande une configuration hardware relativement musclée. Peut-être qu'une création de partitions adéquates sur un lecteur SSD faciliterait le travail des photographies numériques ? Merci pour votre éclairage à ce sujet.

## Replies

**Julien FAUCHER** — 2023-12-10

Bonjour,

Je tiens à préciser que je ne suis pas familier avec le détail de la tambouille interne d'Ansel. Cependant il me semble que, d'un point de vue général (sans aller chercher le détail dans les perfs) Ansel n'a pas besoin d'une installation Linux "particulière" (sous-entendu vis-à-vis d'une installation classique). Il sera de toutes façons toujours bénéfique d'avoir les images sur un SSD pour les vitesses de chargement, mais je pense que la majorité du travail de retouche est fait en mémoire (RAM et/ou graphique). Du coup la particularité du disque dur n'a que peu d'impact sur la vitesse du traitement lui-même. Jusqu'à peu, je travaillais avec un HDD 7200tr/min de façon très satisfaisante.

Attention tout de même, lors de l'export des fichiers traités (écriture du résultat sur disque dur, donc) la vitesse de l'export sera probablement impactée par la technologie de disque. Personnellement, j'exporte rarement de très gros batchs de photos (ou j'ai un peu de temps devant moi), mais peut-être que c'est votre cas. De même, lors de l'import de photos, le traitement des miniature est peut-être impacté par les accès disques.

Du coup, en dehors de la configuration matérielle (quantité de RAM, modèle de carte graphique et probablement modèle de processeur) il ne me semble pas que la gestion de partitions soit particulièrement importante. Et dans tous les cas, il est toujours possible de monter un disque SSD sans que cela n'aie d'impact sur les partitions.

---

**Hydrolivee** — 2023-12-19

Bonjour, je vous remercie de votre commentaire à mon interrogation. Je vois, d'après votre retour, que le travail sur Ansel ne demande pas de partitionnement spécial de la distribution Linux. Travaillant sous Windows 7, je compte installer Ansel sur un SSD sous Ubuntu et donc créer un dual-boot Linux/Windows. En effet, le logiciel Ansel demande un O.S. windows 10 ou 11. Je dois par conséquence faire l'installation sous Linux. Cordialement.

---

**Aurélien Pierre** — 2024-01-15

Ansel fonctionne sous Windows 7, 10 et 11. Windows 7 n'est pas mentionné explicitement dans la doc parce que je n'avais pas assez de retours utilisateurs au moment de la rédaction pour confirmer le bon fonctionnement sous Win 7, mais a priori c'est bon.

