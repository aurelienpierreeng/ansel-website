---
title: "Problem with  Ansel-0.0.0+1768.g8de5c69-x86_64.AppImage; Database messed up?"
date: 2025-04-19
slug: "problem-with-ansel-0-0-0-1768-g8de5c69-x8"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/problem-with-ansel-0-0-0-1768-g8de5c69-x8"
wayback_url: "https://web.archive.org/web/20250427070901/https://community.ansel.photos/view-discussion/problem-with-ansel-0-0-0-1768-g8de5c69-x8"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/problem-with-ansel-0-0-0-1768-g8de5c69-x8`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250427070901/https://community.ansel.photos/view-discussion/problem-with-ansel-0-0-0-1768-g8de5c69-x8).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-04-19.*

For space reasons I had moved older pictures to a different hard disk, in particular the folder 2016. Trying to access a particular sub-folder there and its sub-folder DxO of PureRaw created dng-files, I ran into the following problem: DxO was supposed to contain 137 pictures, but only 119 were displayed. However, all pictures and their .xmp-files were present in the folder. As PureRaw was updated recently, I decided to apply the latest version to the 137 pictures on an external exfat drive with my MacBook. On there ansel version g111f59ef3 from [https://www.qwd.no/ansel.html](https://www.qwd.no/ansel.html) is installed, and I was able to import the original CR2-files and the new dng-files without a problem. Then I tried to use Ansel-0.0.0+1768.g8de5c69-x86_64.AppImage to import the pictures from the exfat-drive, which then showed the correct number of images, BUT when clicking on the appropriate folders claimed that there were no pictures in the current filtered collection. (Has the structure of the xmp-files changed?) Copying the folders to their original position didn't help either. The folder-names are struck out and I cannot remove them. While the mail folder is still listed with 137 pictures, the DxO-subfolder now is only listed with 42 pictures; very strange. After removing the .xmp-files, the folder-names are no longer struck out, but ansel still claims that the folders are empty, despite displaying the correct number of images.

  

The problem persists with the newly self-compiled version of ansel version 8de5c69.

## Replies

**koslowj** — 2025-04-20

I suspect an ownership problem, as all files on the disk in question are owned by root instead of me. Strangely enough, I cannot change this at the moment (sudo chown -R runs but doesn't see to do anything). I won't be able to correct this until May 1, as I'm leaving for a workshop today.

