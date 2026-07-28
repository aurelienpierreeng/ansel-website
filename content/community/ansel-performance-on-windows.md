---
title: "Ansel performance on windows"
date: 2024-07-29
slug: "ansel-performance-on-windows"
tags:
  - Community archive
forum_author: "fourdogslong"
forum_category: "Configuring help"
forum_url: "https://community.ansel.photos/view-discussion/ansel-performance-on-windows"
wayback_url: "https://web.archive.org/web/20240806195812/https://community.ansel.photos/view-discussion/ansel-performance-on-windows"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/ansel-performance-on-windows`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240806195812/https://community.ansel.photos/view-discussion/ansel-performance-on-windows).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **fourdogslong** on 2024-07-29.*

Hi guys, I recently discovered Ansel as well as Darktable, got curious about Ansel because it claims to be faster than DT and I like the idea of it.

However on my windows 11 PC, Darktable feels faster while editing. In Ansel, I need to let go of the mouse for any edit to be displayed/updated, in DT the display is updated as I move the mouse, also, zooming in and out and navigating around the picture in DT has almost no lag as in Ansel I can't do it without getting a "working" message on the preview for a second or two.

Is there anything I need to configure to make it better on windows? Is Linux where it's at?

Lastly, is the option the move the histogram to the right gone right now? I saw in a user manual that such an option existed at some point.

Thanks

## Replies

**Aurélien Pierre** — 2024-07-29

Hi, there is a couple of things to precise here.

Ansel is faster than Darktable because many redundant operations, that computed more than once but which results were eventually discarded, were removed. Computing fewer things makes it objectively faster. Now, whether the speed-up will be noticeable or not on your particular hardware depends on how powerful it is, aka how much waste it can afford before feeling sluggish.

Then we have responsiveness of the GUI, which is another (but related) layer on top: that's how fast the GUI gives you feedback that it got your input right.

> In Ansel, I need to let go of the mouse for any edit to be displayed/updated

This is actually one of the methods used to limit intermediate useless recomputes. Darktable fires recomputations on "button pushed", "button released" and "mouse moved" events, without ensuring you are done interacting. That's fine on high-end hardware, but it can really lock your system on mid-range. Ansel only fires recomputations on "button released". The actual pipeline computations are the same in both applications.

> Lastly, is the option the move the histogram to the right gone right now?

Yes, the redesign of histogram is work in progress. Doc will follow.

---

**fourdogslong** — 2024-07-29

Thanks for your reply! Could an option to enable "mouse moved" be implemented in the future for those of us with capable hardware? I totally understand the reasoning behind it's removal but with a modern PC it feels weird / not natural to have to let go of the mouse to see a result. It makes precise adjustments harder in my opinion. Maybe ctrl+drag could be used to enable the "mouse moved" display refresh or something like that.

I think I will try to install Linux anyway to see how it feels on that OS even though I am not familiar with the OS, it should be a fun experiement anyway. I was editing a picture in DarkTable yesterday, I'm still new to these Open Source software, and it crashed a few times using the color zones module, continuing the same edit in Ansel did not so I see the potential there.

Thanks for your work!

---

**Aurélien Pierre** — 2024-08-13

> Maybe ctrl+drag could be used to enable the "mouse moved" display refresh or something like that.

Right click + drag does what you ask.

