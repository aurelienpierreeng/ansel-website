---
title: "Erreur au démarrage de Ansel-0.0.0+857"
date: 2024-07-09
slug: "erreur-au-démarrage-de-ansel-0-0-0-857"
tags:
  - Community archive
forum_author: "Unknown"
forum_category: "Recovered from web archive"
forum_url: "https://community.ansel.photos/view-discussion/erreur-au-démarrage-de-ansel-0-0-0-857"
wayback_url: "https://web.archive.org/web/20250120175350/https://community.ansel.photos/view-discussion/erreur-au-démarrage-de-ansel-0-0-0-857"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/erreur-au-démarrage-de-ansel-0-0-0-857`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20250120175350/https://community.ansel.photos/view-discussion/erreur-au-démarrage-de-ansel-0-0-0-857).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Unknown** on 2024-07-09.*

Bonjour,

``` ql-syntax
:~$ /home/Applmage/Ansel-0.0.0+857.gea7aee827-x86_64.AppImage  
Something went wrong trying to read the squashfs image.
Erreur de segmentation (core dumped)
```

Système d'exploitation : Kubuntu 22.04

Version de KDE Plasma : 5.24.7

Version de KDE Frameworks : 5.92.0

Version de Qt : 5.15.3

Version de noyau : 5.15.0-113-generic (64-bit)

Plate-forme graphique : X11

Processeurs : 16 × AMD Ryzen 7 5700X 8-Core Processor

Mémoire : 31,2 Gio de mémoire vive

Processeur graphique : AMD Radeon RX 6600 XT

Bonne réception

## Replies

**Aurélien Pierre** — 2024-07-09

Probablement un problème avec fuse. Essayer :

``` ql-syntax
sudo apt --reinstall install fuse
```

---

**Dom** — 2024-07-09

``` ql-syntax
administrateur@Zalman:~$ sudo apt --reinstall install fuse
* No authentication device configured for user "administrateur".
[sudo] Mot de passe de administrateur :
Lecture des listes de paquets... Fait
Construction de l'arbre des dépendances... Fait
Lecture des informations d'état... Fait      
0 mis à jour, 0 nouvellement installés, 1 réinstallés, 0 à enlever et 5 non mis à jour.
Il est nécessaire de prendre 0 o/27,0 ko dans les archives.
Après cette opération, 0 o d'espace disque supplémentaires seront utilisés.
(Lecture de la base de données... 425214 fichiers et répertoires déjà installés.)
Préparation du dépaquetage de .../fuse_2.9.9-5ubuntu3_amd64.deb ...
Dépaquetage de fuse (2.9.9-5ubuntu3) sur (2.9.9-5ubuntu3) ...
Paramétrage de fuse (2.9.9-5ubuntu3) ...
update-initramfs: deferring update (trigger activated)
Traitement des actions différées (« triggers ») pour man-db (2.10.2-1) ...
Traitement des actions différées (« triggers ») pour initramfs-tools (0.140ubuntu13.4) ...
update-initramfs: Generating /boot/initrd.img-5.15.0-113-generic
W: Possible missing firmware /lib/firmware/amdgpu/yellow_carp_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/vangogh_gpu_info.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_rlc.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_mec2.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_mec.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_me.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_pfp.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_ce.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_sdma1.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/cyan_skillfish_sdma.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/sienna_cichlid_mes.bin for module amdgpu
W: Possible missing firmware /lib/firmware/amdgpu/navi10_mes.bin for module amdgpu
I: The initramfs will attempt to resume from /dev/nvme1n1p2
I: (UUID=7f033a75-af89-4e96-8756-40a39ef8118f)
I: Set the RESUME variable to override this.
administrateur@Zalman:~$
```

**vieux_loup@Zalman**:**~**\$ /home/Applmage/Ansel-0.0.0+857.gea7aee827-x86_64.AppImage 

Something went wrong trying to read the squashfs image.

Erreur de segmentation (core dumped)

**vieux_loup@Zalman**:**~**\$

Le problème persiste. En fait fuse n'était pas installé, donc pas nécessaire avant Ansel-0.0.0+837

L'upgrade ubuntu 22.04 vers ubuntu 24.04 devrait être libérée mi août

## Upgrades

Users of Ubuntu 23.10 will be offered an automatic upgrade to 24.04 soon after the release.

Users of 22.04 LTS however will be offered the automatic upgrade when 24.04.1 LTS is released, which is scheduled for the 15th of August.

Convient-il d'attendre la 24.04 LTS ?

---

**Aurélien Pierre** — 2024-07-09

Fuse a toujours été nécessaire pour ouvrir une paquet AppImage puisque ce paquet fonctionne dans un disque virtuel (FUSE = filesystem in userspace). Ceci dit les distributions Linux ont Fuse 2 et Fuse 3, et je ne sais pas lequel est requis. Ici, j'ai les deux et l'AppImage charge sans problème.

---

**Dom** — 2024-07-09

``` ql-syntax
vieux_loup@Zalman:~$ fusermount -V
fusermount version: 2.9.9
vieux_loup@Zalman:~$
```

Suite install fuse3 + reboot

``` ql-syntax
vieux_loup@Zalman:~$ fusermount -V
fusermount3 version: 3.10.5
vieux_loup@Zalman:~$ /home/Applmage/Ansel-0.0.0+857.gea7aee827-x86_64.AppImage  
Something went wrong trying to read the squashfs image.
Erreur de segmentation (core dumped)
vieux_loup@Zalman:~$ /home/Applmage/Ansel-0.0.0+837.g3799e7893-x86_64.AppImage  
Gtk-Message: 19:58:23.555: Failed to load module "colorreload-gtk-module"
Gtk-Message: 19:58:23.555: Failed to load module "window-decorations-gtk-module"

(AppRun.wrapped:10210): Gtk-WARNING **: 19:58:23.607: Theme directory places/128 of theme ubuntustudio-dark has no size field


(AppRun.wrapped:10210): Gtk-WARNING **: 19:58:23.607: Theme directory places/scalable of theme ubuntustudio-dark has no size field


(AppRun.wrapped:10210): Gtk-WARNING **: 19:58:25.455: Theme directory places/128 of theme ubuntustudio-dark has no size field


(AppRun.wrapped:10210): Gtk-WARNING **: 19:58:25.455: Theme directory places/scalable of theme ubuntustudio-dark has no size field
```

``` ql-syntax
vieux_loup@Zalman:~$ locate -i -r /fuse
/etc/fuse.conf
/home/vieux_loup/.cache/JetBrains/PyCharmCE2023.3/python_stubs/-32419094/Cython/Compiler/FusedNode.py
/home/vieux_loup/.cache/JetBrains/PyCharmCE2023.3/python_stubs/cache/803144086d2db3c0bebe97a831bf60b733d1ca0312caf8da30e493ba701753e3/Cython/Compiler/FusedNode.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/ComfyUI/comfy_extras/chainner_models/architecture/face/fused_act.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/ComfyUI/custom_nodes/comfyui_controlnet_aux/src/custom_mmpkg/custom_mmcv/cnn/utils/fuse_conv_bn.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/ComfyUI/custom_nodes/comfyui_controlnet_aux/src/custom_mmpkg/custom_mmcv/ops/fused_bias_leakyrelu.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/fsspec/fuse.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/fsspec/__pycache__/fuse.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/jax/_src/cudnn/fused_attention_stablehlo.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/jax/_src/cudnn/__pycache__/fused_attention_stablehlo.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/_inductor/fx_passes/fuse_attention.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/_inductor/fx_passes/__pycache__/fuse_attention.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/nn/intrinsic/modules/fused.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/nn/intrinsic/modules/__pycache__/fused.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/fuse_modules.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/fuser_method_mappings.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/__pycache__/fuse_modules.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/__pycache__/fuser_method_mappings.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/fx/fuse.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/fx/fuse_handler.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/fx/__pycache__/fuse.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/ao/quantization/fx/__pycache__/fuse_handler.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/fx/passes/utils/fuser_utils.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/fx/passes/utils/__pycache__/fuser_utils.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/native/cuda/fused_adam_amsgrad_impl.cuh
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/native/cuda/fused_adam_impl.cuh
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/native/cuda/fused_adam_utils.cuh
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/native/cuda/fused_adamw_amsgrad_impl.cuh
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/native/cuda/fused_adamw_impl.cuh
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/ops/fused_moving_avg_obs_fake_quant.h
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/ops/fused_moving_avg_obs_fake_quant_compositeimplicitautograd_dispatch.h
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/ops/fused_moving_avg_obs_fake_quant_native.h
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/ATen/ops/fused_moving_avg_obs_fake_quant_ops.h
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/torch/csrc/jit/passes/fuse_linear.h
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/include/torch/csrc/jit/passes/fuse_relu.h
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/nn/intrinsic/modules/fused.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/nn/intrinsic/modules/__pycache__/fused.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/quantization/fuse_modules.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/quantization/fuser_method_mappings.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/quantization/__pycache__/fuse_modules.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/quantization/__pycache__/fuser_method_mappings.cpython-311.pyc
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/quantization/fx/fuse.py
/home/vieux_loup/.local/share/krita/ai_diffusion/server/venv/lib/python3.11/site-packages/torch/quantization/fx/__pycache__/fuse.cpython-311.pyc
/mnt/Stockage/Gestion_PC/1 Applications/Fuser
'/mnt/Stockage/Gestion_PC/1 Applications/Fuser/'$'\n''Forcer un périphérique à se démonter sous Ubuntu Linux.desktop'
'/mnt/Stockage/Gestion_PC/1 Applications/Fuser/Apprenez à utiliser la commande '$'\'''fuser'$'\''' avec des exemples sous Linux.desktop'
/mnt/Stockage/Gestion_PC/1 Applications/Fuser/fuser - identify processes using files or sockets.desktop
/mnt/Stockage/Gestion_PC/1 Applications/Fuser/psmisc.desktop
/mnt/Stockage/Gestion_PC/1 Applications/Fuser/utilities that use the proc file system.desktop
/snap/core/16928/lib/systemd/system/fuse.service
/snap/core/16928/usr/share/bash-completion/completions/fusermount
/snap/core/17200/lib/systemd/system/fuse.service
/snap/core/17200/usr/share/bash-completion/completions/fusermount
/snap/core18/2823/lib/systemd/system/fuse.service
/snap/core18/2823/usr/share/bash-completion/completions/fusermount
/snap/core18/2829/lib/systemd/system/fuse.service
/snap/core18/2829/usr/share/bash-completion/completions/fusermount
/snap/core20/2264/usr/share/bash-completion/completions/fusermount
/snap/core20/2318/usr/share/bash-completion/completions/fusermount
/snap/core22/1122/usr/share/bash-completion/completions/fusermount
/snap/core22/1380/usr/share/bash-completion/completions/fusermount
/usr/bin/fuser
/usr/bin/fusermount
/usr/bin/fusermount3
/usr/include/boost/fusion/functional/adapter/fused.hpp
/usr/include/boost/fusion/functional/adapter/fused_function_object.hpp
/usr/include/boost/fusion/functional/adapter/fused_procedure.hpp
/usr/include/boost/fusion/include/fused.hpp
/usr/include/boost/fusion/include/fused_function_object.hpp
/usr/include/boost/fusion/include/fused_procedure.hpp
/usr/include/boost/hana/fuse.hpp
/usr/include/boost/hana/fwd/fuse.hpp
/usr/include/linux/fuse.h
/usr/lib/modules/5.15.0-113-generic/kernel/fs/fuse
/usr/lib/modules/5.15.0-113-generic/kernel/fs/fuse/cuse.ko
/usr/lib/modules/5.15.0-113-generic/kernel/fs/fuse/virtiofs.ko
/usr/lib/python3/dist-packages/fuse.py
/usr/lib/python3/dist-packages/fuse_python-1.0.2.egg-info
/usr/lib/python3/dist-packages/fuseparts
/usr/lib/python3/dist-packages/Cython/Compiler/FusedNode.cpython-310-x86_64-linux-gnu.so
/usr/lib/python3/dist-packages/Cython/Compiler/FusedNode.py
/usr/lib/python3/dist-packages/Cython/Compiler/__pycache__/FusedNode.cpython-310.pyc
/usr/lib/python3/dist-packages/__pycache__/fuse.cpython-310.pyc
/usr/lib/python3/dist-packages/borg/fuse.py
/usr/lib/python3/dist-packages/borg/fuse_impl.py
/usr/lib/python3/dist-packages/borg/__pycache__/fuse.cpython-310.pyc
/usr/lib/python3/dist-packages/borg/__pycache__/fuse_impl.cpython-310.pyc
/usr/lib/python3/dist-packages/fuse_python-1.0.2.egg-info/PKG-INFO
/usr/lib/python3/dist-packages/fuse_python-1.0.2.egg-info/dependency_links.txt
/usr/lib/python3/dist-packages/fuse_python-1.0.2.egg-info/top_level.txt
/usr/lib/python3/dist-packages/fuseparts/__init__.py
/usr/lib/python3/dist-packages/fuseparts/__pycache__
/usr/lib/python3/dist-packages/fuseparts/_fuse.cpython-310-x86_64-linux-gnu.so
/usr/lib/python3/dist-packages/fuseparts/setcompatwrap.py
/usr/lib/python3/dist-packages/fuseparts/subbedopts.py
/usr/lib/python3/dist-packages/fuseparts/__pycache__/__init__.cpython-310.pyc
/usr/lib/python3/dist-packages/fuseparts/__pycache__/setcompatwrap.cpython-310.pyc
/usr/lib/python3/dist-packages/fuseparts/__pycache__/subbedopts.cpython-310.pyc
/usr/share/bash-completion/completions/fusermount
/usr/share/doc/fuse3
/usr/share/doc/fuse3/changelog.Debian.gz
/usr/share/doc/fuse3/copyright
/usr/share/icons/Papirus/16x16/apps/fuse-emulator.svg
/usr/share/icons/Papirus/16x16/apps/fuse.svg
/usr/share/icons/Papirus/22x22/apps/fuse-emulator.svg
/usr/share/icons/Papirus/22x22/apps/fuse.svg
/usr/share/icons/Papirus/24x24/apps/fuse-emulator.svg
/usr/share/icons/Papirus/24x24/apps/fuse.svg
/usr/share/icons/Papirus/32x32/apps/fuse-emulator.svg
/usr/share/icons/Papirus/32x32/apps/fuse.svg
/usr/share/icons/Papirus/48x48/apps/fuse-emulator.svg
/usr/share/icons/Papirus/48x48/apps/fuse.svg
/usr/share/icons/Papirus/64x64/apps/fuse-emulator.svg
/usr/share/icons/Papirus/64x64/apps/fuse.svg
/usr/share/initramfs-tools/hooks/fuse
/usr/share/man/de/man1/fuser.1.gz
/usr/share/man/fr/man1/fuser.1.gz
/usr/share/man/man1/fuser.1.gz
/usr/share/man/man1/fusermount.1.gz
/usr/share/man/man1/fusermount3.1.gz
/usr/share/man/man4/fuse.4.gz
/usr/share/man/pt_BR/man1/fuser.1.gz
/usr/share/man/ru/man1/fuser.1.gz
/usr/share/man/uk/man1/fuser.1.gz
/usr/src/linux-headers-5.15.0-113/drivers/gpu/drm/nouveau/nvkm/subdev/fuse
/usr/src/linux-headers-5.15.0-113/drivers/gpu/drm/nouveau/nvkm/subdev/fuse/Kbuild
/usr/src/linux-headers-5.15.0-113/drivers/soc/tegra/fuse
/usr/src/linux-headers-5.15.0-113/drivers/soc/tegra/fuse/Makefile
/usr/src/linux-headers-5.15.0-113/fs/fuse
/usr/src/linux-headers-5.15.0-113/fs/fuse/Kconfig
/usr/src/linux-headers-5.15.0-113/fs/fuse/Makefile
/usr/src/linux-headers-5.15.0-113/include/soc/tegra/fuse.h
/usr/src/linux-headers-5.15.0-113/include/uapi/linux/fuse.h
/usr/src/linux-headers-5.15.0-113-generic/include/config/FUSE_DAX
/usr/src/linux-headers-5.15.0-113-generic/include/config/FUSE_FS
/var/lib/dpkg/info/fuse3.conffiles
/var/lib/dpkg/info/fuse3.list
/var/lib/dpkg/info/fuse3.md5sums
/var/lib/dpkg/info/fuse3.postinst
/var/lib/dpkg/info/fuse3.postrm
/var/lib/dpkg/info/fuse3.triggers
/var/lib/flatpak/app/net.sourceforge.Hugin/x86_64/stable/abd76ec6688919f65d8d99971fdc69b0fe232c41d6d45ec0b35b352799d0f733/files/share/hugin/data/output/fused_layers.executor
/var/lib/flatpak/app/org.kde.digikam/x86_64/stable/97a7d6973a13bbb4afa735ce2f2ac6fd1c075cb69b24bd8084f975ab983fb46b/files/share/hugin/data/output/fused_layers.executor
/var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/22.08/f3a591e25e87b8267afc80f350b1ead04d5627492dc7f4b19e9b8a4903c5673a/files/bin/fusermount
/var/lib/flatpak/runtime/org.freedesktop.Platform/x86_64/22.08/f3a591e25e87b8267afc80f350b1ead04d5627492dc7f4b19e9b8a4903c5673a/files/etc/init.d/fuse
/var/lib/flatpak/runtime/org.kde.Platform/x86_64/5.15-22.08/617d94de873c8650b5e6259dca14c6262755def9ad492da5a213b4e2e22a8412/files/bin/fusermount
/var/lib/flatpak/runtime/org.kde.Platform/x86_64/5.15-22.08/617d94de873c8650b5e6259dca14c6262755def9ad492da5a213b4e2e22a8412/files/etc/init.d/fuse
/var/lib/swcatalog/icons/ubuntu-jammy-universe/128x128/fuse-emulator-gtk_fuse.png
/var/lib/swcatalog/icons/ubuntu-jammy-universe/128x128/fuse-emulator-sdl_fuse.png
/var/lib/swcatalog/icons/ubuntu-jammy-universe/48x48/fuse-emulator-gtk_fuse.png
/var/lib/swcatalog/icons/ubuntu-jammy-universe/48x48/fuse-emulator-sdl_fuse.png
/var/lib/swcatalog/icons/ubuntu-jammy-universe/64x64/fuse-emulator-gtk_fuse.png
/var/lib/swcatalog/icons/ubuntu-jammy-universe/64x64/fuse-emulator-sdl_fuse.png
vieux_loup@Zalman:~$  
```

Ansel 837 : Ok

Ansel 857 : Pas Ok

[https://stackoverflow.com/questions/16991414/which-fuse-version-in-my-kernel](https://stackoverflow.com/questions/16991414/which-fuse-version-in-my-kernel)‍‍

---

**Dom** — 2024-07-09

Fonctionne après avoir re-téléchargé Ansel-0.0.0+857

Les mystères de l'informatique !

Merci pour les retours.

---

**Aurélien Pierre** — 2024-07-09

Probablement un téléchargement corrompu…

---

**Aurélien Pierre** — 2024-07-09

[See more...](javascript:void(0))

