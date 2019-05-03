+++
title = "Theory App Prototypes"
date = 2019-04-30T22:28:57-06:00
draft = false
markup = "mmark"
elm = "/js/music.min.js"
+++


In my previous life I was a working pianist. I taught and accompanied a lot. Now as a programmer I still perform and teach. I had a problem teaching. I needed music flashcards. I would use note flash cards but kids would lose them or I would lose them. I wondered if I could write something simple that would work for me. There are many music flash card app available but they don't usually go far enough. They are also usually super cute with dancing elephants and balloons. I want no fluff.

My requirements were:

- mobile first
- available offline (I teach at other's home sometimes)
- rigorous

My first experiment was to use the SVG module in Elm. I ripped out the SVG output from GNU LilyPond and converted it over to Elm. That experiment went well. I kept iterating and making more and more complicated exercises. The following is the result of many months of prototyping. The next step is to put all of these exercises into an <abbr title="Single Page Application">SPA</abbr>.

*Disclaimer: I know there are some quirks with these examples. :confounded: Sometimes a note will shoot off the page. These issues are fixed in my <abbr title="Single Page Application">SPA</abbr>.*

## Note Flash Cards

{{< embedMultipleElm node="notes" module="Notes" >}}

## Basic Interval Cards

{{< embedMultipleElm node="interval-basics" module="IntervalBasics" >}}

## All Intervals

{{< embedMultipleElm node="intervals" module="Intervals" >}}

## Triads In Inversion

{{< embedMultipleElm node="triads" module="Triads" >}}

## Seventh Chords

{{< embedMultipleElm node="sevenths" module="Sevenths" >}}

## Harmonic Analysis

*Beware: Not mobile friendly! :disappointed: Input is best done with a keyboard and a larger screen.*

I am really excited about this last prototype. I have seen nothing like this and I think it would be very useful for more advanced students.

There are 3 types of fields to input on an analysis example: key, chord, and figure.

### Key

There is no validation for now, just input `Bb Major` or `C minor`.

### Chord

Valid inputs are in the form of `<Roman Numeral><hd|dim>(<fig bass>)`. The first roman numeral part is required. The last two parts are optional.

- I
- I(6/4)
- viihd
- viihd(4/2)
- ii(6/b5)
- ii(6/#5)

### Figure

Valid inputs are just the figure part from above.

- 6/4
- 7/b5/#3

{{< embedMultipleElm node="harmony" module="Harmony" >}}


