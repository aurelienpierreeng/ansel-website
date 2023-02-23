---
title: "Darktable : foncer dans le mur au ralenti"
date: 2023-02-15T18:14:01+01:00
draft: false
authors: ["Aurélien Pierre"]
---

Qu'est-ce qui se passe quand une bande de photographes amateurs, devenus développeurs amateurs, rejoints par une poignée de développeurs _back-end_ qui développent de la librairie pour développeurs, se décide à travailler sans méthode ni structure sur un logiciel métier pour utilisateur final dont le cœur de compétence (colorimétrie et psychophysique) se situe quelque part entre un BTS photo et un BAC+5 en sciences appliquées, tout en se promettant de sortir 2 versions par an ? Tout ça bien sûr dans un projet logiciel dont les fondateurs et la première génération de développeurs sont passés à autre chose ?

Devinez !

## Dégradation des fonctions basiques

Les années 2020 sont 40 ans trop tard pour ré-inventer les paradigmes d'interaction entre l'utilisateur et son ordinateur, que ce soit la façon dont on utilise son clavier et sa souris pour piloter une interface ou le comportement d'un navigateur de fichiers. Depuis les années 1980, toute l'informatique grand public a convergé vers une sémantique plus ou moins unifiée, où la touche `échap` ferme l'application courante, un double-clic ouvre un fichier, et où la roulette de la souris fait défiler la vue courante. Darktable[^1] prend un malin plaisir à ignorer tout ça, et les récents changements empirent les choses : il est désormais nécessaire de lire la documentation pour effectuer des tâches aussi simples que trier des fichiers ou définir des raccourcis clavier.

[^1]: En passant, je ne supporte plus la tentative de se différencier pour le principe en écrivant "Darktable", nom propre, sans majuscule. C'est puéril, ce n'est ni amusant ni disruptif, et ça met le bordel dans les menus [freedesktop.org](https://github.com/darktable-org/darktable/blob/master/data/org.darktable.darktable.desktop.in) où la majuscule est de toute façon ajoutée.

### Groupes de modules

Tout commence avec la refonte des [groupes de modules](https://docs.darktable.org/usermanual/4.0/en/darkroom/organization/manage-module-layouts/), en 2020, qui cache la décision de [ne pas décider](https://github.com/darktable-org/darktable/pull/5322) d'une organisation unifiée des modules.

![](/posts/module-groups.jpg)

[Depuis 2018](https://www.mail-archive.com/darktable-dev@lists.darktable.org/msg03402.html), je me bats pour nettoyer l'interface graphique de Darktable et en particulier l'organisation des modules. L'interface graphique devrait encourager les bonnes pratiques en disposant les outils dans l'ordre typique dans lequel ils devraient être utilisés. Les mauvaises pratiques sont celles qui augmentent les risques d'incohérences colorimétriques ou de retouche circulaire, où l'on doit revenir en arrière pour répercuter les changements effectués plus tard, même si elles peuvent fonctionner dans des cas simples.

Cet ordre d'utilisation est principalement dicté par des considérations techniques telles que l'ordre d'application des modules dans la séquence du pipeline et l'utilisation de masques paramétriques et dessinés, dont l'effet dépend des modules appliqués en amont. Ignorer ces considérations techniques revient à chercher des problèmes, même si c'est la grande mode dans les années 2010-20, où l'on essaie de se faire croire que les technologies numériques fonctionnent détachées de toute réalité matérielle pour le seul bonheur de l'utilisateur.

Par exemple, la contrainte imposée sur le design du pipeline d'autoriser un ordre d'utilisation arbitraire des modules [créée des problèmes mathématiquement insolubles](https://github.com/darktable-org/darktable/pull/8673) en ce qui concerne le calcul des coordonnées des nœuds des masques, et aucune solution programmatique n'est possible (à part supprimer la contrainte…) parce que les maths ont dit non.

Sauf qu'une partie significative des utilisateurs programmeurs qui gravitent autour du projet sur Github et autour de la mailing-list développeurs reste convaincue qu'il n'y a ni bon ni mauvais workflow, juste des préférences personnelles. Ainsi, les modules devraient pouvoir se ré-ordonnancer à volonté, tant dans le pipeline que dans dans le workflow, et donc dans l'interface. La confusion vient du fait que la retouche non-destructive est vue à tort comme asynchrone (ce qui serait le cas si l'on n'utilisait ni masques ni mode de fusion) alors que le pipeline des pixels est séquentiel et plus proche d'une logique d'empilement de calques, telle qu'on la trouve dans Adobe Photoshop, Gimp, Krita, etc.

Découpler l'ordre des modules de leur ordre dans le pipeline revient autoriser toutes les utilisations même pathologiques, et à devoir écrire [des pages et des pages](https://docs.darktable.org/usermanual/4.0/en/darkroom/pixelpipe/the-pixelpipe-and-module-order/#changing-module-order) de documentation pour mettre en garde, expliquer quoi faire, comment et pourquoi ; documentation que personne ne lira pour finir par reposer en boucle les mêmes questions sur les différents forums toutes le semaines.

Dans cette histoire, tout le monde perd son temps par la faute d'un design d'interface qui essaie d'être si souple qu'il ne peut être rendu robuste et sécuritaire par défaut. On nage en plein [culte du cargo](https://fr.wikipedia.org/wiki/Culte_du_cargo) libriste, qui aime avoir l'illusion du choix, c'est à dire se voir offrir de nombreuses options dont la plupart sont inutilisables ou dangereuses, au détriment de la simplicité ([KISS](https://fr.wikipedia.org/wiki/Principe_KISS)), offertes à des utilisateurs dont la majorité ne comprend pas les implications de chaque option.

En l'absence de consensus sur l'ordonnancement des modules dans l'interface, un outil compliqué, peu fiable et lourd a été introduit fin 2020 pour permettre à chaque utilisateur de configurer la présentation des modules en onglets. Il est muni de nombreuses options inutiles et stocke la disposition courante dans la base de données en utilisant le nom traduit des modules, ce qui fait que changer la langue de l'interface fait perdre les pré-réglages. Entièrement configurable, il permet aux utilisateurs de choisir comment se faire mal, sans aucun guide de bonne pratique. Cette immondice est codée sur près de 4000 lignes [mélangeant allègrement des requêtes SQL au milieu du code d'interface GTK](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/libs/modulegroups.c#L3499-L3616), et les presets sont créés via des [macros compilateur redondantes](https://github.com/darktable-org/darktable/blob/master/src/libs/modulegroups.c#L1533-L1768), alors que les modules ont tous depuis longtemps un [drapeau binaire](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/iop/borders.c#L196) permettant de régler leur groupe par défaut de façon… modulaire.

Et plus important, il remplace une fonctionnalité simple et efficace, disponible jusque dans Darktable 3.2 : 

![](/posts/more-modules.png)

Un clic sur le nom du module l'active, un deuxième l'ajoute dans la colonne des modules favoris, un troisième le cache de l'interface. Le tout permettant des pré-réglages et stockant la vue courante en texte pur dans le fichier `darktablerc`. Simple et robuste, [codée en 688 lignes](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/libs/modulegroups.c) de code lisible et bien structuré, la fonctionnalité n'est donc pas assez amusante pour le développeur quincagénaire dilettante et il était urgent de la remplacer par une usine à gaz.

### Raccourcis clavier

En 2021 est ajouté ce que j'appelle le grand [turducken](https://fr.wikipedia.org/wiki/Turducken) MIDI. Il s'agit d'étendre l'interface de gestion des raccourcis claviers (déjà étendue en 2019 pour permettre le support des « raccourcis dynamiques », c'est à dire des actions combinées souris + clavier) pour supporter les périphériques MIDI et les manettes de jeux vidéos.

Fin 2022, soit un an et demi après cette fonctionnalité, dans le [sondage que j'ai réalisé](https://www.poll-maker.com/S-Quiz-Results?qp=2539714x3792Bf5e-98#), moins de 10 % des utilisateurs possèdent un périphérique MIDI, et seulement 2% l'utilisent pour Darktable. À comparer avec les 45 % d'utilisateurs qui possèdent une tablette graphique (type Wacom), dont le support par darktable est toujours si bancal que 6 % seulement l'utilisent. En dehors d'un problème de priorité, ce que je ne tolère pas ici, ce sont les effets de bords introduits par ce changement et le coût global qu'il a eu, à commencer par le fait qu'il n'importe pas les raccourcis utilisateur définis dans les versions 3.2 et antérieures, et qu'il rend la configuration de nouveaux raccourcis terriblement compliquée.

Avant le grand turducken, seule une liste restreinte de contrôles graphiques pouvaient être mappés vers des raccourcis claviers ou mixtes (clavier + souris). Cette liste était manuellement sélectionnée par les développeurs. Le grand turducken MIDI introduit permet de conecter _tous_ les contrôles GUI vers des raccourcis, présentant à l'utilisateur une liste de plusieurs milliers d'éléments à configurer, dans laquelle il est difficile de trouver les 3 dont vous avez vraiment besoin, et le moteur de recherche textuel est trop basique pour être utile :

![](/posts/shortcuts.png)

Notez le recours aux « effets », sur lesquels la [documentation](https://docs.darktable.org/usermanual/4.0/en/preferences-settings/shortcuts/) est d'un piètre secours. C'est par déduction (parce [le code n'est pas commenté non plus](https://github.com/darktable-org/darktable/blob/master/src/gui/accelerators.c#L101-L164)) que j'ai fini par comprendre qu'il s'agit d'émulations d'interactions bureautiques classiques (clic et clavier) destinées à être utilisées avec les périphériques MIDI et consoles de jeu (il faudra quand même m'expliquer la signification de `Ctrl-Toggle`, `Right-activate` ou `Right-Toggle` en termes d'interaction bureautique standard).

Ce qui est inadmissible, c'est que l'usage du pavé numérique est cassé [par design](https://github.com/darktable-org/darktable/issues/10628#issuecomment-994795922), notamment pour attribuer des notes chiffrées (étoiles) aux miniatures en table lumineuse. En effet, les touches modificatrices (verrouillage numérique et majuscule) ne sont pas correctement décodées par le bazar, et les chiffres sont traités différemment selon qu'ils sont entrés depuis le clavier "textuel" ou depuis le pavé numérique. Le `1` du pavé numérique est donc invariablement décodé comme un `Keypad End`, peu importe l'état du verrouillage numérique. Voici donc comment j'ai dû configurer les raccourcis numériques avec un clavier BÉPO et dupliquer la configuration pour le pavé numérique :

![](/posts/shortcuts-broken.png)

Il faut juste se souvenir que `Shift+"` et `Kp End` signifient tous deux `1` et penser à dupliquer tous les raccourcis pour le pavé numérique et pour le reste du clavier. En clair, on casse une attente utilisateur des plus basiques, et on envoie paître les critiques sur le design. La régression est mentionnée sur tous les forums Darktable mais n'inquiète personne.

La correction de ~~ce bug~~ cette fonctionnalité a été faite [sur Ansel](https://github.com/aurelienpierreeng/ansel/commit/257a70d2d14d8f8639c7fe8cf65f76bbcf5916e3) et les touches du pavé numérique sont remappées vers des [touches standard directement dans le code](https://github.com/aurelienpierreeng/ansel/commit/9cbf3e681b7a277968f8c9cfad43c693554d6f17), pour un total de 100 lignes de code, commentaires inclus. Effectuer cette correction a été très difficile : j'ai lu [la documentation Gtk](https://docs.gtk.org/gdk3/method.Keymap.translate_keyboard_state.html) et j'ai pompé ligne à ligne leur exemple. 2 ans que ça traîne, pour ça…

La cerise sur le gâteau est que, encore une fois, on a remplacé [1306 lignes de code clair et structuré](https://github.com/darktable-org/darktable/blob/darktable-3.6.x/src/gui/accelerators.c) par [une horreur de près de 4400 lignes](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/gui/accelerators.c) remplie de pépites, comme : 

1. La boucle `while` de la mort ([source](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/gui/accelerators.c#L2898-L2918)):

```C
  gboolean applicable;
  while((applicable =
           (c->key_device == s->key_device && c->key == s->key && c->press >= (s->press & ~DT_SHORTCUT_LONG) &&
           ((!c->move_device && !c->move) ||
             (c->move_device == s->move_device && c->move == s->move)) &&
           (!s->action || s->action->type != DT_ACTION_TYPE_FALLBACK ||
            s->action->target == c->action->target))) &&
        !g_sequence_iter_is_begin(*current) &&
        (((c->button || c->click) && (c->button != s->button || c->click != s->click)) ||
         (c->mods       && c->mods != s->mods ) ||
         (c->direction  & ~s->direction       ) ||
         (c->element    && s->element         ) ||
         (c->effect > 0 && s->effect > 0      ) ||
         (c->instance   && s->instance        ) ||
         (c->element    && s->effect > 0 && def &&
          def->elements[c->element].effects != def->elements[s->element].effects ) ))
  {
    *current = g_sequence_iter_prev(*current);
    c = g_sequence_get(*current);
  }
```

2. Le `switch` `case`  contenant des `if` imbriqués sur 2 niveaux ([source](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/gui/accelerators.c#L892-L954)): 

```C
  switch(owner->type)
  {
  case DT_ACTION_TYPE_IOP:
    vws = DT_VIEW_DARKROOM;
    break;
  case DT_ACTION_TYPE_VIEW:
    {
      dt_view_t *view = (dt_view_t *)owner;

      vws = view->view(view);
    }
    break;
  case DT_ACTION_TYPE_LIB:
    {
      dt_lib_module_t *lib = (dt_lib_module_t *)owner;

      const gchar **views = lib->views(lib);
      while(*views)
      {
        if     (strcmp(*views, "lighttable") == 0)
          vws |= DT_VIEW_LIGHTTABLE;
        else if(strcmp(*views, "darkroom") == 0)
          vws |= DT_VIEW_DARKROOM;
        else if(strcmp(*views, "print") == 0)
          vws |= DT_VIEW_PRINT;
        else if(strcmp(*views, "slideshow") == 0)
          vws |= DT_VIEW_SLIDESHOW;
        else if(strcmp(*views, "map") == 0)
          vws |= DT_VIEW_MAP;
        else if(strcmp(*views, "tethering") == 0)
          vws |= DT_VIEW_TETHERING;
        else if(strcmp(*views, "*") == 0)
          vws |= DT_VIEW_DARKROOM | DT_VIEW_LIGHTTABLE | DT_VIEW_TETHERING |
                 DT_VIEW_MAP | DT_VIEW_PRINT | DT_VIEW_SLIDESHOW;
        views++;
      }
    }
    break;
  case DT_ACTION_TYPE_BLEND:
    vws = DT_VIEW_DARKROOM;
    break;
  case DT_ACTION_TYPE_CATEGORY:
    if(owner == &darktable.control->actions_fallbacks)
      vws = 0;
    else if(owner == &darktable.control->actions_lua)
      vws = DT_VIEW_DARKROOM | DT_VIEW_LIGHTTABLE | DT_VIEW_TETHERING |
            DT_VIEW_MAP | DT_VIEW_PRINT | DT_VIEW_SLIDESHOW;
    else if(owner == &darktable.control->actions_thumb)
    {
      vws = DT_VIEW_DARKROOM | DT_VIEW_MAP | DT_VIEW_TETHERING | DT_VIEW_PRINT;
      if(!strcmp(action->id,"rating") || !strcmp(action->id,"color label"))
        vws |= DT_VIEW_LIGHTTABLE; // lighttable has copy/paste history shortcuts in separate lib
    }
    else
      fprintf(stderr, "[find_views] views for category '%s' unknown\n", owner->id);
    break;
  case DT_ACTION_TYPE_GLOBAL:
    vws = DT_VIEW_DARKROOM | DT_VIEW_LIGHTTABLE | DT_VIEW_TETHERING |
          DT_VIEW_MAP | DT_VIEW_PRINT | DT_VIEW_SLIDESHOW;
    break;
  default:
    break;
  }
```

3. Le `switch` `case` imbriqué du démon, avec des clauses additives sournoisement dissimulées ([source](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/bauhaus/bauhaus.c#L3339-L3415)) :

```C
case DT_ACTION_ELEMENT_ZOOM:
    ;
    switch(effect)
    {
    case DT_ACTION_EFFECT_POPUP:
      dt_bauhaus_show_popup(widget);
      break;
    case DT_ACTION_EFFECT_RESET:
      move_size = 0;
    case DT_ACTION_EFFECT_DOWN:
      move_size *= -1;
    case DT_ACTION_EFFECT_UP:
      _slider_zoom_range(bhw, move_size);
      break;
    case DT_ACTION_EFFECT_TOP:
    case DT_ACTION_EFFECT_BOTTOM:
      if((effect == DT_ACTION_EFFECT_TOP) ^ (d->factor < 0))
        d->max = d->hard_max;
      else
        d->min = d->hard_min;
      gtk_widget_queue_draw(widget);
      break;
    default:
      fprintf(stderr, "[_action_process_slider] unknown shortcut effect (%d) for slider\n", effect);
      break;
    }
```

Les programmeurs comprennent de quoi je parle, pour les autres, sachez que je ne comprends guère plus que vous ce que ça fait : c'est du code de merde et si plusieurs bugs ne sont pas cachés là-dedans, ça sera de la pure chance. Chasser des bugs dans ce merdier relève de l'archéologie de fond d'égoût.

Le vrai problème de ce genre de code, c'est qu'on ne peut pas l'améliorer sans le réécrire plus ou moins complètement : pour le corriger, il faut d'abord le comprendre, et la raison pour laquelle on doit le corriger, est précisément parce qu'il est incompréhensible et dangereux à long terme. On appelle ça de la [dette technique](https://fr.wikipedia.org/wiki/Dette_technique). En clair, tout le travail investi dans cette fonctionnalité va créer du travail additionnel parce qu'il est déraisonnable de garder du code de ce type au milieu d'une base de code de plusieurs centaines de milliers de lignes sans s'attendre à ce que ça nous explose à la face un jour.

C'est d'autant plus ridicule dans le contexte d'une application open-source où l'essentiel du personnel n'est même pas programmeur de formation. Le développeur intelligent écrit du code compréhensible par des idiots.

### Filtres de collections

Jusqu'à Darktable 3.8, les filtres de collections, en haut dans la table lumineuse, servaient à restreindre temporairement la vue sur une collection. La collection est une extraction de la base de données des photos selon certains critères, le plus courant étant d'extraire le contenu de tout un dossier (que Darktable nomme "pellicule" pour confondre tout le monde, car en fait une pelliculle est le contenu d'un dossier – plein de gens croient donc à tort que Darktable n'a pas de gestionnaire de fichiers).

Étant utilisateur de Darktable depuis plus d'une décennie, j'ai une base de données de plus de 140 000 entrées. Extraire une collection parmi ces 140 000 images est une opération lente. Mais mes dossiers contiennent rarement plus de 300 images. Filtrer, par exemple, les photos notées 2 étoiles ou plus, parmi une collection de 300 fichiers est rapide. Et passer d'un filtre à l'autre l'est également. Le filtre n'est donc qu'une vue partielle ou totale d'une collection, optimisée pour un usage marche/arrêt rapide et temporaire.

Sous couvert de refactoriser le code de filtrage, qui prenait en tout et pour tout [550 lignes](https://github.com/darktable-org/darktable/blob/darktable-3.6.x/src/libs/tools/filter.c), le Gaston Lagaffe en chef de Darktable s'est attelé à briser ce modèle pour transformer les filtres en collections comme les autres, au moyen de plus de [6000 lignes de code](https://github.com/darktable-org/darktable/tree/darktable-4.2.x/src/libs/filters) sans compter les innombrables correctifs de bugs qui n'ont fait qu'ajouter des lignes[^4]. Le tout, comme d'habitude, hautement configurable et redondant avec le classique [module collections](https://docs.darktable.org/usermanual/4.0/en/module-reference/utility-modules/shared/collections/) qui est resté là, et servi par des icônes tellement peu claires qu'il a fallu ajouter des infobulles textuelles pour en clarifier le sens.

[^4]: Le fait que les corrections de bugs ajoutent systématiquement des lignes de code au lieu de modifier des lignes existantes est un indice que la logique de programmation de base est mauvaise et induit trop de cas particuliers. Le programmeur rigoureux essaie toujours de garder son code le plus général possible pour éviter le [code spaghetti](https://fr.wikipedia.org/wiki/Programmation_spaghetti).

Dans ce code de qualité, on trouvera le sempiternel `while` sous le `switch case` dans le `if` dans le `if` dans le `for` ([source](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/libs/filtering.c#L1382-L1459)) : 

```C
for(int k = 0; k < num_rules; k++)
  {
    const int n = sscanf(buf, "%d:%d:%d:%d:%399[^$]", &mode, &item, &off, &top, str);

    if(n == 5)
    {
      if(k > 0)
      {
        c = g_strlcpy(out, "<i>   ", outsize);
        out += c;
        outsize -= c;
        switch(mode)
        {
          case DT_LIB_COLLECT_MODE_AND:
            c = g_strlcpy(out, _("AND"), outsize);
            out += c;
            outsize -= c;
            break;
          case DT_LIB_COLLECT_MODE_OR:
            c = g_strlcpy(out, _("OR"), outsize);
            out += c;
            outsize -= c;
            break;
          default: // case DT_LIB_COLLECT_MODE_AND_NOT:
            c = g_strlcpy(out, _("BUT NOT"), outsize);
            out += c;
            outsize -= c;
            break;
        }
        c = g_strlcpy(out, "   </i>", outsize);
        out += c;
        outsize -= c;
      }
      int i = 0;
      while(str[i] != '\0' && str[i] != '$') i++;
      if(str[i] == '$') str[i] = '\0';

      gchar *pretty = NULL;
      if(item == DT_COLLECTION_PROP_COLORLABEL)
        pretty = _colors_pretty_print(str);
      else if(!g_strcmp0(str, "%"))
        pretty = g_strdup(_("all"));
      else
        pretty = g_markup_escape_text(str, -1);

      if(off)
      {
        c = snprintf(out, outsize, "<b>%s</b>%s %s",
                     item < DT_COLLECTION_PROP_LAST ? dt_collection_name(item) : "???", _(" (off)"), pretty);
      }
      else
      {
        c = snprintf(out, outsize, "<b>%s</b> %s",
                     item < DT_COLLECTION_PROP_LAST ? dt_collection_name(item) : "???", pretty);
      }

      g_free(pretty);
      out += c;
      outsize -= c;
    }
    while(buf[0] != '$' && buf[0] != '\0') buf++;
    if(buf[0] == '$') buf++;
  }
```

et autres `if` imbriqués sur deux niveaux dans des `switch case` nécessaires au support des raccourcis clavier ([source](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/libs/filters/rating_range.c#L201-L265)).

Cette dernière saloperie a été la goutte d'eau qui a fait déborder le vase et m'a fait forker Ansel. Je refuse de continuer à travailler sur une bombe à retardement dans une équipe qui ne voit pas le problème et qui fait mumuse avec du code sur son temps libre. Coder les amuse peut-être, moi pas. Et réparer les conneries de gamins irresponsables qui ont deux fois mon âge, surtout quand ils cassent des trucs que j'ai nettoyé il y a 3 ou 4 ans, me met en rage.

### Table lumineuse

La table lumineuse a subi deux ré-écritures quasi complètes, la première début 2019, visant à optimiser le code pour rendre la vue plus rapide, la deuxième fin 2019, qui ajoute de nombreuses fonctionnalités discutables dont la vue [sélection](https://docs.darktable.org/usermanual/development/fr/lighttable/lighttable-modes/culling/).

Rapidement, le mode sélection est décomposé en deux modes : la sélection dynamique et la sélection statique, qui gèrent le nombre d'images différemment. Beaucoup d'utilisateurs n'ont toujours pas compris la différence 4 ans plus tard. On a donc alors la vue par défaut (gestionnaire de fichier), la vue table lumineuse zoomable (que personne n'utilise), la vue sélection statique, sélection dynamique, et le mode prévisualisation (une seule image en plein écran).

Puis de nouvelles options d'apparence sont ajoutées aux miniatures de la table lumineuse, permettant de définir les surimpressions : surimpressions permanentes basiques, surimpressions permanentes avec infos EXIF étendues, les mêmes mais affichées seulement au survol, et enfin au survol temporisées (avec minuterie réglable).

Le code d'interface qui fait le rendu des miniatures et de leur surimpressions doit donc tenir compte de 5 vues différentes et de [7 variantes d'affichages](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/dtgtk/thumbnail.h#L38-L48), soit 35 combinaisons possibles. Le code qui assure le redimensionnement correct des miniatures [fait donc 220 lignes à lui seul](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/dtgtk/thumbnail.c#L1565-L1786).

Mais ça ne s'arrête pas là, puisque le code de rendu graphique des miniature est partagé également avec la barre "pellicule", ce qui fait en fait 36 combinaisons possibles dans le rendu des miniatures. Multiplié par 3 thèmes de couleur de base, ça fait donc 108 jeu d'instruction CSS possibles pour styliser l'interface… dont beaucoup de combinaisons [ont été oubliées dans la grande refonte graphique de Darktable 4.0](https://github.com/darktable-org/darktable/pull/11835), et comment aurait-il pu en être autrement ?

Dans Darktable 2.6, on avait donc __4193 lignes__ pour l'ensemble, qui ne comportait que la vue gestionnaire de fichier, table lumineuse zoomable et prévisualisation plein écran avec deux modes d'affichage des surimpressions (toujours visible ou visible au survol) :

* 2634 lignes dans [views/lighttable](https://github.com/darktable-org/darktable/blob/darktable-2.6.x/src/views/lighttable.c) pour la vue table lumineuse et le rendu des miniatures,
* 1124 lignes dans [libs/tools/filmstrip.c](https://github.com/darktable-org/darktable/blob/darktable-2.6.x/src/libs/tools/filmstrip.c) pour la barre pellicule, dont une partie duplique partiellement le code de la table lumineuse, en ce qui concerne le rendu des miniatures,
* 435 lignes dans [libs/tools/global_toolbox.c](https://github.com/darktable-org/darktable/blob/darktable-2.6.x/src/libs/tools/global_toolbox.c), pour le menu de boutons permettant d'activer ou désactiver l'affichage des surimpressions.

Après Darktable 3.0 et l'ajout des modes de sélection, on passe à __6731 lignes__ :

* 5149 lignes dans [views/lighttable](https://github.com/darktable-org/darktable/blob/darktable-3.0.x/src/views/lighttable.c)
* 1177 lignes dans [libs/tools/filmstrip.c](https://github.com/darktable-org/darktable/blob/darktable-3.0.x/src/libs/tools/filmstrip.c),
* 405 lignes dans [libs/tools/global_toolbox.c](https://github.com/darktable-org/darktable/blob/darktable-3.0.x/src/libs/tools/global_toolbox.c)

Après Darktable 3.2 et l'ajout des 7 variantes de surimpressions hautement configurables et la refactorisation du code, on passe à __8380 lignes__:

* 1463 lignes dans [views/lighttable.c](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/views/lighttable.c)
* 1642 lignes dans [dtgtk/culling.c](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/dtgtk/culling.c), où les fonctionnalités des vues sélection ont été détachées,
* 2447 lignes dans [dtgtk/thumbtable.c](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/dtgtk/thumbtable.c), où sont gérés les conteneurs de miniatures pour la table lumineuse et
* 1736 lignes dans [dtgtk/thumbnail.c](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/dtgtk/thumbnail.c), où sont gérées les miniatures en elles-mêmes,
* 169 lignes dans [dtgtk/thumbnail_btn.c](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/dtgtk/thumbnail_btn.c), où sont déclarés des boutons spécifiques aux miniatures,
* 115 lignes dans [libs/tools/filmstrip.c](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/libs/tools/filmstrip.c)
* 808 lignes dans [libs/tools/global_toolbox.c](https://github.com/darktable-org/darktable/blob/darktable-3.2.x/src/libs/tools/global_toolbox.c)

Dans Darktable 4.2, après correction de nombreux bugs, on arrive à un total de __9264 lignes__ :

* 1348 lignes dans [views/lighttable.c](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/views/lighttable.c)
* 1828 lignes dans [dtgtk/culling.c](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/dtgtk/culling.c), pour le code spécifique à la vue sélection,
* 2698 lignes dans [dtgtk/thumbtable.c](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/dtgtk/thumbtable.c), pour le code construisant les conteneurs de miniatures,
* 2093 lignes dans [dtgtk/thumbnail.c](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/dtgtk/thumbnail.c), pour le code de rendu des miniatures elle-mêmes,
* 166 lignes dans [dtgtk/thumbnail_btn.c](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/dtgtk/thumbnail_btn.c), pour les boutons spécifiques aux miniatures
* 109 lignes dans [libs/tools/filmstrip.c](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/libs/tools/filmstrip.c)
* 1022 lignes dans [libs/tools/global_toolbox.c](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/libs/tools/global_toolbox.c)

Le nombre de lignes est une chose, mais ce n'est pas la pire. En effet, si vous démarrez `darktable -d sql` et que vous survolez une miniature de la table lumineuse, vous allez obtenir en console :

```bash
140.8252 [sql] darktable/src/common/image.c:311, function dt_image_film_roll(): prepare "SELECT folder FROM main.film_rolls WHERE id = ?1"
140.8259 [sql] darktable/src/common/image.c:387, function dt_image_full_path(): prepare "SELECT folder || '/' || filename FROM main.images i, main.film_rolls f WHERE i.film_id = f.id and i.id = ?1"
140.8271 [sql] darktable/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
140.8273 [sql] darktable/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
140.8275 [sql] darktable/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
140.8277 [sql] darktable/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
140.8279 [sql] darktable/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
140.8280 [sql] darktable/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
140.8282 [sql] darktable/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
140.8284 [sql] darktable/src/common/tags.c:635, function dt_tag_get_attached(): prepare "SELECT DISTINCT I.tagid, T.name, T.flags, T.synonyms, COUNT(DISTINCT I.imgid) AS inb FROM main.tagged_images AS I JOIN data.tags AS T ON T.id = I.tagid WHERE I.imgid IN (104337) AND T.id NOT IN memory.darktable_tags GROUP BY I.tagid  ORDER by T.name"
140.8286 [sql] darktable/src/common/tags.c:635, function dt_tag_get_attached(): prepare "SELECT DISTINCT I.tagid, T.name, T.flags, T.synonyms, COUNT(DISTINCT I.imgid) AS inb FROM main.tagged_images AS I JOIN data.tags AS T ON T.id = I.tagid WHERE I.imgid IN (104337) AND T.id NOT IN memory.darktable_tags GROUP BY I.tagid  ORDER by T.name"
140.9512 [sql] darktable/src/common/act_on.c:156, function _cache_update(): prepare "SELECT imgid FROM main.selected_images WHERE imgid=104337"
140.9547 [sql] darktable/src/common/act_on.c:156, function _cache_update(): prepare "SELECT imgid FROM main.selected_images WHERE imgid=104337"
140.9550 [sql] darktable/src/common/act_on.c:288, function dt_act_on_get_query(): prepare "SELECT imgid FROM main.selected_images WHERE imgid =104337"
140.9552 [sql] darktable/src/libs/metadata.c:263, function _update(): prepare "SELECT key, value, COUNT(id) AS ct FROM main.meta_data WHERE id IN (104337) GROUP BY key, value ORDER BY value"
140.9555 [sql] darktable/src/common/collection.c:973, function dt_collection_get_selected_count(): prepare "SELECT COUNT(*) FROM main.selected_images"
140.9556 [sql] darktable/src/libs/image.c:240, function _update(): prepare "SELECT COUNT(id) FROM main.images WHERE group_id = ?1 AND id != ?2"
140.9558 [sql] darktable/src/common/tags.c:635, function dt_tag_get_attached(): prepare "SELECT DISTINCT I.tagid, T.name, T.flags, T.synonyms, COUNT(DISTINCT I.imgid) AS inb FROM main.tagged_images AS I JOIN data.tags AS T ON T.id = I.tagid WHERE I.imgid IN (104337) AND T.id NOT IN memory.darktable_tags GROUP BY I.tagid  ORDER by T.name"
```

ce qui veut dire que 18 requêtes SQL sont faites dans la base de données, destinées à récupérer les informations de l'image, et démarrées à chaque fois que le curseur survole une nouvelle miniature dans la table lumineuse, pour aucune raison car les métadonnées n'ont pas changé depuis le précédent survol.

Dans Ansel, en retirant la plupart des options, j'ai réussi à économniser 7 requêtes, ce qui n'empêche pas les requêtes dupliquées :

```bash
12.614534 [sql] ansel/src/common/image.c:285, function dt_image_film_roll(): prepare "SELECT folder FROM main.film_rolls WHERE id = ?1"
12.615225 [sql] ansel/src/common/image.c:356, function dt_image_full_path(): prepare "SELECT folder || '/' || filename FROM main.images i, main.film_rolls f WHERE i.film_id = f.id and i.id = ?1"
12.616499 [sql] ansel/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
12.616636 [sql] ansel/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
12.616769 [sql] ansel/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
12.616853 [sql] ansel/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
12.616930 [sql] ansel/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
12.617007 [sql] ansel/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
12.617084 [sql] ansel/src/common/metadata.c:487, function dt_metadata_get(): prepare "SELECT value FROM main.meta_data WHERE id = ?1 AND key = ?2 ORDER BY value"
12.617205 [sql] ansel/src/common/tags.c:635, function dt_tag_get_attached(): prepare "SELECT DISTINCT I.tagid, T.name, T.flags, T.synonyms, COUNT(DISTINCT I.imgid) AS inb FROM main.tagged_images AS I JOIN data.tags AS T ON T.id = I.tagid WHERE I.imgid IN (133727) AND T.id NOT IN memory.darktable_tags GROUP BY I.tagid  ORDER by T.name"
12.617565 [sql] ansel/src/common/tags.c:635, function dt_tag_get_attached(): prepare "SELECT DISTINCT I.tagid, T.name, T.flags, T.synonyms, COUNT(DISTINCT I.imgid) AS inb FROM main.tagged_images AS I JOIN data.tags AS T ON T.id = I.tagid WHERE I.imgid IN (133727) AND T.id NOT IN memory.darktable_tags GROUP BY I.tagid  ORDER by T.name"
```

Le problème est que le code source imbrique des commandes SQL à l'intérieur des fonctions qui dessinent l'interface graphique, et déméler ce fouillis à travers les différentes couches héritées de la refactorisation est encore une fois de l'archéologie.

On est sur un cas de figure où la "refactorisation" a en réalité complexifié le code et où fusionner le code de rendu des miniatures entre la barre pellicule et la table lumineuse n'a fait qu'ajouter des `if{ }` internes à plusieurs niveaux qui en compliquent encore la structure, juste pour obéir aveuglément au principe de réutilisation du code.

## Le cosmétique prend le dessus sur la stabilité

Darktable 4.2 introduit la prévisualisation des styles dans la chambre noire. Ça serait génial si les styles n'étaient pas cassés en profondeur, lorsqu'utilisés avec un ordre du pipeline non standard ou des instances multiples de modules. Le problème est qu'une solution propre et pérenne passe par la théorie des [graphes orientés](https://fr.wikipedia.org/wiki/Graphe_orient%C3%A9), et là forcément, on a perdu nos pisseurs de code copié-collé.

Dans le même esprit, on a de grosses incohérences sur les copier-coller d'historique en mode _écraser_ lorsque des presets utilisateur par défaut sont également utilisés (notamment dans les module balance des blancs). Mais c'est bien plus amusant de saloper l'interface, alors ça restera là encore longtemps.

Darktable 3.6 et 3.8 ont introduit pleins de variantes de l'histogramme : vectorscope, forme d'onde verticale, espaces de couleurs avancés et exotiques. Sauf que si vous lancez `darktable -d perf` en console et que vous allez en chambre noire, vous allez voir quantité de

```bash
23.748084 [histogram] took 0.003 secs (0.000 CPU) scope draw
23.773753 [histogram] took 0.005 secs (0.004 CPU) scope draw
23.783284 [histogram] took 0.001 secs (0.000 CPU) scope draw
```

à chaque fois que vous bougez le curseur dans la fenêtre (et même pas forcément sur l'histogramme). C'est l'histogramme qui est redessiné à chaque interaction de la souris avec la fenêtre. Le même problème affecte de [nombreux éléments graphiques custom](https://github.com/darktable-org/darktable/issues/11836) et sa cause est non-identifiée. Notez qu'il n'affecte pas Ansel, donc la cause devait être logée quelque part dans les 23 000 lignes de code que j'ai viré.

Par 2 fois, j'ai essayé de refactoriser [l'immondice qu'est devenue cette fonctionnalité](https://github.com/darktable-org/darktable/blob/darktable-4.2.x/src/libs/histogram.c), mais une nouvelle fonctionnalité plus urgente a été poussée à chaque fois en invalidant mon travail. J'ai fini par laisser tomber.

Le niveau de pourrissement atteint par l'histogramme est tel qu'une ré-écriture complète prendrait moins de temps qu'une refactorisation, surtout que l'histogramme est prélevé bien trop tard dans le pipeline, dans l'espace de couleur écran, ce qui rend le définition d'un espace de couleur histogramme caduque étant donné que le gamut est écrêté dans l'espace écran quoi qu'il arrive. Et devinez quoi… Darktable 4.4 aura encore plus d'options, avec la possibilité de définir des harmonies de couleur (fondamental pour les geeks qui font de la peinture au numéro et retouchent des histogrammes).

Reste qu'à chaque fois que vous bougez la souris, un grand nombre de recalculs superflus sont démarrés pour rien. À quel point c'est mal ? Je me suis amusé à mesurer la consommation CPU de mon système au repos, avec l'utilitaire Linux `powertop`. Le protocole est simple : un ordinateur portable (CPU Intel Xeon Mobile de 6e génération) sur batterie en mode éco, rétroéclairage écran au minimum, on ouvre l'application, on ne touche à rien pendant 4 min et on regarde la consommation CPU globale du système telle que rapportée par `powertop` au cours de la 5e minute :

* Système de base (pas d'application ouverte à part `powertop` dans un terminal) : __3,0 à 3,5 % CPU__
* Ansel :
  * ouvert sur la table lumineuse : __2,9 à 3,4 % CPU__,
  * ouvert sur la chambre noire : __3,8 à 4,5 %__
* Darktable :
  * ouvert sur la table lumineuse : __6,6 à 7,1 % CPU__,
  * ouvert sur la chambre noire : __30,9 à 44,9 % CPU__ _(non, ce n'est pas une erreur de virgule)_,

Je ne comprends pas ce que Darktable calcule lorsqu'on le laisse ouvert sans y toucher, parce qu'il n'y a rien à calculer. Darktable en table lumineuse consomme à lui seul autant que tout le système Fedora 37 + l'environnement de bureau KDE + un gestionnaire de mot de passe tiers et un client Nextcloud qui tournent en tâche de fond, et il consomme 10 fois plus que tout le système lorsqu'ouvert en chambre noire.

Tout ceci pointe vers du code d'interface graphique très buggé. Dans Ansel, j'ai retiré une grande partie du code sale, sans pour autant optimiser quoi que ce soit par ailleurs, et ces chiffres ne font que valider mon choix : le code sale cache des problèmes indétectables à la lecture, et on ne peut pas continuer comme ça.

Je suis apparemment le seul à trouver anormal de priver le pixel pipeline de 1/3 à 1/2 de la puissance CPU pour peinturlurer une stupide interface.  En tout état de cause, il n'y a aucune raison valable pour qu'un logiciel qu'on laisse ouvert sans y toucher transforme un ordinateur en grille-pain, surtout depuis qu'on n'achète plus de gaz russe.

## Travailler contre soi même

Les quelques exemples ci-dessus donnent un aperçu de la complexification du code source, mais aussi de sa dégradation au cours du temps en terme de qualité, car des fonctionnalités basiques et robustes sont remplacées par du [code spaghetti](https://fr.wikipedia.org/wiki/Programmation_spaghetti) confus et sournoisement buggé. Derrière ce problème de lisibilité, c'est finalement une dégradation de la maintenabilité à moyen terme qui n'augure rien de bon pour le futur du projet, avec l'approbation du mainteneur.

Depuis 4 ans que je travaille à temps plein sur darktable, 2022 est la première année où je suis pratiquement incapable d'identifier la source de la plupart des bugs d'interface, tant la logique de fonctionnement est devenue tordue et le code incompréhensible.

L'équipe Darktable travaille contre elle-même en essayant de supporter trop d'options différentes, produisant du code dont le résultat de l'exécution dépend de trop de variables d'environnement, pouvant interagir de trop de manières différentes. Tout ça pour éviter de prendre des décisions de design qui pourraient en froisser certains en limitant les fonctionnalités et les options disponibles.

C'est simple : le travail effectué coûte de plus en plus de travail en maintenance.

La débauche d'options et de préférences, qui est la stratégie Darktable pour (ne pas) gérer les désaccords sur le design à adopter, créent des cas d'utilisation ultra-contextuels où aucun utilisateur n'a les même options activées et où il est impossible de reproduire les bugs dans un environnement différent. Et demander aux utilisateurs d'attacher leur fichier de configuration `darktablerc` aux rapports de bugs n'aideraient pas non plus les développeurs car ce fichier fait maintenant 1287 lignes globalement illisibles.

Les bugs bizarres et difficiles à reproduire s'empilent, y compris sur des ordinateurs [System 76](https://system76.com/) conçus spécialement pour Linux, où l'on ne pourra pas invoquer de problèmes de pilotes. De nombreux bugs incohérents et aléatoires que j'ai constaté en donnant des cours de retouche ne sont pas répertoriés sur le trackeur de bug, et il est à peu près clair qu'ils dorment dans les méandres de la débauche de `if` et `switch case` qui sont ajoutés à un rythme alarmant depuis 2020.

Régler ces bugs étranges et contextuels ne peut se faire qu'en simplifiant la séquence de contrôle du programme et donc en limitant le nombre d'options utilisateur. Mais la brochette de geeks qui s'agite sur le projet ne veut pas en entendre parler.

En fait, Darktable soufre de plusieurs problèmes :

1. Un noyau dur de développeurs assez médiocres mais disposant de beaucoup de temps libre pour faire n'importe quoi, animés par les meilleures intentions du monde mais sans conscience des dommages qu'ils causent,
1. La complaisance du mainteneur, qui laisse passer du code dégueulasse pour être sympa,
1. Un manque cruel de compétences en mathématiques pures, algorithmique, traitement de signal, sciences de la couleur et généralement en raisonnement et abstraction, qui sont requises au delà du code de traitement de pixels pour simplifier et factoriser les fonctionnalités,
1. Une sale manie de "développer" par copié-collé de code récupéré ailleurs dans Darktable ou dans d'autres projets libres qui utilisent des architectures de pipeline différentes mais sans l'adapter en conséquence (pour adapter, il faut comprendre comment ça marche, et ça c'est trop demander…).
1. Un refus pur et simple de supprimer des fonctionnalités pour faire de la place aux nouvelles et garder un certain équilibre,
1. Un biais d'échantillon, où les seuls utilisateurs qui interagissent avec le développement via Github sont programmeurs et anglophones. Le fait est que le commun des mortels ne comprend pas ce qu'est une forge logicielle et qu'il est difficile d'encourager les non-programmeurs à créer un compte Github pour remonter les bugs. On parle d'une population d'utilisateurs [composée à plus de 44 % de programmeurs](https://eng.aurelienpierre.com/2023/01/who-are-the-darktable-users/#Conclusion-of-this-part) et à plus de 35 % de titulaires d'un diplôme universitaire (ils sont respectivement 6 % et 15 % dans la population générale).
6. Un développement à marche forcée, sans agenda, sans concertation, où chaque utilisateur de Github peut polluer les discussions avec un avis non-éclairé sur les travaux en cours. Le fait est que le traitement d'image paraît facile et est sans danger, si bien que toute personne capable de calculer un logarithme se sent compétente. Mais les erreurs fondamentales dans la chaîne colorimétrique de Darktable prouvent chaque jour le contraire…
7. Une absence de priorité dans les fonctionnalités à refactoriser, stabiliser ou étendre : tous les projets sont ouverts en même temps, même s'ils entrent en conflits les uns avec les autres.
8. Une quantité d'activité (emails et notifications) impossible à suivre, entre les commentaires, les discussions hors-sujet, les bugs qui n'en sont pas, les propositions de changement de code et les changements effectifs qui peuvent impacter votre propre travail, ce qui fait qu'il faut être partout tout le temps ; il y a énormément à lire mais peu à garder, la discussion pour la discussion grève la productivité, et l'absence de structure de travail en est la cause principale.
9. des bugs non-bloquants dissimulés à la hâte avant de les avoir compris, au lieu de les régler pour de bon à la source, qui déplacent voire aggravent les problèmes à long terme sans laisser de traces dans une documentation pérenne,
10. un calendrier de sortie de version qu'on tient coûte que coûte même quand ce n'est pas réaliste, alors que personne ne nous l'impose,
11. des changements de code qui peuvent arriver partout tout le temps, qui font qu'on travaille sur des sables mouvants en permanence et qu'il faut travailler aussi vite et mal que les autres pour ne pas se retrouver largué derrière le volume et la fréquence des changements (_commits_),
12. des nouvelles fonctionnalités qui dégradent l'utilisabilité et complexifient l'interface sans régler de problème défini et tiennent lieu de projets récréatifs à des programmeurs non formés à la conception/ingéniérie.

Mais le plus rageant, c'est cette obstination à vouloir remplacer des fonctionnalités simples et fonctionnelles par des horreurs de sur-ingéniérie destinées à satisfaire des usages déviants et marginaux en emmerdant tout le monde avec des listes interminables d'options mal pensées. Le meilleur endroit pour cacher un arbre, c'est au milieu de la forêt, et beaucoup ne l'ont pas encore compris.

Concernant le nouveau mode de filtrage, par exemple, je suis arrivé à la conclusion qu'il plaît à des gens qui font un usage exagérément restrictif des fonctionnalités de catalogage, en utilisant des mots-clés trop spécialisés, et souvent en balançant toutes leurs photos dans le même dossier. Ils se retrouvent donc à devoir faire des requêtes complexes pour isoler des sous-ensembles trop restreints parmi des ensembles trop larges. Un problème qui devrait se régler en changeant de méthode de travail (ranger les images dans des dossiers et sous-dossiers pertinents, attribuer des mots-clés suffisamment génériques pour éviter des requêtes `mot clé 1 ET mot clé 2`), et pas en leur donnant plus d'outils pour continuer à travailler aussi mal mais plus vite, au prix de complexifier l'interface pour tous ceux qui ont des besoins basiques.

## Confondre agitation et activité

Darktable est devenu le club informatique du lycée, là où les geeks s'amusent. C'est globalement un condensé de toutes les pires histoires d'entreprises informatiques à ceci près que le projet ne génère pas un centime, donc il est urgent de se demander pourquoi on s'impose ça.

Côté utilisateur, on salue l'effervescence du projet darktable (oui, ça bouge), sans se rendre compte que l'emballement des commits n'est pas de l'activité mais de l'agitation, et que le travail effectué n'importe comment coûte de plus en plus de travail à maintenir.

On a bien un semblant de contrôle qualité, via les tests d'intégration, qui mesurent l'erreur perceptuelle sur des traitements photo de référence, mais ils ne déclenchent même plus d'émotion quand on voit une erreur moyenne sur une image d'un delta E de 1.3 (faible) alors que la nature du changement apporté aurait dû avoir un delta E strictement nul. Si __le__ test passe (parce qu'on ne teste qu'une image SDR sur une scène studio), on ne cherche pas à comprendre ni à valider si la théorie tient debout. On a transformé le test en décharge de responsabilité, tant que la métrique d'erreur reste sous le seuil de validation…

Pire, avec la sortie de darktable 4.0 — _Geektable_ –, j'ai vu sur Youtube les gens commencer à se plaindre que cette release n'était pas très excitante. À force de droguer nos utilisateurs à la release superlative, blindée de fonctionnalités qu'on n'a pas eu le temps de tester correctement (une bande de gars à temps partiel qui produit autant de travail en si peu de temps, vous rêvez encore ?), on en a fait des accros au sapin de Noël blindé pour être sûr que, le jour où l'envie nous prend d'être enfin responsables et de sortir des versions stables (donc ennuyeuses), ça se retournera contre nous.

L'équipe de Darktable met en œuvre des méthodes de travail qu'on retrouve dans toutes les boîtes à _burn-out_ où les employés utilisent tous leurs congés maladie jusqu'au dernier. Les _pull requests_ de plus de 3 mois sont invariablement en conflit avec la branche principale, vue que celle-ci est secouée tous les mois pour "des tests généralisés". Sauf que les rares utilisateurs qui compilent la branche principale (master) n'ont pas la moindre idée de ce qu'il faut tester en particulier, à moins de disséquer l'historique des commits Git, ce qui implique de comprendre à la fois le langage C et l'impact des changements en pratique sur le logiciel.

Pour limiter les branches à durée de vie trop longue, qui finiront invariablement en conflit avec la branche principale, on a trouvé une solution brillante : on sort  2 releases par an, faisant du développement à marche forcée à base de code pas fini et peu testé un art de vivre, sans jamais réaliser que le problème de fond, c'est d'abord l'absence de planification, mais aussi le fait que les contributeurs codent avant d'avoir défini le problème à résoudre (quand il y a un vrai problème à résoudre, et pas juste un mec qui s'est dit que "ça serait cool si…"), en modifiant en parallèle les mêmes parties, sans concertation.

La poussière n'a pas le temps de retomber qu'on est déjà en train de secouer à nouveau la base de code, sans jamais se donner de phases de stabilisation où l'on ne fait que nettoyer les bugs (et je ne parle pas du mois de _feature-freeze_ avant la release, mais de releases consacrées seulement à l'amélioration du code). Le trackeur de bugs explose dans les 3 semaines suivant chaque release, puisqu'une part significative des utilisateurs n'utilisent que les paquets pré-compilés, ce qui coïncide en plus avec les vacances d'été et les vacances de Noël, où j'ai personnellement autre chose à faire que me taper des rapports de bugs après le sprint épuisant que représente le mois précédent les releases.

Depuis 2021, quand je mets à jour mon dépôt Git avec les derniers changements de la branche master de Darktable, c'est en me demandant ce qu'ils ont encore cassés __cette fois ci__. On casse plus vite qu'on ne répare et généralement, les réparations cassent autre chose. En fait, les seuls utilisateurs qui trouvent Darktable stable sont ceux qui en font une utilisation très basique, ce qui est ironique pour une application dont l'argument de vente est précisément d'être avancée.

Alors on me sert le fait que c'est du travail gratuit, comme si c'était une excuse. En fait, c'est une circonstance aggravante : si ce n'est pas payé, pourquoi on s'impose des conditions de travail comme celles-là ??? En dehors du fait que ce travail gratuit me colle un burn-out post-release par an, il coûte de plus en plus cher en maintenance et la maintenance est de plus en plus désagréable. Ce n'est pas du travail gratuit.

De plus, il est fourni par des gens qui ont un temps et une énergie limités. Si la ressource est limitée, il va falloir arrêter de me raconter des histoires : on est dans les mêmes contraintes de rentabilité qu'une entreprise, les cotisations sociales en moins, et sans gestion des priorités, on va se faire dépasser par de la dette technique qu'on n'aura pas les ressources pour maintenir.

## Qu'est-ce qu'on attend pour être heureux ?

Le fait que Darktable soit un rouleau compresseur en plein emballement et sans pilote, qui génère une quantité de travail croissante, n'est pas bon signe pour un projet qui approche des 15 ans. Normalement, un projet mature ralentit le rythme parce qu'il est assez complet pour être utilisable et que les gens qui bossent dessus ont trouvé un rythme de croisière et des méthodes de travail efficaces.

Je suis dessus à temps plein depuis le 2018, pour des revenus qui s'étalent entre 800 et 900 € par mois, et c'est peu dire que c'est mal payé pour endurer les conséquences désastreuses du travail d'amateurs désorganisés qui veulent juste participer à quelque chose qu'ils trouvent cool au mépris de la qualité du produit fini et de son utilisabilité par des moldus de l'informatique.

Si je baisse le nez un mois et demi pour développer un espace de couleur perceptuel, quand je relève la tête, c'est pour découvrir la nouvelle usine à gaz qui viole un peu plus le paradigme vue-modèle-contrôleur et me faire signifier que j'arrive trop tard pour m'opposer au projet. Si je prends 3 semaines de vacances en août, c'est pour découvrir que le mainteneur à court-circuité (une fois de plus) ma révision sur un changement mathématique sur ledit espace de couleur, qui suppose de s’asseoir calmement à tête reposée pour remonter le fil du calcul, tout ça parce que… fallait aller vite ? Mais, bordel, c'était quoi l'urgence ?

J'ai dû recevoir la notification quelque part au milieu des 2234 emails que Github m'a envoyé entre janvier et août 2022 (en 2021, c'était 4044), sans parler des utilisateurs qui me _ping_ un peu partout, sur Youtube, Reddit, Matrix, Github, Telegram, directement par email et anciennement sur pixls.us (693 emails en 2022, 948 en 2021). Tout ça pour des gens en complet décalage, qui ne réalisent pas que je fais ça toute la semaine, que la photo est leur loisir à eux mais mon travail à moi, et que j'aimerais juste qu'on me lâche le chat les week-ends et jours fériés. Sans compter que les plus emmerdants ne sont pas ceux qui rétribuent financièrement mon travail.

Je n'ai ni le temps ni l'envie de faire chercheur, designer et en plus secrétaire, tout en faisant du baby-sitting technique au milieu d'une équipe de Gaston Lagaffe qu'il faut à la fois former et surveiller parce qu'ils sont incapables de :

1. établir un planning de développement avec un ordre de priorité des nouvelles fonctionnalités sur lesquelles "on" va travailler,
2. fournir un cahier des charges des besoins et des problèmes, avec un cas d'utilisation réel, __avant__ de se jeter sur leur éditeur de code et de faire n'importe quoi pour développer une nouvelle fonctionnalité qui se cherche un problème à résoudre,
3. évaluer le coût de maintenance du changement avant d'inventer la pompe à lardons bionique à osmose inversée qui ne marche que les jours pairs si Jupiter est en quadrature inverse avec Saturne,
4. limiter les pertes et arrêter les frais quand ils s'engagent dans des impasses de design introduisant des régressions pires que les hypothétiques bénéfices attendus,
5. prendre sur soi et reculer une release si le code n'est manifestement pas prêt (ou alors je n'ai rien compris et les actionnaires vont nous virer si on release en retard ???).

L'absence de management et de leadership, tant au niveau de la gestion quotidienne du projet (bugs et feature requests) que des orientations de design à moyen-long terme est en train de détruire lentement mais sûrement le projet, d'autant qu'il ne reste plus un seul des fondateurs du projet dans l'équipe de développement et qu'il faut rétro-ingénier les plans de conception initiaux du logiciel à coups de `grep` dans le code. Si c'était supportable avec une équipe réduite où tout le monde se connaissait, Darktable est devenu un projet à fort trafic pendant les confinements Covid et cette façon de fonctionner n'est plus tenable avec ces effectifs.

Allez lire le code ! Comparez la branche `darktable-2.6.x` avec la `darktable-4.2.x`, fichier par fichier, vous m'en direz des nouvelles !

Tout ce que j'entends jusqu'à présent, c'est des phrases en boîte du genre « c'est comme plein d'autres projets libres » et « on n'y peut rien ». Les gens sont effrayés par le travail que représente un fork (on m'a écrit pour me dire que ça revenait à diviser la productivité), sans réaliser la quantité de ressources actuellement gaspillées par le projet Darktable et le stress permanent de devoir s'appuyer sur une base de code instable et déstabilisée trop souvent. Jusqu'à présent, Ansel m'a coûté moins de fatigue, moins de temps perdu à faire de la politique et [j'ai réglé une quantité significative de problèmes](/en/doc/special-topics/from-darktable/) dont certains étaient rapportés depuis 2016 sans signe d'intérêt de la foutue « communauté ».

Sans compter qu'Ansel a des binaires pré-compilés automatiquement chaque nuit, pour Linux (.AppImage) et pour Windows (.exe), afin de permettre de __vrais__ tests généralisés, y compris par des gens incapables de compiler du code source eux-mêmes. [J'ai demandé ça en 2019](https://github.com/darktable-org/darktable/issues/3925), mais apparemment les geeks ont mieux à faire, et il a fallu que j'y mette 70 h moi-même pour que ça arrive. L'opération est déjà un succès et a permis de régler en quelques jours des bugs Windows qui auraient traîné des semaines dans Darktable.

Côté productivité, je rappelle que la table lumineuse a été ré-écrite totalement 2 fois depuis 2018 (la dernière mouture n'est pas meilleure ni plus rapide) et le grand changement des filtres de collections introduit en [avril 2022](https://github.com/darktable-org/darktable/pull/11066) a écrasé un autre changement proposant le même type de fonctionnalité (mais avec 600 lignes à la place de 6000) introduit en [février 2022](https://github.com/darktable-org/darktable/pull/10694) (la version de février est celle disponible dans Ansel). On ne peut décemment pas parler de productivité quand le travail d'un contributeur écrase littéralement le travail précédent d'un autre dans un intervalle d'un mois, par simple faute d'une gestion de projet. On appelle ça se marcher sur les pieds.

Du coup on fait quoi pour régler le problème ? On soufre en silence ? On vit dans le déni ? On continue à régler des trucs qu'un autre cassera dans un an quand on aura de dos tourné ? On continue à faire croire aux moldus, à longueur de forums photo, que le libre c'est aussi bien que le propriétaire, tout en se gardant comme joker le fait que c'est gratuit donc t'as pas le droit de te plaindre ? C'est pas un peu facile et malhonnête, ce double discours ?

Ça vous dirait pas d'arrêter de faire passer l'habitude pour de l'expérience et le fatalisme pour de la sagesse, mais plutôt d'attaquer le problème à sa source ??? Vous ne pensez pas que vous et moi méritons mieux que du logiciel conçu par des amateurs dont le seul talent est d'avoir du temps libre et de pouvoir se permettre de bosser gratos parce qu'ils sont passés managers et que les gosses sont à la fac ?

Ou alors je me suis trompé depuis le début, et le logiciel libre, c'est donner des outils trop compliqués à des geeks qui n'en ont pas vraiment besoin, en essayant de convaincre le reste du monde que le libre n'est pas une hyper-niche pour développeur ???

## 4 ans de travail pour en arriver là

Après 4 ans à avoir bossé sur Darktable à temps plus que plein pour une paie sous 70% du salaire minimum, et 2 ans à subir l'insatisfaction chronique d'entacher mon nom en participant à faire de la merde, j'ai forké Ansel et je ne reviendrai pas en arrière.

En 4 ans, j'ai amené à ce logiciel quelque chose qui lui manquait cruellement : un workflow de retouche unifié, à base d'un ensemble de modules __conçus__ pour travailler ensemble, mais opérant chacun sur un aspect distinct, là où les modules de Darktable étaient plutôt une collection de plugins disparates. On parle de :

* filmique,
* l'égaliseur de tons,
* le module de flous physiques,
* les deux versions de la balance couleur,
* la calibration des couleurs, incluant l'interface de profilage par color checker directement en chambre noire et la balance des blancs par des méthodes standardisées par la Commission Internationale de l'Éclairage,
* le module négadoctor d'inversion des négatifs d'après Kodak Cineon,
* le module diffusion et netteté pour l'ajout et la suppression de flou basé sur la diffusion thermique,
* le mode "laplacien guidé" de reconstruction des hautes lumières.

J'ai développé également des outils plus fondamentaux qui ont servi de base aux précédents modules :

* un solveur d'équations différentielles anisotropiques du 4e ordre dans le domaine des ondelettes pour le module diffusion et netteté,
* une adaptation du précédent en laplacien guidé pour la reconstruction en RGB de signaux endommagés par propagation de gradients, pour le module reconstruction des hautes lumières,
* un modèle d'apparence des couleurs perceptuel prenant en compte l'effet Helmholtz-Kohlrausch dans le calcul de la saturation pour limiter l'effet "fluo" typique qui accompagne les resaturations intenses, pour le module balance couleur,
* un coup de main théorique dans le développement du filtre guidé invariant en exposition (EIGF), pour le module égaliseur de tons,
* un solveur d'équations vectorielles linéaires par la méthode de Choleski,
* différentes méthodes d'interpolations à l'ordre 2, 3, et radiales.

Dans l'interface graphique, j'ai notamment :

* refactorisé les déclarations de style, en les retirant les règles du code source C pour les mapper à la feuille de style CSS, permettant ainsi d'avoir des thèmes d'interface multiples et redéfinis par l'utilisateur,
* introduit le mode de prévisualisation [_focus-peaking_](https://docs.darktable.org/usermanual/4.0/en/module-reference/utility-modules/shared/focus-peaking/) et le mode d'[évaluation des couleurs ISO 12 646](https://docs.darktable.org/usermanual/4.0/en/module-reference/utility-modules/darkroom/color-assessment/),
* introduit le vocabulaire de couleur [dans la pipette de couleur globale](https://docs.darktable.org/usermanual/4.0/en/module-reference/utility-modules/darkroom/global-color-picker/), permettant d'extraire le nom de la couleur à partir de ses coordonnées chromatiques, à destination des daltoniens.

Après tout ça, j'ai écrit des dizaines de pages de documentation en deux langues, publiés des articles et des dizaines d'heures de vidéo sur YouTube pour démontrer comment utiliser les modules que j'ai développé, dans quelles circonstances et pour quel bénéfice, incluant des retouches rapides en 3 à 5 modules maximum qui permettent de venir à bout de 75 à 80 % des photos, peu importe leur plage dynamique. Dans le monde libre, à part peut-être pour des projets soutenus par des fondations (comme Krita et Blender), ce niveau de support et de documentation n'existe simplement pas, et même dans le monde commercial, ce ne sont pas les développeurs qui se chargent de ce travail.

Malgré cela, je n'ai jamais dépassé 240 donateurs, à mettre en rapport avec environ 1800 répondants uniques [ayant participé aux sondages Darktable de 2020 et 2022](https://eng.aurelienpierre.com/2023/01/who-are-the-darktable-users/#Conclusion-of-this-part), et qui déclarent dépenser en moyenne [entre 500 et 1000 €/an](https://www.poll-maker.com/S-Quiz-Results?qp=2539714x3792Bf5e-98#) pour leur photographie.

Je ne vais pas les regarder détruire l'utilisabilité de ce logiciel en essayant de me convaincre que c'est le progrès et qu'on n'y peut rien. En fait de progrès, c'est la vision délirante du progrès vu par une bande de quinquagénaires dilettantes. Depuis 2 ans, je ronge mon frein, en fermant ma gueule pour être sympa, mais en regardant la dégradation des fonctionnalités de base, complexifiées pour supporter des lubies de développeur fou, je pense que j'aurais mieux fait d'être désagréable plus tôt. Être sympa n'a rien réglé puisque la tendance, non seulement se poursuit, mais en plus s'accélère et il n'y aura pas de prise de conscience. On ne peut pas attendre de ceux qui sont à la source des problèmes de les régler.

Et quitte à travailler pour une « communauté » intéressée principalement par la gratuité du logiciel, qui a décidé que mon travail ne valait pas le salaire minimum, ça sera selon mes termes et mes standards.

En terme de fonctionnalités, Darktable a déjà beaucoup trop et il faut couper. Depuis 10 ans que je l'utilise, il a toujours été blindé de trucs mal foutus. Le challenge aujourd'hui, c'est présenter les fonctionnalités intelligemment, et régler les bugs gênants __avant__ que ces andouilles en introduisent des nouveaux, voire ne les règlent à leur manière : en cachant la poussière sous le tapis. En sachant que le pipeline graphique de Darktable a 15 ans, et qu'on ne pourra pas l'optimiser beaucoup plus que ça, d'autant qu'il a été déjà bien torturé pour éviter une réécriture complète (et qu'une réécriture complète du pipeline n'aurait pas d'avantage si on doit garder Gtk comme librairie graphique puisque c'est la principale perte de performance).

Les solutions dont Darktable a besoin impliquent de retirer du code et des options, pas d'en ajouter toujours plus. La robustesse est à ce prix. L'équipe Darktable fait exactement l'inverse et n'apprend pas de ses erreurs. Ils sont en train de se coincer eux-mêmes dans une impasse, et il sera trop tard quand il s'en rendront compte.

Avec Ansel, je veux un moyen de finir ce travail sereinement pour que les utilisateurs de Linux ait un outil fiable, cohérent et performant pour leur photographie artistique. Avant de passer à [Vkdt](https://github.com/hanatos/vkdt/) parce que le design actuel montre ses limites.

## En finir avec l'open-source toxique

Le monde du logiciel open-source est d'une remarquable hypocrisie, et Darktable en soufre comme plein d'autres projets. En perdant votre temps sur les forums de ce type (le plus emblématique étant [pixls.us](https://discuss.pixls.us)), vous découvrez assez vite que les stéréotypes libristes sont la principale cause de l'échec du logiciel libre chez les particuliers[^2] :

[^2]: À tous les gros malins qui voudraient faire croire au succès du libre en pointant le succès d'Android — dont la base est un noyau Linux —, je voudrais rappeler qu'Android est saturé de surcouches propriétaires Google. En tant qu'utilisateur d'un ROM Android dé-googlisée (/e/ OS), je suis bien placé pour savoir que quantité de services et applications ne fonctionnent pas ou pas correctement sans les surcouches Google. De plus, la nature des librairies, API, et sous-couches technologiques (libres ou pas) ne doit pas faire oublier les près de 20 ans de recherche et développement investis par une entreprise commerciale sur l'interface utilisateur, rendant l'utilisation de briques de base libres totalement anecdotique. Sans parler du fait que les pilotes matériels doivent toujours être supportés à part et que toute version d'Android n'est pas compatible avec tout téléphone Android à cause de ces soucis de pilotes.

__Le libriste de principe__
: Pour lui, un logiciel supporté par la communauté et conçu démocratiquement par comité est la chose la plus importante, même si les gens impliqués dans la conception n'ont ni expérience ni qualification dans le domaine et que le [design par comité](https://en.wikipedia.org/wiki/Design_by_committee) produit systématiquement des moutons à 3 pattes que seuls les concepteurs savent utiliser. Toute erreur fondamentale de design est juste un challenge en attente de correction par la communauté, et vos patchs correctifs sont les bienvenus®. En effet, dans le monde du libriste de principe, tout utilisateur est forcément programmeur et tout problème logiciel se résume à un problème de code (rien ne connecte l'ordinateur au monde extérieur qui nécessiterait des compétences hors programmation). Le libriste de principe n'a pas compris que [l'intelligence collective](https://fr.wikipedia.org/wiki/Intelligence_collective#Conditions_d%E2%80%99%C3%A9mergence_dans_des_groupes_humains) n'existe pas sans structure de coordination active, mais que la [paresse sociale](https://fr.wikipedia.org/wiki/Paresse_sociale) et la [pensée de groupe](https://fr.wikipedia.org/wiki/Pens%C3%A9e_de_groupe) n'ont pas besoin de conditions pour émerger. L'attente de contributions aléatoires venant de contributeurs providentiels a causé des dommages profonds à la culture de résolution de problèmes dans les projets open-source, invitant à l'absence de prise de responsabilité et au dilettantisme.

__Le radin malin__
: Fatigué de payer 12 €/mois d'abonnement à Adobe, il veut faire des économies de logiciel, quand bien même il flambe plusieurs milliers d'euros annuels en matériel photo et informatique sans aucun regret, car investir dans un capital dévaluable, c'est toujours investir, mais payer un abonnement pour un service, c'est perdre de l'argent. Il se plaindra à longueur de forum que l'ersatz libre est moins pratique et moins efficace que l'original propriétaire, mais n'investira pas un kopek dans le développement parce que c'est gratuit, point final. Il s'attend à ce que des équipes de développement de moins de 10 personnes à temps partiel, sans budget ni gestion de projet, délivrent des fonctionnalités comparables à ce que font des entreprises capitalisées à plusieurs milliards de dollars employant des cohortes de développeurs sortis des meilleures universités depuis 30 ans. Dans le pire des cas, le radin malin demandera en boucle pourquoi tout projet libre n'est pas rattaché à une fondation (pointant Krita ou Blender en exemples), sans jamais proposer ses services pour en gérer la trésorerie ni la fiscalité dans un contexte de main d'œuvre internationale travaillant à distance.

__L'évangéliste du grand public__
: Il essaiera de convertir tout le monde à sa religion libriste, en essayant de convaincre que les logiciels libres sont faciles d'utilisation car il suffit de saisir des lignes de commande cryptiques dans le bon ordre au bon endroit, impliquant d'installer des listes de dépendances dont le nom change suivant la distribution Linux utilisée, sans se rendre compte que 49 % des utilisateurs d'ordinateurs ne [savent pas comment installer un logiciel sur leur système](https://eng.aurelienpierre.com/2023/01/who-are-the-darktable-users/#Ability-to-interact-with-the-computer), même quand il s'agit seulement de télécharger un paquet exécutable. À la moindre critique sur le design, il s'offensera qu'on puisse critiquer un truc gratuit et prendra de haut les gens qui veulent juste que ça marche parce qu'ils ont autre chose à faire que travailler pour leur ordinateur. L'évangéliste est nocif au libre en terme d'image car les échanges qu'il entretient avec le grand public sont positifs uniquement lorsqu'il s'agit d'idéologie, mais deviennent défensifs voire dénégatifs dès que les problèmes pratiques sont abordés, si bien que le reste du monde en conçoit l'idée que le libre n'est fait que par des endoctrinés pour des endoctrinés du même genre.

__L'anarcho-communiste à tendance bobo rive-gauche__
: Pour lui, le logiciel libre est un bien commun qui appartient à tout le monde, et est la seule traduction concrète de l'idéologie marxiste-léniniste. Évidemment, on passera sous silence que :
	1. "tout le monde" n'a pas les droits d'écriture sur le code source,
	2. forker un projet libre, pour résoudre le problème précédent, est en fait très mal vu,
	3. le "bien commun" est utilisé (car utilisable) seulement par la frange la plus éduquée de la population,
	4. le "bien commun" est maintenu (et maintenable) seulement par une minorité de gens appartenant aux 7 % de la population mondiale sachant programmer,
	5. l'absence chronique de financement du libre implique nécessairement que seuls des riches oisifs puissent y consacrer du temps à perte — sans égard à leurs compétences.
: L'anarcho-communiste est tellement auto-centré qu'il ne réalise même plus que le libre est fait par et pour des hommes blancs riches, éduqués, d'un certain âge, et il n'a aucune solution tangible à proposer pour inclure les simples et les idiots communs à sa petite utopie théorisée depuis le fauteuil en cuir de son _country club_.

Ces stéréotypes devraient être systématiquement censurés sur les forums libristes si l'on veut qu'ils deviennent autre chose que des entre-soi confortables où l'on méprise les moldus qui font tourner Windows sur leur machine parce que ça marche.

Côté développement, le logiciel libre attire d'autres stéréotypes dont on se passerait tout autant car ils consomment du temps et de l'énergie sans rien produire en retour.

__L'éternel étudiant__
: Il aime apprendre, sans cesse un nouveau langage de programmation, sans cesse un nouveau défi, et le libre est son écosystème de choix, car on peut y passer toute une vie à apprendre sans jamais rien  livrer quoi que ce soit d'abouti. En tant qu'utilisateur, c'est une vie d'émerveillement sans cesse renouvelé qui l'attend, mais il est incapable de comprendre que d'autres ne se soucient que d'obtenir un résultat à livrer voire à vendre. En tant que contributeur, c'est un éternel stagiaire qui traite tout projet logiciel comme un navire-école, sans se soucier de la mise en production ni de l'utilisateur final. Par contre, il draine du temps et de l'énergie car il faut le former, sans certitude qu'il contribue à suffisamment long terme pour que ça rembourse l'investissement. Le problème se pose quand ce genre d'individu demande activement de l'attention en pensant apporter de la valeur au projet alors qu'il ne fait qu'épuiser les ressources sur son projet-doudou qu'il laissera à l'état de "prototype cool" jamais terminé, et dont la maintenance et la dette technique échoueront à ceux qui ont pris le temps de le former.

__Le Léonard de Vinci des années 1990__
: Typiquement programmeur ou ingénieur avec un CV impressionnant mais dans un domaine sans rapport, ayant fait sa carrière technique dans les années 1980 ou 1990 et passé au management ou retraité depuis quelques décennies, il déborde d'idées pour tout améliorer, nourries par des connaissances superficielles dans de nombreux sujets connexes, mais généralement inapplicables au projet en question. Il vous charge de prototyper ses idées en considérant que ça sera facile pour vous, sans notion de leur faisabilité ou de leur capacité à solutionner le problème identifié. Ses idées sont des rêveries techniquement irréalistes, soit parce que la théorie n'existe pas ou les contredit, soit parce que la quantité de travail nécessaire dépasse la force de travail disponible, et vous n'arriverez pas à lui faire comprendre que son expérience technique est soit périmée soit inapplicable, voire les deux. Le Léonard de Vinci est la hantise des trackers de _feature request_ parce qu'il est prolixe, inconscient de son incompétence relative au projet en question (une variante de [la maladie du Nobel](https://fr.wikipedia.org/wiki/Maladie_du_Nobel)), mais ne se contente jamais d'un "non". Il demande un temps considérable pour lire et répondre à ses messages, mais ne prendra pas le temps de lire la documentation technique que vous lui fournirez pour expliquer pourquoi ses idées ne peuvent pas marcher.

__L'obsédé de l'UI/UX__
: On peut lui accorder au moins un bon point, celui d'avoir compris que le design des logiciels open-source est immonde et borderline masochiste. Le problème de l'obsédé de l'UX, c'est qu'il résoud le problème à coups de mots clés et de pensée magique en répétant en boucle son mantra : simplifier. Mais il vous simplifierait une boîte de vitesses manuelle en enlevant la marche arrière et justifierait l'opération par le fait que les boîtes de vitesses automatiques n'ont que 4 réglages, en trouvant ça tout à fait naturel. Malheureusement, en logiciel, on travaille avec des réglages dont l'effet est moins évident que celui d'une boîte de vitesse… Il y a des discussions UI/UX légitimes à avoir dans tout projet, mais on ne peut pas les détacher des contraintes techniques internes. Or l'obsédé de l'UI/UX n'est sensible qu'à la partie cosmétique du problème, et pas au fait du fonctionnement sous le capot : invariablement, il approche les développeurs en faisant des critiques et des propositions ignorant les contraintes techniques, donc inapplicables, invariablement les développeurs l'envoient paître parce qu'il n'est ni le premier ni le dernier, ce qu'il interprète comme un désintérêt des développeurs pour l'ergonomie. Les discussions de design dans et autour des projets open-source sont donc des pertes de temps massives qui resurgissent à intervalle régulier parce que les gens font des croquis d'interface rêvée avant de se préoccuper de l'aspect fonctionnel de la tâche à accomplir par le logiciel et des liens entre l'interface graphique et la mécanique interne.

---

Tous ces caractères colorés forment le noyau dur des communautés libristes, et leur présence ne rend service à personne. Sur les forums, ils repoussent même les personnes dont le niveau informatique est insuffisant, ce qui revient à maintenir un cloisonnement efficace entre les sorciers (qu'on trouvera sur IRC et sur les forums), et les moldus (qu'on trouvera sur Facebook et Telegram, sur lesquels les sorciers ne jettent un œil que lorsqu'il y a matière à mépriser les moldus).

Or le logiciel, libre ou pas, est une fin vers un moyen et lorsque la fin est de produire des images, une communauté définie d'abord par sa capacité à exécuter des lignes de commande dans un terminal tourne rapidement à l'endogamie, ce qui ne bénéficie à personne mais tant qu'on ne connaît pas mieux…

Le design de qualité prend du temps, le code de qualité demande des compétences. Pondre des prototypes logiciels demande quelques heures par-ci par-là, transformer un prototype en un produit fini raisonnablement utilisable demande plusieurs années de design itératif, avec feedback utilisateur[^3] à chaque itération. Or le mode de fonctionnement actuel du libre, concernant les logiciels de traitement photo, fait non seulement qu'on ne sortira jamais rien d'autre que des prototypes mal foutus, mais en plus que la "communauté" actuelle des libristes n'attend finalement rien d'autre, pourvu qu'on continue de produire des jouets pour geeks excitants à intervalle déraisonnable.

[^3]: Et quand je parle de feedback utilisateur, je parle d'information traitée sur laquelle on a pris une certaine distance, pas d'un micro-trottoir où chaque témoignage a la même importance. Creuser à travers chaque retour utilisateur pour tenter de comprendre quel est le problème et où il se situe (traitement des pixels, interface graphique, concepts et documentation, manque de formation ou simplement mauvaises habitudes) prend également du temps.

On ne peut pas compter sur une telle communauté pour produire des logiciels généralement utilisables par le grand public, et je refuse de construire du logiciel de traitement photo qui sélectionne ses utilisateurs en fonction de leur niveau informatique. Le traitement d'image comporte bien assez de difficultés inévitables (liées à la physique des capteurs, aux bizarreries de la perception sensorielle humaine, et aux compromis induis par la chaîne de traitement numérique), que les logiciels propriétaires ont choisis de cacher à l'utilisateur final en retirant de la flexibilité, il est inacceptable de créer des complications informatiques par dessus et de se planquer derrière le côté "ouvert" de l'open-source pour échapper aux critiques. La seule chose réellement ouverte, dans l'open-source, c'est le code source – mais seulement à condition de savoir le lire et d'avoir le temps de le disséquer, et l'ouverture du code n'est une garantie ni de qualité ni de maintenabilité.

Le libre n'est ni une fin en soi ni excuse pour quoi que ce soit. Et la typologie de la « communauté » des libristes du traitement d'image est tout simplement toxique.
