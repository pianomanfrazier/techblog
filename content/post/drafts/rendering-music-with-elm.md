+++
title = "Rendering Music With Elm"
date = 2020-02-06T22:41:41-07:00
draft = true
+++

Why reinvent the wheel? Other stuff has been done.

## JavaScript

- [VexFlow](http://www.vexflow.com/)

## Online

- [Flat.io](https://flat.io)
- [Noteflight](https://www.noteflight.com/)


## Desktop Apps

- [LilyPond](http://lilypond.org/)
- [Dorico](https://www.steinberg.net/en/shop/dorico.html)
- [Sibelius](https://www.avid.com/sibelius)
- [Finale](https://www.finalemusic.com)

## GNU LilyPond

Text based music type setting program similar to LaTeX.

I want to programmatically generate music stuffs. Diagrams, charts, and visualizations. Need something that I can control the output.

Turns out there are some pieces that are tricky.

## Clefs

Draw notes in context of the clef: treble, bass, alto, or tenor.

## Accidental Stacking

See the Dorico blog on this problem [here](https://blog.dorico.com/2014/03/development-diary-part-six/).

> However, as with more or less any aspect of engraving, a set of simple rules and some exceptions to those rules do not account for every possible case, and the job of deriving algorithms to produce pleasing accidental stacks in every case is by no means trivial.
>
> --- Daniel Spreadbury

The definitive book on music layout, [Behind Bars by Elaine Gould](https://www.amazon.com/Behind-Bars-Definitive-Guide-Notation/dp/0571514561)

This is one of the hardest problems.

{{< youtube BvyoKdW-Big >}}

{{< youtube eyEcRZ3ZzgA >}}

Now that we have rendering in Elm what can we do with it. We can generate stuff. Using a theory backend library we can generate transposed stuff. Generate chords and flashcards.

## Music Theory Drills

- https://app.knowyourtheory.com

## Visualization

- https://elm-piano-teacher.netlify.com
- https://www.knowyourtheory.com/resources/circle-of-fifths-explorer/

## Drawing the piano keyboard

The keyboard is assymetrical. Map visualizations from the keyboard to the staff or *vice versa*.
