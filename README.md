## Install

You will need Hugo v0.124.x minimum to build. You may have to install it manually because it probably isn't what you have in your distribution repository.

### This website

```bash
$ git clone https://github.com/aurelienpierreeng/ansel-website
# Stored for example in /home/user/dev/ansel-website
$ cd ansel-website
$ sh build-modules.sh
```

### Ansel doc

Ansel Doc is an important part of the Ansel website, but since it's under a different license and forked from GNU/GPL dtdocs, it can't be on this repo. We want to edit both as a pack but we need to be able to commit them separately on different repositories. Here is the solution.

Ansel doc is fetched automatically as a module of this website on your disk as part of the `build-modules.sh` script above, which also auto-generates the translated pages through `.po` files. You will find it in the local folder of the website, under `_vendor/github.com/aurelienpierreeng/ansel-doc/`. No file should be manually edited there, this is only for auto-generated content.

To edit Ansel docs, do

```bash
$ git clone https://github.com/aurelienpierreeng/ansel-doc
# Stored for example in /home/user/dev/ansel-doc
$ cd ansel-doc
```

And then, edit the (English) content of `ansel-doc/content`.

## Interactive editing/Live preview

### Start the development server

Hugo lets you open a rendered version of the website, on a local development server, to preview your changes into your web browser.

If you only want to edit this website, run from `./ansel-website` directory:

```bash
hugo server --disableFastRender
```

If you want to edit the docs and see the results in realtime as part of this website, after you cloned the docs (see previous step), run from `./ansel-website` directory:

```bash
env HUGO_MODULE_REPLACEMENTS="github.com/aurelienpierreeng/ansel-doc -> ../../ansel-doc/" hugo server --disableFastRender
```

This trick will dynamically load the docs module from your local folder rather than from Github, which means the local changes done to the docs will immediately appear into the main website through your development server.

### Updating translations

Both the docs module and the current website have scripts to auto-update translations, stored in their respective `tools/` folder, which means the procedure and the commands to call are the same for docs and website, you just need to call them from the right directory.

To resynchronize English Markdown files with the `.pot` and `.po` files, run:

```sh
tools/update-translations.sh
```

To build translated Markdown files from `.po` files, run:

```sh
tools/build-translations.sh --add
```

To cleanup translated Markdown files, run:

```sh
tools/build-translations.sh --remove
```

Translated files should never be commited with Git, so the last command is useful to clean your working directory before committing.

Translations should be made by opening the files `po/content.LANG.po`, for example with [Poedit](https://poedit.net/). Once you are done, save the `.po` and open a pull request here with the new file. 

### Open Obsidian

Open `./ansel-website/content` as an Obsidian vault. Obsidian is able to resolve folder symlinks as if they were local folders, so we basically see the website as a whole, which makes it easier to make internal links between doc and website in the editor.

Working in Obsidian is significantly nicer than working in VS Code to edit "text" text (as opposed to code text in monospace), since the editor is less bloated and monospace fonts are eye-straining after a couple of hours for full paragraphs.


### Start Hugo server in terminal

If we start `hugo server` from `./ansel-website` in a terminal while editing in Obsidian, the doc will still be taken from the Hugo module downloaded from upstream Github, therefore discarding the local changes we could have made. We want to use our local copy.

We need to tell Hugo to temporarily and locally alias `./ansel-doc` in place of `github.com/aurelienpierreeng/ansel-doc`. This is achieved with:

```bash
env HUGO_MODULE_REPLACEMENTS="github.com/aurelienpierreeng/ansel-doc -> ../../ansel-doc/" hugo server --disableFastRender
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
