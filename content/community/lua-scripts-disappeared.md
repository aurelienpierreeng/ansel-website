---
title: "Lua scripts disappeared?"
date: 2023-08-19
slug: "lua-scripts-disappeared"
tags:
  - Community archive
forum_author: "tflorac"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/lua-scripts-disappeared"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/lua-scripts-disappeared`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **tflorac** on 2023-08-19.*

Hi,

Quite old Darktable user, I just installed release 26acfc2 of Ansel today on Windows 10.

After activating Lua panel and installing scripts, I can't get access to the scripts list anymore (in dark room or in light table):

*\[attachment lost: image was hosted on the retired forum\]*

Is it normal also that the "Metadata" display panel is not included in the same "container" as Open, Library and Export panels?

Best regards,

Thierry

## Replies

**Lukas** — 2023-09-02

It looks like you are experiencing the same problem as described here: https://github.com/aurelienpierreeng/ansel/issues/50

The report is quite old and it states that the work on that issue is *on hold* but maybe you can make something of Auréliens last comment.

About the "Metadata" display, I think it's normal that it is not included in the container. You can however configure what it shows with the hamburger menu and "ctrl+scroll" to change it's height.

