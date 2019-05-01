+++
title = "Building Music Theory App"
date = 2019-04-30T22:28:57-06:00
draft = true
markup = "mmark"
elm = "/js/music.min.js"
+++

In my previous life I was a concert pianists. Now as a programmer I still perform and teach. I had a problem teaching. I needed music flashcards. I would use note flash cards but kids would lose them or I would lose them. I wondered if I could write something simple that would work for me. There are many music flash card app available but they don't usually go far enough. And they are usually super cute with dancing elephants and balloons.

My requirements were:

- mobile first
- available offline (I teach at other's home sometimes)
- rigorous

My first experiment was to use the SVG module in Elm. I ripped out the SVG output from GNU LilyPond and converted it over to Elm. That experiment went well. I rendered random notes to the treble clef. There was no user input.

# Note Flash Cards

{{< embedMultipleElm node="notes" module="Notes" >}}

# Basic Interval Cards

{{< embedMultipleElm node="interval-basics" module="IntervalBasics" >}}

# All Intervals

{{< embedMultipleElm node="intervals" module="Intervals" >}}

# Triads In Inversion

{{< embedMultipleElm node="triads" module="Triads" >}}

# Seventh Chords

{{< embedMultipleElm node="sevenths" module="Sevenths" >}}

# Harmonic Analysis With Parsers

{{< embedMultipleElm node="harmony" module="Harmony" >}}

# Single Page Application

