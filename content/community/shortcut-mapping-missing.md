---
title: "Shortcut Mapping missing?"
date: 2025-01-09
slug: "shortcut-mapping-missing"
tags:
  - Community archive
forum_author: "GLCAnsel"
forum_category: "Configuring help"
forum_url: "https://community.ansel.photos/view-discussion/shortcut-mapping-missing"
wayback_url: "https://web.archive.org/web/20250120185715/https://community.ansel.photos/view-discussion/shortcut-mapping-missing"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/shortcut-mapping-missing`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250120185715/https://community.ansel.photos/view-discussion/shortcut-mapping-missing).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **GLCAnsel** on 2025-01-09.*

I cannot access shortcut mapping features.

I am trying to set up a Behringer X-Touch Mini midi controller -- but can find none of the mapping features described in the Ansel documentation.

Specifically, the “visual shortcut mapping” and “shortcut mapping screen” appear to be inaccessible. 

The documentation ( [https://ansel.photos/en/doc/preferences-settings/shortcuts/](https://ansel.photos/en/doc/preferences-settings/shortcuts/) )  describes access to each of these. (first, via a keyboard icon supposedly visible in the “top panel of any Ansel view” -- but despite careful searching, I cannot find the icon/button.)  (second, “accessed from the global preferences dialog” -- but no preferences panel presents anything related to “shortcut mapping screen”)

What am I missing, please?  

mci

## Replies

**Aurélien Pierre** — 2025-01-10

MIDI support has been dropped and the shortcut manager needs a rewrite, since it is beyond maintable. Shortcuts will be limited to typical keyboard. Properly designed, they should make MIDI devices useless.

The docs are not up-to-date in that regard, sorry.

---

**GLCAnsel** — 2025-01-10

Thanks for the clarification and for your ongoing excellent work on this complex project.

