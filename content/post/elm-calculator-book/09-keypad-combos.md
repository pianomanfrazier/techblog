+++
title = "Elm Calculator Part 9 - Combination Key Input"
date = 2020-05-11
draft = false
markup = "mmark"
tags = ["elm", "elm calculator book"]
+++

{{< elmCalcBookBlurb >}}

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/v0.9>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/compare/v0.9...v0.10>
- ***ellie:*** <https://ellie-app.com/72nYc5Zj9Hma1>

Users can press backspace to delete a single digit. How would we allow the user to clear the whole input area? Or clear the whole stack?

We'll provide a keyboard combination to support this. So we can allow users to press CTRL + BACKSPACE and it would clear the input box and CTRL + SHIFT + BACKSPACE would clear the whole stack.

We have already done the hard work in the previous chapter. We need to tweak our update function to check for CTRL + SHIFT or just CTRL before we check the other keys.

```elm
update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        ...
        HandleKeyboardEvent event ->
            if event.ctrlKey && event.shiftKey then
                case event.keyCode of
                    KK.Backspace ->
                        update ClearAll model

                    _ ->
                        ( model, Cmd.none )

            else if event.ctrlKey then
                case event.keyCode of
                    KK.Backspace ->
                        update Clear model

                    _ ->
                        ( model, Cmd.none )
            else
                case event.keyCode of
                    KK.Multiply ->
                    ...
```

And that's it. We now have key combos.

The next chapter will cover testing. We will write a test using elm-test and elm-program-test to verify our calculator.
