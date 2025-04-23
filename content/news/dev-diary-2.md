---
title: 'Dev diary #2 : introducing Chantal'
date: 2023-04-28
tags:
  - Development
authors:
    - Aurélien Pierre
---

2022 was so bad in terms of junk emails and noise that I started the [Virtual Secretary](https://virtualsecretary.aurelienpierre.com/), a Python framework to write intelligent email filters by crossing information between several sources to guess what incoming emails are and whether they are important/urgent or not. When I'm talking about junk emails, it's also Github notifications, pings on pixls.us (thank God I closed my account on that stupid forum), YouTube, and direct emails from people hoping to get some help in private.

Having become "the face" of darktable, mostly because I'm one of the few to bother providing user education and training instead of just pissing code, I didn't see that coming, and I wasn't prepared. A lot of people now mistake me with the front desk, which doesn't help abstract thinking on coding matters, let alone taking time to actually produce art. The problem is all the time lost dealing with info/noise/input is not spent solving problems, and time is the only thing for which you cannot get a refund.

After a while, I figured it would be nice to extend the Virtual Secretary with a machine-learning classifier, which would guess in what folder incoming emails should go, by extracting the content of the emails already in said folder. It's actually much easier to implement than what I thought, but the time-consuming bit is to write text filters to clean-up the input (because garbage in, garbage out, especially for spam emails which are generally improperly formatted).

But the ultimate goal, in my wildest dreams, was to build an autoresponder for people asking questions already answered on one of the many websites I have contributed to over the years. It's a constant frustration to see that all the pages of doc I have written over the years are lost in Internet limbo. On FLOSS-centric forums, benevolent guys also tend to experience the same kind of fatigue : repeating again and again the same info, linking the same pages, to never-ending hords of newbies who don't know what to look for. Just look at Reddit darktable : every 14 days, someone else asks why the lighttable thumbnails don't look like the darkroom preview. Even discarding the amount of frustration and angryness here, the number of man-hours lost in repeating is outstanding. Just because information is lost.

The true problem of search engines is you need to know what keywords to look for. Which is circling back to the fact that newbies don't know the slang. So they don't know what to look for. They don't have any entry point in the matrix. Except other humans. Which sucks for the ones having to do the work, usually for free.

After merging a neural layer of word2vec word embedding (big words to say it's unsupervised machine learning finding how words are contextually related in sentences, that is finding syntactical structures, synonyms and the likes), as a first step in my email classifier (which is now up to 92 % accuracy), I wondered if this wouldn't been usable to build a context-aware and synonym-aware search engine, able to look past exact keywords.

Turns out a couple of guys from Bing had the same idea in 2016, and published their maths, so I implemented them. Then proceeded to add a web interface on top. That gave birth to [Chantal](https://chantal.aurelienpierre.com), the AI you are kindly asked to bother before bothering me. The current version is trained against 101.000 internet pages from my own websites, darktable & Ansel docs, along with some reliable color-science ressources. It indexes 15.500 pages in French and English and can process search queries in either or both of these languages. One of its mean features is to propose you a list of keywords associated to your query, so you can refine/reorient/try things you wouldn't have thought of before.

Hope that helps.

That work showed me how poorly indexable many websites are. To account for the lack of XML sitemap on forums.darktable.fr and color.org, I had to write a recursive crawler. But even then, many pages don't have description meta tags and a proper date tag. It means you need to use regular expressions and indirect methods trying to identify the metadata, and manually tune the HTML parser to extract the actual content part of the webpage (discarding sidebars, menus, asides and advertising if any).

Then, you get to love Q&A forums like Stack Overflow, where proper questions start a thread, proper answers follow, and the best answers are selected by the community. "Thank you" and "me too" messages are explicitly forbidden in the conditions of use. On forums like pixls.us or forums.darktable.fr, proper technical information gets lost in the middle of semi-technical rambling, life stories and bros bonding over tales of software, in a continuous thread where nothing distinguishes relevant from irrelevant, accurate from inaccurate, and gross misunderstandings of color theory. From a machine crawling perspective, there is very little to exploit here, and investing time on such platform is a dry loss.

More (technical) info:

- [Websites suck](https://eng.aurelienpierre.com/2023/04/websites-suck./) : on the technical challenges of crawling and indexing HTML (and… PDF) webpages, in a time where people say big things like "Web 4.0" or "Internet of Things", but basic things like providing page sitemaps or putting the date of internet publications in standard formats is still too much to ask of webmasters and CMS,
- [Designing an AI search engine from scratch in the 2020's](https://eng.aurelienpierre.com/2024/03/designing-an-ai-search-engine-from-scratch-in-the-2020s/) : on how Chantal was built and how the Dumbrish synthetic language was created to generalize natural French and English, plus some regex bonanza,
- [Thoughts on Word2Vec AI for information retrieval applications](https://eng.aurelienpierre.com/2025/05/thoughts-on-word2vec/) : on how the input cleanup is by far the worst time-consuming step of designing an AI and language models that become too semantically accurate don't make better search engines.
