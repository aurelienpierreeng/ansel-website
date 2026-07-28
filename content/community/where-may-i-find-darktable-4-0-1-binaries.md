---
title: "Where may I find darktable 4.0.1 binaries for linux mint/ubuntu?"
date: 2023-05-22
slug: "where-may-i-find-darktable-4-0-1-binaries"
tags:
  - Community archive
forum_author: "ariznaf"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/where-may-i-find-darktable-4-0-1-binaries"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/where-may-i-find-darktable-4-0-1-binaries`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **ariznaf** on 2023-05-22.*

I am currently using Ansel in linux mint as my main development program, in fact I am using is exclusively.

But it lacks some things I would like to use from time to time as the maps module to add gps info to my photos choosing location on a map.

I would like to use darktable for that situations, but I would like to share the database with ansel, so I cannot use the last version, but 4.0.1

The problem is that in darktable web they provide links to install it in binary form opensuse.org but they seem to provide only binaries for the last version.

Where can I find them?

I don't like to compile from sources if possible.

I have tried installing it using apt but there seems to be only verion 3.8 and 4.2 in the standard packages.

## Replies

**bridgemen** — 2023-05-22

Hello there, which version of linux mint do you use ?

I am using mint 21.1 (vera) (ubuntu base 22.04), and I have darktable 4.2.1 is installed (.deb) from:

https://software.opensuse.org/download.html?project=graphics:darktable&package=darktable

There are 4 entry's for Ubuntu (base for mint), maybe You find what you need ?

I also use ansel as the first package to use and darktable to compare with.

Greets, Eric.

---

**ariznaf** — 2023-05-22

Thank you for your response and time.

I am using Vera too, the last version.

Yes that is the source for binaries it seems they use that site to generate the binaries for multiple Linux distribution.

But 4.2 is not compatible at database level with Ansel.

And I could not find 4.0 link their in opensuse.

Have you found a link for it?

EDIT

Thank you, the link you have provided seems to include deb packages to 4.0 too, I had not found it previously in the link provided to opensuse in darktable site.

  

I will try that package.

---

**ariznaf** — 2023-05-22

Well, I have downloaded the darktable .deb package and tried to install it via gdebi and dpkg.

But there are broken dependencies.

They complain about libicu71 liblensfun1:amd and libopenexr-3-1-30 not been installed.

I have tried to install them via apt install but it complains about not being able to locate the package.

---

**bridgemen** — 2023-05-23

Hello,

I do see that the darktable version 4.0.1 for Ubuntu 22.10 is proposed in that link. I don't know if that darktable version would work in Ubuntu 22.04, so linux mint 21.1 (vera).

I hope that the "map module" will soon become available in ansel, because I also use it to fill in the lat-long coordinates, in darktable and not yet in ansel.

I can't think of anything else to help further, sorry.

---

**ariznaf** — 2023-05-23

Thank you, I could not find the way to install the deb packages and its dependencies.

  

I suppose the only way would be to compile from source, but it does not sound easy as you would need to compile all dependencies too.

---

**bridgemen** — 2023-05-23

Yeah, compiling from source is indeed not as simple as some play with it ... Me, I like most the deb packages to install, and I 'm used to follow the most standard linux setup, without the bling bling of the latest software, stability is most usefull and at ease to live with.

---

**bridgemen** — 2023-05-25

Hi again, I searched with the following string "darktable 4.0.1" and found this:

https://github.com/darktable-org/darktable/releases/download/release-4.0.1/darktable-4.0.1.tar.xz

I did not compiled this on my system, but maybe it does work for you ??

Greets, Eric.

---

**ariznaf** — 2023-05-25

Yes I had found and discovered that.

But it seems to be a snapshot of the sources and you need to compile everything.

I don't know if it includes the dependencies.

If I don't find binaries will try to compile that (would need a compile environment)

---

**ariznaf** — 2023-05-26

I could finally get darktable 4.0.1 installed using flatpak, as there seems to be no apt source for that version that can be installed in current linux mint/ubuntu releas directly.

Compiling from source requires donwnloading and compiling sources for the old dependencies.

I am not fan of the flatpak way, but it fits situations like this where there are many dependencies or incompatibilities with current versions of libraries in your system.

You can install it using the flatpak command and pointing it to flathub repository.

Flathub does not guarantee storing all versions or the time it would store available ones.

You can list the available versions and the list of commits uploaded to flathub using this command:

\`\`\`

flatpak remote-info --log flathub org.darktable.Darktable

\`\`\`

The commit for the 4.0.1 version (2022-9-18) Is: ffe32b5c29648562b2c400c4bf3df2832ca165a216ea6292e5a741f7e353955b

It seems you cannot install directly the commit you want (install subcommad does not admit commit option), but yo can install the last version and then downgrade to the commit you want using:

\`\`\`

sudo flatpak install org.darktable.Darktable

sudo flatpak update --commit=ffe32b5c29648562b2c400c4bf3df2832ca165a216ea6292e5a741f7e353955b org.darktable.Darktable

\`\`\`

After that you have version 4.0.1 of darktable installed in your system as al flatpak package.

---

**Aurélien Pierre** — 2023-05-28

The map module is still in Ansel and can be re-enabled in preferences -\> views.

---

**ariznaf** — 2023-05-28

I have enabled it (as I showed in the other thread) but there is no such option after restart.

I am using the Ansel version downloaded as appimage (0.0.0+285)

