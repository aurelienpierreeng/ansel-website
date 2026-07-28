---
title: "Encouragement and how can I help?"
date: 2024-06-02
slug: "encouragement-and-how-can-i-help"
tags:
  - Community archive
forum_author: "robbrown"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/encouragement-and-how-can-i-help"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/encouragement-and-how-can-i-help`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **robbrown** on 2024-06-02.*

I'm watching this project with great interest. It is great to see a project and a small community try to move photography editing forward for open source. I never really got in to Darktable as it seemed too confusing and too bloated, especially since 4.0 and on. Already with the early work here on Ansel I see some great promise.

My wishes for the project, and perhaps some good tenets:

- Prioritize user experience over features (for the sake of features). ie simple to understand and use the basics, with the ability to drill down to get more powerful editing options, if that is needed. Also an emphasis on good application speed as part of that experience.
- Good product lifecycle:
- think about the problem to solve first, design it correctly, engineer, test. Get feedback, and fine tune.
- be ok to deprecate old functionality / tools that could be better served by newer ones to avoid bloat and confusion
- keep experiments in a sandbox: Darktable 4+ is a classic case of sandboxing any and every idea in a production environment. In my experience, it is better to keep such experiments out of production, get the feedback and then move forward.... but only if the user experience is maintained.
- Good community & Tenets
- I've read some of the back story about Ansel and Darktable, and understand the frustrations with the latter project. It seems that Darktable had (or maybe steered away from) no tenets. I do hope that the Ansel project sticks to some solid tenets, which are regularly pointed to and considered when any change is made. In my professional experience developing and deploying complex systems good tenets allow a project to move in the right direction.

How can I help?

1.  While I'm not a developer, I'm a product manager and could perhaps help on this side of things.
2.  A simple act of \$. I have set up a recurring payment, and hope others do too.

## Replies

**Aurélien Pierre** — 2024-06-03

Thanks and welcome !

For now the focus is on improving core functionnalities :

- making the picture import tool closer to a generic file picker (front-end is done but showed back-end issues, back-end has been rewritten and is almost ready for testing),
- making the pixelpipeline cache work properly so intermediate modules states can be stored instead of recomputed all the time (Darktable had an interesting way of solving cache consistency issues… by clearing the complete cache all the time),
- protecting the pictures from concurrent access throughout the app, but in an unified way (Darktable had 3 or 4 different thread-locks mechanisms to manage all corner cases).

So for now it's mostly code, and not the sexy kind.

