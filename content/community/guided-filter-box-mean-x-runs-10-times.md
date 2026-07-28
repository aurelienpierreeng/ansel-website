---
title: "guided_filter_box_mean_x runs 10 times slower than guided_filter_box_mean_y"
date: 2024-01-06
slug: "guided-filter-box-mean-x-runs-10-times"
tags:
  - Community archive
forum_author: "jjw"
forum_category: "Developers talk"
forum_url: "https://community.ansel.photos/view-discussion/guided-filter-box-mean-x-runs-10-times"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/guided-filter-box-mean-x-runs-10-times`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **jjw** on 2024-01-06.*

While profiling some opencl code, I noticed the guilded_filter_box_mean_x takes about 10 times more time than box_mean_y. (see data/kernels/guided_filter.cl) Which is strange because the number of computations is almost identical.

I tracked it down to the calling code (cl_box_mean) in src/common/guided_filter.c In the sizes\[\] array sent to dt_opencl_enqueue_kernel_2d, the array elements are (1, height). The current kernel in darktable git has an updated version of this kernel and the equivalent cl_box_mean call.

I experimented and simply **changed the element order to (height, 1)**, and then **switched the x,y coordinate index mapping to global_id(1),global_id(0)** in guided_filter.cl This produced the correct execution time and result. This is what was also changed in the darktable code.

As far as I can tell this impacts hazeremoval and feathering in the blending masks.

## Replies

**Aurélien Pierre** — 2024-01-15

C is a row-major language, it's expected that running 1D filters across rows or columns gives very different runtimes results. OpenCL is another beast since a lot of what's actually going on is vendor-specific. Now, y should be slower than x, but it also depends if your picture is portrait or landscape.

I don't know the specifics here and I have no time to check for now, but switching coordinates doesn't seem like a good idea and I especially don't trust the darktable cartpushers to ensure algebraic consistency of results when they speed up code by looking only at runtimes.

You would have to output a control TIFF image at each intermediate step and compute an RMSE to ensure numerical validity of results. In my experience, switching coordinates on convolution filters can look ok if you manage width and height correctly (as in: no segfault), but in case of a programmer mistake, pixels values errors will appear close to the edges and in ways that are not necessarily immediately obvious, especially if no sharp details are to be found in those regions.

---

**jjw** — 2024-01-15

I figured this out -- the global_id(0) values are arbitrary, and defined by the calling chunk of code.

Think of those global ID's in kernel code as the GPU thread controller saying "I want the subthread to process a job, identified by an id number.

The x,y names you see in the kernel code is just an intuitive way to translate the job id to a coordinate.

So when running the 1d filter "down" the columns, the first entry ( global_id(0) ) is specifying the the column (i.e. x) value for the subthread to process. When running across rows, global_id(0) now holds the row (i.e. y) value for the subthread to process. So global_id(1) really is meaningless in this specific case.

OpenCL will use the total number of "jobs" in global_id(0) and split those over all the GPU's available.

The problem occurs when there is only one "job" that will be delivered in the global_id(0). OpenCL apparently then assigns this to one GPU, waits for completion of the first global_id(1), then increments the global_id(1), gives it to the single GPU, waits, ....

The folks over at darktable did also discover this logic error and corrected it.

---

**Aurélien Pierre** — 2024-01-16

Ok then, if you have identified what's going on, you can either open an issue on Github or submit a PR if you can code it. I don't have time for that in the next weeks, and that will require some peace of mind to carefully follow and not mess up something else.

---

**jjw** — 2024-01-17

I'll submit a PR on github. Not much change to the code. Will try to get that done in the next few days.

