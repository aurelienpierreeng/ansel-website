---
title: "May I open the catalog from linux and windows in a dual boot system?"
date: 2023-03-27
slug: "may-i-open-the-catalog-from-linux-and"
tags:
  - Community archive
forum_author: "ariznaf"
forum_category: "Configuring help"
forum_url: "https://community.ansel.photos/view-discussion/may-i-open-the-catalog-from-linux-and"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/may-i-open-the-catalog-from-linux-and`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **ariznaf** on 2023-03-27.*

I have decided to try Ansel under linux, as I am thinking of going the linux way (I have been using it for some things for many years, but I could not abandone windows as some professional apps are not found in linux).

I have a dual boot machine now and have installed linux mint with cinnamon.

I can mount the ntfs partition where raw photo archives and darkatable 4.0 catalog reside.

How do I configure ansel in linux to open that catalog by default?

Is there any danger opening the catalog that was created in DT for windows?

The problem I can think of is that the paths to the photos saved in the catalog won't be correct under linux as they will be different.

Is there a way to tell Ansel where the photos reside?

Would it be possible to open the catalog from windows and linux when I change booting mode?

Anyone has tried it previously?

Thank you for your advices.

## Replies

**Aurélien Pierre** — 2023-03-27

The catalog is an SQLite database, you can use it the same with Ansel, no matter the OS. You can start Ansel with any config directory you want, even hosted on the Windows partition, with `ansel --configdir /path/to/your/config`.

Now, the issue will be that all the pathes to images will be referenced from the Windows perspective (`C:\\non-sense\etc`), which will not be resolved from Linux. All in all, you would better write XMPs from Windows (menu Run -\> Save all developments to XMP), then import the images from their folders from Linux.

Same with Linux, when you are done with an edit, save all developments to XMP.

To synchronize each Windows/Linux database with XMP, you have again the command into the Run menu.

---

**ariznaf** — 2023-03-27

Thank you for the reply.

I have been making tests, it is possible to change new location of each import session, you can select it and all the paths in that session are updated, but that is not a thing you want to do each time you switch between Windows and Linux sesion.

It seems a flaw in the design of the program to save absolute paths to the photo files, relatives paths and a import location would make it easier to move files around or access the same database from several computers.

In lightrom you create import directories and when you move a directory you only have to change the location of that directory and all files that depend on it get updated.

  

The solution seems to be to have two databases and use .xmp sidecar files to update changes. I will have to try.

Thank you.

---

**Aurélien Pierre** — 2023-03-28

First of all, dt was designed for Unix-like systems, and was only ported to Windows much later.

Then, using relative pathes alone will most likely not fix problems of cross-platform filesystem compatibility. In fact, several parts of the code handling filenames and pathes have 2 variants, one for Unix-like and another for Windows. There is also the issue that Linux uses UTF-8 encoding while Windows still uses ISO something, which is a never-ending source of filename bugs for non-latin characters.

Having 2 DB is slightly annoying but more robust overall.

---

**ariznaf** — 2023-03-29

Thank you.

Yes, as It is now, It Will be better yo have separate databases.

But path related problems have been solved long time ago.

There is a posix compliant library in Windows for accesing files and for having no problem with paths. All you have to do is use a function to convert Linux path strings before doing the file system call that works in Windows and Linux.

But in a program already coded with thousands of lines It may be difficult to change It.

May be something yo have un mind in a new development (vkdt?).

