---
title: New build options for Linux
date: 2023-06-16
tags:
  - Development
authors:
    - Aurélien Pierre
---

I accidentally discovered that the Linux build script used a "package" build, meaning the CPU optimizations are limited to generic ones in order to produce portable binaries that can be installed on any x86-64 platform. By "using", I mean the package build was not explicitely disabled, so it was enabled by default.

Anyway, this is now disabled by default, since the actual packages (.exe and .appimage) are not built through that script, which is primarily meant to help end-users. To get the previous behaviour back, you would need to run:

```
$ sh build.sh --build-package --install --sudo
```

Not using the package build option may increase performance on CPU by 20 to 30 % depending on your hardware, thanks to platform-specific optimizations.

I have also introduced a new argument that will launch the Git updating commands that users seem to forget all the time. There is a caveat, though : updating the source code by calling Git from within the script doesn't update the script for the current run, so this method doesn't work when the script itself is modified. Fortunately, we don't change this script often.

The argument to update the source code and the submodules (Rawspeed, Libraw) :

```
$ sh build.sh --update --install --sudo
```

I have also modified the internals of that script in order to automatically :

- update the Lensfun database of lenses,
- add a global system shortcut (.desktop file) so the software will be globally available from the app menus,
- add a global system command so the ansel is globally available from the terminal.

The goal of all these changes is obviously to make it more user-friendly to use a self-built version of the software, allowing to improve performance, especially for computers without GPU. The one-pit-stop command would be :

```
$ sh build.sh --update --install --sudo --clean-all
```

But of course, you will need to run the Git update manually one last time before, to update the script itself :

```
$ git pull --recurse-submodule
```

Alternatively, you can directly download the build script, and replace the old build.sh one at the root of the source code directory.
