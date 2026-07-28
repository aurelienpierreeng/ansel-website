---
title: "Ansel on Mac"
date: 2023-04-30
slug: "ansel-on-mac"
tags:
  - Community archive
forum_author: "erik"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/ansel-on-mac"
wayback_url: "https://web.archive.org/web/20241210185138/https://community.ansel.photos/view-discussion/ansel-on-mac"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/ansel-on-mac`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20241210185138/https://community.ansel.photos/view-discussion/ansel-on-mac).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **erik** on 2023-04-30.*

Hi! I have managed to build and run ansel on my MacBook. For those who are interested, I will publish the builds [here](https://www.qwd.no/ansel.html). All builds that I upload have been tested on my machine, and it will be a true "works on my machine" scenario. At the moment I have a MacBook Pro 16", 2019, running macOS Ventura (13.3.1). The closer your machine are to this, the more likeliy it is that the build will work for you as well. These builds are unofficial and I will not do any support. New builds will be uploaded every now and then.

## Replies

**Laurent Perraut** — 2023-04-30

Hi Erik, many thanks! I'm working on the same goal but with the intention to compile on Apple silicon. I forked ansel [here](https://github.com/lologor/ansel/) and commit some changes in particular in the packaging/macosx area - but not only. Build is running through and Ansel (I took the liberty to put a capital letter) works quite stable but I still have minor issues:

- GTK 3.24.37 version of hombrew still causing some issues, in particular in local menues (selecting an entry doesn't always work)
- Roboto fonts still need to be manually installed and "Roboto Condensed" font still creates a warning that it couldn't be found at start.
- Long time stability isn't garanteed due to version changes of a lot of dependencies. Time will say if this is stable. That's the reason why I didn't create a Pull Request until now.

Maybe we can learn from each others experience...

---

**erik** — 2023-05-01

Hi Laurent, good work on the fork! I completely agree with you that dependency management is one of the big challenges for of long term stability. The dependency management on my machine is a bit of a mess. I initially wanted to install all dependencies via MacPorts (as I have had better experience with that than with brew), but after a lot of miserable debugging I ended up having some dependencies install with brew and some with MacPorts. I am not sure what the best method would be going forward, but it is definitely not the way I have set it up now. Perhaps pinning the dependency versions an install them in an isolated build environment would be the most “stable” approach? but I don’t know. I also encountered a regression with Apple's bundeled compiler in Command Line Tools 14.3, so it is not just dependency management that pose a risk for long term build stability.

I had some issues with menus not working with GTK 3.24.34 a while back, but I patched it manually after following the guidance [here](https://github.com/darktable-org/darktable/issues/12727#issuecomment-1322477622), and I haven’t noticed any issues since then. But perhaps I haven’t used Ansel enough to encounter an issue yet. I haven’t really touched the roboto fonts, so I don’t really know about that.

---

**Laurent Perraut** — 2023-05-01

Hi Erik, thanks for pointing out the issue with GTK and menus. I experienced this problem in earlier tries but it is solved with the latest releases. My problem is choosing a menu entry e.g. in "Filmic rgb / Options / Color science". Choosing an entry endup often by selecting the first entry. Only with insisting or with the keyboard another entry can be selected. Strange. I'm curious if you have the same issue.

I created a file to record dependencies, to be at least capable to "recover" when necessary. I didn't get issues with the Xcode compiler so far.

---

**erik** — 2023-05-02

Strange, I havn't experienced the issue that you are describing. If I go to "Filmic rgb / Options / Color science" and click on any of the options, it is chosen correctly every time. I don't have to "force" the correct choice with the keyboard. It might be a bit far fetched, but the only significant difference between our build systems are GTK 3.24.37 (brew) and GTK 3.24.34+patch (MacPorts) so the issue might be there. I assume you have a M1/M2 mac? I don't know if it is possible, but it would be interesting to know if you experience the same issue with the build "*ansel-v0.0.0+287~g4937a8b41*" listed [here](https://www.qwd.no/ansel.html) (that is the build I am running at the moment). EDIT: link

---

**Lukas** — 2023-05-02

This is awesome! Thank you for sharing your efforts. I'll try the build in the coming days

---

**Aurélien Pierre** — 2023-05-02

(It would be great if we could coordonate efforts here). Cool stuff !

---

**Laurent Perraut** — 2023-05-02

Hi Erik, yes I'm running an M2 Pro mac mini. I downloaded your build but it doesn't start. It claims libgmic is missing and I cannot install it on my mac and run mixed code (ansel on x86_64, library on arm64). I tried the build of darktable 4.2.1 and I get a similar behaviour... in both build after a second the entry can be selected. BUT I also tried my build of darktable 3.8.1 (yes I got it running on my M2 mac as well but broke somewhere the building process...) and there it simply works!

I will follow two paths:

- Even if unprobable, exclude that the issue is due to a local problem. If someone following this discussion can test my image (at own risk of course) on a latest Ventura 13.3.1 arm64 system, that would be great: [https://filedn.com/lxq2oIO61Rdjuk1dvBFLayu/Ansel-v0.0.0%2B297~g092df1dfe-arm64.dmg](https://filedn.com/lxq2oIO61Rdjuk1dvBFLayu/Ansel-v0.0.0%2B297~g092df1dfe-arm64.dmg)
- Try to understand the differences between the two builds: libraries, darktable/ansel code

But beside that, Ansel runs pretty stable! I'm quite close of retiring darktable 3.8.1 - my last production version...

---

**erik** — 2023-05-03

Thanks for giving it a try. It is not unlikely that I stuffed up somewhere and built using a shared library or something. If the build complains that it is missing libgmic then I assume it won’t work for anybody else either. I will take a look on my side as well.

---

**Laurent Perraut** — 2023-05-05

Short news: It's a local problem. I used a virtual maschine with a fresh installed macos and have no issue with the combo boxes... At least an issue less!

---

**Laurent Perraut** — 2023-05-13

Short news (2): I solved my issue: The mouse double click setting in macos was shifted to "slow". This was translated in GTK+ (gtk-double-click-time) with a value of 1800 ms... that's really slow. Back to default value and the issue is gone.

I will continue to chase the font issue now.

---

**Laurent Perraut** — 2023-05-14

Short news (3): I created a new image [here](https://filedn.com/lxq2oIO61Rdjuk1dvBFLayu/Ansel-v0.0.0%2B307~g1bb0edc13-arm64.dmg) for Apple silicon (M1/M2). What's new:

- Roboto fonts are now integrated in the app bundle. Issue with condensed ones solved (maybe break with other fonts...).
- Ansel icon is now bound to the app.
- Newest libs from homebrew built in, without breaking the app (so far I could test).
- Build for macos 13.3.1.

Feel free to test (at your own risk of course...)!

---

**Aurélien Pierre** — 2023-06-09

That's a manually-built image or is there some script that can run in a Github action here ?

---

**Laurent Perraut** — 2023-06-09

Hi Aurélien, this is based on scripts (https://github.com/lologor/ansel/tree/master/packaging/macosx/\[1-4\]\*.sh). I amended the original scripts from Darktable. I tested them on a freshly install macos instance and this was working. Making use of GitHub action is something I never did before. I would need to learn that to be capable to contribute.

---

**Aurélien Pierre** — 2023-06-09

Ok, if it is scripted and works locally, I can make it work with Github actions. I have way more experience with those than I would have wanted. The only issue is Github provides only x86_64 machines for Mac OS, no ARM64.

---

**isaac** — 2023-06-20

Firstly big thanks to @Aurélien Pierre for Ansel.

Thanks for looking into this ﻿@Laurent Perraut﻿ I'm interesting in using Ansel (current Darktable user) on Mac too but for Intel. Trying to build Ansel using your scripts I'm getting a Segmentation Fault in iop_profile.c

``` ql-syntax
clang: fatal error: unable to execute command: Segmentation fault: 11
Apple clang version 14.0.3 (clang-1403.0.22.14.1)
Target: x86_64-apple-darwin22.5.0
Thread model: posix
InstalledDir: /Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/bin
[ 46%] Building C object bin/CMakeFiles/lib_ansel.dir/common/tags.c.o
[ 46%] Building C object bin/CMakeFiles/lib_ansel.dir/common/undo.c.o
make[2]: *** [bin/CMakeFiles/lib_ansel.dir/common/iop_profile.c.o] Error 254
make[2]: *** Waiting for unfinished jobs.
```

I have removed -DBUILD_SSE2_CODEPATHS=OFF from your script as this is for Intel.

If I remove -DBINARY_PACKAGE_BUILD=ON it will build cleanly.

Sorry if this is a n00b question, I'm not very experienced with C (I'm actually a Java developer). I'm wondering if its a local issue with brew as I use it for work tools as well.

Running Ventura 13.4.

---

**isaac** — 2023-06-20

Sorry ﻿@erik﻿ I didn't realise you created this thread. I am currently testing your latest build thanks BTW. It looks like the version I managed to build locally, in that the theme appears a little broken to me. I don't see the 'Ansel' branding on the top left nor do I see the views on the top right Lighttable \| Darkroom etc. From my little testing it appear to work ok.

*\[attachment lost: image was hosted on the retired forum\]*

---

**Lukas** — 2023-06-20

Hey @isaac, in regard of the Ansel logo and the missing views in the top right, your screenshot looks fine. Both elements have been removed some time ago. On the other hand your screenshots still shows a different configuration of the top and bottom panel. However, that's all work in progress, so it might not be worth chasing down the reasons. I would really like to build Ansel on my Mac too, but being stuck on BigSur ﻿😬﻿ I don't know where to start.

---

**isaac** — 2023-06-20

Cheers for the info ﻿@Lukas﻿ I was going off the screenshot on the Ansel homepage

---

**erik** — 2023-06-20

Hi! I have problems with the segmentation faults too. I haven't manage to solve it (properly), but I have narrowed it down a bit:

1.  It appears to be an issue when building Ansel with newer versions of clang. It seems to compile without issues with the build tools that is packaged with Apple Command Line Tools 14.2 or older. One quick fix is to downgrade you Apple Command Line Tools to version 14.2, but this is quite annoying as Apple is very eager to upgrade them again to the latest version.
2.  The segmentation fault only happens when the optimisation flag is set (-O1, -O2, -O3, etc). If the optimisation flag is removed, the file (iop_profile.c) compiles without issues on newer versions of clang.
3.  According to git bisect, the compiler has issues with the changes introduced in this commit: [https://github.com/aurelienpierreeng/ansel/commit/db783b2c6c13f362297632a72f28f021696c90c1](https://github.com/aurelienpierreeng/ansel/commit/db783b2c6c13f362297632a72f28f021696c90c1). There might be other commits as well, but this is the first one that breaks when trying to compile iop_profile.c

I will try to look into it, but I am not an expert in C by any means. At the moment I am just building with Apple Command Line Tools 14.2 and call it a day. But this is a fix, not a solution. I will upload a new build ([here](https://www.qwd.no/ansel.html)) for intel Macs later today.

EDIT: Developer Tools -\> Command Line Tools

---

**Laurent Perraut** — 2023-06-20

Hi ﻿@isaac﻿ , I don't have an Intel mac at hand currently, I cannot test at the moment. I get Ansel compliled on my arm mac using xcode cli tools version 14.3.1. As soon I get access to an Intel mac I'll try.

---

**isaac** — 2023-06-21

Hi All,

I've managed to track down the Segmentation Fault issue after commenting sections of code in the iop_profile.c file and slowing adding methods back one at a time.

It's caused by \_\_DT_CLONE_TARGETS\_\_

It seems the Mac c compiler doesn't like the 'target_clones' attribute. Updating darktable.h to ignore this for Mac allows me to compile cleanly.

Line 129 changed

``` ql-syntax
#if __has_attribute(target_clones) && !defined(_WIN32) && !defined(NATIVE_ARCH)
```

To

``` ql-syntax
#if __has_attribute(target_clones) && !defined(_WIN32) && !defined(__APPLE__) && !defined(NATIVE_ARCH)
```

﻿@Laurent Perraut﻿ you would have been skipping this because of the M1 architecture

---

**isaac** — 2023-06-21

I also managed to use ﻿@Laurent Perraut﻿ 's ./3_make_hb_ansel_package.sh script to create an app. Though instead of updating graphicsmagick as suggested in the BUILD_hb.txt

I just created a 'naughty' symlink for missing libtiff.6.dylib ﻿🔨﻿

``` ql-syntax
ln -s /usr/local/opt/libtiff/lib/libtiff.5.dylib /usr/local/opt/libtiff/lib/libtiff.6.dylib 
```

---

**Laurent Perraut** — 2023-06-21

Hi ﻿@isaac﻿ , wow good debugging! I took over your change in my fork. Thanks!

---

**Laurent Perraut** — 2023-06-21

Hi ﻿@isaac﻿ , I took over the instructions from the updated script out of the darktable repository. I recall I went into trouble (but I don't recall what exactly) and this was solving it.

---

**isaac** — 2023-06-21

Thanks for putting that change into your fork.

It's odd I haven't figured out why I needed to create that symlink above yet. I think it's some kind of conflict in brew.

Binary file ./macosx/package/Ansel.app/Contents/Resources/lib/gdk-pixbuf-2.0/2.10.0/loaders/libpixbufloader-tiff.so matches libtiff.6.dylib

I have the latest libtiff (4.5.1) installed by brew however it only provides libtiff.5.dylib that I can see.

**Update:** I assumed wrong was a local brew issue I only had 4.5.0 installed for some odd reason. ﻿🙄﻿

---

**isaac** — 2023-06-27

A totally cosmetic issue I have fixed locally is to change the 'heavy check' unicode 2714 to a normal 'check' unicode 2713 in the \`import.c\` file as on my Mac at least Unicode 2713 is available in a lot more fonts (including Roboto). This fixes the missing character in the Import dialog. See below:

*\[attachment lost: image was hosted on the retired forum\]*

*\[attachment lost: image was hosted on the retired forum\]*

I'm not sure if Aurélien is planning on re-writing any of this, I can create a PR but I don't want to waste his time if that is the case.

---

**Yann-Loïs** — 2023-06-27

I tried ansel-v0.0.0%2B336~g551be1d00.tar.gz on my intel NUC5 running Monterey. No direct launching , but running first ansel executable in terminal and then clicking ansel.app, it's OK ! Maybe could you find how to follow the usual way ...

---

**isaac** — 2023-06-30

I am building locally using Laurent's scripts and running on Ventura, and the initial app launch seems to be slow. But it launches fine after that for me.

edit: it is most likely because CMAKE_OSX_DEPLOYMENT_TARGET=13.3.1 which is Ventura

---

**Jiyone** — 2023-07-06

> I'm not sure if Aurélien is planning on re-writing any of this, I can create a PR but I don't want to waste his time if that is the case.

Please go create a PR !

---

**aoberoi** — 2023-08-17

Is there an Issue or PR I can follow to stay on top of (or help contribute to) the work for automating macOS arm64 builds?

The GitHub public roadmap indicates that arm64 runners for Actions are planned for Q4: https://github.com/orgs/github/projects/4247. However, if you look at the details, it has been pushed a couple times, so I wouldn't hold my breathe on it.

Another possible solution would be to use GitHub's affordance for self-hosted runners, paired with a cloud hosted Mac, as described here: https://blog.pantsbuild.org/m1-support-self-hosted/. Looking at MacStadium's pricing, it seems like the lowest cost bare metal mac would be about \$99 USD/month. I'd guess this cost is more than this project could put forward to get macOS builds.

---

**LucaZulberti** — 2023-11-20

Hi all, I successfully compiled and launched ansel with commit a8f73ed51b389015b89dbe38857f652b7439c7bf from [https://github.com/lologor/ansel](https://github.com/lologor/ansel/commits/master) on MacBook Pro M1 with MacOS Sonoma 14.1.1.

I have installed clang 16 from homebrew, OpenMP, zlib, and all the other dependencies...

Steps (or add CMAKE_C/CXX to build.sh)

``` ql-syntax
mkdir build
cd build
cmake -G "Ninja" -DCMAKE_INSTALL_PREFIX=/opt/ansel -DCMAKE_BUILD_TYPE=Release -DCMAKE_C_COMPILER=/opt/homebrew/Cellar/llvm/16.0.6/bin/clang -DCMAKE_CXX_COMPILER=/opt/homebrew/Cellar/llvm/16.0.6/bin/clang++ -DBINARY_PACKAGE_BUILD=OFF "/Users/luca/Git/ansel"
cmake --build . -- -j4
```

Anyway, there are some aspects to be fixed:

1.  A lot of: ansel/src/develop/masks/detail.c:230:3: warning: loop not vectorized: the optimizer was unable to perform the requested transformation; the transformation might be disabled or specified as part of an unsupported transformation ordering \[-Wpass-failed=transform-warning\] #pragma omp parallel for simd default(none)
2.  /Users/luca/Git/ansel/src/is_supported_platform.h:58:9: warning: Building without SSE2 is highly experimental. \[-W#pragma-messages\] \#pragma message "Building without SSE2 is highly experimental."
3.  /Users/luca/Git/ansel/src/is_supported_platform.h:59:9: warning: Expect a LOT of functionality to be broken. You have been warned. \[-W#pragma-messages\] \#pragma message "Expect a LOT of functionality to be broken. You have been warned."
4.  And at startup:

``` ql-syntax
[dt_detect_cpu_features] Not implemented for this architecture.
[dt_detect_cpu_features] Please contribute a patch.
[dt_init] SSE2 instruction set is unavailable.
[dt_init] expect a LOT of functionality to be broken. you have been warned.

(process:9390): GLib-GObject-CRITICAL **: 21:58:49.259: g_object_set: assertion 'G_IS_OBJECT (object)' failed
[dt_detect_cpu_features] Not implemented for this architecture.
[dt_detect_cpu_features] Please contribute a patch.
[dt_codepaths_init] will be using experimental plain OpenMP SIMD codepath.
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152
[dt_pthread_create] info: bumping pthread's stacksize from 524288 to 2097152

(ansel:9390): GLib-GObject-CRITICAL **: 21:58:52.419: invalid cast from 'GtkMenuBar' to 'GtkWindow'

(ansel:9390): Gtk-CRITICAL **: 21:58:52.419: gtk_window_add_accel_group: assertion 'GTK_IS_WINDOW (window)' failed
```

  

I will try to rebase on the upstream repo, and I hope to find solutions for those problems with time... Thank you for your work!

---

**Laurent Perraut** — 2023-12-17

Since two weeks I'm building a version of Ansel for MacOS arm64 (Ventura 13.3.1 or higher required) every week. All commits to date are included. In addition I fixed some GTK issues appearing on MacOS with the import and export dialogs - and some of the issues mentioned by Luca.

Be aware that the current version of Ansel (https://github.com/aurelienpierreeng/ansel) is work-in-progress. Aurélien and the developers are currently re-writing / re-factoring a lot of legacy code. You may experience issues and not working functions. But you will also enjoy the increased in speed as well!

Here the download link: [https://filedn.eu/lJJ6pRXjWFxSzF0qSaw2PjF/Ansel-v0.0.0%2B653~g0507839b5-arm64.dmg](https://filedn.eu/lJJ6pRXjWFxSzF0qSaw2PjF/Ansel-v0.0.0%2B653~g0507839b5-arm64.dmg)

Thanks for testing and giving feedback!

---

**koslowj** — 2024-11-04

Dear Ansel-on-Mac developers, what is the current status of your project(s)?

---

**sidney1310** — 2025-01-02

I just tried my first shot at building from git head on a Macbook Pro 2017 (Intel) running Ventura 13.7.2 using homebrew and the "custom way" build instructions. The only thing I had to change to get it to build was that the FindICU.cmake that is in the repo does not put any -I option for the icu4c include files in the the CPPFLAGS and so the compile fails. Rather than figure out how to fix it, I just built without icu, as that is optional anyway. It runs, though with some error messages to the terminal on startup, and crashes if I try to resize the window. It does seem like something that can be worked with.

