---
title: Documenting Ansel
date: 2025-10-13
weight: 9
---

## Introduction 

There are different ways to access information :

1. __(chono)logical__, like reading page by page, line by line, until you reach the end of the publication,
2. __thematic__, like getting to the table of contents and jumping straight to the part you are interested at, __provided the content is divided into meaningful units of content__,
3. __transversal__, like following a "related posts" section based on content similarity (defined manually, with tags & keywords, or learned by AI topic analysis), or explicit cross-references. For example, most websites have archives listing all pages that have a certain tag/keyword, books have glossaries.
4. __hint-based__, like presenting a bibliography of more in-depth publications or a "more info" section at the end of the content, or anticipating on later content,
5. __source-based__, following references (typically footnotes or marginnotes) to publications from where the info is extracted, mostly for verification purposes,
6. __information retrieval__, aka search engine.

You have to support all of them at once because they are complimentary and the best in context depends on the initial knowledge and needs of the reader. Not one of those ways is superior to the others. This means there is a fair deal of "keywords stuffing" to do into your writing, as to ensure that keyword-based content analysis and information retrieval by keywords will work as expected.

A manual/documentation is not a course, but sticking to a dry list of features/GUI controls and their definition is… too dry. You need to create links between content (which is not merely HTML links). In Ansel, [workflows](../workflows/) start with a goal, and unroll the tooling to achieve it. [Documentation](../doc/) starts with the tooling and presents how and where it can be used. But those are the two ends of the spectrum, and the reality is always a bit in-between.

Knowledge is a [network graph](https://en.wikipedia.org/wiki/Knowledge_graph) anyway. You just have to mind the links between the nodes. They are at least as important as the content.

## Practical implementation in Ansel

Ansel uses [Hugo](https://gohugo.dev) as its CMS, both for the documentation and the rest of the [website](./website/index.md). The practical implementation of the principles enunciated above will have to deal with Hugo's core features.

### (Chrono)logical and thematic access

Hugo content is organized into [sections](https://gohugo.io/content-management/sections/) that are essentially sub-folders of the main `/content` folder. Sub-folders can be infinitely nested. The theme of the website presents the treeview of all sections in the left sidebar, on wide screens (desktop). Sections and sub-section top levels can be (un)collapsed upon user request. This treeview provides the top-level table of contents which acts as __thematic access__.

Within sections, the relative order of pages can be manually defined using the [`weight` parameter](https://gohugo.io/methods/page/weight/#article) in Markdown headers, like so :

```yaml
---
title: Documenting Ansel
date: 2025-10-13
weight: 9
---

My content here
```

The `weight` parameter is optional. If not used, the pages listings will typically use the `date` to order content, but could also use alphabetical ordering on page title. This ordering provides the __(chrono)logical access__.

Whithin pages, if there are more than two sections in the content (defined by second-level titles, e.g. `<h2>` in HTML or `##` in Markdown), internal table of content will be automatically added by Hugo into the right sidebar, on wide screens (desktop).

### Transversal access

Tags can be defined on the website using the `tags` parameter in the Markdown header, like so :

```yaml
---
title: This page title
date: 2022-12-04
tags:
    - color science
    - pipeline
---

Your content
```

Tags are optional and are displayed as clickable links in several places in the website theme. Clicking on one tag opens its archive, listing all pages having this tag. This provides __transversal__ access.

Writers are also encouraged to add cross-links in their content, from website pages to other website pages, to promote transversal access. Concepts that have an entry on the website should be turned into links to the page describing each concept.

### Hint-based

Writers are free to add a _Bibliography_ or _More information_ section at the end of their pages, with a list of publications and links. Those publications can be internal or external to Ansel project. They can be peripheral to the topic treated in the content.

It is also possible to finish pages with an opening on the next logical step, when writing on workflows or modules.

### Source-based

Hugo supports extended Markdown, which [supports footnotes](https://www.markdownguide.org/extended-syntax/#footnotes). These are recommended to reference sources, like so :

```markdown
The typical observer has Just Noticeable Difference (Delta E) of 2.3[^1]

[^1]: Some Author, Some Publisher, _A real-world, large-sampled, study of vision parameters for white, rich, educated, American students of the Rochester Institute of Technology_, (some year). [URL](https://doi.org/xxxxx)
```

Ansel has not settled for any particular academic formatting of source citations at this point, although the [IEEE citation style](https://ieee-dataport.org/sites/default/files/analysis/27/IEEE%20Citation%20Guidelines.pdf) seems the best-suited to the footnote approach with numerical index.

Ensure to include the [DOI](https://www.doi.org/) of the publication, or at least some long-term URL at which it can be retrieved now and in the future.

### Information retrieval

For now, [Chantal](https://chantal.aurelienpierre.com) handles that part. The web index is manually and periodically updated.

## Guidelines

Writing, even technical, is an art that is difficult to reduce to a set of definite guidelines or best practices, because this varies upon the context. You should be careful of not getting more catholic than the Pope. A good rule of thumb is to write to solve problems, which means start by asking yourself why and from where the reader landed on the page you are writing :

1. what kind of knowledge the reader is supposed/assumed to already have ?
    - the reader should ideally be aware of those prerequisites, so maybe start with a list of links,
    - anything not in this list should be defined and explained on your page,
2. what kind of task the reader is attempting to complete that led them to this page ?
    - do they want a quick cheatsheet, or a detailed how-to, or a theoritical background ? You may have to choose one arbitrary.
    - this will decide what hints you may add in-text to improve the knowledge network,
    - this should probably bias the whole vantage point of your content and its length/depth.


A good way of assessing documentation quality is by looking at the frequently asked questions (or least understood topics) on forums. If the topic is already covered but questions keep arising, it can be because the documentation is not clear or the relevant pages is buried into the network and not discoverable enough.