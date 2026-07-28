---
title: "Optimization"
date: 2025-05-21
slug: "optimization"
tags:
  - Community archive
forum_author: "Bless"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/optimization"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/optimization`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Bless** on 2025-05-21.*

Hello. i came up with the idea of a program to help optimize the processing.

I noticed that i often apply exposure +2 to compensate...

Need to write code that analyzes the similarity of the actions and structurizes them in %Ratio, analyzing processing of each image.

And shows messages to the user on this basis.

Example : You have used the exposure module in 98% of you images with a value of +2 \* Wuld you like to apply it automatically, in the next 3 sessions? \*

And later if it seemed convenient leave it. Or suggestion to fix HotKeys.

Ps. I still can't put Ansel on Windows 7 /

G L \* A L L \*

## Replies

**Maurizio Paglia** — 2025-05-23

Hi!

I like Ansel so much because nothing is auto-magically executed.

If you need to apply the same fix (in your example exp +2) on 98% of the images you take, I suggest to enter a preset in your preferences.

Or you can apply a +2 EV directly in your camera menu.

I have now an archive of about 27.000 photographs: I really will be scared before clicking OK...

---

**Aurélien Pierre** — 2025-05-23

Yes, styles are currently out of order, but user-defined module presets can be automatically applied based on EXIF (camera, ISO, shutterspeed, etc.). That's much more robust than listening to high-level user actions, especially since modules can have multiple instances so the code choosing which one to listen will be the first brittle link of a terrible chain.

For Windows 7, it is not supported by Ansel (and is not anymore supported by Microsoft, by the way), never has been. It used to work, I have heard somewhere that now you need to manually install MSVCR if that is your error.

