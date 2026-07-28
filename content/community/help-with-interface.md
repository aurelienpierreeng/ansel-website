---
title: "help with interface"
date: 2023-09-20
slug: "help-with-interface"
tags:
  - Community archive
forum_author: "nirceu"
forum_category: "Feedback & use cases"
forum_url: "https://community.ansel.photos/view-discussion/help-with-interface"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/help-with-interface`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **nirceu** on 2023-09-20.*

Hi there, first, Ansel is great, much faster and pleasant to use on older systems than DT. But there are some things that really hold me adopting Ansel as my "go to raw processing app":

- I totally understand the focus on the pipeline, but when a search for a module, the pipeline tab rolls to the left and get lost on that tab bar. I think that pipeline tab should be fixed on the left corner. It will save some time, mouse wheel rolls and clicks; (and yes, i read the article about removing the old iconic tab, but... i'm used to customize interface options on software that allows changes to suit my needs, and had my "favorites" tab well balanced...)
- is there any way to resize the "Display Metadata" tab? for me, when enabled, it covers a fixed 3/4 of the left panel, and i cannot figure out how to resize it from the gui (i use the metadata to compare files in different folders, and enabling/disabling that module every time to change the active folder is annoying);
- i can't find a way to configure the default set of modules enabled for "new" raw files. Every first time a raw file is opened, Ansel enables: 1.original, 2.raw black/white point, 3.demosaic... yada yada... 12.orientation. I can't figure out how to change the order, neither the items on this default list. Is it possible btw? Creating a new set of default modules or change the stack order will speedup my workflow;

And, one more time: congratulations for Aurélien (and others here who can code) for this initiative, you guys rock!

I really don´t know if my complaints are pathetic or important in any way, but they are coming from an inexperienced user, trying to leave adobe lightroom (for the average user, LR can do magic!).

hugs from Brasil and sorry about my english mistakes (self taught)!

## Replies

**Lukas** — 2023-09-21

Hey Nirceu,

- you can ctrl+scroll while hovering "Display Metadata" to resize it. It's not very intuitive, but other modules resize the same way. Also you can configure which entries should be shown by clicking on the hamburger menu of the module.

---

**nirceu** — 2023-09-27

I've tried that but no go... btw, I found a way to solve my issue, found the relative size of the tab on a line on the file /home/~user/.config/ansel/anselrc

plugins/lighttable/metadata_view/windowheight=250 (the value that worked for me)

But thanks for the reply!

