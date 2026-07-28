---
title: "Trojan in latest release ansel-0.0.0+1333.g9242d5a5-win64.exe ?"
date: 2025-02-21
slug: "trojan-in-latest-release-ansel-0-0-0-1333"
tags:
  - Community archive
forum_author: "Ed Mathis"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/trojan-in-latest-release-ansel-0-0-0-1333"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/trojan-in-latest-release-ansel-0-0-0-1333`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Ed Mathis** on 2025-02-21.*

This morning I went to the github nightly builds and downloaded ansel-0.0.0+1333.g9242d5a5-win64.exe. When I tried to move the file to my storage directory Windows Defender immediately quarantined the file. Looking further, it reported a trojan embedded in the file. Click on the title of this posting to see a copy of Defender's report.

Is this a false positive?

*\[attachment lost: image was hosted on the retired forum\]*

## Replies

**topoldo** — 2025-02-21

Me, too! Windows 11 Pro 24H2. Ansel version: sama as Ed Mathis.

Regards,

Topoldo

---

**Aurélien Pierre** — 2025-02-21

Well, all I can tell you is I didn't put a trojan in there and my Github account hasn't been breached, which means no malicious code was injected there. If you got the .exe straight from Github, that should be fine. Now, if you got the .exe from somewhere else, I can't guarantee it has not been tampered with.

You could try from an earlier version too, see if the antivirus catches it too. Anyway, those use binary fingerprints to detect viruses, so false-positives happened in the past and will happen again.

---

**Ed Mathis** — 2025-02-21

I got it straight from Github this morning, where I always get the updates. The previous version -1329 downloaded and installed just fine with no warnings. Dunno...... I'll try again after Windows Defender undergoes a few more updates that may solve the false positive.

---

**Aurélien Pierre** — 2025-02-21

There are 65/70 antivirus that pass clean… https://www.virustotal.com/gui/file/b7685065159d284931f8188c1947c37b6dd32d6b5d161ed55536865dc490ca2e

But I tested all Ansel versions since 1329, and they all trigger 3 to 5 antiviruses in the pack. It's been seen before…

---

**Aurélien Pierre** — 2025-02-22

For the record, Windows antivirus has an history of detecting Wacatac malware everywhere: https://www.reddit.com/r/antivirus/comments/14bhb6u/trojanwin32wacatacbml_trojanscriptwacatacbml/

