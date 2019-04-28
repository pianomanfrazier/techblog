+++
title = "Music Theory in Elm"
date = 2019-04-13T16:35:55-06:00
draft = true
markup = "mmark"
+++

Lately I have been working on a music theory learning app. The app combines short video tutorials with music theory exercises, think Khan Academy combined with Duo Lingo.

Several things needed to be in place before I could write an application around music theory. I needed a music **theory engine**. The engine would allow me to ask things like, "What is a major 6^th^ above a given note?" or "What are the notes of an A major 7^th^ chord in 1^st^ inversion?"

I also needed a **rendering engine**. There are several other projects that render music in the browser, like [VexFlow](http://www.vexflow.com/), but those projects were too big for what I was trying to do. I did not need to render a whole sheet of music to the browser. I only needed some intervals, chords, key signatures and such.

I first experimented rendering music in the browser using Elm's SVG package. It worked better than I expected. The other music rendering libraries usually support SVG and canvas. Being able to stick to SVG made things simpler.

Once I had a **theory engine** and a **rendering engine** I could do something like this (click the button):

{{< embedElm src="/js/seventh_flashcards.min.js" >}}

## Prior Work

Several years ago I had forked a previous Python project [Mingus](https://github.com/bspaans/python-mingus). I had augmented the project to use theory in a more semantic way. For example, in Mingus, there were no perfect intervals only major and minor. In actual music theory there is no such thing as a major 5^th^, only perfect, diminished, and augmented 5^th^s. I worked at it for a couple of weeks but was not happy with the result.

Compared to Python, the modeling of the domain as types in Elm is much more readable. Most music theory APIs make use of parsing strings to describe things, like `Music.note('a4')` or `Music.note('a4').chord('maj7')`. In Elm I can describe notes, chords, inversion, *etc.* all in types like `getSeventhChord (Note A 4 Natural) Maj7`.

## Why I Chose Elm

I dabbled into Elm before starting this project. I got confused with routing in Elm 0.18, but the routing module of Elm 0.19 was easier to use. With the release of Elm 0.19, I decided to try to write a single page application (SPA) in Elm.

I started with the **theory engine**. Throughout the whole process, I wrote unit tests with Elm Test. When I finished I had something that just worked. I wrote the engine several months ago and have not had to touch the core logic since. Drawing inspiration from [Making Impossible States Impossible](https://youtu.be/IcgmSRJHu_8) I modeled everything in Types. Coming from imperative languages this was a new thing for me. My Note looked like this:

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

In the render engine I use case matching to render the accidentals:

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

## Experiments Beget Experiments

> The journey of a thousand miles begins with a single step.
Quote: -- Lao Tzu

My first experiement doing music in the browser what to draw an a note using SVG in Elm. That went well so I tried to make random notes. This required that I learned how [Random](https://package.elm-lang.org/packages/elm/random/latest/) works in Elm. Using messages I could trigger getting random things like

- get random clef
- now get a random note

```elm
update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        GetRandomClef ->
            ( model
            , Random.generate
                NewClef
                    <| Random.Array.sample
                    <| Array.fromList model.clefPool
            )

        NewClef clef ->
            let
                possibleNotes = notesForClef clef
            in
            ( { model | clef = clef }
            , Random.generate
                NewNote
                    <| Random.Array.sample
                    <| Array.fromList possibleNotes
            )

        NewNote note ->
            ( { model | note = note }, Cmd.none )
```

This flow of getting random things worked great because in order to get a random note I first needed to get the clef. Once I had the clef I can then select a note from possible notes in that clefs range.

Now that I had random note flashcards, I now thought about generating random intervals and chords. In order to do this I needed a **theory engine**.