---
title: "Inconsistent 'datetime' on Export"
date: 2025-01-25
slug: "inconsistent-datetime-on-export"
tags:
  - Community archive
forum_author: "Steve"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/inconsistent-datetime-on-export"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/inconsistent-datetime-on-export`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Steve** on 2025-01-25.*

I have just exported 99 raw images to jpeg and only 31 of the 99 jpegs have the 'Date Taken' appear. Seems something is blocking the the writing of the 'datetime' to the jpeg. I really need the 'datetime' with the jpeg

## Replies

**Steve** — 2025-01-25

I figured it out, somehow the export preferences got changed

---

**Steve** — 2025-01-25

No, there seems to be a bug that effects the original date taken data on some files.

1 - unedited export

2 - edited orientation

3 - added metadata

*\[attachment lost: image was hosted on the retired forum\]*

---

**Steve** — 2025-01-26

I am able to continually repeat the issue with the one file, but not with others. Noticed that when I select an amount of files to export, it starts exporting the first 4 or five very fast then it goes silent for 2-3 minutes (with very little GPU usage) then after a few minutes it starts exporting the rest of the files. I'm wondering what goes on during those few minutes

---

**Aurélien Pierre** — 2025-03-06

Possibly linked to https://github.com/aurelienpierreeng/ansel/issues/453

---

**Steve** — 2025-03-09

I have been able to narrow down the issue further.

If I have been using Ansel to edit and then close Ansel and reopen Ansel and Export, the issue arises.

I do an Uninstall and a complete Delete of ALL files associated with Ansel, then a clean install of Ansel.

I then Import and Export. All is exported correctly.

It seems once one uses Ansel to edit images, or an image's Metadata, then closing Ansel, it triggers a change from where the Export function goes to retrieve the image metadata. It seems it is not retrieving any data at all.

Something happens upon the closing and re-opening of Ansel to cause this ???

Please see screen shot. 1st column is before uninstall/delete. 2nd column is a fresh install and only function used in Ansel is to Import & Export a jpeg

---

**Aurélien Pierre** — 2025-03-14

Please see and try https://github.com/aurelienpierreeng/ansel/issues/453#issuecomment-2725622620

