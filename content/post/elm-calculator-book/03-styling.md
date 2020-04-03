+++
title = "Elm Calculator Part 3 - Add CSS"
date = 2020-03-27
draft = false
markup = "mmark"
tags = ["elm", "elm calculator book"]
description = "Learn how to build a calculator with elm from scratch."
socialImage = "/img/elm-calculator/elm-calc-splash.png"
socialImageAlt = "Elm Calculator"
+++

{{< elmCalcBookTOC num="3">}}

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/v0.2>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/compare/v0.1...v0.2>
- ***ellie:*** <https://ellie-app.com/72nSDGTwkY4a1>

I like to get my projects looking good before I start working on functionality. We'll start by looking at DuckDuckGo's calculator.

<https://duckduckgo.com/?q=calculator&ia=calculator>

We can make a simplified version of this with the number pad and the basic operators.

To see how RPN calculators work play around with some examples online. Search for "online RPN calculator" and you'll find some examples.

## The buttons

We need a bunch of buttons.

Our end goal is that we produce some HTML that looks like this:

```html
<button class="cell single bg-white">1</button>
```

Or for a double yellow button:

```html
<button class="cell double bg-yellow">1</button>
```

And some CSS to go with it.

```css
.double {
    width: 50%;
}
.single {
    width: 25%;
}
.bg-yellow {
    background-color: yellow;
}
.bg-white {
    background-color: white;
}
```

## The buttons in Elm

Let's write our HTML using Elm.

We'll call each piece (or button) a cell in our button grid.

```elm
cell : Size -> Color -> String -> Html Msg
cell size color content =
    button
        [ class <|
            String.join " " <|
                [ "cell", sizeToString size, colorToString color ]
        ]
        [ text content ]
```

Notice it takes a size, color, and a content string and then returns some HTML. Size and Color are custom types. We'll get to that in a minute. Let's talk about an alternative approach first.

Another approach would be to make a function that took a bunch of class name strings like the following.

```elm
cell : String -> String -> String -> Html Msg
cell size color content =
    button
        [ class <|
            String.join " " [ "cell", size, color ]
        ]
        [ text content ]
```

The problem with this approach is that we can put any string into this function. We could try to make a purple button, `cell "single" "purple" "1"`, but we have not defined a "purple" class.

We could also make the mistake of mixing up the arguments like `cell "1" "yellow" "double"`. Or typos like `cell "yelow" "double" "1"`.

We can have the compiler help us not make these kinds of mistakes by using types.

## Elm Types for the win

Let us define our custom types. This will constrain the input to our functions. It also makes the code more readable.

```elm
type Size
    = Single
    | Double
    | Triple

sizeToString : Size -> String
sizeToString size =
    case size of
        Single -> "single"
        Double -> "double"
        Triple -> "triple"
```

And we do the same thing with the colors.

```elm
type Color
    = Yellow
    | Gray
    | White

colorToString : Color -> String
colorToString color =
    case color of
        Yellow -> "bg-yellow"
        Gray   -> "bg-gray"
        White  -> "bg-white"
```

Now if we try to make a button like `cell Single Purple "1"`, the compiler will give us a nice error warning.

```txt
-- NAMING ERROR --------------- /home/ryan/projects/elm-calculator/src/Main.elm


I cannot find a `Purple` variant:

60|     cell Single Purple "1"
                    ^^^^^^
These names seem close though:

    Triple
    Double
    Single
    True

```

Or fix typos like in `cell Single Yelow "1"`.

```txt
-- NAMING ERROR --------------- /home/ryan/projects/elm-calculator/src/Main.elm


I cannot find a `Yelow` variant:

60|     cell Single Yelow "1"
                    ^^^^^
These names seem close though:

    Yellow
    EQ
    Err
    False

```

This is the power of the type system. If you can understand this one feature of Elm you will begin to really see why people like the language. The compiler becomes your best friend.

## The Input box

The last thing we need is an input area on top of the buttons.

```elm
inputBox : Float -> Html Msg
inputBox num =
    div
        [ class "input-box"
        ]
        [ text <| String.fromFloat num
        ]
```

## Putting it all together

```elm
view : Model -> Html Msg
view model =
    div []
        [ h1 [ class "h1" ] [ text "RPN Calculator" ]
        , div
            [ class "calculator" ]
            [ inputBox 78.9 -- dummy value for now
            , section
            ]
        ]
```

```elm
section : Html Msg
section =
    div [ class "section" ]
        [ cell Single Gray "←" -- top row
        , cell Single Gray "C"
        , cell Single Gray "CE"
        , cell Single Yellow "÷"
        , cell Single White "7" -- 2nd row
        , ...
        , ...                   -- 3rd row
        , cell Single White "0" -- 4th row
        , cell Single White "."
        , cell Double Yellow "Enter"
        ]
```

```elm
inputBox : Float -> Html Msg
inputBox num =
    div
        [ class "input-box"
        ]
        [ text <| String.fromFloat num
        ]
```

Now that we have something looking decent, we can start on programming the behavior of our calculator.
