+++
title = "Elm Calculator Part 8 - Support Keypad Input"
date = 2020-05-01
draft = false
markup = "mmark"
tags = ["elm", "elm calculator book"]
description = "Learn how to build a calculator with elm from scratch."
socialImage = "img/elm-calculator/elm-calc-splash.png"
socialImageAlt = "Elm Calculator"
+++

{{< elmCalcBookTOC num="8">}}

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/v0.8>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/compare/v0.7...v0.8>
- ***ellie:*** <https://ellie-app.com/72nXvQqPq37a1>

It would be nice if users could input numbers into our calculator using their number pad on their keyboard.

We need to tell our program what to do when a user presses these keys. So we need to add some more messages to our application.

We will be using the package [Gizra/elm-keyboard-event](https://package.elm-lang.org/packages/Gizra/elm-keyboard-event/latest/).

First we need to install the package so we can import it into our code. The ellie-app version of this chapter has the package installed. Open the side menu and look at the installed packages. You should see I have added 3 new packages as dependencies.

![Ellie app installed packages](/img/elm-calculator/ellie-app-packages.png){#fig:elliepackages width=60%}

To install a package in ellie-app use the search bar.

![Install package on Ellie app](/img/elm-calculator/ellie-install-package.png){#fig:ellieinstallpackage width=70%}

Or you can install a package locally on the command line.

```bash
elm install Gizra/elm-keyboard-event
```

We will also need to import [SwiftsNamesake/proper-keyboard](https://package.elm-lang.org/packages/SwiftsNamesake/proper-keyboard/latest/) which is a dependency of elm-keyboard-event. We need this because we will be using these types directly in our application.

```bash
elm install SwiftsNamesake/proper-keyboard
```

And lastly we need `elm/json` to decode the JSON message coming from the browser for our events. Don't worry. This is not as scary as it sounds.

```bash
elm install elm/json
```

## Refactor to use Elm subscriptions

Since these keyboard events are going to be coming from the browser, our Elm application needs to subscribe to these events. In order to do subscriptions we need to refactor our application.

Right now we have been using `Browser.sandbox` in our main function.

```elm
main : Program () Model Msg
main =
    Browser.sandbox
        { init = initialModel
        , view = view
        , update = update
        }
```

### Change to `Browser.element`

We need to change it to `Browser.element` so that we can add subscriptions.

```elm
main : Program () Model Msg
main =
    Browser.element
        { view = view
        , init = \_ -> init
        , update = update
        , subscriptions = subscriptions
        }
```

This is going to impact our whole application. We'll let the compiler guide us through this refactor. The biggest change will be to our `update` function.

It will need to change from

```elm
update : Msg -> Model -> Model
```

to

```elm
update Msg -> Model -> ( Model, Cmd Msg )
```

We need to return the model and a command message. We won't be using command messages in this application so don't worry about it. We just need to fix the code so it will compile again.

Most of the time we can just return the tuple `( model, Cmd.none )`.

```elm
update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        SetDecimal ->
            if String.contains "." model.currentNum then
                ( model, Cmd.none )
    ...
```

The `init` also needs to return a command message.

```elm
init : ( Model, Cmd Msg )
init =
    ( { stack = []
      , ...
      }
    , Cmd.none
    )
```

## Add subscriptions

Now we can work on adding the subscriptions. First we need to import some stuff.

```elm
import Browser.Events exposing (onKeyDown)
import Json.Decode as D
import Keyboard.Event as KE exposing (KeyboardEvent, decodeKeyboardEvent)
import Keyboard.Key as KK
```

We are now going to subscribe to the `onKeyDown` event in the browser. After our application gets the event we then need to decode the event into something Elm can deal with. Since events come in the from the browser as a JSON message we need to decode the JSON into an Elm type.

Luckily for us, we don't need to worry about writing a decoder for these events. The `Gizra/elm-keyboard` package provides this for us.

```elm
subscriptions : Model -> Sub Msg
subscriptions model =
    onKeyDown (D.map HandleKeyboardEvent decodeKeyboardEvent)
```

This `subscriptions` function is going to return a subscription message. In this case a `HandleKeyboardEvent` type.

We need that in our message type.

```elm
type Msg
    = ...
    | HandleKeyboardEvent KeyboardEvent
```

## Handle the key events

Now we can put this message and handle it in our update function.

```elm
update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        ...
        HandleKeyboardEvent event ->
            case event.keyCode of
                KK.Add ->
                    update (InputOperator Add) model

                KK.Subtract ->
                    update (InputOperator Sub) model

                KK.NumpadZero ->
                    update (InputNumber 0) model

                ...

                -- ignore anything else
                _ -> ( model, Cmd.none )
```

I used a small trick here. When we get a key matching one of our cases, just call the appropriate update function again.

What I hope you take away from this chapter is how nice it is to refactor things in Elm. We made some sweeping changes to our application and the compiler was able to help us out.

Now that we have keyboard input, it would be nice if the user had some more options for deleting the stack frames. The next chapter will cover using key combinations such as ctrl-shift-delete to clear out the frames.
