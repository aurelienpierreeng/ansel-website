---
title: "Windows 7"
date: 2023-03-24
slug: "windows-7"
tags:
  - Community archive
forum_author: "Vintage Lens Lover"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/windows-7"
wayback_url: "https://web.archive.org/web/20230601123252/https://community.ansel.photos/view-discussion/windows-7"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/windows-7`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20230601123252/https://community.ansel.photos/view-discussion/windows-7).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Vintage Lens Lover** on 2023-03-24.*

After the excitement of discovering Ansel I was pretty gutted to see the Windows download was for Windows 10 and 11 only. Despite of this I thought I'd download the installer and see if it would work on Windows 7 and to my pleasant surprise it does!

Is there any reason Windows 7 compatibility should break in the future?

Yes, I am bitterly clinging onto Windows 7 for games and Affinity Photo until I figure out how to get all that running on Linux too. Having Affinity Photo and Ansel on different boot drives would be far from ideal.

## Replies

**Aurélien Pierre** — 2023-03-24

The Windows download is marked for 10 and 11 because I know it works on these. Not knowing if it does on 7, I will make no promise that I can't keep.

I'm glad to hear it works on 7 too.

As with any software relying on 3rd-party libraries, the challenge is rather to ensure each and every one of them keeps working on platform XYZ. The most potential I see for breakage is from Gtk, which behaves already unreliably on Windows in some contexts, and as many FLOSS projects, lacks dev and beta-testers on Windows.

---

**Vintage Lens Lover** — 2023-03-24

Fair enough and thank you for the reply!

I'll have to figure out how to install it on Linux (and how to get Affinity Photo ported too). I know there were some people who made progress on porting AF using WINE but it looked complicated.

P.S. - Your rant on DT4 was highly amusing. Well done putting together Ansel! I only installed it last night, it's taking a little getting used to but so far it does actually feel a little faster.

---

**ariznaf** — 2023-03-28

I have not tried, but It is quite probable that It world with no problema.in Windows 7.

It all depends on having a display driver forbyourbgpu with OpenGL 1.2 support in orden to have GPU support.

But you can allways use the CPU.

DT does not seem ti use OS advance features or new libraries o technologies, but the GPU.

---

**Vintage Lens Lover** — 2023-03-28

Yes, it IS working fine in Windows 7 so far.

Windows 10 was always a line in the sand for me so I've been migrating to Linux over the last two to three years (wish I'd done it sooner).

Coming from DT 4.2.1 a few of the modules complained when importing from XMP: Highlight Reconstruction, Filmic and I think Lens Correction were not happy. I had Highlight Reconstruction set to "inpaint opposed" in DT and had to select a new option in Ansel.

---

**Vintage Lens Lover** — 2025-01-09

I don't really expect it to be fixed, but the more recent builds of Ansel throw up an error in Windows 7 now. [ansel-43e4fce-win64.exe](https://github.com/aurelienpierreeng/ansel/releases/download/v0.0.0/ansel-43e4fce-win64.exe) seems to be the latest version to successfully launch in Windows 7, in case anyone else was dealing with the same issue.

---

**Aurélien Pierre** — 2025-01-10

Can you be more specific on the error ?

I suppose the most probable cause for this Windows the building environment (MSYS2, MingW64, URTC64, etc.) that got updated to something incompatible.

---

**Vintage Lens Lover** — 2025-01-10

Thanks for the response. A box pops up which says:

"ansel.exe - Entry Point Not Found

The procedure entry point CreateFile2 could not be located in the dynamic link library KERNEL32.dll."

