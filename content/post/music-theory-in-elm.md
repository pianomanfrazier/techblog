+++
title = "Music Theory in Elm"
date = 2019-04-13T16:35:55-06:00
draft = false
markup = "mmark"
tags = ["elm", "music"]
+++

Lately I have been working on a music theory learning app. The app combines short video tutorials with music theory exercises, think Khan Academy combined with Duo Lingo.

In this post I am going to discuss my previous work with music computation libraries. I then discuss how Elm solves some of the problems I've had with my previous approaches. Using Elm's type system I can leverage the compiler as well as make more readable code. I finish by discussing how I generate random notes and chords using Elm's [random](https://package.elm-lang.org/packages/elm/random/latest/) package.

## A Theory Engine

Several things needed to be in place before I could write an application around music theory. I needed a music **theory engine**. The engine would allow me to ask things like, "What is a major 6^th^ above a given note?" or "What are the notes of an A major 7^th^ chord in 1^st^ inversion?"

I also needed a **rendering engine**. There are several other projects that render music in the browser, like [VexFlow](http://www.vexflow.com/), but those projects were too big for what I was trying to do. I did not need to render a whole sheet of music to the browser. I only needed some intervals, chords, key signatures and such.

I first experimented rendering music in the browser using Elm's SVG package. It worked better than I expected. The other music rendering libraries usually support SVG and canvas. Being able to stick to SVG made things simpler.

Once I had a **theory engine** and a **rendering engine** I could do something like this (click the button):

{{< embedElm src="/js/seventh_flashcards.min.js" >}}

## Prior Work

Several years ago I had forked a previous Python project [Mingus](https://github.com/bspaans/python-mingus). I had augmented the project to use theory in a more semantic way. For example, in Mingus, there were no perfect intervals only major and minor. In actual music theory there is no such thing as a major 5^th^, only perfect, diminished, and augmented 5^th^s. I worked at it for a couple of weeks but was not happy with the result.

Compared to Python, the modeling of the domain as types in Elm is much more readable. Most music theory APIs make use of parsing strings to describe things, like `Music.note('a4')` or `Music.note('a4').chord('maj7')`. In Elm I can describe notes, chords, inversion, *etc.* all in types like `getSeventhChord (Note A 4 Natural) Maj7`.

## Designing With Elm Types 

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

## Generating Random Notes

The flow of doing [random](https://package.elm-lang.org/packages/elm/random/latest/) stuff in Elm is much different than JavaScript. You ask the Elm runtime to perform a Command. Once you get used to it, the mindset is really powerful.

This way of generating random things is especially useful for doing music exercises. When generating music stuff there is often an order of operations. I need one random thing before I can compute the next random thing. For example:

- get random clef
- now get a random note from the note range of that clef

```elm
view : Model -> Html Msg
view model =
  ...
  button
    [ onClick GetRandomClef ]
    [ text "Next Note" ]

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

## Random Chords

The order of precedence for generating a random 7^th^ chord would be:

- get random clef
- get random inversion
- get the root of the chord based on the range of the clef and the inversion
- get random chord quality (doesn't matter when we get this)

In order to get the root of the chord, the clef and the inversion must be known first, otherwise the chord might render off the page.

F>[![Clef Range Issue](/img/clef_range_problem.svg)](/files/clef_range_problem.html)
Figure: Clef Range Issue

So the actual range of the clef needs to be reduced by the distance from the bottom note.

F>[![Clef Range Issue](/img/clef_range.svg)](/files/clef_range.html)
Figure: Actual Clef Range

```elm
Random.generate
    NewNote
        <| Random.Array.sample
        <| Array.fromList
        <| possibleNotes model.clef inversion
```

# Conclusion

Writing a music app in Elm has been delightful. Coming from JavaScript, Python, and other C-like languages the syntax may seem strange. After a few hours, this strangeness wears off. The type system also can make for some very readable code. It is nice to see that new languages, like Rust, are supporting [types and pattern matching](https://doc.rust-lang.org/book/match.html).

