---
title: Dev diary #1
date: 2023-03-19
tags:
  - Development
authors:
    - Aurélien Pierre
---

It's been roughly 3 months that I rebranded "R&Darktable" (that nobody seemed to get right), into "Ansel", then bought the domain name and created the website from scratch with Hugo (I had never programmed in Golang before, but it's mostly template code).

Then I spent a total 70 h on making the nightly packages builds for Windows and Linux work for continuous delivery, something that Darktable never got right ("you can build yourself, it's not difficult"), only to see the bug tracker blow up after release (nothing better than chaining the pre-release sprint with a post-release one to reduce your life expectancy).

People keep asking for a Mac build because they have no notion of the amount of work it requires while the Brew package manager breaks lib dependencies on a weekly basis when you are not lucky. Mac OS simply requires an unreasonable amount of care, which becomes a dry loss when you know that not even 9 % of Darktable users run it. Also, for the last time, Github (actually, the Microsoft Azure instances providing Github actions runners) has no ARM system, so anyway a nightly Mac build would necessarily be on AMD64 architecture, that is old MacBook from before Apple decided once again to go full Apple on its own island. Don't expect 90 % of the free world to scurry over a tech nobody needed and barely anybody uses.

From then, I have optimized the local laplacian in highlights reconstruction with a stupid trick : processing a downsized image instead of the full-resolution one. I had this idea in the back of my mind for a long time but feared the detrimental side-effects. But since clipped areas are signal-less anyway, processing a slightly blurrier version is almost invisible. Also, the shoulder of your typical S/filmic tone curve will anyway compress everything close to white, so it reduces percieved sharpness by reducing contrast in highlights no matter what. We are talking 96 % speed-up on CPU (mostly because we can process the image at once with no tiling).

Using that, I developed an experimental noise and chromatic aberrations pre-filter re-using multi-scale guided laplacians. It's not bad, but again quite slow.

Since February, most of the work has been spent on cleaning up the GUI by moving collections of buttons, either the full-text ones or the weird icon ones, to the global menu and rewiring the keyboard shortcuts to that. It makes feature more discoverable while reducing screen real estate.
