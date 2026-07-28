---
title: " Gtk-WARNING **: Theme parsing error: gtk.css"
date: 2023-06-07
slug: "-gtk-warning-theme-parsing-error-gtk-css"
tags:
  - Community archive
forum_author: "Aurélien Pierre"
forum_category: "Bugs and strange behaviours"
forum_url: "https://community.ansel.photos/view-discussion/-gtk-warning-theme-parsing-error-gtk-css"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/-gtk-warning-theme-parsing-error-gtk-css`.
No crawler ever captured this particular thread, so the text below — taken straight from the forum database — is the only copy left.

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Aurélien Pierre** on 2023-06-07.*

If you launch either Darktable or Ansel from the terminal, you will get a bunch of lines like :

``` ql-syntax
(ansel:67698): Gtk-WARNING **: 23:41:46.739: Theme parsing error: gtk.css:199:34: The :inconsistent pseudo-class is deprecated. Use :indeterminate instead.
(ansel:67698): Gtk-WARNING **: 23:41:46.742: Theme parsing error: gtk.css:1649:16: '-gtk-icon
-size' is not a valid property name
```

The 2 important parts here are :

- **WARNING**: computer programs have 3 levels of messages (info, warning, error). Only errors are blocking, warnings are nothing more than that (usually meaning that developers did something ugly but still sort-of working), and can be disregarded by end-users,
- **gtk.css**: this file is the main stylesheet provided by the desktop theme installed on the desktop environment, which is outside of the scope of Ansel and Darktable.

This warning means that the Adwaita dark theme uses invalid or outdated styling statements that Gtk fails to decode (despite being the default Gnome theme). Ansel and Darktable use this desktop theme to initialize the GUI styling of the application (then apply their customizations on top), which is why the warning appears here, but there is ultimately nothing that can be done in the scope of either project to fix it, and that's something you need to report to the author of the theme.

---

Si vous lancez soit Darktable soit Ansel depuis le terminal, vous obtiendrez une paire de lignes du genre : 

``` ql-syntax
(ansel:67698): Gtk-WARNING **: 23:41:46.739: Theme parsing error: gtk.css:199:34: The :inconsistent pseudo-class is deprecated. Use :indeterminate instead.
(ansel:67698): Gtk-WARNING **: 23:41:46.742: Theme parsing error: gtk.css:1649:16: '-gtk-icon
-size' is not a valid property name
```

Les deux parties importantes ici sont : 

- **WARNING (avertissement)** : les programmes informatiques ont 3 niveaux de messages (info, avertissement, erreur). Seules les erreurs sont bloquantes, les avertissements ne sont rien d'autre que cela (indiquant généralement que les développeurs ont fait quelque chose de sale mais tout de même globalement fonctionnel), et peuvent être ignorés par les utilisateurs finaux,
- **gtk.css** : ce fichier est la feuille de style principale fournie par le thème installé sur l'environnement de bureau, qui est hors du champ d'Ansel et Darktable.

Cet avertissement signifie que le thème de bureau Adwaita sombre utilise des clauses de style invalides ou obsolètes que Gtk échoue à décoder (bien qu'étant le thème par défaut de Gnome). Ansel et Darktable utilisent ce thème du bureau pour initialiser le style de l'interface graphique de l'application (puis appliquent leurs personnalisations par dessus), ce qui explique pourquoi cet avertissement apparaît ici, mais en bout de ligne, il n'y a rien qui puisse être fait au niveau de ces deux projets pour régler le problème, et c'est quelque chose que vous devriez rapporter à l'auteur du thème.

## Replies

**ariznaf** — 2023-06-12

May be that theme is a bit old or deprecated and it is time to change the default theme for another one?

---

**Aurélien Pierre** — 2023-06-13

Adwaita is the base and default theme maintained by the Gnome team, which happens to overlap a lot with the Gtk team, so I would assume it to be closely updated.

