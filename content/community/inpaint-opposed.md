---
title: "Inpaint Opposed"
date: 2023-06-11
slug: "inpaint-opposed"
tags:
  - Community archive
forum_author: "Steve"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/inpaint-opposed"
wayback_url: "https://web.archive.org/web/20240422115447/https://community.ansel.photos/view-discussion/inpaint-opposed"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/inpaint-opposed`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240422115447/https://community.ansel.photos/view-discussion/inpaint-opposed).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Steve** on 2023-06-11.*

I would really like to see the 'Inpaint Opposed' method added to the Highlight Reconstruction module

## Replies

**Aurélien Pierre** — 2023-06-13

What benefit does it bring over guided Laplacian ? I have not seen examples yet where it brings better results.

---

**Steve** — 2023-06-14

Thanks, I just watched your video https://youtu.be/F3CeJ1F4wV8 and now I do not see a need for 'Inpaint Opposed'

---

**isagalaev** — 2023-12-21

Hello! Sorry to dig this one out, I'm trying to switch to Ansel form Darktable, and this one is the first feature I'm definitely missing. It's main benefit over guided Laplacian is that the it works with my Fuji X-Trans sensor. Or rather, I think it's because of the sensor because I vaguely (mis)remember Aurélien saying in one of the videos that implementing Laplacian for these sensor is crazy hard. Am I mistaken? For what it's worth, I simply don't see this option in my recently downloaded Ansel.

---

**migmoq** — 2023-12-21

Could you attach a RAF file for which the "Inpaint Opposed" works better than Guided Laplacian in the Highlight Reconstruction module?

---

**isagalaev** — 2023-12-21

Huh? I'm saying that Guided Laplacian is simply not available for my RAFs (neither in Ansel, not in DarkTable), there's nothing to compare. Inpaint Opposed is the only option I have (in DarkTable), and it works fine.

---

**migmoq** — 2023-12-22

Ha yes. Sorry, I misunderstood you. I thought you said the Inpaint Opposed was better than Guided Laplacian for RAF. And indeed, after checking, no Guided Laplacian nor Inpaint Opposed is provided for RAF. So, if Guided Laplacian is difficult to implement for RAFs, perhaps the better solution is to fetch the Inpaint Opposed from Darktable.

---

**isagalaev** — 2023-12-22

"Fetch from Darktable" may be a bit oversimplifying the amount of effort :-) But really the question is, if those two are similar enough, there's no point in having both of them in Ansel. There may be several different options:

- Port Inpaint Opposed and retire Guided Laplacian, if they're shown to be similar enough
- Make Guided Laplacian work for X-Trans sensors
- Port Inpaint Opposed and keep Guided Laplacian, but only show one of them for X-Trans or Bayer sensors respectively

It's ultimately a question for ﻿@Aurélien Pierre﻿, since he's probably the only person on the planet (or at least this forum) with the most background on this particular question.

P.S. I could try my hand at porting Inpaint Opposed, although it's been a while since I touched a non-trivial code base in C.

