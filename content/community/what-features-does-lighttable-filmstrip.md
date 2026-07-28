---
title: "What features does lighttable/filmstrip thumbnails have ?"
date: 2023-06-10
slug: "what-features-does-lighttable-filmstrip"
tags:
  - Community archive
forum_author: "Aurélien Pierre"
forum_category: "General"
forum_url: "https://community.ansel.photos/view-discussion/what-features-does-lighttable-filmstrip"
wayback_url: "https://web.archive.org/web/20240422123145/https://community.ansel.photos/view-discussion/what-features-does-lighttable-filmstrip"
---

{{< note >}}
**Archived discussion.** This page is a verbatim copy of a thread from
`community.ansel.photos`, the Ansel community forum, which ran from March 2023
until it was taken offline in June 2025 after the site was compromised — a counterfeit
site had been planted inside the forum software, so the whole thing had to come down.

The original address was `https://community.ansel.photos/view-discussion/what-features-does-lighttable-filmstrip`.
You can check this copy against the [snapshot in the Internet Archive](https://web.archive.org/web/20240422123145/https://community.ansel.photos/view-discussion/what-features-does-lighttable-filmstrip).

Answers may refer to older versions of Ansel, and image attachments did not survive the
shutdown. Current discussion happens on
[GitHub Discussions](https://github.com/aurelienpierreeng/ansel/discussions).
{{< /note >}}

*Posted by **Aurélien Pierre** on 2023-06-10.*

I'm about to start a full rewrite of the lighttable thumbnails, which happen to be used also in the "duplicate" module (in darkroom) and in the filmstrip (bottom of darkroom, map and print views).

The reason why this rewrite is needed is it uses its own (newer and messed up) way of selecting pictures, while the selection methods from the "selection" menu (ported as-is from the former "select" module), use the original darktable way (older and cleaner). Some shortcuts are mapped to the old way, some to the new way (aka different behaviour depending how you select), and the code is so convoluted that there is no way to fix it in-place without breaking things.

Stacking thumbnails onto a square grid should not lead to complicated code. Yet it does. Beside design mistakes, the reason is many features have been hacked on top of the original ones, without the necessary cleanup steps and the view/model/controller has been messed up so everything is a view. It's only by reading the source code that you discover some well hidden features documented nowhere.

I would like you to help me list the features associated with the thumbnails, so I can flatten them before starting the redesign.

So far, I have :

- rate/reject pictures with cursor and number keys,
- fold/unfold groups of pictures (click on the icon),
- open sidecar audio memo notes (apparently it was all the rage on pro-range cameras in the 2010's),
- notify if pictures have been edited (list of history steps on hover),
- drag and drop to desktop environment copies/open files in external apps/file system,
- drag and drop inside collection reorders images (when using the "custom" sorting order),
- copy-pasting "thumbnails" actually copy-pastes development history,
- navigation with arrow keys, selection with space bar, open in darkroom with enter key,

What I want to add :

- a way to open arbitrary pictures in a pop-up window, for full-size preview and to be able to edit in darkroom with a reference image,
- an alternative text view (triggered with Alt key) overlaying EXIF info on the whole thumbnail for as long as the Alt key is held,
- sidecar text notes (raw text and Markdown) to keep track of steps and picture life cycle,
- a way to add color labels straight from the thumbnail,
- a way to zoom-in in all thumbnails at the same factor,
- a way to spot the content in zoomed-in thumbnails as to align zoomed-in pics to the same content when framing changes.

Anything else ?

## Replies

**Pedro Rodríguez** — 2023-06-10

That's it for me. Have you given any more thought to what I suggested yesterday regarding removing selection altogether and having always at least 1 pic selected?

---

**Aurélien Pierre** — 2023-06-10

The selection needs to be kept, but we don't need to force a dummy selection either.

See how it's done in the darkroom modules, when you hit page up/down: if no module is selected, page down inits a new selection from the first element, or page up inits a new selection from the last element, otherwise we start from the selected element.

But anyway, that's already lower level than what I want here (what it should do, before how it should do it).

---

**Steve** — 2023-06-10

Personally I do not like or use the import in LightTable. I see no benefit to having all the raw files in a folder imported into Ansel.

I think Ansel should just have a very simple browser that does not import files into Ansel. One can fly through all RAW files quickly and click to import.

I had tried for years to use the Import and just hate it.

Now my workflow is very smooth and quick. (I have the Nikon .NEF file properties associated to Ansel)

My Nikon workflow is...

1 - Open Windows File Explorer on 2nd monitor

2 - Open Nikon NX Studio on main display

3 - Rate all keepers in full screen preview in Nikon NX Studio

4 - Click on any keeper in Windows File Explorer and it imports the file into Ansel

This way I only have the keepers imported.

I would love to see a very simple file browsing ability built into Ansel prior to actual import. One could view/click to import at full screen preview. Once the keeper is importer, then do all that is further needed in LightTable/DarkTable. I know the 'add to library' has the thumbnail view but it it would be a much better UI if the 'add to library' was actually a file preview/browser that could be maximized to full screen with the preview becoming the main object making up 95% of the screen with the ability to zoom into picture at 100% to check for focus etc. and then click on the 'add to library' button to import. Or better still, add a check box to each file and one can go through all the files and click the check box for the keepers and then click the 'add to library' button. Once the 'add to library button has been clicked, the 'add to library' window should not close, there should be a dedicated close button.

---

**ariznaf** — 2023-06-12

All your proposals sound good to me, but I would need to see it working in order to know how it works, as I don't fully understand some of the descriptions.

Being able to change easily from one photo to another while in darktable would be of help.

Rignt now, using arrow keys to change the photo you are developing seems not to work, and using the mouse you have to double click in the photo over the thumbnail in the filmstrip to activate it, a single click would be mor intuitive for me.

In darkroom the filmstrip seems to show only the photos that are in the lightroom if there is some filter activated.

Then if you want to see more photos (like change from 4 stars to 3 stars) you need to go back to ligtroom.

Being able to change filters from wihin darktable would be great.

Right now only stars and a few more info is shown in the thumbnails.

I think there is plenty room to show more info.

And when you change selected photo, showing some info as an overlay for a few seconds would be great (info not in thumnail, like name, camera model, aperture, etc, as I told other time lightroom does a good job in that).

  

Changing stars and color selection does not work consistently.

Color selection cannont be changed inside the thumbnail, it is in the botton of the interface, whil stars are shown in the thumnail and can be changed from there (which is great, being able to do so with color selection would be great).

You cannot assign 0 stars (no stars) to the photos using the mouse, you have to use the keyboad, while you can assin no color selection to a photo using the mouse (a similar option to stars would be great).

Finally, there is an interface option in ligtroom that let you assign meaningfull name to color selections, instead of just purple or red.

Everybody uses that colors for different things, assigning a name for the color (just as an interface option than maps each color to a name that is displayed instead, nothing to be saved with each photo) is more readable and let you remember the use you had assigned to each color (people like me that can be some months without using the camera tend to forget their own conventions).

For now is all I can think of about photo management.

---

**migmoq** — 2023-06-12

For me photo management and the editing should be done in Lightable and not in darkroom. So staring has to be done in the Lightroom and not in the Darkroom. Each room have their own aim/functionality. The aim of the lightroom is for the collection management and, more important, for the editing. Editing shouldn't be done in the darkroom. As well as the filtering of the images to process as they have to be done in the Lightroom (it's one of its goal). And thankfully only the filtered images are accessible in the darkroom through the filmstrip! Without it, it would be a discrepancy to pass easily to one image to other one for their processing.

+1 to naming colors.

---

**ariznaf** — 2023-06-12

I support se you are refering to metadata editing.

But indeed it is done in darkroom as you can change many metadata there, asong as developing photos.

  

Being able to access and change the filter selection from darktable is not editing just s quick way to broaden or narrow the criteria without having to go back and forth between lightable and darkroom.

  

If you don't need it it is as easy as not using the filter accessible from darkroom.

But if I wan't to bride the criteria from 4 stars to 3 stars or just decided to narrow it to photos taken with the 16 mm for a moment I don't see the what can hurt a quick access to the filter criteria from darkroom instead of having to go to kightabke to change it then to darkroom to make a few changes and back to lightable to again set the criteria an.back to darkroom to continue developing.

---

**migmoq** — 2023-06-12

No, I refer to the editing process, id est the process in which is done a selection of images to keep for a peculiar project or series. In this case, generally stars are used, and in my case, each step of the process (that is usually performed in different days) a star is added until there is no more images to eliminate (I keep only the images with the more stars). Other users prefer to use colors for this process or a combination of colors and stars. Others ones use tags or collections instead in this process.

Nevertheless, after thinking a little more about you have written, I understand the need to fix the starring of one or more images when in the darkroom. Indeed, stars can be also used other than for the editing. And indeed, this can be an interesting feature. For me, it is more the filtering of the images directly in the darkroom that hurts me as the darkroom isn't done for that and I fear an additional complexity of code and of UI.

The lightroom/darkroom in Ansel/Darktable is a metaphor coming from the analog images development and printing: the lightroom is the place you are both managing your archives of images and filtering the ones you want to work on for a given project or a series. You want all of your images taken in 16mm? Do it in the lightroom and then keep some of them according to your own criteria. Then in the darkroom just process the images you have kept. If suddenly you want to change the filtering in the darkroom, then I think you are using the darkroom for a bad purpose; you aren't used it just to develop your images but both to do the editing and the processing intertwined.

---

**ariznaf** — 2023-06-12

I haven't talk about stating in darkroom, just having easy access to the filter that lets you select the photos that are shown in the filmstrip and not havi g to go back an forth from lighttable. Classification has been previously made in light table but filtering is about selecting the photos you are going to work with and you usually need to broaden or narrow that selection when working with them.

  

If you prefer go back to light able you always can do that instead of accessing the filtering criteria from the darkroom.

---

**Steve** — 2023-06-12

I would like to see a number rating 0 to 9 added

I would like to see a alfa rating a - z

I would like to see the number of stars increased to 9

and perhaps the number of colors increased

I shoot live music and I find the need to define band/member/rating/misc. As in a music festival there may be 12 bands that perform, each have band members, each member photo needs to be rated, there are also misc photos that include audience, backstage etc that need to be separated from the artists.

I would love to be able to apply all those ratings prior to an actual import into Ansel. Probably a very big job to do but as I mentioned in other posts, I really see the need for a simple file browser prior to import.

---

**ariznaf** — 2023-06-12

I think 5 stars and colours are standard, they are standardized in the metadata and CMP specifications, I believe.

---

**Lukas** — 2023-06-13

Hey Steve,

whenever I need to get to that level of detail in filtering, I use tags to be able to show only images containing on particular person for example.

Regarding your other request to have a file browser inside the import dialoge I don't really see the need. At the moment you can either do your culling and rating before import in other software as you describe with Nikon NX Studio (or other options from what I have gathered in "I don't use Lighttable at all"-discussions) or do it after the import with the help of Ansel's Lighttable (once it's rework is done that is). Why add a third option that lives "in between"?

---

**Aurélien Pierre** — 2023-06-13

Import workflow is outside the scope of the current discussion. Ansel needs some sort of file browsing of collections with thumbnails. Having to rely on external apps to select keepers is a no-go.

---

**Aurélien Pierre** — 2023-06-13

Rating has to be between 0 and 5 as per XMP specs (https://developer.adobe.com/xmp/docs/XMPNamespaces/xmp/).

Defining band/member/music should be done with tags (already feasible, tags are hiearchical and can be retrieved as collections).

Anything more relying on text shall be done in text sidecar files.

---

**Steve** — 2023-06-16

> ... the 'add to library' has the thumbnail view but it it would be a much better UI if the 'add to library' was actually a file preview/browser that could be maximized to full screen with the preview becoming the main object making up 95% of the screen with the ability to zoom into picture at 100% to check for focus etc. and then click on the 'add to library' button to import. Or better still, add a check box to each file and one can go through all the files and click the check box for the keepers and then click the 'add to library' button.

---

**migmoq** — 2023-06-17

One thing I wish to have restored in the lighttable: the current number of images that are displayed. This is a meaningful information for me during the editing in a way I wish to know to how number of photos I reduced a given collection of images (according the goal of those photos: web site, book, zine, ...)

---

**Balistic** — 2023-06-17

You have a special workflow using other softwares in addition to Ansel (Nikkon NX Studio). It is your choice, so it is your responsability to fit Nikkon Studio with Ansel, not the responsability of Aurélien Pierre to bend Ansel to fit your OWN workflow.

I personnaly use Digikam with Darktable/Ansel. I made my own adaptations to get the two working together, I did not ask A.P to do it for me.

If you wanna use a "Raw converter" with a simple file preview/browser, there is ART/Rawtherapee which already do that.

If you want to use Ansel with a file explorer, you can use Windows/Linux files explorer and right clic "Open with Ansel" to open and import immediately your picture with Ansel. If the picture was already imported in Ansel, it will just open it. You do not need to start Ansel and then "Import".

The Import function of Ansel is essential : this is the way Ansel get the medatada of the pictures and is able to perform quick search in his own library. Lightroom and a lot of other Raw softwares have the SAME behaviour. You can not expect a software to be able to perform quick search based on metadata and at the same time be a simple file browser with no library database.

---

**cyberspeck** — 2023-06-17

I'd love to be able to switch the group leader from RAW to JPG for all selected images with one click (or shortcut). Sony ARWs only have a very small built-in jpg preview that is too small to be used when comparing only 2 images on the screen. Then Ansel starts building thumbnails based on the RAW file and that takes too long to allow reasonably quick culling. There is a lua script that allows that, but lua seems do not work with Ansel.

---

**Benoit de Maistre** — 2023-07-17

The list under "So far, I have :" is already quite good, but I have a few comments/questions that arise :

If I understand correctly the same logic will apply also to the darkroom thumbnail strip ? This will really help to rationalise and streamline the process if this is the case !

I have years of use of Bibblelabs and then Aftershot (on old version no more supported), and in this software the view is shared between thumbnail and development panel with the thumbnail taking the available space : either none (development panel takes the full panel), or one line or one column of thumbnails or the full central panel filled with a grid of thumbnail, without changing the functions or shortcuts of each part. The rating, color, tags can then be modified without a change of mode also changing the way to do it.

grouping ungrouping is there in Ansel but I did not see a visual clue of the groups in the lightable without hovering on the groups, is there a way to have the line around all groups ?

also the logic of sorting and grouping can have some strange interactions (when the sorting is changed, it is now breaking the groups on the lightable, the group is still here when switching back to personalised sorting). One way to handle this is to force the group to stick together and follow the sorting according to the group leader only (seems better than breaking the group but if implemented it has other side effects : if you then change the group leader and the new group leader is sorted at another place, then either the whole group has to jump at that other place and seems to diseapear or you have to trigger a scrolling of the full lightable around the new group place ... )

For the pop up window, may be it is easy enough to have a quick export to a default easy to remember folder (for exemple the system default picture folder) and open the picture with the system default picture viewer from there ?

A key adding Exif text information when pressed is usefull, with also the filename if possible ? But how so much info will be able to fit onto a small thumbnail ?

I use sometime the zoom in several picture at the same time in my old no more supported Aftershot, but it is easy to use as you only need to select several pictures in the thumbnail strip (using the same keys ou mouse inputs than on the full thumbnail view), and then Aftershot split its main panel in up to six pictures, with the normal zoom and panning shortcuts either acting on the last selected clicked picture or acting on all pictures at the same time if you press an additionnal button locking synchronised zoom and pan. However I am not sure how this can be implemented in Ansel where the darkroom mode is so independent from the lightable mode.

---

**Pedro Rodríguez** — 2023-11-12

Just a couple of thoughts on this issue that I'm really looking forward to having solved.

The image grid serves two main purposes as far as i can tell:

\- Navigation: to open a particular picture for development, or to take an action on a picture or group of pictures.

\- Culling: to select which pictures are worth keeping and processing.

For navigation I'd say you generally need a smaller magnification, and the current system of arrow keys to move around, spacebar for selection, etc. Works ok.

For culling it is a pain. The best scenario for me for this workflow would be right arrow + number to rate pictures (or "r" to reject). This way you can fly through this boring task without ever lifting your fingers from two keys. It would also be helpful to be able to have a higher magnification to see one picture at a time at a larger size to check focus without opening the image, while you can keep track of upcoming images on the film strip.

Also, and I know we have talked about it, but I still think that jpeg previews are the safest option for people with not very powerful computers. You'd still get complaints that the starting point doesn't look like the jpeg, but that's way better than complaints for having computers freeze trying to generate previews.

---

**Lukas** — 2024-05-13

> navigation with arrow keys, selection with space bar, open in darkroom with enter key

Why do we need to press spacebar?

> For culling it is a pain. The best scenario for me for this workflow would be right arrow + number to rate pictures (or "r" to reject). This way you can fly through this boring task without ever lifting your fingers from two keys.

This sums it up for me

