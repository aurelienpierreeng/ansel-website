---
title: Welcome Ansel GPT !
date: 2025-05-03
tags:
    - Announcement
authors:
    - Aurélien Pierre
---

After I finally [wired the whole website and docs](../contribute/translating.md) to a water-tight translation workflow (using po4a on top of Hugo), which happens to use the exact same toolset and logic as the Ansel application, I got the idea of [automating empty translations](../contribute/translating.md#auto-tools-and-helper-scripts), first from the software translation files, then through ChatGPT API, which does a very fair job at translating Markdown syntax.

Working alone, you can't rely on [social loafing](https://en.wikipedia.org/wiki/Social_loafing), so you have to be clever. You can see [the list of things I have already automated](../contribute/workflows.md) in background for Ansel.

Having written a whole [AI search engine myself](dev-diary-2.md), which means mostly a web crawler (because that was the most tedious part to write and debug), I got the opportunity to see this website from the eyes of a bot. Piece by piece, I modified the HTML templates and metadata to make it easier to crawl, index and search, first for the internal search engine,[^1] then for [Chantal AI](https://chantal.aurelienpierre.com).

[^1]: Which actually works client-side in Javascript in your own browser, meaning it works offline too, should you install this website as a webapp to keep the documentation locally.

Even with Chantal, I still get too many recurring questions regarding information that is already written somewhere. Sure, the documentation is a bit lagging behind the code, but the [commit messages](https://github.com/aurelienpierreeng/ansel/commits/master/) I write aim at being non-technical enough for power-users to understand what's going on these days in the software.

I get that there is nothing worse than being trapped in your problem without a timely answer, but then I can't possibly serve as help-desk for every guy on every timezone with everything that needs cleanup in this stupid software. Which means there is still a gap to fill.

The main drawback of Chantal is the language model is quite heavy to retrain, and I can't possibly automate it on some server. Then, websites can't be crawled too fast without being blocked by servers, so that doesn't take too much power but that requires some computer to be plugged-in for a week with a stable internet connection. Which means I update the language model and the web index only 4 times a year. As of now, the web index contains 63.452 pages, the language model knows 47.579 words, and I have finally managed to make it fairly compliant with the memory I/O limitations of a shared hosting.

The plan, right now, is to automate website crawling on some server, because that's not too heavy, then retrain the model overnight on my own computer (which takes around 4 h of computation and almost all of my 32 GB of RAM…).

Anyway, during my fiddling with ChatGPT API, I discovered that you can train your own custom GPT.[^2] This is as simple as feeding it text content it can use, and now ChatGPT can also load websites, sitemaps and can be configured to send requests to Rest API. So, without further ado [__meet Ansel GPT__](https://chatgpt.com/g/g-680d2f861a608191a0f7549eadd40f2e-ansel-gpt).

[^2]: Provided you are a ChatGPT Plus subscriber, for a not-so-modest 23€/month.

Ansel GPT is configured to cache and update once a week Github issues, commits, community forum posts, and all of the present website. It is able to provide complex (and fairly accurate) answers regarding what module to use, how and when, in Ansel, as well as on color theory concepts. I also configured it to use Chantal AI backend, which is (almost) a Rest API and the GPT will follow the links indexed by Chantal to improve its answers.

The caveat is using Ansel GPT is reserved to ChatGPT Plus subscribers, so I feel like I worked 2 days to configure everything so OpenAI can bank on my work. But anyway, if that's at least less work for me on the semi-long run, let's call it a win.
