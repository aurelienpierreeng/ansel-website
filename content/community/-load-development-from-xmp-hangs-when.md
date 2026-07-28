---
title: "'Load development from xmp' hangs when done in darkroom"
date: 2023-05-25
slug: "-load-development-from-xmp-hangs-when"
tags:
  - Community archive
forum_author: "ariznaf"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/-load-development-from-xmp-hangs-when"
wayback_url: "https://web.archive.org/web/20231001124105/https://community.ansel.photos/view-discussion/-load-development-from-xmp-hangs-when"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/-load-development-from-xmp-hangs-when`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20231001124105/https://community.ansel.photos/view-discussion/-load-development-from-xmp-hangs-when).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **ariznaf** on 2023-05-25.*

Ansel version: 0.0.0+285

OS version: linux mint Vera 21.1 Cinnamon.

graphics driver: nivida-driver-530 (propietary driver).

OpenCL in use.

  

How to reproduce the bug (if it is a bug):

1.  Open a photo in the darkroom.
2.  open the duplicate manager at the left panel.
3.  Select Original to create a duplicate with neutral development.
4.  Select the menu option 'Edit/Load development from xmp' and select another xmp of other photo (or a previously xmp generated from the same photo).
5.  After that Ansel hangs and does not respond.

  

When you do the same from the lighttable (using act on selection/duplicate -\> Edit/Delete development -\> Edit/Load development from xmp) it works.

## Replies

**ariznaf** — 2023-06-07

Nobody can confirm the problem? Is it only a problem in my system or in linux mint?

---

**Jofial** — 2023-06-07

To me the same thing happens to me. It only works if I copy and paste the .xmp

---

**Aurélien Pierre** — 2023-06-07

The duplication from lighttable is original code from the 1st generation of darktable developers, the duplication from the module in darkroom is a second-thought hack from the same guy who butched the GUI, using duplicated code, so none of this surprises me.

Keep using the lighttable duplication for now. I will have a look at some point.

---

**ariznaf** — 2023-06-07

strange way of working, there is long time since functions have been invented to be called and not duplicate code. You seem right that there are crazy code in darktable.

Great, thank you, I hope it will be fixed at some point, not an urgent bug to be fixed, as there is a way to do the task.

