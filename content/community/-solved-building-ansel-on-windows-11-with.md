---
title: "(Solved) Building Ansel on Windows 11 with msys2"
date: 2023-08-16
slug: "-solved-building-ansel-on-windows-11-with"
tags:
  - Community archive
forum_author: "dtuser"
forum_category: "Installing help"
forum_url: "https://community.ansel.photos/view-discussion/-solved-building-ansel-on-windows-11-with"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/-solved-building-ansel-on-windows-11-with`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **dtuser** on 2023-08-16.*

Hi there,

First post here, so hi everyone. I’ve been able to build darktable on Windows (mysys urtc64) with no problem. So I decided to give Ansel a try. I followed Aurelien’s build instructions but I can’t go past the linker step.

I am pretty sure I missed something obvious.

Thanks for your help.

``` ql-syntax
FAILED: bin/libansel.dll bin/libansel.dll.a
cmd.exe /C "cd . && C:\msys64_ucrt\ucrt64\bin\cc.exe -Wall -Wno-format -Wshadow -Wtype-limits -Wvla -Wold-style-declaration -Wno-unknown-pragmas -Wno-error=varargs -Wno-format-truncation -Wno-error=address-of-packed-member -std=c99 -fopenmp -march=native -msse2 -g -Wfatal-errors -mfpmath=sse -O3 -DNDEBUG -O3 -ffast-math -fno-finite-math-only -fexpensive-optimizations  -Wl,--enable-runtime-pseudo-reloc -shared -o bin\libansel.dll -Wl,--out-implib,bin\libansel.dll.a -Wl,--major-image-version,0,--minor-image-version,0 @CMakeFiles\lib_ansel.rsp  && cd ."
C:/msys64_ucrt/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: bin/CMakeFiles/lib_ansel.dir/common/presets.c.obj: in function `get_preset_element':
C:/msys64_ucrt/home/ms/ansel/src/common/presets.c:154:(.text+0x18): undefined reference to `__imp_xmlXPathNewContext'
C:/msys64_ucrt/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64_ucrt/home/ms/ansel/src/common/presets.c:160:(.text+0x60): undefined reference to `__imp_xmlXPathEvalExpression'
C:/msys64_ucrt/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64_ucrt/home/ms/ansel/src/common/presets.c:168:(.text+0x8b): undefined reference to `__imp_xmlNodeListGetString'
C:/msys64_ucrt/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64_ucrt/home/ms/ansel/src/common/presets.c:175:(.text+0xa6): undefined reference to `__imp_xmlFree'
C:/msys64_ucrt/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64_ucrt/home/ms/ansel/src/common/presets.c:177:(.text+0xb4): undefined reference to `__imp_xmlXPathFreeObject'
C:/msys64_ucrt/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: C:/msys64_ucrt/home/ms/ansel/src/common/presets.c:180:(.text+0xbd): undefined reference to `__imp_xmlXPathFreeContext'
C:/msys64_ucrt/ucrt64/bin/../lib/gcc/x86_64-w64-mingw32/13.2.0/../../../../x86_64-w64-mingw32/bin/ld.exe: bin/CMakeFiles/lib_ansel.dir/common/presets.c.obj: in function `dt_presets_save_to_file':
...
collect2.exe: error: ld returned 1 exit status
[44/402] Building C object lib/ansel/plugins/lighttable/CMakeFiles/menu.dir/tools/menu.c.obj
ninja: build stopped: subcommand failed.
```

## Replies

**dtuser** — 2023-08-23

BTW, I was able to compile it on Ubuntu v22 with no problem whatsoever. But still no luck on Windows MSYS2. Any help would be welcome.

---

**Scorpion078** — 2023-08-31

You should try again now.

3 days ago there were quite a few new commits to the code and I was able to build it on windows with no problems.

---

**dtuser** — 2023-09-01

It worked, thank you!

