---
title: Coding style
date: 2024-07-14
weight: 5
---

## Values

### Users should not have to read the manual

_(Some restrictions apply)_

Image processing is hard. It uses notions of optics and color "science". No matter if you shoot digital or analog, _illuminant_, _dynamic range_, _gamut_ and _chroma_ will affect your process, in ways you may not have foreseen, and it might be a good idea to understand what they mean and where they come at play. Digital has its own lot of issues, from _color spaces & management_ to _alpha compositing_. Not much we can do here, except providing documentation : you need the skills. But that is, at least, the core of what we do.

Managing files and navigating in a graphical interface are things computer users have been doing for decades, using well-known paradigms that converged to pretty unified semantics. Users should not have to read a manual to discover why mouse scrolling is blocked, for example, or how to increase the opacity of a mask, or even what all those silly custom-drawn icons mean.

Users should not have to read the manual because, anyway, they won't. Instead, they will annoy developers with questions already answered somewhere on the extensive docs, which are too long to read because they have to explain why too much standard stuff is not handled in a standard way.

Acknowleging that, bad design loses the time of both users and developers, and it's time to cut the losses, for everybody's sake.

### If it ain't broken, don't fix it

Too much of Darktable "design" has started with "it would be cool if we could ...". I'll tell you what's cool : hanging good pictures of yours on your walls ASAP. Visual arts are not performing art (like music or theater), so only the result matters. Everything that comes before is overhead, and you typically want to keep it minimal. That's not to say that the process can't be enjoyed in itself. However, to enjoy the process, you need to master your tools and to bend them to __your__ will, otherwise you only fight them and the whole process amounts to frustration. Problem is, Darktable "design" puts too much effort into being different for the sake of it.

In this process of adding "cool new stuff", Darktable has broken keyboard shortcuts and a lot of basic GUI behaviours, replacing clean code with spaghetti and adding more GUI clutter without ever pruning stuff.

__Ansel__ has an [explicit](./design.md) design process that mandatorily starts with defined problems met by defined users. Turns out the quantity of code to write is inversely proportionnal to the amount of thinking you have done on your solution, typically to spot the root problem out of what users tell you, and find the simplest path to solution (which is often not even a software solution...).

But bugs don't wait for you in the thinking, they wait only in the code you wrote. So, the more you think, the less you code, the less maintainance burden you create for yourself in the future. But of course... you need to have enough time to think things through. Essentially, that means bye bye to Saturday-afternoon, amateur-driven hacking !

### Don't extend it if you can't simplify it first

A lot of Darktable hacking has been done by copy-pasting code, from other parts of the software, or even from other projects, mostly because contributors don't have time nor skills to undertake large rewrites. This triggers code duplication and increases the length of functions, adding internal branching and introducing `if` and `switch case` nested sometimes on more than 4 levels, making the structure and logic more difficult to grasp and bugs more difficult (and frustrating) to chase, while being more likely to happen.

In any case, when the code responsible for existing features is only growing (sometimes by a factor 10 over 4 years), it raises serious questions regarding future maintainablity, in a context where contributors stick around for no more than a couple of years, and developers have a limited time to invest. It's simply irresponsible, as it sacrifices long-term maintainability for shiny new things.

Simplifying and generalizing code, through clean APIs, before adding new features is a must and Ansel only accepts code I personaly understand and have the skills to maintain. KISS.

## Basic coding logic

Pull requests that don't match the minimum code quality requirements will not be accepted. These requirements aim at ensuring long-term maintainability and stability by enforcing clear, legible code structured with a simple logic.

1. Procedures need to be broken into unit, reusable functions, whenever possible. Exception to this are specialized linear procedures (no branching) doing tasks too specific to be reused anywhere, but in this case use comments to break down the procedures in "chapters" or steps that can be easily spotted and understood.
2. Functions should achieve only one task at a time. For example, GUI code should not be mixed with SQL or pixel-processing code. Getters and setters should be different functions.
3. Functions should have only one entry and one exit point (`return`). The only exceptions accepted are an early return if the memory buffer on which the function is supposed to operate is not initialized or if a thread mutex lock is already captured.
4. Functions should have legible, explicit names and arguments name that advertise their purpose. Programs are meant to be read by humans, if you code for the machine, do it in binary.
5. Functions may only nest up to 2 `if` conditional structures. If more than 2 nested `if` are needed, the structure of your code needs to be reevaluated and probably broken down into more granular functions.
6. `if` should only test uniform cases like the state or the value of ideally one (but maybe more) variable(s) of the same type. If non-uniform cases need to be tested (like `IF user param IS value AND picture buffer IS initialized AND picture IS raw AND picture HAS embedded color profile AND color profile coeff[0] IS NOT NaN`), they should be deferred to a checking function returning a `gboolean` `TRUE` or `FALSE` and named properly so fellow developers understand the purpose of the check without ambiguity on cursory code reading, like `color_matrix_should_apply()`. The branching code will then be `if(color_matrix_should_apply()) pix_out = dot_product(pix_in, matrix);`
7. Comments should mention why you did what you did, like your base assumptions, your reasons and any academic or doc reference you used as a base (DOI and URLs should be there). Your code should tell what you did explicitly. If you find yourself having to explain what your code is doing in comments, usually it's a sign that your code is badly structured, variables and functions are ill-named, etc.
8. Quick workarounds that hide issues instead of tackling them at their root will not be accepted. If you are interested in those, you might consider contributing to upstream darktable instead. The only exceptions will be if the issues are blocking (make the soft crash) and no better solution has been found after some decent amount of time spent researching.
9. Always remember that the best code is the most simple. KISS. To achieve this goal, it's usually better to write code from scratch rather than to try mix-and-matching bits of existing code through heavy copy-pasting.

In an ideal world, any PR would follow [design patterns best practices](https://en.wikipedia.org/wiki/Software_design_pattern).

Some random pieces of wisdom from the internet :

{{< quote author="Brian W. Kernighan" class="full-width ps-0 ms-0 my-2" >}}
Everyone knows that debugging is twice as hard as writing a program in the first place. So if you're as clever as you can be when you write it, how will you ever debug it?
{{< / quote >}}

{{< quote author="Martin Fowler, Refactoring: Improving the Design of Existing Code" class="full-width ps-0 ms-0 my-2" >}}
Any fool can write code that a computer can understand. Good programmers write code that humans can understand.
{{< /quote >}}

{{< quote author="John Woods" class="full-width ps-0 ms-0 my-2" >}}
Always code as if the guy who ends up maintaining your code will be a violent psychopath who knows where you live.
{{< /quote >}}

{{< quote author="Martin Fowler, Refactoring: Improving the Design of Existing Code" class="full-width ps-0 ms-0 my-2" >}}
Whenever I have to think to understand what the code is doing, I ask myself if I can refactor the code to make that understanding more immediately apparent.
{{< /quote >}}

{{< quote author="[Rich Skrenta](http://www.skrenta.com/2007/05/code_is_our_enemy.html)"  class="full-width ps-0 ms-0 my-2" >}}
<div class="mb-3">
Code is bad. It rots. It requires periodic maintenance. It has bugs that need to be found. New features mean old code has to be adapted. The more code you have, the more places there are for bugs to hide. The longer checkouts or compiles take. The longer it takes a new employee to make sense of your system. If you have to refactor there’s more stuff to move around.
</div>
<div>
Code is produced by engineers. To make more code requires more engineers. Engineers have n^2 communication costs, and all that code they add to the system, while expanding its capability, also increases a whole basket of costs. You should do whatever possible to increase the productivity of individual programmers in terms of the expressive power of the code they write. Less code to do the same thing (and possibly better). Less programmers to hire. Less organizational communication costs.
</div>
{{< /quote >}}

{{< quote author="[John Byrd](https://www.quora.com/profile/John-Byrd-2)" class="full-width ps-0 ms-0 my-2" >}}
Good programmers write good code. Great programmers write no code. Zen programmers delete code.
{{< /quote >}}

<div class="clearfix"></div>

## Specific C coding logic

Ansel as well as darktable are written in C. This language is meant for advanced programmers to write fast bugs in OS and system-level applications. It gives too much freedom to do harmful things and can't be debugged before running the program, or writing your own tests (which can be bugged themselves, or can bias the kind of bugs they let through, and anyway, nobody writes tests). Yet most contributors are not trained for C, many of them are not even professional programmers (though professional C programmers should probably not be let anywhere nead end-user applications), so C is a dangerous language for any open source app.

C will let you write in buffers that have not been allocated (resulting in `segfault` error) and will let you free them more than once, but will not free buffers when they are not needed anymore (resulting in memory leaks if you forgot to do it manually). Problem is, since buffer alloc/free may be far away (in the program lifetime as in the source code) from where you use them, it's easy to mess that up. C will also let you cast any pointer to any data type, which enables many programmer mistakes and data corruption. The native string handling methods are not safe _(for reasons I never bothered to understand)_, so we have to use the GLib ones to prevent security exploits.

Basically, C makes you your own and worst enemy, and it's on you to observe safety rules which wisdom will become clear only once you break them. Much like the bugs in a C program. Consider that you write your code to be read by dummies who never programmed in C before.

You also need to keep in mind that the compiler will do most optimizations for you, but will be super conservative about them. The rule of thumb is, if your code is easily understandable by an human (simple logic), it will be properly understood by the compiler, which will take the appropriate optimization measures. The other way around, manual optimizations in the code, that yield cryptic code assumed to be faster on single-threaded systems, usually backfires and yields slower programs after compilation.

### Patterns and structures

1. `for` loops are reserved for iterating over arrays of size known beforehand, so the number of looping steps is known. Stretching that logic, they can also be used to iterate over `GList *` items (which have no size property since they are dynamically allocated), although this checks if each item `(GList *)->next` is not `NULL`. `for` loops should generally not use `break` or `return` statements inside their control flow, unless the loop is looking for a specific item inside the array and returns is as soon as it is found. If your loop has a stopping condition, use `while`.
2. C is not an object-oriented language, but you can and should use OO logic when relevant in C by using structures to store data and pointers to methods, then uniform [getters and setters](https://en.wikibooks.org/wiki/Object_Oriented_Programming/Getters_and_Setters) to define and access the data.
2. structures like `while`, `for`, `if`, or `switch` should not be nested over more than 3 (and preferably 2) levels. Use functions if that happens :
    ```C
    // Bad
    void stuff(float *array, char *output)
    {
      if(condition)
      {
        for(int i = 0; i < 5; i++)
        {
          if(array[i] > 1.f)
            array[i] = ...
        }
        output = "true";
      }
      else
      {
        ...
      }
    }

    // Good
    char *_process(float *array)
    {
      for(int i = 0; i < 5; i++)
      {
        if(array[i] > 1.f)
          array[i] = ...
      }
      return "true";
    }
    void stuff(float *array, char *output)
    {
      if(condition)
      {
        output = _process(array);
      }
      else
      {
        output = _something_else(array);
      }
    }

    ```
3. Long sequequences of checks should be put in function returning `gboolean` clearly stating what we are checking, so in procedures, we get:
    ```C
    gboolean _is_raw(dt_image_t *image)
    {
      return (image->flag & DT_RAW == DT_RAW) &&
             (image->buffer != NULL) &&
             strcmp(image->ext, "dng");
    }

    void stuff(dt_image_t *image)
    {
      if(_is_raw(image))
        ...
      else if(_is_raster(image))
        ...
    }
    ```
    instead of
    ```C
    if((image->flag & DT_RAW == DT_RAW) && (image->buffer != NULL) && strcmp(image->ext, "dng"))
      ...
    else if(...)
      ...
    ```

3. Always access data from buffers using the array-like syntax, from their base pointer, instead of using non-constant pointers on which you perform arithmetic. For example, do:
    ```C
    float *const buffer = malloc(64 * sizeof(float));
    for(int i = 0; i < 64; i++)
    {
      buffer[i] = ...
    }
    ```
    Do not do:
    ```C
    float *buffer = malloc(64 * sizeof(float));
    for(int i = 0; i < 64; i++)
    {
      *buffer++ = ...
    }
    ```
    The latter version is not only less clear to read, but will prevent parallelization and compiler optimizations because the value of the pointer depends on the loop iteration and would need to be shared between threads if any. The former version leads to a memory access logic independent from the loop iteration and can be safely parallelized.
4. The use of inline variable increments (see a [nightmare example here](https://www.youtube.com/watch?v=_7Wok3JoOcE)) is strictly forbidden, unless it's the only operation of the line. These are a mess making for many programming errors. This is permitted :
    ```C
    uint32_t counter;
    for(int i = 0; i < 64; i++)
    {
      if(array[i] > threshold)
        counter++;
    }
    ```
5. The `case` statements in the `switch` structure should not be additive. Do not do:
    ```C
    int tmp = 0;
    switch(var)
    {
      case VALUE1:
      case VALUE2:
        tmp += 1;
      case VALUE3:
        do_something(tmp);
        break;
      case VALUE4:
        do_something_else();
        break;
    }
    ```
    On cursory reading, it will not be immediately clear that the `VALUE3` case inherits the clauses defined by the previous cases, especially in situations where there are more cases. Do:
    ```C
    int tmp = 0;
    switch(var)
    {
      case VALUE1:
      case VALUE2:
        do_something(tmp + 1);
        break;
      case VALUE3:
        do_something(tmp);
        break;
      case VALUE4:
        do_something_else();
        break;
    }
    ```
    Each case is self-enclosed and the outcome does not depends on the order of declaration of the cases.

7. Sort and store your variables into structures that you pass as function arguments instead of using function with more than 8 arguments. Do not do:
    ```C
    void function(float value, gboolean is_green, gboolean is_big, gboolean has_hair, int width, int height, ...)
    {
      ...
    }

    void main()
    {
      if(condition1)
        function(3.f, TRUE, FALSE, TRUE, 80, 90, ...);
      else if(condition2)
        function(3.f, FALSE, TRUE, TRUE, 80, 90, ...);
      else
        function(3.f, FALSE, FALSE, FALSE, 110, 90, ...);
    }
    ```
    Do:
    ```C
    typedef struct params_t
    {
      gboolean is_green;
      gboolean is_big;
      gboolean has_hair;
      int width;
      int height;
    } params_t;

    void function(float value, params_t p)
    {
      ...
    }

    void main()
    {
      params_t p = { .is_green = (condition1),
                    .is_big = (condition2),
                    .has_hair = (condition1 || condition2),
                    .width =  (condition1 || condition2) ? 80 : 110,}
                    .height = 90 };
      function(3.0f, p);
    }
    ```
    The former example is taken from [darktable](https://github.com/darktable-org/darktable/blob/master/src/bauhaus/bauhaus.c#L2210-L2251). The copy-pasting of the function calls is unnecessary and the multiplication of positional arguments makes it impossible to remember which is which. It also doesn't show what arguments are constant over the different branches, which will make refactoring difficult. The latter example is not more concise, however the structure not only makes the function easier to call, but the structure declaration allows to explicitly set each argument, with inline checks if needed. The dependence of the input arguments upon the external conditions is also made immediately clear, and the boolean arguments are directly set from the conditions, which will make the program easier to extend in the future and less prone to programming error due to misunderstandings in the variables dependence.

### OpenMP optimisations

Pixels are essentially 4D RGBA vectors. Since 2004, processors have special abilities to process vectors and apply Single Instructions on Multiple Data (SIMD). This allows us to speed-up the computations by processing an entire pixel (SSE2) up to 4 pixels (AVX-512) at the same time, saving a lot of CPU cycles.

Modern compilers have auto-vectorization options that can optimize pure C, and the OpenMP library allows to provide hints to improve that, provided the code is written in a vectorizable way and uses some pragmas are used.

Write vectorizable code : https://info.ornl.gov/sites/publications/files/Pub69214.pdf

Best practices for auto-vectorization:

* avoid branches in loops that change the control flow. Use inline statements like `absolute = (x > 0) ? x : -x;` so they can be converted to bytes masks in SIMD,
* pixels should only be referenced from the base pointer of their array and the indices of the loops, such that you can predict what memory address is accessed only from the loop index,
* avoid carrying `struct` arguments in functions called in OpenMP loops, and unpack the `struct` members before the loop. Vectorization can't be performed on structures, but only on `float` and `int` scalars and arrays. For example:
    ```lang-C
    typedef struct iop_data_t
    {
      float[4] pixel;
      float factor;
    } iop_data_t;

    float foo(float x, struct iop_data_t *bar)
    {
      return bar->factor * (x + bar->pixel[0] + bar->pixel[1] + bar->pixel[2] + bar->pixel[3]);
    }

    void loop(const float *in, float *out, const size_t width, const size_t height, const struct iop_data_t bar)
    {
      for(size_t k = 0; k < height * width; ++k)
      {
        out[k] = foo(in[k], bar);
        // the non-vectorized function will be called at each iteration (expensive)
      }
    }
    ```
    should be written:
    ```lang-C
    typedef struct iop_data_t
    {
      float[4] pixel DT_ALIGNED_PIXEL; // align on 16-bits addresses
      float factor;
    } iop_data_t;

    #ifdef _OPENMP
    #pragma declare simd
    #endif
    /* declare the function vectorizable and inline it to avoid calls from within the loop */
    inline float foo(const float x, const float pixel[4], const float factor)
    {
      float sum = x;

      /* use a SIMD reduction to vectorize the sum */
      #ifdef _OPENMP
      #pragma omp simd aligned(pixel:16) reduction(+:sum)
      #endif
      for(size_t k = 0; k < 4; ++k)
        sum += pixel[k];

      return factor * sum;
    }

    void loop(const float *const restrict in,
              float *const restrict out,
              const size_t width, const size_t height,
              const struct iop_data_t bar)
    {
      /* unpack the struct members */
      const float *const restrict pixel = bar->pixel;
      const float factor = bar-> factor;

      #ifdef _OPENMP
      #pragma omp parallel for simd default(none) \
      dt_omp_firstprivate(in, out, pixel, factor, width, height) \
      schedule(simd:static) aligned(in, out:64)
      #endif
      for(size_t k = 0; k < height * width; ++k)
      {
        out[k] = foo(in[k], pixel, factor);
      }
    }
    ```
* if you use nested loops (e.g. loop on the width and height of the array), declare the pixel pointers in the innermost loop and use `collapse(2)` in the OpenMP pragma so the compiler will be able to optimize the cache/memory use and split the loop more evenly between the different threads,
* use flat indexing of arrays whenever possible (`for(size_t k = 0 ; k < ch * width * height ; k += ch)`) instead of nested width/height/channels loops,
* use the `restrict` keyword on image/pixels pointers to avoid aliasing and avoid inplace operations on pixels (`*out` must always be different from `*in`) so you don't trigger variable dependencies between threads
* align arrays on 64 bytes and pixels on 16 bytes blocks so the memory is contiguous and the CPU can load full cache lines (and avoid segfaults),
* write small functions and optimize locally (one loop/function), using OpenMP and/or compiler pragmas,
* keep your code stupid simple, systematic and avoid smart-ass pointer arithmetic because it will only lead the compiler to detect variable dependencies and pointer aliasing where there are none,
* avoid types casts in loop,
* declare input/output pointers as `*const` and variables as `const` to avoid false-sharing in parallel loops (using  `shared(variable)` OpenMP pragma).

### Code formatting

- Use spaces instead of tabs,
- Indentation uses 2 spaces,
- Remove trailing spaces,
- `{` and `}` go to their own line,

## Guidelines

1. **Do things you master** : yes, it's nice to learn new things, but Ansel is not a sandbox, it's a production software, and it's not the right place to get your training.
2. **KISS and be lazy** : Ansel doesn't have 50 devs full-time on deck, being minimalistic both in features and in volume of code is reasonable and sane for current management, but also for future maintenance. *(KISS: keep it stupid simple)*.
3. **Do like the rest of the world** : sure, if everybody is jumping out of the window, you have a right to not follow them, but most issues about software UI/UX have already been solved somewhere and in most cases, it makes sense to simply reuse those solutions, because most users will be familiar with them already.
5. **Programming is not the goal** : programming is a mean to an end, the end is to be able to process large volume of pictures in a short amount of time while reaching the desired look on each picture. Programming tasks are to be considered overhead and should be kept minimal, and the volume of code is a liability for any project.
