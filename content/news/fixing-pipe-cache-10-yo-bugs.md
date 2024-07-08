---
title: Fixing the pipeline cache and 10 years-old bugs
date: 2024-07-07
tags:
  - Development
authors: ["Aurélien Pierre"]
---

## Recap of the previous episodes

0. Between 2020 and 2022, [Darktable underwent a mass-destruction enterprise](./darktable-dans-le-mur-au-ralenti/index.en.md), by a handful of guys with more freetime and benevolence than actual skills,
1. In 2022, [I started noticing an annoying lag](https://github.com/aurelienpierreeng/ansel/issues/29) between GUI interactions with sliders controls and feedback/update of said sliders. For lack of feedback stating that the value change was recorded, users could change it again, thereby starting additionnal pipeline recomputes and effectively freezing their computer because stupid GUI never said "got you, wait for a bit now".
2. I discovered that pipeline recomputations orders were issued twice per click (once on "button pushed", once on "button released" events), and once again for each mouse motion, but also that the GUI states were updated seemingly after pipe recompute.
3. I [fixed that](./undarktable-ing-gui-controls.md) by almost rewriting the custom GUI controls (Bauhaus lib). I thought that preventing reckless recompute orders was gonna solve the lag : it didn't. Then, I discovered that requesting a new pipeline recompute before the previous ended waited for the previous to end, despite a shutdown mechanism implemented many years ago that should have worked.
4. I [fixed that](./implementing-kill-switch.md) by implementing a kill-switch mechanism on pipelines, following comments in the code from the 2010's and internal utilities that may well have never worked. This did not always work because the kill order came often with a noticeable delay. Once again, the GUI lag was not fixed.

…


## Episode 5 : paying the technical debt

What I discovered should really make it to the manuals of computer science in the chapter about what __not__ to do if you want to write a semi-reliable application.

So, whenever an image-processing parameter was changed in a module, a request was sent to add a new history entry into the database (often more than once per interaction, as shown above). History entries are nothing more than a snapshot of one module's internal parameters (including masks). If a change was detected compared to the previous history entry, a `PIPELINE_STATE` flag was set to the value `DIRTY` to indicate that the pipe would need a recompute and a `gtk_widget_queue_draw()` was sent which, as the name suggests, asks Gtk to redraw the main darkroom preview and the navigation thumbnail, but __in an asynchronous way__ (understand : whenever it finds the time, after everything previously started completes). This will have its importance later.

It took me a __very long time__ to figure out how the pipeline was actually started, because none of the code attached to modules and pipeline contained anything saying "go compute that". In other words, none of the module code contained any explicit recompute instruction.

I had to reverse-engineer the pipeline code from the other end, looking for how the pipeline __could__ be started and greping each option, until I figured out the unspeakable : the first generation of Darktable's devs had wired a callback function to the `redraw` event on the darkroom main preview and navigation thumbnail, but in a completely unrelated place in the code. In that __GUI__ callback, the value of the `PIPELINE_STATE` flag was checked, and either sent the backbuffer pixmap directly to the widget if the flag was `VALID` or asked for a pipe recompute if the flag was `DIRTY`, and that recompute __itself requested a `gtk_widget_queue_draw()`__ upon completion.

This method has one merit : it's lazy coding. Then it has a shitload of drawbacks and issues :

1. it's __not__ dev-friendly, especially in a software project were code greping and comments are all the doc we can dream of. It took many hours to understand the logic through program archaeology. If a command is issued, I want to read `command_issued()` in the right place in the code, because C is already difficult enough to follow without mixing riddles into debug.
2. since `gtk_widget_queue_draw()` (called __twice__ in the worst-case scenario) is only added on the queue and processed asynchronously, it adds any lag that Gtk could suffer (while processing other bits of the GUI or previous frames) before any pipeline recompute is only started, which is unnecessary since the pipeline lives in its own thread in parallel,
2. the great MIDI turducken, listening for pointing, keyboard and MIDI events to dispatch shortcuts, seemed to have overloaded the global GUI with listeners looping over all known shortcuts, which made Gtk lag to the point where it became noticeable,
3. it prevents any kill-switch mechanism from being useful, both because of delays and because of flags readings were interleaved with thread locks (and race conditions). In addition, waiting to acquire the pipeline thread lock (mutex) would freeze the GUI thread during the corresponding time, which was probably one of the causes of the slider lag before updating its position,
4. the chained calls to the `redraw` event callback, through `gtk_widget_queue_draw()`, promoted "endless" stuttering loops of (useless) intermediate redraws which seemed to hit people with slow computers more than those with power beasts. Those were particularly difficult to reproduce, depending on hardware performance, so you can find forums were people are convinced that Darktable is the slowest software ever while others report excellent performance.

So I fixed the whole logic by :

1. making the `redraw` callback stupid (drawing whatever pixmap buffer was available, unconditionnaly),
2. handling explicit pipeline recomputes in the module and history code, with the pipeline recomputes asking for a widget redraw upon pipeline completion, (yes, it's more code, and it is tedious, but now you can optimize recomputes manually — performance matters),
3. removing the special handling of "duplicate" history items (leading to some pollution when dealing with masks, this will need to be fixed later).

You might think that was a problem solved and a job well done, but that's leaving Darktable's geniuses out of the equation.

See, the _crop_ and _perspective_ modules are special modules : opening them enables an "editing mode" that disables any cropping to show the full image. This is needed to drag the cropping frame (or adjust other positionnings) from the main preview, over the full original image. Problem is, there was no explicit way of asking for a pipe recompute… other than adding a new history item. So the modules added a fake history item (later reverted) only to invalidate the pipe and call the `gtk_widget_queue_draw()` function. But then, that polluted the history stack with "empty" steps, so another guy added a special handling case that merged history steps if no parameter changes happened. But then, the history stack (from the _history_ module, as stored in database) does not follow the _undo/redo_ history stack, leading users to misunderstandings regarding what _undo/redo_ really does.

__And this, ladies and gentlemen, is how shitty design is promoting more shittier design in an endless sprawl of madness.__

Remember that all that stems from the need to make the pipe kill-switch work, so you can interrupt a recompute in the middle when you know its output will be discarded anyway. So for that I had to move the recompute request out of Gtk code, and call it everywhere required. But then I had to rewire the pipeline updating logic in _crop_, _perspective and rotation_, _liquify_ and _borders_ modules, and I still have to fix _retouch_ (which is the worse PITA of the lot).

Other than making it clearer to read, and possible to optimize the calls, the current logic also starts the pipe outside of the GUI thread, without waiting for Gtk to _please_ find the time to redraw the frame. As usual, people with crazy CPU will notice little to no benefit, performance-wise, which is probably why this is a non-issue in the Darktable team in the first place.

## Episode 6 : paying the back interests on the technical debt

So, at that point, I had made pipeline recomputes explicit from the modules and GUI controls, and dispatched them sparingly (which is the benefit of dispatching them explicitely). And still, I noticed that playing with modules coming late in the pipe was slow. In fact, launching `ansel -d perf` showed that
all the pipeline, starting at the _demosaicing_ module, was recomputed even though I was interacting with a late module that took its input from _color balance_.

Darktable has had a pixel cache forever. It basically stores the intermediate states of the picture, in-between modules. So, having pipe recomputes starting from much below the current module meant it was mostly useless. It turned out that the cache used only 8 cache lines, which is really under-using today's crazy amounts of RAM. But increasing that to 64 didn't help with cache misses : the cache was still mostly useless, and the most part of the pipe was still recomputed.

We need to pause a bit here. Even a mechanical engineer with no proper programming education like myself knows what an [LRU cache](https://en.wikipedia.org/wiki/Cache_replacement_policies) is :

1. you create a fixed list of slots (cache lines),
2. once you have something to cache, you allocate a memory buffer of previously-known size to one of those slots and assign it an unique identifier. That could be a a checksum, a random hash or even a timestamp, it just has to be cooked always the same way and lead to something unique,
3. when you need data associated with some unique identifier, you query the list of slots and search if that ID is known :
    - if it is, you fetch its associated buffer,
    - if it is not :
      - if you still have empty slots, you create the associated buffer and copy the data for later reuse,
      - if you don't, you clear out the oldest slot and reuse it to host your new data.

In that process, you only need to know the size of the buffers and the IDs. It's very general, you can cache anything, even different objects, your cache doesn't have to be aware of the content, not even how the IDs are generated. It's clean, it's elegant, it's unassuming, it's generic, I would trust it with my life because it's far more robust than whatever security system you find in modern cars.

So when something __that__ simple doesn't work, it's usually because someone tried something "clever" and failed. What the Darktable team typically does in that case, is `switch case` their way through all pathological corner-cases and make it into something even more complicated (by handling all exceptions manually with heuristics), just to ensure no one later has a chance to find the root cause of the error.

For example, there were attempts at reweighting the priority of the cache lines to ensure the module before the one currently edited in GUI was cached. Not only did it not work, but it re-inforced the ties between pipeline code and GUI code, in a way that was not even thread-safe (which is why it didn't work). GUI stuff should happen at the input and at the output of the pipeline computations, not in-between, because _again_, different threads, but also it violates the modularity principle (keep program layers separated and enclosed as much as possible), and this software __needs to stop__ making everything depend on everything.

Again, it took me 8 months, including mandatory breaks from that utter shitshow, to get to bottom of the problem in a way that leads to a __simplifying solution__. And I will present the findings in a linear way, like a story, but keep in mind I started discovering things in a fuzzy and random way because it's all scattered in the sourcecode, so it will look less messy than it truly was.

We start with the unique ID. What truly represents a module's state in an unique fashion ? Well, a "cryptographic" checksum of its internal parameters. Cool, so Darktable had that implemented for a long time. Except it didn't account for the module instance number, and dealt with all kinds of `if` in the process. Not complete, not robust, not even needed. Hash everything, the hash will represent the state of variables.

Yeah, but modules can be reordered, so how do we take care of pipeline order ? Well, you take all the hashes of all modules, in pipeline order, and start accumulating linearly. Great. Except Darktable actually had 2 of those, one for GUI purposes that started from the end of the pipeline (so, in reverse order), one for pipeline purposes, in the pipeline order but unaccessible from GUI (for example… to get an histogram), and again, both mixing that with all sorts of checks to handle special cases (color picker, mask preview, etc.).

Not to mention, the module internal state does not vary whether you are in the full preview or in the navigation thumbnail, in darkroom. And yet, the checksum was fully recomputed twice, once for each pipeline. Actually, make that four times, since there is also the GUI checksum (used mostly for _perspective_ and _retouch_ modules)

And, last but not least, when zoomed-in in darkroom, only the visible portion of the image (the _Region Of Interest_, aka ROI) is computed, meaning we need to keep track of where we are in the picture in our caching mechanism. But that was completely left out of the checksum. Big bug here, and old.

So, how did Darktable _still manage to "work"_, you ask ?

Well, by flushing more or less entirely the cache on any pathological operation : zoom, pan, mask preview, color picker, enabling/disabling _crop_ and _perspective_ modules editing state. That's a way of dealing with consistency without dealing with consistency : torch it. Making it mostly useless, as the very low cache hits stats show (just start `ansel -d dev` to show it).

How did I solve the problem ?

1. When a new module history entry is added, the parameters checksum is computed, taking parameters, masks, blending options, instance number, order in pipeline, etc. into account. Meaning all pipelines share the same checksum/ID here (possible future use would be to save it into database),
2. Before a pipeline is computed, we compute the global checksum of all modules, from start to end, taking into account the mask display state, the checksum of previous modules, and the ROI (size and coordinates). This checksum can be directly accessed later, without additional computation.
3. The cache deals with this global checksum, and only that. No ifs, no buts, no heuristics, no conditions, no workarounds.
4. Modules can request a cache bypass, for example when using color picker. This contaminates later modules in the pipeline before the pipe is computed, so the cacheless state is known early and doesn't affect upstream modules. That should only be a workaround before color pickers can actually use cache lines directly, and could be reused for future modules doing non-standard stuff (painting ?).

Benefits :

1. The module-wise, internal, checksum is computed once for all pipelines,
2. Because the pipeline-wise, global, checksum of each module is known before starting the pipeline recompute :
    - it can also be used for GUI synchronization, so I merged both Darktable checksums into one,
    - it is constant within the scope of the pipeline, allowing to share cache lines between several pipelines (for example, demosaicing and denoising) with limited thread locking issues[^2]
3. Modules doing weird things have an uniform and predictable way of requesting a cache bypass from GUI events, should they need it.

[^2]: The source code actually has a 10-years-old `TODO` comment detailing how to do that.

This logic is not only more efficient (fewer computations), it's also simpler and can be extended for interesting features. From the cache perspective, we deal with nothing else than a checksum, every module state of interest is convolved in it.

But, more importantly, the cache is finally useful, especially when going back-and-forth in editing history, using undo/redo, or enabling/disabling modules. Overall responsiveness of the GUI is much better.

I'm sure there are undiscovered caveats and details that I forgot to re-wire to the new logic, and the _retouch_ module is still mostly broken, but adapting to something that simple should be doable.

## Meanwhile in Darktable 4.8

1. Pipeline checksum is computed during pipeline runtime, so it's unknown outside,
2. Because of that, they didn't deduplicate the GUI vs. pipeline checksums… good luck tracking inconsistencies between both in the future,
3. [Their cache handling code](https://github.com/darktable-org/darktable/blob/master/src/develop/pixelpipe_cache.c) is more than twice as large as [mine](https://github.com/aurelienpierreeng/ansel/blob/master/src/develop/pixelpipe_cache.c) and uses heuristics (over the type of pipeline, kind of module, state of masks display, color picker use, and caching hints defined manually in modules) to work around issues. The cache is not content-agnostic anymore and good luck debugging these spaghetti.[^3]
4. They are still entirely computing the module parameters (internal) checksum twice, once for each pipeline,
4. It took them almost 2 years to get there (since 4.0 release),
5. I would love to see their cache hits/misses stats (do I want to revive my PTSD by opening that soft ever again ? I'll pass, thanks).
6. People who think having more monkeys waving their hands in the air guarantees better quality should stop thinking.


## Conclusion

The amount of time spent and recently-broken shit to fix to get there was properly unbearable, but it was made worse by code scattered in a non-modular fashion without a clear distinction between what belongs to the (G)UI, what belongs to the backend, what belongs to  module histories and what belongs to pipeline nodes. The cache thing only took 8 months, mostly archaelogy and reverse-engineering, on top of what was already done in GUI controls and explicit pipeline recomputes.

There are still issues to fix :

- the number of available cache lines is an user preference and doesn't check for available memory left on device,
- the histogram/scopes module is mostly broken by design, because it was handled through special heuristics (now removed) on a module that is invisible in GUI (`gamma.c`). The new logic makes it possible to force-cache it and to fetch the cache line from the GUI thread.
- internal module's histogram are not immediately drawn when going in darkroom,
- color-pickers handling could be simplified and made more elegant,
- history handling still have some corner cases.

However, since I'm refusing to "fix" anything if my fix doesn't make things more simple, that strategy is starting to pay because the code is a lot more linear, with fewer cases to test, and ultimately sligthly faster. As I make progress, it's slowly becoming more readable and more fixable. Then, of course, shaking the core of the software to that extent is bound to break things (which shouldn't break if the code was modular).

There comes the legitimate question asking : why bother fixing Ansel/Darktable ugly legacy and not move on to something better, faster and shinier (like Vkdt) ? Well, Vkdt (or anything else new) will stay a rough prototype, competing with other rough prototypes (that's _Open Source_ in a nutshell), years away from a generally-usable product. Adding another unfinished/half-assed prototype to the landscape will do no good. It would be nice to have something __not__ scruffy and fairly finished, for a change. Besides, the (very) old code of Darktable is clean and sturdy (well, for the most part), it's only the past few years that have taken a turn for the shittiest. `git blame` always shows the same 3 names on the really shitty lines, to a point where I sometimes find myself automatically deleting the corresponding lines when I saw who wrote them, out of habit.

There is also the fear that, no matter how fast Vulkan makes Vkdt, what really makes Darktable shitty is bad decisions, bad priorities, programming mistakes, lessons not learned, and if those mistakes are reproduced over Vkdt, it might take longer to realize the consequences with more horsepower, but ultimately things will go the same way. Having more resources makes it more affordable to be stupid… until it doesn't and you realize how trapped you are.

[^3]: It should be noted that "my" cache code is actualy pretty much how Roman Lebedev and Johannes Hanika wrote it 10 years ago. I simplified a couple of things, mostly removing stuff added since then, and added nothing of my own, because it's a Garbage In/Garbage Out situation where you should rather clean your input rather than trying to handle any corner case internally through unlegible heuristics.
