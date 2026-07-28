---
title: "Question about the behavior of the filmstrip in the darkroom"
date: 2025-01-25
slug: "question-about-the-behavior-of-the"
tags:
  - Community archive
forum_author: "koslowj"
forum_category: "Feedback & use cases"
forum_url: "https://community.ansel.photos/view-discussion/question-about-the-behavior-of-the"
wayback_url: "https://web.archive.org/web/20250520202210/https://community.ansel.photos/view-discussion/question-about-the-behavior-of-the"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/question-about-the-behavior-of-the`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250520202210/https://community.ansel.photos/view-discussion/question-about-the-behavior-of-the).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **koslowj** on 2025-01-25.*

In the darkroom, the space bar causes the next picture to be displayed. If the filmstrip is visible, both the last image and the now current one are then selected. In particular, rating the current image automatically also overwrites the rating of the previous image. The analogous phenomenon occurs when using the back-key, just in the other direction. Is this the intended behavior? Sometimes I like to rate all the pictures of a directory by stepping through them from start to finish. To maximise the view, I prefer to hide the filmstrip. But then I have no way of stepping forward or backwards, as the arrow-keys don't do the job.

## Replies

**Jiyone** — 2025-01-25

> Is this the intended behavior?

No it's not, an there are many other things happening about the filmstrip ﻿﻿😅﻿﻿:

- Removing images from the library will remove any picture selected AND the one currently open.
- On the contrary, doing **image \> rotate \> 90° (counter) clockwise** will turn selected pictures EXCEPT the one currently open even if selected.
- BUT doing **edit \> past history** on several images works as intended (the currently opened picture is safe if it's not selected).

The filmstrip is a mini lighttable, and the lighttable will need to be rewritten. Remember that Ansel is "work in progress" and things can appear broken overnight.

