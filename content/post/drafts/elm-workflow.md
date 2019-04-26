+++
title = "Elm Workflow"
date = 2019-04-25T22:37:15-06:00
draft = true
markup = "mmark"
+++

{{< progress title="elm" width1="50%" width2="20%">}}
{{< progress title="js" width1="30%" width2="70%">}}

## Design With Types

My favorite part about working with Elm is the Type system. When I start a new feature I design the model and the types around that model. For the music theory app that I am building I created a Theory Engine to compute all things music theory. It was nice to design types and records in a way that described my problem domain. Here are some example types and records:

```elm
type NoteName
    = C
    | D
    | E
    | F
    | G
    | A
    | B

type Accidental
    = DoubleFlat
    | Flat
    | Natural
    | None
    | Sharp
    | DoubleSharp
```

I can then define render and toString functions on all these types.

```elm
noteNameToString : NoteName -> String
noteNameToString note =
    case note of
        C -> "C"
        D -> "D"
        ...

renderAccidental : Accidental -> Svg msg
```

Since I am using pattern matching on the types the compiler will enforce that I handle every type variant. I then call these render functions in my view.

F>![Render note model](/img/render-note-model.png)
Figure: Render Note Model 

This is also a great way to solve a lot of other problems as well. See [Kris Jenkins on slaying a UI Antipattern](http://blog.jenkster.com/2016/06/how-elm-slays-a-ui-antipattern.html).


## TypeError Undefined

F>![JS undefined error](/img/js-undefined.png)
Figure: JS undefined error

Several months ago, I was doing a project with Vue using Vuetify. I noticed that Vuetify had updated their library with a new component I wanted to use so I updated Veutify. This completely broke my application. There were null and undefined errors throughout the application. It took about a days worth of work to track down the source of the problem. The combobox value was being set to null when a user didn't select anything. This was different behavior than before and broke everything. I had that component on nearly every page of my application.

## Debugging

I often have the experience that when I can get my program to compile in Elm it usually works. A lot of time is spent up front designing the model and messages and then the verification process is much smoother. Debugging is also easier than normal JavaScript.

You have two options to debug in Elm. You can use `Debug.log` or the time traveling debugger. For larger Elm applications I use [Create Elm App](https://github.com/halfzebra/create-elm-app) which includes the time traveling debugger. If I get unexpected behavior I usually start by inspecting the model and then the messages that generated the model from the debugger.

F>![Elm Time Debugger](/img/time-debugger.png)
Figure: Elm Time Traveling Debugger

Elm 0.19 does not come with the debugger when you run `elm reactor` like you could in Elm 0.18. You can however just use `Debug.log` or `Debug.toString model` in the view function. To inspect a particular event I would place a `Debug.log` in my update function.

```elm
view : Model -> Html Msg
view model =
    div
        []
        [ text <| Debug.toString model ]

update : Msg -> Model -> (Model, Cmd Msg)
update msg model =
    case msg of
        BtnClick ->
            Debug.log "Button Clicked" <|
            ( { model | btnClicked = true }, Cmd.none)
```

## Elm Reactor

I usually start with an idea by making a stand alone Elm `browser.element` and run it using `elm reactor`. I iterate on this until it is usable. At that point I turn the file into an Elm module and move it into my single page application. I usually start by changing the model and then let the compiler tell me what to change.

## Single Page Application

One of the biggest hurdles for me using Elm was getting a single page application with routing working. Previously I used Vue and the Vue CLI sets up a router that is really easy to get started with. I started with the [package.elm-lang.org source](https://github.com/elm/package.elm-lang.org/tree/master/src/frontend) and hacked it down to the bare minimum. I kept removing functions and let the compiler tell me what to fix to get it compiling again. I kept doing this process until I had a few pages with a couple routes.

Here is what I ended up with. [Elm Routing Example](https://github.com/pianomanfrazier/elm-routing-example/)