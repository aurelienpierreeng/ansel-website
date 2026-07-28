---
title: "Image upload improvements"
date: 2023-03-23
slug: "image-upload-improvements"
tags:
  - Community archive
forum_author: "MartijnBraam"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/image-upload-improvements"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/image-upload-improvements`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **MartijnBraam** on 2023-03-23.*

I'm using the piwigo export module to upload images to my [custom album software](https://pictures.brixit.nl/) which works absolutely great. My only great issue with it is that login credentials won't want to be stored.

While this solution works well enough I think this feature can be better than just the piwigo api. I would like to also send the sidecar file and raw files to my album solution since it can also present that as optional downloads with the pictures alongside the metadata. Also it does not support uploading pictures that are not part of an album so I'd have to make a dummy album to just upload single pictures.

There's way more album hosting solutions than mine so maybe it makes sense to make a slightly more generic and way better documented API to support uploading images?

## Replies

**Aurélien Pierre** — 2023-03-23

Upload to web services typically use Rest API and each API is slightly different on server end, so I am not confident that we could have one unified client API to handle them all.

The now-defunct Flickr API used to use the key/wallet service of the OS (Gnome Keyring or KDE Wallet), I think the lack of support for them in Piwigo is just developer's lazyness. Problem remains that these are not avalaible outside of Linux anyway, so portability is a concern here.

---

**MartijnBraam** — 2023-03-23

Regarding the password: I would be happy already if that was just stored with a preset in the piwigo module.

Every web service has it's own unique rest API but for the various open source album generators I would guess it's possible to spec out a more generic one. Uploading pictures is not rocket science.

Currently my python software is pretending to be PHP for the api: https://git.sr.ht/~martijnbraam/Photoflow/tree/master/item/photoflow/frontend/piwigo.py

I guess the piwigo api but slightly reworked to be actually REST would make a great generic API any album software and photo editor could implement. I guess that's slightly out of scope for Ansel but since this is a discussion board with possibly more developers :)

---

**Aurélien Pierre** — 2023-03-23

> Regarding the password: I would be happy already if that was just stored with a preset in the piwigo module.

As clear text ? :-/

> Uploading pictures is not rocket science.

Playing politics with different dev teams who have different priorities is more difficult than rocket science, a lot more time consuming and typically less successful.

> I guess the piwigo api but slightly reworked to be actually REST would make a great generic API any album software and photo editor could implement. I guess that's slightly out of scope for Ansel but since this is a discussion board with possibly more developers :)

I have also wanted to get something working for WordPress and I have half-working OAuth2/Rest Python code for Instagram ([connect](https://github.com/aurelienpierreeng/VirtualSecretary/blob/main/src/facebook-login.py) and [list](https://github.com/aurelienpierreeng/VirtualSecretary/blob/7271006c8d22f5db54daf91d27d4cfc5c7fa9884/src/protocols/instagram_server.py#L196-L210), but no post yet). But before thinking general, I would rather have 2 or 3 services implemented and see how closely they are related.

