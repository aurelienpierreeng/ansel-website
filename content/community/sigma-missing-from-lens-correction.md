---
title: "Sigma missing from lens correction?"
date: 2023-05-01
slug: "sigma-missing-from-lens-correction"
tags:
  - Community archive
forum_author: "Kivlegu"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/sigma-missing-from-lens-correction"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/sigma-missing-from-lens-correction`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Kivlegu** on 2023-05-01.*

I'm noticing Sigma lenses are missing from the lens correction module. I also think it's not been updated for a while in the windows build since the Sigma 56mm F1.4 DC DN is missing in the mil-sigma.xml file.

## Replies

**Kivlegu** — 2023-05-01

I built it myself using the guide in the github repo and now have the sigma lens I was missing. I assume the build machine isn't running the lensfun update command, considering how fresh the installer on the website is.

---

**Aurélien Pierre** — 2023-05-05

If Lensfun indeed supports your lenses all you have to do is to run the script `lensfun‑update-data`. If Lensfun does not support your lenses, then it's something to see with them : [https://github.com/lensfun/lensfun](https://github.com/lensfun/lensfun). In any case, lens support is done be the Lensfun project.

Ansel package builds (Windows and Linux) run the updating command above before building, so your issue would mean the up-to-date libraries are not embedded into the package.

---

**Kivlegu** — 2023-05-06

My build had it. Yours didnt. The lens was added ages ago.

