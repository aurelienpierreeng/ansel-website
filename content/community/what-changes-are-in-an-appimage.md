---
title: "What changes are in an appimage?"
date: 2025-01-12
slug: "what-changes-are-in-an-appimage"
tags:
  - Community archive
forum_author: "Annabel"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/what-changes-are-in-an-appimage"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/what-changes-are-in-an-appimage`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Annabel** on 2025-01-12.*

Recently I created issue \#396, Aurelien fixed it, thanks, and this led to Commit cf52835. I tried to see if this led to any mention of the next appimage, but didn't spot anything, and in any case **I have little familiarity with github**. (Also the issue mentions "0.1" so maybe this change is some way off being built in?). So: Is there a way to see when a change will go into an appimage, or how to see what changes are in the current appimage?

## Replies

**Aurélien Pierre** — 2025-01-12

Ok, so here is how it works:

1.  You can see the history of commits there: https://github.com/aurelienpierreeng/ansel/commits/master/
2.  The AppImage and Windows build have an uniform naming pattern. For example, for tonight's package, it's **Ansel-0.0.0+1028.gecaf9d6f-x86_64.AppImage**. **0.0.0+1028** means we are 1028 commits after version tag 0.0.0. Then, g**ecaf9d6f** means "Git **ecaf9d6f**", where ecaf9d6f is the last commit that was included in the AppImage.
3.  Find that commit ID in the commit history:

*\[attachment lost: image was hosted on the retired forum\]*

So this is the step at which the package was built. Every commit older than this one will be included in the package.

Or… the packages are nightly builds, auto-built everyday around 1am UTC. Meaning anything that got commited the previous day gets included.

---

**Annabel** — 2025-01-12

Thanks, that's very clear. I'm impressed by how many changes you do each day.

---

**Aurélien Pierre** — 2025-01-12

Well, don't be. I keep changes minimal and focused on one single topic. That's a trick to be able to go back anytime in the history of commits, if a bug or a regression appears, and find precisely what commit introduced it. Splitting changes into small steps makes that easier, and makes the number of changes more impressing, but it's an illusion.

