+++
title = "What I've Learned from 3000 Lines of Elm"
date = 2019-04-13T16:35:55-06:00
draft = false
markup = "mmark"
+++

I have been spending a lot of time lately working on a side project for learning and teaching music theory. The app combines short video tutorials followed by music theory exercises. Like Khan Academy combined with Duo Lingo.

I needed several things in place before I could write an application around music theory. I needed a music **theory engine**. The engine would allow me to ask things like, "Given a note what is the note a Major 6th above?"

I also needed a **rendering engine**. There are several other projects that render music in the browser, like [VexFlow](http://www.vexflow.com/). I needed a small package that would only do a limited number of things. I did not need to render a whole sheet of music to the browser. I only needed some intervals, chords, key signatures and such. Since SVG is now [widely supported](https://caniuse.com/#search=svg) I wanted something lean that would render SVG only. Elm's SVG package was a perfect fit.

Once those 2 things were in place I could do something like the following:

{{< embedElm src="/js/seventh_flashcards.min.js" >}}

## Why I Chose Elm

I had dabbled into Elm before starting this project. With the release of Elm 0.19, I decided to try to write something substantial in Elm. I wanted to write a single page application (SPA) and needed front end routing. I got confused with routing in Elm 0.18 but with Elm 0.19 the routing module seemed easier to use.

I started with the **theory engine**. Throughout the whole process, I wrote unit tests with Elm Test. When I finished I had something that just worked. I wrote the engine several months ago and have not had to touch the core logic since. Drawing inspiration from [Making Impossible States Impossible](https://youtu.be/IcgmSRJHu_8) I modeled everything in Types. Coming from imperative languages this was a new thing for me. My Note looked like the following:

```Elm
type alias Note =
    { name : NoteName, octave : Int, accidental : Accidental }

type NoteName
    = C
    | D
    | E
    | F
    | G
    | A
    | B

type Accidental
    = DoubleSharp
    | Sharp
    | Natural
    | None
    | Flat
    | DoubleFlat
```

In the render engine I can use case matching to provide a rendering for the accidentals:

```Elm
renderAccidental : Accidental -> Svg msg
renderAccidental accidental =
    case accidental of
        DoubleSharp ->
            svg [...] [...]
        
        Sharp ->
            svg [...] [...]
        
        ...
```

Several years ago I had forked a previous Python project [Mingus](https://github.com/bspaans/python-mingus). I had augmented the project to use theory in a more semantic way. For example, in Mingus, there were no perfect intervals only major and minor. In actual music theory there is no such thing as a major 5^th^, only perfect, diminished, and augmented 5^th^s. I worked at it for a couple of weeks but did not like how it worked.

Compared to Python, the modeling of the domain as types is much more readable. The Elm compiler is always there guiding me through.

## What I've Learned

Writing in a pure functional language has taught me a lot. It has given me a paradigm shift in how I write all code. When I write Java at my current job I am more aware of side effects. I try to cut (or remove if possible) side effects from my functions.

I try to break down problems into simple composable functions. This has several benefits. The code is easier to reason about. It is easier to test. It is easier to debug.

If all goes well, my theory app should be ready to release by this summer.
