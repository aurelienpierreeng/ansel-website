---
title: "Do OpenCL accelerated modules scale with GPU memory?"
date: 2023-11-21
slug: "do-opencl-accelerated-modules-scale-with"
tags:
  - Community archive
forum_author: "David Miguel"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/do-opencl-accelerated-modules-scale-with"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/do-opencl-accelerated-modules-scale-with`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **David Miguel** on 2023-11-21.*

Its the moment for me, I can spare some money to buy a used graphic card for work.

So I wonder, is an entry level gaming card enough for Ansel?

Do workstation cards (with more memory) make sense for Ansel?

In other words, what do I prioritize when shopping for a card: raw GPU computing power or memory?

## Replies

**Aurélien Pierre** — 2023-11-23

It's hard to guess the actual performance of a GPU by just reading its specs. Only benchmarks can tell.

For example, Nvidia has the GeForce (gamers) and Quadro (pro) ranges, but they use the same chips. From what I understood, it seems GeForce are optimized for real-time rendering (high FPS in video games), while Quadro are optimized for offline rendering (3D rendering, machine-learning, etc.). Offline and real-time are different way to use the memory and lead to different optimization choices in the drivers (continuous I/O at low latency vs. timed I/O at high FLOPS).

Nonetheless, it seems the GeForce models consistently get better scores in OpenCL benchmarks… Go figure.

You may find relevant benchmarks for OpenCL perf here :

- https://compubench.com/result.jsp
- https://browser.geekbench.com/opencl-benchmarks

I would just pick the highest ranking model that your money can buy.

If you stumble upon other benchmarks and tests, be sure they test OpenCL, because the performance of DirectX, OpenGL, Vulkan, TensorFlow, etc. is mildly relevant for us here. Also, the trick is performance depends on the driver version too.

Finally, there is a trick with GPU used for OpenCL : you don't need them connected to your screen. Say you have an integrated Intel chip or a weak discrete GPU, you can keep it to render anything graphic (OpenGL, desktop environment, etc.) and send the image buffer to the display via HDMI/VGA/DisplayPort. Then you can use your beefy GPU only through OpenCL.

I have seen benchmarks where offscreen GPU offers twice as much speed than what you get with them onscreen.

---

**migmoq** — 2023-11-24

I'm taking advantage of the question about OpenCL to ask an additional one: some GPU supports OpenCL 3 whereas others supports OpenCL 2.1.

What is the expectation of Ansel on the version of OpenCL?

---

**Aurélien Pierre** — 2024-01-17

Ansel uses the OpenCL 1.2 API. Note that I have seen benchmarks where some tasks take longer to complete with OpenCL 2 than 1, so it's not necessarily better. Also, the OpenCL versions are API versions, they mostly just add new methods and types to speed-up development, ultimately the performance depends how vendor implement the API.

