---
title: 'Un-darktable-ing GUI controls'
date: 2023-11-25
tags:
  - Development
authors:
    - Aurélien Pierre
---

Darktable has its own GUI widgets library, for sliders and comboboxes (aka drop-down menus or selection boxes), called Bauhaus (in the source code, it's in `src/bauhaus/bauhaus.c`). While they use Gtk as a backend, Bauhaus are custom objects. And like many things in Darktable, custom equals rotten.

In 2022, ‍I noticed [parasite redrawings and lags](https://github.com/aurelienpierreeng/ansel/issues/29), when using them, leading to a frustrating user experience : the widget redrawing seemed to wait for pipeline recomputations to complete, which meant that users were not really sure their value change was recorded, which could lead them to try again, starting another cycle of expensive recomputation, and effectively freezing their computer for several very frustrating minutes of useless intermediate pipeline recomputations.

As it happens, static code analysis tools find that the Bauhaus library is also the [4th most complex sourcecode file](https://sonarcloud.io/component_measures?metric=complexity&selected=aurelienpierre_darktable%3Asrc%2Fbauhaus%2Fbauhaus.c&view=list&id=aurelienpierre_darktable) in the whole Darktable software in terms of cyclomatic complexity, with a score of 735 and a technical debt estimated to 1 day and 7 hours. If you are no programmer, cyclomatic complexity measures the number of different paths the code can take, and high values make it not only more difficult to understand (hence to debug), but also more prone to edge-cases, bugs and contextually-dependent weird issues. [Cyclomatic complexity](https://en.wikipedia.org/wiki/Cyclomatic_complexity) is an indirect metric of the probablity that this code will blow up in your face when you least expect it, something to take into account when the most prolific "developers" in your team are a primary school teacher, a pediatrician and a banking consultant.

What's particularly frustrating is I already worked to simplify this file, back in 2019. 3 years later, it was as if I did nothing, thanks to [feature creep](https://en.wikipedia.org/wiki/Feature_creep) and MIDI/gamepad support. When the parasite redrawings showed up, I was left with unintelligible [spaghetti code](https://en.wikipedia.org/wiki/Spaghetti_code) that I was properly unable to fix. A first attempt to correct wrong stuff lead to a dead-end, back in August 2022, and got me discouraged. Trying to work around it was not going to cut it.

So I had to rewrite it almost completely, which was no fun and took me a crazy amount of hours (I stopped counting at 3 weeks, full-time, and that was for the second attempt in August-November 2023).

Did you know that, once a combobox had the focus (either because you clicked on it or gave it focus via a keyboard shortcut), you could start typing the first letters of the label you wanted to select and it would automatically select the closest item in the list ? Neither did I before undertaking this task, because it's documented nowhere. As were many hidden features in there, added to comply with deviant and marginal use cases, but complexifying the code structure for everybody. (Spoiler alert : I kept this particular feature, but removed others).

## ‍List of improvements

- Cursor coordinates (in popups) are computed only at once place, then stored. That saves a lot of intermediate recomputations, some of them being inconsistent because the code was copy-pasted and duplicated instead of using [getters and setters](https://en.wikipedia.org/wiki/Mutator_method). Now, coordinates offsets and changes are handled through unified getters and setters, meaning any future change will need to happen only in one place, and the whole code uses that.
- New values (from sliders and comboboxes) are not dispatched anymore to the pixel pipeline during scrolling or drag-and-dropping, but only at the end. This relies on a machine-learned timeout recording the average time needed to compute a full pipeline. The GUI will wait for 20 ms to 2.5 s to dispatch changes to pipeline, avoiding to recompute at every scrolling or dragging step, which makes for useless and redundant, yet expensive, computations that only make the software lag. Similarly, they are now dispatched only on the button-released event, instead of button-pressed and button-released events (given that a typical mouse click sends both events). It should spare quite a lot of needless pipeline recomputes.
- Widgets are redrawn immediately on user events, before the new values are dispatched to the pixel pipeline. This ensures immediate user feedback, even though the actual pixel result may come later, and limit frustration on slow computers.
- Do not dispatch value-changed events if the widgets got user interaction but their value didn't actually change.
- Capture clicks on the comboboxes chevron (right arrow). Previously, you needed to click on the label to unroll the combobox drop-down menu, which was super frustrating if you came from software with a proper GUI. The chevron itself didn't respond to clicks.
- Do not scroll comboboxes drop-downs. That feature started like a cool project : having the currently-selected item aligned with the label. Problem is the drop-down popup positionning is ultimately handled by the desktop environment, we can only ask it politely to do what we wish, but there is no guarantee our wishes will be honoured. Also, it is possible to make the popup roll outside the viewport, nothing prevents it. All in all, it's brittle and random, better stick with default window positionning.

## Deprecated features

The ability to assign keyboard shorcuts to sliders and comboboxes is for now removed. Sliders and comboboxes are anyway linked to arrow keys and mouse scroll __once they get the focus__[^1], and it is still possible to assign focus capturing to a keyboard shortcut. The current logic is therefore to request focus through keyboard shortcuts, then edit the value using arrow keys. Focus requests also automatically make the widget visible in GUI, scrolling the sidebar if needed.

[^1]: In GUI programming, a widget has the focus when it is the one recording keyboard events. Text entries are the most obvious example, but Darktable hacked that concept to generalize to pretty much every widget.

Anyway, the current shortcuts system will have to be entirely replaced by native Gtk accelerators, which are already used for the global menu (and were used in Darktable prior to 2021). Currently, we have both systems, one of which being a monstruosity of complexity and probably responsible for slow-downs. KISS.

## Caveats

The "format" combobox in export module doesn't initialize its value properly. This is a non-standard Bauhaus widget that needs extra care. For the time being, you will need to refresh the storage option or to reload a preset.

Whenever you remove the flaky old paint that held the rusty walls, you risk doing collateral damages. Be careful with Ansel when using AppImage and Win EXE tagged Ansel-57ed58d from tonight and report anything weird.

## Downloads

- [Ansel-57ed58d-x86_64.AppImage](https://github.com/aurelienpierreeng/ansel/releases/download/v0.0.0/Ansel-57ed58d-x86_64.AppImage)
- [Ansel-57ed58d-win64.exe](https://github.com/aurelienpierreeng/ansel/releases/download/v0.0.0/ansel-57ed58d-win64.exe)

## Geeky details

The current changes have reduced :

- cyclomatic complexity from 735 to 494
- cognitive complexity from 796 to 432
- technical debt from 1 day and 7 hours to 4 hours and 50 min.

[More details](https://sonarcloud.io/component_measures?metric=cognitive_complexity&selected=aurelienpierreeng_ansel%3Asrc%2Fbauhaus%2Fbauhaus.c&view=list&id=aurelienpierreeng_ansel)

If you are no programmer, these metric just mean that the code will be easier and less time-consuming to maintain in the future, and probably less bug-prone.
