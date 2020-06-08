+++
title = "Elm Calculator Part 5 - Adding Decimal Support"
date = 2020-04-10
draft = false
markup = "mmark"
tags = ["elm", "functional programming", "elm calculator book"]
description = "Learn how to build a calculator with elm from scratch."
socialImage = "img/elm-calculator/elm-calc-splash.png"
socialImageAlt = "Elm Calculator"
+++

{{< elmCalcBookTOC num="5">}}

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/v0.5>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/compare/v0.3...v0.5>
- ***ellie:*** <https://ellie-app.com/72nWGqwYmXSa1>

In the last chapter, we input numbers as floats and did some math to shift the numbers around. This will be a big problem when we start to introduce decimals.

## Failed attempt still using floats

You'll notice that I skipped v0.4 of the app. This was my failed attempt to keep using math to manipulate the user input number.

If we try to do something similar with floats we get the following.

```elm
> 0.1 + 0.02
0.12000000000000001 : Float
```

Here is my code for reference.

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/v0.4>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/compare/v0.3...v0.4>
- ***ellie:*** <https://ellie-app.com/72nWgBWynwRa1>

## Change inputNumber to String

Again like before, I like to start a new feature or refactor by changing the model.

```elm
type alias Model =
    { stack : List Float
    , currentNum : String
    }

initialModel : Model
initialModel =
    { stack = []
    , currentNum = "0"
    }
```

As you can see in the model only the `currentNum` is a String. At some point we need to parse our input into an actual number so we can do operations on it. We'll do that when we push the number to the stack.

The way we'll parse is using `String.toFloat`. Let's play around with this function in the elm repl. If you have elm installed, go to a terminal and type `elm repl`.

As of writing this book the official Elm Guide <https://guide.elm-lang.org/core_language.html> has a live repl you can play with on the webpage. No installation necessary. This is helpful if you have been following along on ellie-app.

```elm
> String.toFloat
<function> : String -> Maybe Float
```

Why does it return a `Maybe Float`? What happens if we try to give this function a string that isn't a number?

```elm
> String.toFloat "abcd"
Nothing : Maybe Float
> String.toFloat "123.456"
Just 123.456 : Maybe Float
```

This is Elm's way of dealing with uncertainty. If it can't parse it, it will return a `Nothing` otherwise it will return a `Just <some float>`. Let's look at some other examples and then we'll explore this `Maybe` thing a bit more.

Again, Elm types are powerful but take some getting used to.

### Parse float in JavaScript and Python

Here is the same thing in JavaScript.

```js
» parseFloat("abcd")
← NaN
» parseFloat("123.456")
← 123.456
```

And again in Python.

```python
>>> float("123.456")
123.456
>>> float("abcd")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: could not convert string to float: 'abcd'
```

No matter what language we are using, we need to deal with these kind of errors. Elm uses the `Maybe` type. JavaScript returns `NaN`, not a number. And Python throws a `ValueError`.

## The Maybe type

The Maybe type is something that took me a while to understand. I had been writing quite a bit of Elm code but I just kind of ignored it. Hopefully I can make it click for you sooner.

Let's play around with the `Maybe` type in the elm repl.

The `Maybe` type is defined as the following.

```elm
type Maybe
    = Just a
    | Nothing
```

What this means is that `Just` can hold any value.

```elm
> Just 1
Just 1 : Maybe number
> Just 1.2
Just 1.2 : Maybe Float
> Just "123.456"
Just "123.456" : Maybe String
> Just (Just 1)
Just (Just 1) : Maybe (Maybe number)
> Just Nothing
Just Nothing : Maybe (Maybe a)
```

And `Nothing` is just nothing.

```elm
> Nothing
Nothing : Maybe a
```

So how is this useful?

Let's go back to parsing strings. The compiler will make sure we deal with the case our string doesn't parse into a number.

```elm
parsedNumber = String.toFloat model.currentNum
```

What is the type of `parsedNumber`? It's a `Maybe Float`. Meaning it can be `Just Float` or it can be `Nothing`. We can now pattern match on these two cases.

```elm
case parsedNumber of
    Nothing ->
        -- deal with the case it doesn't parse
    Just num ->
        -- yay it parsed! Do something with num
```

This is how Elm in practice has ***no runtime errors***. The compiler will help us to think about uncertainty and require us to deal with it.

Now that we know about `Maybe` we can continue on.

## Push the parsed float to the stack

Now that we can parse strings to floats we can update the model when a user clicks "Enter".

```elm
update : Msg -> Model -> Model
update msg model =
    case msg of
        ...

        Enter ->
            let
                maybeNumber =
                    String.toFloat model.currentNum
            in
            case maybeNumber of
                Nothing ->
                    { model | error = Just "PARSE ERR" }

                Just num ->
                    { model
                        | stack = num :: model.stack
                        , currentNum = "0"
                    }
```

The compiler will now tell us that there is no `error` field in our model. So let's add that.

```elm
type alias Model =
    { stack : List Float
    , currentNum : String
    , error : Maybe String
    }

initialModel : Model
initialModel =
    { stack = []
    , currentNum = "0"
    , error = Nothing
    }
```

We might not have an error, so we'll make the error a `Maybe`.

We also need to display the error if it exists. Let's pattern match on the error in our view to display the error.

```elm
case model.error of
    Nothing ->
        inputBox (text model.currentNum)

    Just err ->
        inputBox (span [ class "error" ] [ text err ])
```

## Input the decimal

Inputing the decimal requires some special treatment. Users should not be able to put in multiple decimals into a number.

First add the message.

```elm
type Msg
    = InputOperator Operator
    | ...
    | SetDecimal
```

Then handle the message in the update.

```elm
update : Msg -> Model -> Model
update msg model =
    case msg of
        SetDecimal ->
            if String.contains "." model.currentNum then
                model

            else
                { model | currentNum = model.currentNum ++ "." }
```

Now we need to be able to input negative numbers and we will have a fully functioning calculator. The next chapter will add negative number support.
