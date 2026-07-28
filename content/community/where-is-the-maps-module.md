---
title: "Where is the maps module?"
date: 2023-05-19
slug: "where-is-the-maps-module"
tags:
  - Community archive
forum_author: "ariznaf"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/where-is-the-maps-module"
wayback_url: "https://web.archive.org/web/20231001125440/https://community.ansel.photos/view-discussion/where-is-the-maps-module"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/where-is-the-maps-module`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001125440/https://community.ansel.photos/view-discussion/where-is-the-maps-module).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **ariznaf** on 2023-05-19.*

I like to add the gps location of some of my photos.

In darktable there was de map module that let you do it.

In Ansel modules seem to be named ateliers, and many are hidden by default, but may be activated in preferences/other views.

I have activated print, map and slideshow views.

Print and slideshow do work, map is not listed in the ateliers menu even being activated.

Is this a bug?

Where is the map view?

## Replies

**martin** — 2023-05-24

Works for me in Ansel version 0.0.0+285, Win10.

Edit \> Preferences \> other views \> Enable the map view - activate

Even if I do not use the Location/Map very often it is very usefull to me when needed.

Would be really nice to keep that feature in future Ansel.

AtB

Martin

---

**ariznaf** — 2023-05-24

I am using the appimage in Linux mint.

  

I have activated the map view in config but there is no map option in atelier menu.

  

I will look at the version and if there is a new one.

---

**ariznaf** — 2023-05-24

Well I have downloaded last version in appimage (0.0.0+285) and installed it.

I have run it and checked that map view is enabled in the configuratin.

But map view does not show in the atelier menu yet (I have reinitiated Ansel, just in case).

May be you need something more installed in the system?

May be it does not work in linux?

Is anyone using it in linux?

---

**martin** — 2023-05-25

I tried running the Appimage xxx.285 on Ubuntu and indeed, no Map Atelier running. But i was surprised to find the Print Atelier working, which is not visible in Win10 Version xxx.285 of Ansel.

AtB

martin

---

**ariznaf** — 2023-05-25

Print module never worked in windows.

There was no print module in the windows version of darktable in any versions.

The reason (if I remember it well) is that it uses cups and it is not available in windows, windows and linux manage printing quite differently.

What surprises me is that maps seems to work in windows but it is not available in linux.

---

**martin** — 2023-05-25

> Print module never worked in windows.

  

Did not know that. Never missed it.

Thanks for the hint!

AtB

martin

---

**Aurélien Pierre** — 2023-05-28

You need to restart the software after you enable the map view in the preferences.

---

**ariznaf** — 2023-05-28

Thank yo but I have activated it several days ago and restarted Ansel many time, no map module there.

  

I am using the downloaded appimage 0.0.0+285 in linux mint vera.

This are the options in preferences

*\[attachment lost: image was hosted on the retired forum\]*

And this the Atelliers menu after restart

*\[attachment lost: image was hosted on the retired forum\]*

---

**Aurélien Pierre** — 2023-05-28

Ok so that would suggest that some map library dependency is not properly embedded into the AppImage. You will need to install it on your system for the time being.

My money is on the package `libosmgpsmap-1.0-dev`. Can you try to install it or something similar (check for "OSM GPS MAP", with or without spaces, in your package manager) ? It doesn't have to be the version 1.0 exactly.

---

**ariznaf** — 2023-05-28

You seem to be right, a friend that compiles from sources said me it worked for him and it seems to work in windows.

I have installed the library using apt and now it works, so it seems it was a missing dependency in the appimage.

Please if you correct it in the next version tell us in order to remove that library (by the way it seems to be quite a big bunch of related libraries).

---

**Aurélien Pierre** — 2023-05-28

What is and is not embedded in the AppImage is defered to an automatic script to follow dependencies, issues with partial Lensfun embedding have already been reported, so OSM will be part of the same task of manually boundling missing libs.

---

**bridgemen** — 2023-05-29

Hello,

I have installed libosmgpsmap-1.0-dev as Aurélien proposed earlier in this thread, tested both last appimage and compiled version, and there is the map view available and working. Linux mint 21.1 cinnamon.

ps: need to restart after changes in preferences ...

Greets, Eric.

---

**Aurélien Pierre** — 2023-06-09

The missing dependency (libosmgpsmap) is now bundled in the AppImage (thanks ﻿@Alynx Zhou﻿), along with other missing dependencies, so everything should work as intended.

---

**ariznaf** — 2023-06-09

Thank you.

I have uninstalled the maps library from my system and all related libraries, and the new appimage seems to wok with the map module, so the problem is solved.

I think the thread can be closed.

