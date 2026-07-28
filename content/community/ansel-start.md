---
title: "Ansel start"
date: 2025-05-23
slug: "ansel-start"
tags:
  - Community archive
forum_author: "Maurizio Paglia"
forum_category: "Feature requests"
forum_url: "https://community.ansel.photos/view-discussion/ansel-start"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/ansel-start`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Maurizio Paglia** on 2025-05-23.*

Starting Ansel is a rather long process.

The system works, but nothing happens... then you can see the tittlebar appear and then the whole window is drawn.

First start is very long. After the first start the time is lower but anyway rather long.

So comes my \[stupid?\] question: is it possible to draw something informing the user Ansel is starting? Like a splash screen or another informative message.

Thank you

## Replies

**Aurélien Pierre** — 2025-05-23

The start is not supposed to be long. What can get long is the OpenCL benchmark (but it has its own progress window), or building the OpenCL kernels… which shouldn't happen if they are cached and your GPU driver wasn't updated. Perhaps start with `ansel -d all` and see what takes so long (note that the long-running operation will be written in terminal only when it completes, so the last command displayed for a long time will be the one before the faulty one).

---

**Jiyone** — 2025-05-23

How long is long?

What OS are you using ?

---

**Steve** — 2025-05-23

Ansel loads in less 1.5 seconds on Windows 11

---

**Maurizio Paglia** — 2025-05-24

It loads in about 1 minute.

Running on Linux OpenSUSE Thumbleweed (compiled from source).

I will follow Pierre indications and will post results

---

**Maurizio Paglia** — 2025-05-24

Well... actually Ansel start is very long ONLY on its first launch. If I close Ansel and start it again, the startup is OK.

Data coming from \<ansel -d all\>

1st launch

``` ql-syntax
0,199928 [init sql] library: /home/mau/.config/ansel/library.db, data: /home/mau/.config/ansel/data.db
46,356198 [sql] /home/mau/Sistema/git/ansel/src/common/tags.c:583, function dt_set_darktable_tags(): exec "DELETE FROM memory.darktable_tags"
```

2nd launch

``` ql-syntax
0,049295 [init sql] library: /home/mau/.config/ansel/library.db, data: /home/mau/.config/ansel/data.db
0,170053 [sql] /home/mau/Sistema/git/ansel/src/common/tags.c:583, function dt_set_darktable_tags(): exec "DELETE FROM memory.darktable_tags"
```

And again.

1st launch

``` ql-syntax
46,636524 [image_cache] has 53426 entries (50 MiB)
[opencl_init] opencl related configuration options:
[opencl_init] opencl: ON
[opencl_init] opencl_library: 'default path'

@@ 953,7
   KERNEL SOURCE DIRECTORY:  /opt/ansel/share/ansel/kernels
   KERNEL BUILD DIRECTORY:   /home/mau/.cache/ansel/cached_kernels_for_NVIDIAGeForceRTX3050_57015302
   CL COMPILER OPTION:       -cl-fast-relaxed-math
   KERNEL LOADING TIME:       4.0630 sec
[opencl_init] OpenCL successfully initialized.
[opencl_init] here are the internal numbers and names of OpenCL devices available to Ansel:
[opencl_init]       0  'NVIDIA GeForce RTX 3050'

@@ 966,1214
[dt_opencl_update_priorities]       image   preview export    thumbs
[dt_opencl_update_priorities]       1  1  1  1
[opencl_synchronization_timeout] synchronization timeout set to 200
51,184912 [imageio_load_module_format] loading `copy' from /opt/ansel/lib64/ansel/plugins/imageio/format/libcopy.so
```

2nd launch

``` ql-syntax
0,419813 [image_cache] has 53426 entries (50 MiB)
[opencl_init] opencl related configuration options:
[opencl_init] opencl: ON
[opencl_init] opencl_library: 'default path'

@@ 953,7
   KERNEL SOURCE DIRECTORY:  /opt/ansel/share/ansel/kernels
   KERNEL BUILD DIRECTORY:   /home/mau/.cache/ansel/cached_kernels_for_NVIDIAGeForceRTX3050_57015302
   CL COMPILER OPTION:       -cl-fast-relaxed-math
   KERNEL LOADING TIME:       0.0182 sec
[opencl_init] OpenCL successfully initialized.
[opencl_init] here are the internal numbers and names of OpenCL devices available to Ansel:
[opencl_init]       0  'NVIDIA GeForce RTX 3050'

@@ 966,1195
[dt_opencl_update_priorities]       image   preview export    thumbs
[dt_opencl_update_priorities]       1  1  1  1
[opencl_synchronization_timeout] synchronization timeout set to 200
0,756859 [imageio_load_module_format] loading `copy' from /opt/ansel/lib64/ansel/plugins/imageio/format/libcopy.so
```

Total time 1st launch: 66.45

Total time 2nd launch: 10,28

---

**Maurizio Paglia** — 2025-05-24

I can pass you the complete logs (first and second launch). Tested also a third one that is basically the same of the second one.

So the problem seems to be only on the first time Ansel is launched after the user login.

---

**Aurélien Pierre** — 2025-05-24

That points toward an issue in the database init/loading. How large is your library.db ?

---

**Aurélien Pierre** — 2025-05-24

I have pushed a slight optimization of the database init, you can pull and retry. In preferences -\> storage -\> database -\> check for database maintenance, ensure that maintenance (aka database optimization) is not performed at startup.

---

**Maurizio Paglia** — 2025-05-25

160 MiB

---

**Maurizio Paglia** — 2025-05-25

OK, now ansel starts in about 30/35 seconds (was 1 minute before the pull of this morning).

I confirm time consuming steps are still

``` ql-syntax
0,277029 [sql] Checked database schema and migrated if needed
13,358479 [sql] Checked db_info
```

and

``` ql-syntax
14,148173 [image_cache] has 53426 entries (50 MiB)
[opencl_init] opencl related configuration options:
[opencl_init] opencl: ON
[opencl_init] opencl_library: 'default path'

@@ 942,8
   DRIVER VERSION:           570.153.02
   DEVICE VERSION:           OpenCL 3.0 CUDA, SM_20 SUPPORT
   DEVICE_TYPE:              GPU
   GLOBAL MEM SIZE:          7849 MB
   MAX MEM ALLOC:            1962 MB
   MAX IMAGE SIZE:           32768 x 32768
   MAX WORK GROUP SIZE:      1024
   MAX WORK ITEM DIMENSIONS: 3

@@ 961,7
   KERNEL SOURCE DIRECTORY:  /opt/ansel/share/ansel/kernels
   KERNEL BUILD DIRECTORY:   /home/mau/.cache/ansel/cached_kernels_for_NVIDIAGeForceRTX3050_57015302
   CL COMPILER OPTION:       -cl-fast-relaxed-math
   KERNEL LOADING TIME:       4.6061 sec
[opencl_init] OpenCL successfully initialized.
[opencl_init] here are the internal numbers and names of OpenCL devices available to Ansel:
[opencl_init]       0  'NVIDIA GeForce RTX 3050'

@@ 974,1409
[dt_opencl_update_priorities]       image   preview export    thumbs
[dt_opencl_update_priorities]       1  1  1  1
[opencl_synchronization_timeout] synchronization timeout set to 200
19,245620 [imageio_load_module_format] loading `copy' from /opt/ansel/lib64/ansel/plugins/imageio/format/libcopy.so
```

Maybe a shell script for db optimization could be auto-started after the login in my Linux box?

I am asking since startups after the first take about 10 seconds.

Thank you agai

---

**Aurélien Pierre** — 2025-05-25

Optimization is done on user request, automatically from the preferences (at startup, closing, both or never), or manually when using the global menu *Run*. No need for an additional script here. What I did in my recent commit is prevent it from (always) running at startup (which was a bug, judging by what the comment said).

But there is not much more I can do here. On my computer too, the most consuming step of the DB init is the same as yours (checking db_info), but it takes 0.4 s with a 470 MiB library. That step is mandatory, there is nothing more I can strip from there without risking inconsistent data savings.

---

**Maurizio Paglia** — 2025-05-25

Thank you indeed for your kind support

