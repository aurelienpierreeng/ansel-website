---
title: "False positive?"
date: 2023-11-27
slug: "false-positive"
tags:
  - Community archive
forum_author: "Alessandro"
forum_category: "Installing help"
forum_url: "https://community.ansel.photos/view-discussion/false-positive"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/false-positive`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Alessandro** on 2023-11-27.*

Good morning, I would like to try using this software which seems very valid but there is no way to do it on my Windows PC as it is detected as a virus. Virustotal online also sees it like this in a couple of search engines...

## Replies

**Aurélien Pierre** — 2023-11-28

It seems to be a reputation score fetched from databases, not a content analysis. Reputation means anybody able to report it is able to blacklist it.

.exe files are built every night on Github virtual server instances using Windows Server 2022. The code source is auditable, those virus-finding gentlemen can help themselves through the code…

---

**Aurélien Pierre** — 2023-11-28

I ran the latest .Exe again and it gives another result : https://www.virustotal.com/gui/file/a49810851b32b7a22c84d9bb9b5e8c90372b8b9f50de8b11326d4cd1c445c918?nocache=1

Meh…

---

**Alessandro** — 2023-11-29

Thank you. Yes, I was imaging that was just a false positive.

---

**Alessandro** — 2023-11-29

Nothing... I tried again with this: [ansel-1d3f83d-win64.exe](https://github.com/aurelienpierreeng/ansel/releases/download/v0.0.0/ansel-1d3f83d-win64.exe)

but my antivirus complained again and quarantined it. I will have to wait for a "lucky" exe... :-(

---

**Aurélien Pierre** — 2023-12-01

Can't you just bypass the antivirus and install anyway ? On my Windows, I have disabled all security features, they are annoying more than anything. Granted, I don't use Windows to open shady email attachments and I install pretty much nothing on it.

---

**3dguy** — 2023-12-09

﻿@Aurélien Pierre﻿ I've went through the same issue when I distributed my 3D render farm management software. Lost a couple of customers due to the false positives. I can give details on how to fix this on your side, writing the details would take some work though, could you ping me here (or via email) if I should go ahead?

---

**Alessandro** — 2023-12-12

Thank you but that won't be necessary. The main proposal of my initial post was just to alert the creator of this software and potentially other users of the problem. I think that no programmer likes the idea tha his creation is marked as a virus.

