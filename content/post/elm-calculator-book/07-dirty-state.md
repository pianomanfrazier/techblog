+++
title = "Elm Calculator Part 7 - Add Dirty State"
date = 2020-04-24
draft = false
markup = "mmark"
tags = ["elm", "elm calculator book"]
description = "Learn how to build a calculator with elm from scratch."
socialImage = "img/elm-calculator/elm-calc-splash.png"
socialImageAlt = "Elm Calculator"
+++

{{< elmCalcBookTOC num="7">}}

This allows users to overwrite the input area with a new number if the calculator is in a dirty state.

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/v0.7>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/compare/v0.6...v0.7>
- ***ellie:*** <https://ellie-app.com/72p3SNcV8Fva1>

The way it works is if a user has just entered a number in, the input area is now dirty. Users can press enter again to keep pushing that same number on the stack. Or they can start typing a new number and it will over-write the existing number.

![Dirty State](/img/elm-calculator/dirty-state.png)

We need to add another piece of state to our model.

```elm
type alias Model =
    { stack : List Float
    , currentNum : String
    , error : Maybe String
    , dirty : Bool
    }


initialModel : Model
initialModel =
    { stack = []
    , currentNum = "0"
    , error = Nothing
    , dirty = False
    }
```

In the model update we need to add some logic around when the input field is dirty.

We need to do this to the `Clear`, `Enter`, `InputOperator`, `SetDecimal`, `SetSign`, and `InputNumber` messages.

*Note: When I initially wrote the code I forgot to flip the flag on `SetDecimal` and `SetSign`. The Master branch has this fix. v0.7 does not.*

```elm
Clear ->
    { model | currentNum = "0", dirty = False }

Enter ->
    ...
    { model
        | ...
        , dirty = True
    }

InputOperator operator ->
    ...
    { model
        | ...
        , dirty = True
    }

InputNumber num ->
    ...
    else if model.dirty then
        { model
            | ...
            , dirty = False
        }
```

The next chapter is going to add support for users to enter numbers into the calculator using their number pad on their keyboard.
