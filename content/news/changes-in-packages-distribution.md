---
title: Changes in Ansel packages distribution
date: 2026-04-10
tags:
  - Development
authors:
    - Aurélien Pierre
---

## Target clones

Compiling the software natively on the computer use to improve runtimes on CPU by around 30 %. The reason is the compiler makes specific optimizations for the target hardware on which it is compiled, while pre-built packages have to stay generic and trigger more conservative optimization for the sake of wide support. Note that OpenCL kernels are, anyway, compiled for your particular GPU using your OpenCL driver, so the story is different there.

In 2016, GCC introduced [target clones](https://maskray.me/blog/2023-02-05-function-multi-versioning), followed in 2023 by CLang, for which I added support in Darktable in 2019 in some parts only (noticeably, the _tone equalizer_). This experiment had never been scaled to the whole software until now.

Target clones essentially allow to build different versions of the code, optimized for different hardware architectures, and the software will choose the right one to execute at runtime. Since this relies on `ifunc`, this is supported only on Linux (and even there, not for all versions of `libc`) and Mac OS Intel, so expect no Windows support. The same feature on Windows would have to be coded manually.

With generalized target clones, Ansel AppImages packages now run significantly faster, and within a 5 % margin compared to native builds (aka compiling yourself).

## Linux AppImage

2 months ago, an annoying bug forcing the recompilation of all OpenCL kernels at each AppImage start was fixed. The reason was that AppImage are mounted in a random container (unstable through restarts), while the integrity check performed on kernels (as to recompile only when they changed) hardcoded the path of the binary. That AppImage-only penalty is now solved.

AppImages have been modified to accept command-line arguments and expose other binaries than the main GUI. This allows:

1. to get debug logs through `./Ansel-xxxx-x86_64.AppImage -d dev -d perf -d opencl -d verbose`,
2. to process images without GUI through `./Ansel-xxxx-x86_64.AppImage ansel-cli input.raw output.tif`
3. to call other internal programs (see the [docs](/doc/install/linux/#run-the-appimage)).

## Docker images

Nightly builds have been added as [Docker images](https://hub.docker.com/r/aurelienpierre/ansel) too. These will allow to run `ansel-cli` on backend servers. Note though that Ansel CLI is not safe to run on servers with public web access, as it doesn't prevent code injection and doesn't sanitize user inputs in any way. Docker images are based on Ubuntu 24.04.

One possible use case of Docker images would be to run rendering farms to offload Ansel image exports to servers with large GPU :

- send the RAW and editing XMP to the server,
- get the resulting JPG.

On reasonably-fast networks, that would prevent users from buying expensive hardware if they only rarely use it to its full potential, while sharing the cost of a 24/7 remote server between users.

## MacOS

MacOS nightly builds have been added last October for the Apple M (Arm64) architecture. In September 2025, Github added runners for MacOS 15 Sonoma on Intel architecture. This allowed to add support of Intel i386 for Ansel nightly builds today.

Note that [Apple Intel architecture](https://github.com/actions/runner-images/issues/13045) is planned for deprecation by Github in August 2027 since Apple has discontinued support of this architecture. After this, there will be no easy way of building Ansel for Apple Intel hardware.

## About nightly builds

Nightly-builds are auto-generated on Github runners (think of them as virtual servers you can start and stop from scripts to execute things), every morning between 5 and 7 am UTC. The generated packages are added to the [pre-release notes](https://github.com/aurelienpierreeng/ansel/releases/tag/v0.0.0), which acts as a repositories, and provides 1.5 year of build histories so you get a chance to rollback to a previously-working version if code changes suddently break the application in a way that prevents you from using it.

The nightly builds are entirely dependent:

- on Github for providing the runners, 
- on [Homebrew](https://docs.brew.sh/) for providing the MacOS dependencies ecosystem,
- on [MSYS Pacman](https://www.msys2.org/) for providing the Windows dependencies ecosystem,
- on [Ubuntu](https://ubuntu.com/download/server) for providing the Linux dependencies ecosystem.

That's a lot of third parties to rely on, and nightly builds often break just because Github deprecated a runner or one of MSYS/Ubuntu/Homebrew renamed a package, removed it or upgraded it to a newer version that changes API and breaks with Ansel internals. So, despite the apparent automatization of the whole workflow, regular maintenance is still needed and nightly builds might stay broken for some time.