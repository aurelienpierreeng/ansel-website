## Install

### This website

```bash
$ git clone https://github.com/aurelienpierreeng/ansel-website
# Stored for example in /home/user/dev/ansel-website
$ cd ansel-website
$ hugo mod get -u ./...
$ hugo server
```

### Ansel doc

```bash
$ git clone https://github.com/aurelienpierreeng/ansel-doc
# Stored for example in /home/user/dev/ansel-doc
```

## Edit as a whole

Ansel Doc is an important part of the Ansel website, but since it's under a different license and forked from GNU/GPL dtdocs, it can't be on this repo. We want to edit both as a pack but we need to be able to commit them separately on different repositories. Here is the solution.

### Symlink the doc into the website

We can't import the whole `./ansel-doc` repo directly within `./ansel-website/content/doc` because it's a full website in its own right and the default Hugo folders (layouts, static, etc.) will be interpreted as sub-sections when Hugo builds HTML. Also it will mess-up Git history.

Instead, create a folder symlink within `./ansel-website/content/doc` to the local folder `./ansel-doc` :
```bash
$ ln -s /home/user/dev/ansel-doc/content /home/user/dev/ansel-website/content/doc
```
It's important to not add trailing `/` to the folders names.

### Open Obsidian

Open `./ansel-website/content` as an Obsidian vault. Obsidian is able to resolve folder symlinks as if they were local folders, so we basically see the website as a whole, which makes it easier to make internal links between doc and website in the editor.

Working in Obsidian is significantly nicer than working in VS Code to edit "text" text (as opposed to code text in monospace), since the editor is less bloated and monospace fonts are eye-straining after a couple of hours for full paragraphs.

### Tell Git to STFU

In `.gitignore` of `./ansel-website`, add `content/doc` to not commit the symlink or even follow it.

### Start Hugo server in terminal

If we start `hugo server` from `./ansel-website` in a terminal while editing in Obsidian, the doc will still be taken from the Hugo module downloaded from upstream Github, therefore discarding the local changes we could have made. We want to use our local copy.

We need to tell Hugo to temporarily and locally alias `./ansel-doc` in place of `github.com/aurelienpierreeng/ansel-doc`. This is achieved with:

```bash
env HUGO_MODULE_REPLACEMENTS="github.com/aurelienpierreeng/ansel-doc -> ../../ansel-doc/" hugo server
```

Keep that terminal in a corner of your display so any syntactic mistake immediately made in Obsidian raises the appropriate concerns, because Hugo and Obsidian are not fully compatible regarding raw HTML and Markdown syntax.

### Dealing with broken links

There is an extension for that : https://github.com/graydon/obsidian-dangling-links. Once installed, it shows the links that point to no existing file throughout the whole vault, including main website and doc :

![](obsidian-screenshots-broken-links.jpg)

In the node graph view, broken links also appear by their path `../../stuff.md` instead of appearing by their filename.

In each page editor, it is possible to see what pages are linking the page currently opened, including the headings anchor, which is useful before changing headings and therefore destroying internal links :

![](obsidian-screenshots-external-links.jpg)


### Improving content meshing

Horizontal linking, through tags and internal links, is just as important as vertical linking, following hierarchical trees.

Obsidian can show the vault-wise available tags for reuse:

![](obsidian-screenshots-available-tags.jpg)

It can also show the best candidate internal links for each keyword in the page, under the "Unlinked mentions" collapsible:

![](obsidian-screenshots-available-links.jpg)


### Checking content organization

It's often hard to follow the chaining of headings in a Markdown page, when using a typical code editor. Obsidian has an "outline" widget that allows to keep the table of contents in sight when writing, to ensure the hierarchy of headings is consistent :

![](obsidian-screenshots-document-outline.jpg)
