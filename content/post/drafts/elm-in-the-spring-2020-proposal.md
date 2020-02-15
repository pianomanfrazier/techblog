+++
title = "Elm in the Spring 2020 proposal"
date = 2020-02-06T23:47:42-07:00
draft = true
markup = "mmark"
+++

## Title

Music Engraving with Elm

## Pitch

Let's build a music notation rendering library in Elm.

Before computers, music scores were engraved by hand on metal plates. With computers we can "engrave" music scores, yet these scores rarely match the quality of a hand engraved score.

What makes music engraving so hard?

## Description

Have you ever wanted to render music notation on a web page?

With our own rendering engine we could randomly generate music flashcards. We could also make interactive visualizations of music concepts.

In the Renaissance era (around the 16th century) music was typeset with movable type. Later on as music got more complex, music scores were engraved onto metal plates. With the advent of computers, music engraving is still a challenge.

Let's explore first hand why it is difficult by writing a small rendering library in Elm.

One of the most difficult problems is accidental stacking. We'll explore this problem in some depth with examples. Finally we will come to a solution that not perfect but good enough.

## Notes

I have Master's and Bachelor's degrees in Piano Performance. I also have a B.S. in Computer Science.

As a side project, I have been building music teaching tools on the web using Elm.

This talk is about making a music notation rendering library in Elm. I will cover some basic information about music notation and also little about printed music notations history. I am going to go through building out a small portion of a rendering library.

The hardest problem I had to solve was accidental stacking. This is how to arrange many flats (or sharps) vertically when they are placed on a chord.

Outline

- What is Music Notation? -- 2 min
- Motivation (Why roll your own music renderer?) -- 2 min
- How hard is it? -- 7 min
  - draw staff (5 lines)
  - draw clef (treble clef)
  - draw note (middle C)
  - accidentals (we now have a problem)
- Accidental Stacking is hard. Here's why. -- 5 min
- Typesetting vs. Engraving -- 5 min
  - typesetting (i.e. movable type) was used in Renaissance era
  - as music got more complex had to now engrave by hand on metal plates
- Music Engraving as Art (examples) -- 2 min
  - show old and new composer's hand written scores
  - most notably George Crumb whose weird scores are also works of art
- Good enough solution to Accidental Stacking problem -- 7 min
  - go through an algorithm to get good enough result
  - make a state machine (go top to bottom and right to left)

## Bio

Ryan Frazier is a pianist, music teacher, and web developer. He grew up playing a lot of Beethoven, Bach, and Brahms. The last few years he has been digging deep into the world of Jazz piano.

Ryan holds Master's and Bachelor's degrees in Piano Performance. He also has a B.S. in Computer Science.

As a side project, Ryan has been building music teaching tools on the web using Elm.
