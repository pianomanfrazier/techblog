+++
title = "Elm Workflow"
date = 2019-05-08T05:00:00-00:00
draft = false
markup = "mmark"
+++

{{< progress title="elm" width1="50%" width2="20%">}}
{{< progress title="js" width1="30%" width2="70%">}}

## Dev Time vs. Debug Time

With any programming language or paradigm there are trade-offs. With Elm you trade a longer development time with a shorter debug time. The way the language works forces you to think about how you design your solution.

When it compiles, it works. Most of the time.

With Vue I can put up a prototype quickly using component libraries like [Vuetify](https://vuetifyjs.com). The downside is that I have no guarentees about how those components work. It may work out. The components may also have undocumented quirks. You have no guarentees that when you update the library your application won't explode.

Semanitic versioning is enforced on all Elm packages. What this means is that if you update a package nothing breaks.

> Forget what you have heard about functional programming. Fancy words, weird ideas, bad tooling. Barf. Elm is about:
> 
> - No runtime errors in practice. No null. No undefined is not a function.
> - Friendly error messages that help you add features more quickly.
> - Well-architected code that stays well-architected as your app grows.
> - Automatically enforced semantic versioning for all Elm packages.
> 
> No combination of JS libraries can ever give you this, yet it is all free and easy in Elm. Now these nice things are only possible because Elm builds upon 40+ years of work on typed functional languages.
Quote: -- The Elm Guide[^1]

[^1]: See [Why a *functional* language](https://guide.elm-lang.org/#why-a-functional-language).

## Design With Types

My favorite part about working with Elm is the Type system. When I start a new feature I design the model and the types around that model. For the music theory app that I am building, I created a Theory Engine to compute all things music theory. It was nice to design types and records in a way that described my problem domain. Here are some example types and records:


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

Pattern matching ensures that I handle every case. This guarentees that I provide a render function for each note name. I then call these render functions in my view.

This is also a great way to solve a lot of other problems as well. See [Kris Jenkins on slaying a UI Antipattern](http://blog.jenkster.com/2016/06/how-elm-slays-a-ui-antipattern.html).

## TypeError Undefined

F>![JS undefined error](/img/js-undefined.png)
Figure: JS undefined error

Several months ago, I was doing a project with Vue using Vuetify. I noticed that Vuetify had updated their library with a new component I wanted to use so I updated Veutify. This completely broke my application.

There were null and undefined errors throughout the application. It took about a days worth of work to track down the source of the problem. The combobox value was being set to null when a user didn't select anything. I had that component on nearly every page of my application.

## Debugging

If you do need to debug you have two options in Elm. You can use `Debug.log` or the time traveling debugger. For larger Elm applications I use [Create Elm App](https://github.com/halfzebra/create-elm-app) which includes the time traveling debugger. If I get unexpected behavior I usually start by inspecting the model and then the messages that generated the model from the debugger.

F>![Elm Time Debugger](/img/time-debugger.png)
Figure: Elm Time Traveling Debugger

F>![Render note model](/img/render-note-model.png)
Figure: Render Note Model 

Elm 0.19 does not come with the debugger when you run `elm reactor` like you could in Elm 0.18. You can use `Debug.log` or `Debug.toString model` in the view function. To inspect a particular event I would place a `Debug.log` in my update function.

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

One of the biggest hurdles for me using Elm was making a single page application. The Vue CLI sets up a router that is easy to get started with.

I started with the [package.elm-lang.org source](https://github.com/elm/package.elm-lang.org/tree/master/src/frontend) and hacked it down. I kept removing functions and let the compiler tell me what to fix. I kept doing this process until I had a minimal setup with a few pages.

Here is what I ended up with. [Elm Routing Example](https://github.com/pianomanfrazier/elm-routing-example/)

## Conclusion

Elm is **Awesome** :tada: :confetti_ball:. Starting out with Elm I thought it would be too hard to build something big in it. What I am learning is that as my projects grow my code stays clean and easy to read. There are certain types of errors that will never happen because the compiler checks them for me.

Now if only I could convince my workplace to use Elm.
