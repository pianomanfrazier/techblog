+++
title = "Elm Calculator Part 6 - Supporting Negative Numbers"
date = 2020-04-17
draft = false
markup = "mmark"
tags = ["elm", "elm calculator book"]
+++

{{< elmCalcBookTOC num="6">}}

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/v0.6>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/compare/v0.5...v0.6>
- ***ellie:*** <https://ellie-app.com/72p2Gt2gpkXa1>

Users need to be able to input negative numbers. Since negatives are different than the subtract operation we need to handle this separately.

Many RPN calculators I have seen have a toggle sign button.

```elm
section : Html Msg
section =
    div [ class "section" ]
        [ ...
        , cell (onClick SetSign) Single White "+/-"
        , cell (onClick Enter) Single Yellow "Enter"
        ]
```

And then let's add the message type and update the model.

```elm
type Msg
    = ...
    | SetSign
```

We need to do some string checking to make this work.

```elm
update : Msg -> Model -> Model
update msg model =
    case msg of
        ...
        SetSign ->
            -- don't allow the user to make a negative zero
            if model.currentNum == "0" then
                model

            -- drop the negative sign from the string
            else if String.startsWith "-" model.currentNum then
                { model | currentNum = String.dropLeft 1 model.currentNum }

            -- add the negative sign
            else
                { model | currentNum = "-" ++ model.currentNum }
```

And that's it. We now have a working calculator.

The next few chapters will be adding some nice extra features.
