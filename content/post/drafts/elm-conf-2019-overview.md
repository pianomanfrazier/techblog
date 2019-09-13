+++
title = "Elm Conf Overview"
date = 2019-09-12T12:49:42-06:00
draft = true
markup = "mmark"
+++


## Tessa Kelly --- Writing Testable Elm

### Links

- The Slides --- https://slides.com/tessak/writing-testable-elm 
- [elm-program-test](https://elm-program-test.netlify.com/)
- Twitter --- [@t_kelly9](https://twitter.com/t_kelly9)

### Talk Overview

Write your code such that it is more testable.

To guide her talk she had a pretend code base that was new to her. There was a bug in the code and she went through the process of debugging and writing tests to cover the bug. Under the current state of the code it was hard to test.

She refactored the code so that it was easier to test and the bug was a lot easier to recognize.

For example

```elm
doThing : a -> a
doThing thing =
   -- recieve and do anything 

doStringThing : String -> String
doStringThing stringThing =
    -- almost as bad
```

Make clearer defined functions so the compiler can help you avoid errors. A common pattern is to pass in the model or a large record into a function.

```elm
secondsActive : Model -> Maybe Posix.Time -- BAD!!!
```

vs

```elm
secondsActive : Posix.Time -> User -> Int
secondsActive currentTime user =
    -- figure out the time in seconds
```

### Key Points

- test breakalbe ideas
- write tests for people
- lean on the compiler to write better defined code

The "evil pair exercise". A technique used at NoRedInk. One person writes a test and the other person writes Elm such that the tests pass but the code is actually wrong. *This is what I understood, but I may be wrong*


## Abadi Kurniawan --- Building Highly Performant Animations in Elm



## Brooke Angel --- A Month of Accessible Elm



## Ryan Frazier (yours truly) --- Building a Music Theory API with Types



## James Carlson --- Making Elm Talk to Your Personal Supercomputer


## Liz Krane --- Building a Music Learning Game with Elm, Web MIDI, and SVG Animation



## James Gary --- Game Development in Elm: Build Your Own Tooling


## Katie Hughes --- GraphQSquirrel


## Ian Mackenzie --- A 3D Rending Engine for Elm



## Katja Mordaunta --- Growing an Elm Project With the Whole Team



