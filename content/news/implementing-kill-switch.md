---
title: 'Implementing kill-switch on pipeline'
date: 2023-11-28
tags:
  - Development
authors:
    - Aurélien Pierre
---

I have thought, for a very long time, that there was some kill-switch mechanism on the pixel pipeline. The use case is the following :

1. you are changing a module parameter,
2. the previews (the central darkroom one and the thumbnail in left panel, also used for histogram and color pickers) recompute their pipeline to account for that change,
3. one of the previews finishes rendering before the other, and the result is obviously __not__ what you wanted,
4. you change again the module parameter, without waiting for the recomputation to finish.

In that case, you want to kill all active pipelines because their output will not be used, and start recomputing everything immediately with new parameters. Except Darktable doesn't do that, it lets the pipeline finish before restarting it, and looking at the comments in the source code, it seems to be a fairly recent regression and not the originally intended behaviour.

I have (re)implemented this feature in Ansel, but it's tricky because we are dealing with different threads (GUI, editing history and pipeline on CPU/OpenCL) and we need to synchronize them properly.

If this goes bad, you may experience garbled previews from inconsistent cache states. This is a GUI issue only, and the mitigation strategy is to go to the global menu -> Run -> Invalidate all caches.

To debug, you may start Ansel with :

```
$ ansel -d perf
```

When interacting with sliders and comboboxes in GUI (for example here in exposure module), you will get :

```
100,407003 [dev_process_all] sending killswitch signal on running pipelines took 0,000 secs (0,000 CPU)
100,509816 [dev_pixelpipe] took 0,011 secs (0,023 CPU) processed `exposure` on GPU, blended on GPU [full]
100,510498 [dev_pixelpipe] took 0,019 secs (0,035 CPU) processed `exposure` on GPU, blended on GPU [preview]
100,533228 [dev_pixelpipe] took 0,023 secs (0,061 CPU) processed `lens correction` on GPU, blended on GPU [full]
100,558939 [dev_pixelpipe] took 0,026 secs (0,129 CPU) processed `tone equalizer` on CPU, blended on CPU [full]
100,563703 [dev_pixelpipe] took 0,005 secs (0,008 CPU) processed `unbreak input profile` on GPU, blended on GPU [full]
...
```

Normal behaviour is the `[dev_process_all] sending killswitch signal` line should appear at the time of your interaction, and should be followed by a recomputation starting at the module you interacted with (not the one before, not the one after), up to the end (display encoding module).
