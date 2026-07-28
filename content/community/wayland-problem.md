---
title: "Wayland problem?"
date: 2024-03-24
slug: "wayland-problem"
tags:
  - Community archive
forum_author: "Maurizio Paglia"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/wayland-problem"
wayback_url: "https://web.archive.org/web/20240530224314/https://community.ansel.photos/view-discussion/wayland-problem"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/wayland-problem`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240530224314/https://community.ansel.photos/view-discussion/wayland-problem).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Maurizio Paglia** on 2024-03-24.*

Ciao,

I opened a photo folder and found some images are NOT rotated.

Double click on the image in order to enter the darkroom and on the terminal I receive the following error:

``` ql-syntax
[image_cache_write_release] sqlite3 error 19
```

Since I am testing Wayland on my KDE, can this be a Wayland connected problem?

Thanks,

Maurizio

## Replies

**Aurélien Pierre** — 2024-03-24

Ciao,

I don't see how switching display would affect database read-write, unless there is an hidden race condition and some is faster with Wayland.

---

**Maurizio Paglia** — 2024-03-26

Yes, this is logic.

Switched to Xorg. Launched Ansel from a terminal.

Images now are swowed correctly but opening them the error is still there...

Same error also simply hovering with the mouse on them from the lighttable!

Not on all images but only on some of them...

Do you think I need to perform some maintenance operation on the database?

---

**Aurélien Pierre** — 2024-03-29

The SQLite error code 19 seems to indicate that an attempt to create an element with an already existing key was made : https://stackoverflow.com/questions/3415589/unable-to-insert-in-sqlite-error-code19

Did you manipulate the database yourself ? That might be a corruption.

---

**Maurizio Paglia** — 2024-04-01

Ciao, I did any manual operation on the SQLite database and I really do not know when this problem raised for the first time since I never start Ansel from a terminal...

I can try to replace the databse with one from a recent backup and see it it will work.

thanks

