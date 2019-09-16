+++
title = "Elm Conf 2019 Overview"
date = 2019-09-18
draft = false
tags = ["elm"]
hasMath= true
+++

Elm conference was awesome. It was my first developer conference I have attended and my first time giving a conference talk. The Elm community is very nice and welcoming.

I wanted to write up all my notes for the future.


## Tessa Kelly --- Writing Testable Elm

- The Slides --- https://slides.com/tessak/writing-testable-elm 
- [elm-program-test](https://elm-program-test.netlify.com/)
- Twitter --- [@t_kelly9](https://twitter.com/t_kelly9)


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

Pass in the specific thing from the model that you need. This function is much easier to test.

### Key Points

- test breakable ideas
- write tests for people
- lean on the compiler to write better defined code

She mentioned the "evil pair exercise", apparently a technique used at NoRedInk. One person writes a test and the other person writes Elm such that the tests pass but the code is actually wrong. *This is what I understood, but I may be wrong*.


## Abadi Kurniawan --- Building Highly Performant Animations in Elm

- GitHub --- [abadi199](https://github.com/abadi199)
- https://github.com/abadi199/elm-animation-exploration


Abadi explored 3 different ways of doing animation in Elm.

### Method 1: Pure Elm

This method requires you to subscribe to an `animationFrameDelta` and then on every `tick` do something.

With multiple animations you now need to keep track of time elapsed and manually keep track of synchronizing animations. It becomes hard to handle lots of animations.

#### Pros

Not many pros here.

#### Cons

- cumbersome
- no browser/hardware optimization
- breaks the current Elm debugger

### Method 2: CSS Animation

This method uses CSS as a side effect using the elm-css library Animation module.

#### Pros

- highly performant
- declarative

#### Cons

- still hard to synchronize several animations

### Method 3: Web Animation API

Using the web animation API provided by the browser you can directly animate things. You have access to the underlying processes that CSS animation uses.

Abadi is developing a library that accesses this web animation API in elm.

#### Pros

- performant
- declarative
- simpler to synchronize multiple animations

#### Cons

- limited browser support for the web animation API (Firefox and Chrome only)



## Brooke Angel --- A Month of Accessible Elm

- The Slides --- https://slides.com/brookeangel/accessible-elm
- GitHub --- [tesk9](https://github.com/tesk9)
- https://github.com/tesk9/accessible-html
- https://github.com/avh4/elm-program-test

She talks about the impact of making small goals to change habits. She talked about trying a small health goal for a month and seeing if that worked. She found some success with achieving these small goals.

Her team at NoRedInk was making an effort to improve accessibility for their platform. She was overwhelmed by all that needed to be done so she took a similar approach as her health goals. She made some small goals to try for a month to change some habits.


### What does accessible mean?

Goals should be specific. A good place to start with accessible is the acronym POUR. See https://webaim.org/articles/pour/

- **P**erceivable
- **O**perabale
- **U**nderstandable
- **R**obust

### Example

She explored the process of rewriting a section of the "select an interest" UI.

As a first easy attempt at testing its accessibility she turned off all CSS styling.

All the clickable items were not buttons but `ul > li`. It was not easy to tell these were clickable elements.

Furthermore, when a user selected an item the selected list of items did not even show anything to the user. She also had to rewrite the tests that covered this UI.

She rewrote the tests in [elm-program-test](https://github.com/avh4/elm-program-test) a new integrated testing library. She also wrote [tesk9/accessible-html](https://github.com/tesk9/accessible-html). This package will check if you are violating accessible principles in the markup like attaching events to non-clickable elements like `<div>` or `<span>`.


## Ryan Frazier (yours truly) --- Building a Music Theory API with Types

- slides --- https://typed-music-theory.netlify.com
- app --- https://app.knowyourtheory.com

I have written about it in my other posts [here](/post/music-theory-in-elm) and [here](/post/theory-app-prototypes).

I incrementally build up a model of a music note and explain the music theory along the way.


## James Carlson --- Making Elm Talk to Your Personal Supercomputer

- https://futhark-lang.org/ 
- GitHub --- [jxxcarlson](https://github.com/jxxcarlson)


A different talk from the other web related stuff. The personal supercomputer is the GPU.

There was a lot of math involved. It was the best concise explanation of Linear Algebra I have heard.

### What is Futhark?

A GPU processing language written by Troels Henriksen. The compiler is written in Haskell and shares many similarities with Elm. The compiler generates code for C, opencl, pyopencl, and maybe someday JS or Elm.

Futhark generates parallel processing code for the GPU.

Futhark is an array language.

You can put annotations on data types to help the compiler.

In place updates with some fancy type theory. This allows for \\(\mathcal{O}(n)\\) instead of \\(\mathcal{O}(n^2)\\) array updates.

### Classifying fossils

Doing matrix multiplication is computationally expensive. 

This is a good use case for the GPU. Classifying fossils is a linear algebra problem. Fossil bones can be measured and its features can be put into a \\(\mathcal{R}^{30}\\) vector.

### How to use it with Elm

Elm <---> Python <---> GPU/Futhark

Currently Elm talks to a python server that calls out to Futhark to run computations. However in the future GPU support may be available to access the GPU with JavaScript in the browser. In which case, Futhark might be able to target web assembly and this could all be run in the browser.

Elm <---> JS <---> GPU/Futhark


## Liz Krane --- Building a Music Learning Game with Elm, Web MIDI, and SVG Animation

- twitter --- [@learningnerd](https://twitter.com/learningnerd)
- GitHub --- [learningnerd](https://github.com/LearningNerd/)

A very entertaining talk going through the process of building her first Elm app.

She drew inspiration from an old Mario Teaches Typing game. She built a piano key drilling app that had similar mechanics.

### Beginner mistakes

- parenthesis all the things
- forward function all the things (`someFunc |> param |> func2 ...`)
- make all states possible (return `Maybe` for everything)

### Building the game animation

There are lots of animation concepts like 'lerping' and 'tweening'.

Worked on getting the physics correct to have the character jump up onto the note. Needed the physics of projectile motion.

My favorite quote from the conference.

> Zeno's paradox...
> It goes halfway, half of that and so on and so on, and you never reach the end. But because
> of JavaScript rounding errors you will.
>
> --- Liz Krane


## James Gary --- Game Development in Elm: Build Your Own Tooling

- https://github.com/jamesgary/elm-config-ui
- GitHub --- [jamesgary](https://github.com/jamesgary)


James is doing game development in Elm full time. He has had to build up some tooling to make the development process easier.

His demonstration was a flocking algorithm. He needed to tweak the parameters of the algorithm in an easy way to see how the changes effected the output.

He suggests we build tools to shorten the development feedback cycle.

He drew inspiration from [dat.GUI.js](https://github.com/dataarts/dat.gui) as well as other game engines like Unity that let you tweak things and get immediate feedback.

James built something similar to dat.GUI.js in Elm. The goal was to keep no magic numbers in Elm. Adding a new field required a lot of boilerplate to setup. He made a code generation script that would add a new typed field to his data model. This new field would then be available for tweaking in the config ui.


## Katie Hughes --- GraphQSquirrel

- GitHub ---  [glitteringkatie](https://github.com/glitteringkatie)
- project --- https://github.com/glitteringkatie/squirrel-degrees


Another very entertaining talk. She used the Marvel Comics API and a GraphQL server.

Her comics were comic themed. She even had a commissioned drawing by the comic illustrators of Squirrel Girl for the presentation.

Her goal was to do a 7 degrees of Kevin Bacon thing with the comic character Squirrel Girl.

Squirrel Girl is a good candidate because she is in relatively few commics but she has met some key characters in the Marvel universe like Iron Man, Craven the Hunter, and Galaxtos (probably butchered the names, I don't do comics).

Squirrel Girl is an efficient root of the graph because her primary connections are few.

She proposed the talk thinking everything would work through GraphQL. She discovered though that GraphQL didn't provide all the information she needed so she had to augment the data with REST queries. It was a good example of what can go wrong in engineering and how to be flexible and change plans as needed.

She walks through optimizing the queries to resolve this large graph traversal. Doing some simple caching she was able to bring her query count way down.

### Do I need tests?

> Writing tests is a form of self care

At the beginning of the project she wrote no tests. However she would often reach her daily query limit on the API and then she would have to stop work for the day.

Writing tests allowed her to develop faster and not be limited by the API limit.


## Ian Mackenzie --- A 3D Rending Engine for Elm

- GitHub --- [ianmackenzie](https://github.com/ianmackenzie)
- Twitter --- [@ianemackenzie](https://twitter.com/ianemackenzie)
- https://github.com/ianmackenzie/elm-3d-scene 

### Other related projects that were used

- https://github.com/ianmackenzie/elm-geometry
- https://github.com/ianmackenzie/elm-units
- https://github.com/w0rm/elm-physics


Ian has a strong mechanical engineering background. His goal is to design robots with Elm. He has been building up tooling to do so in the browser. The latest project, elm-3d-scene, allows for rendering of 3D objects with a high level API.

It was possible to render 3D objects using webGL, elm-explorations/webGL, in elm but it is low level and hard to write well. You need to know webGL and how shaders work.

### High level features needed

- lights
- shadows
- shapes
- materials

Needs to be all strongly typed

- position
- direction
- color
- units

### elm-3D-scene

Drew inspiration from Three.js and game engines like Frostbit and Unreal. It is not a port of any of these systems but creates a new API.

There were some **awesome demos** in this talk demonstrating with lots of objects and animations in 3D. The package is not yet in the Elm packages but will hopefully be there soon.


## Katja Mordaunt --- Growing an Elm Project With the Whole Team

Katja is from the UK and works for NeonTribe. They develop app for small non-profit organizations.

This talk wasn't about building anything new. It was stories of introducing developers to Elm at work and how we as developers and managers can do better.

It is really hard to summarize her experiences. One key experience was that they got a new project and she wanted to write it in Elm. Katja didn't have many developers to help her so she recruited a graphic designed and introduced her to programming. Katja felt the learning curve for a new developer learning Elm was very smooth.

### Questions to consider

- How can we create spaces and cultures to not feel the best at everything all the time?
- How can we improve the democracy of our collaborations?
- Do labels and job roles prevent us from sharing knowledge openly?

She then offers some suggestions and thought how we can address these issues.



