---
title: "AMD OpenCL installation changed"
date: 2024-09-28
slug: "amd-opencl-installation-changed"
tags:
  - Community archive
forum_author: "Nikoh"
forum_category: "Feedback & use cases"
forum_url: "https://community.ansel.photos/view-discussion/amd-opencl-installation-changed"
wayback_url: "https://web.archive.org/web/20241009033713/https://community.ansel.photos/view-discussion/amd-opencl-installation-changed"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/amd-opencl-installation-changed`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20241009033713/https://community.ansel.photos/view-discussion/amd-opencl-installation-changed).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Nikoh** on 2024-09-28.*

Hello ﻿@Aurélien Pierre﻿, just to inform you that the installation command has changed if you want to update it in your wiki here:

[https://ansel.photos/en/doc/install/linux/](https://ansel.photos/en/doc/install/linux/)

``` ql-syntax
sudo amdgpu-install --usecase=opencl --opencl=rocr --no-dkms
```

This should be enough, after downloading and installing the amd package to manage the installation of its drivers.

