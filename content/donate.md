---
title: Donate
date: 2025-05-28
draft: false
authors:
  - Aurélien Pierre
---

<script async
  src="https://js.stripe.com/v3/buy-button.js">
</script>

{{% row %}}
{{% card title="Stripe" icon="null fab fa-stripe" %}}
One-time donations only
<td><stripe-buy-button buy-button-id="buy_btn_1RTntjE1FFuDJgxwE9QvEx4D" publishable-key="pk_live_9NsIdgsFvOh4ryQT5YjLHydq00dJjBfyqY">
</stripe-buy-button></td>
{{% /card %}}

{{% card title="Paypal" icon="null fab fa-paypal" %}}
One-time or recurring
<form action="https://www.paypal.com/donate" method="post" target="_top">
<input type="hidden" name="hosted_button_id" value="NUDGUKGYY24HN" />
<input class="btn btn-primary" type="submit" border="0" name="submit" title="PayPal - The safer, easier way to pay online!" alt="Donate with PayPal button" value="Donate" />
<img alt="" border="0" src="https://www.paypal.com/en_FR/i/scr/pixel.gif" width="1" height="1" />
</form>
{{% /card %}}
{{% /row %}}

{{% row %}}

{{% card title="Liberapay" icon="credit-card" %}}
Liberapay uses PayPal and Stripe internally but can act as an anonymization layer if you want. Recurring only (you can stop recurrence right after the first payment).

<a class="btn btn-primary" src="https://liberapay.com/aurelienpierre/donate">Donate</a></td>
{{% /card %}}
{{% /row %}}


Ansel __is not__ a hobby project. It is a working tool designed to get job done. What is the difference ?

## Chores

Planning for long-term maintenance, stability and robustness implies doing chores, like refactoring code, simplifying the programming structure, and identifying what features need to be pruned. In addition of being tedious, these chores are often unpleasant, as they don't involve any creativity and don't produce any cool new feature that will boost marketing, but often require to understand some tangled and messy code written as someone else's Saturday project.

It's just boring responsible management, yet time-consuming. But someone needs to do it.

## Design

Design is what happens when you search for the simplest, minimalist, solution to somebody's problem. Design requires the designer to understand the problem from the human perspective, and to know the available technologies well enough to find out the most suited one.

The opposite of design is blindly "adding support for ...", which implies you cram your application with as many features as you can, until you can't maintain it anymore and you move on to the next project. This is called [feature creep](https://en.wikipedia.org/wiki/Feature_creep) and its effect on people is called [feature fatigue](https://www.jstor.org/stable/30162393). It harms both projects and people.

Here again, the task is time-consuming, in addition of requiring a special set of skills (_engineering_), that require time themselves to master (_and going to actual engineering school_). It goes way beyond the mere ability to write code, most of it actually happens before any code is written, and when properly done, it also reduces the amount of code needed, thus helping maintainability.

## Overhead

The product is never the product, the product is always the service in which the product is a key component. Delivering some software as an installable executable is not so hard. Thinking that alone brings value to people is being deluded. Providing user support in a timely manner, user education and debugging is the hardest part, as it is a recurring task and a cognitive load, but that is required so user can actually get the job done.

500 hours (and counting) have been invested into developing [Chantal AI](https://chantal.aurelienpierre.com) search engine and language model for image processing, which actually started another open-source project ([Virtual Secretary](https://github.com/aurelienpierreeng/VirtualSecretary)). Not even commercial software have dedicated AI to agregate knowledge from documentations, user forums and scientific publications, in order to improve user support.

In addition, technical and scientific reports documenting the underlying theory of software improvements in Ansel and Darktable are in open access on [Aurélien Pierre's website](https://eng.aurelienpierre.com).

## Responsible management

Ansel has:

- a developer [documentation](https://dev.ansel.photos/) to prevent contributors to avoid reverse-engineering the code and help long-term maintenance,
- automatic [camera support](./resources/supported-cameras.md) updates,
- [many other automation tools](./contribute/workflows.md) to help maintainability and debugging,
- a much reduced [code complexity](https://github.com/aurelienpierreeng/ansel#code-analysis),
- a code vs. comment ratio of 12.4 %.

All this may sound cryptic to most users. It just means the maximum was made to help stability and debugging, even for contributors who are not familiar with the code base, therefore removing the [bus factor](https://en.wikipedia.org/wiki/Bus_factor).


## You can be a part of that

The kind of individuals that have the professional skills mentionned above tend to find well-payed and stable job opportunities. If they are already practicing their skills professionally all week long, chances are they want to rest from them on the spare time.

That's _very_ bad news for open-source/libre applications because it means they are left with random contributions from amateurs, resulting in a long-known problem : open-source applications are the half-baked, lower-end alternatives to their commercial counterparts, being open somehow making it tolerable to a minority of users who value privacy over getting their job done.

__Open-source needs to pay well to attract skilled engineers, in order to produce industry-grade applications__. It's really not rocket science : people need to pay their bills first. Then perhaps work on cool stuff if they can. Not the other way around.

__By financing Ansel, you are making it possible for Aurélien Pierre to put the required time on fixing things properly and on solving your actual problems, without having to live in financial stress.__ You are also giving other engineers incentives to do the same in other projects by demonstrating it is possible.

__You are contributing to a culture of fair work retribution in open-source__, which too often rely on exploiting free labour and precariat.

You can donate through [Liberapay](https://liberapay.com/aurelienpierre/donate) or directly from here (see below).

Liberapay allows anonymous donations through Stripe, or regular donations through PayPal. Donations from here support only PayPal for now. As of 2023, both services charge very similar fees.

Thank you.

<div style="text-align: center">
<img src="https://img.shields.io/liberapay/receives/aurelienpierre.svg?logo=liberapay" style="display: inline; margin: 0 1rem 1.5rem 0!important;"><img src="https://img.shields.io/liberapay/patrons/aurelienpierre.svg?logo=liberapay" style="display: inline; margin: 0 1rem 1.5rem 0!important;"><img src="https://img.shields.io/liberapay/goal/aurelienpierre.svg?logo=liberapay" style="display: inline; margin: 0 0 1.5rem 0!important;">
</div>

_Note :_ Aurélien Pierre  has worked on Darktable since the end of 2018, being the author of the darktable UCS 22 color space, of modules like filmic, tone equalizer, color balance, diffuse & sharpen, lens blur, and of the scene-referred workflow, in addition of having refactored the GUI code, allowing for user-defined graphic theming.

Ansel was forked on Darktable 4.0 since dt's contributors lost their mind and disperse their efforts on peripheral features that are costly on every level.
