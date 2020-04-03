+++
title = "Elm Calculator Part 10 - Testing"
date = 2020-05-15
draft = false
markup = "mmark"
tags = ["elm", "elm calculator book"]
description = "Learn how to build a calculator with elm from scratch."
socialImage = "img/elm-calculator/elm-calc-splash.png"
socialImageAlt = "Elm Calculator"
+++

{{< elmCalcBookTOC num="10">}}

- ***browse:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/tree/master>
- ***diff:*** <https://gitlab.com/pianomanfrazier/elm-calculator/-/commit/c5c32b5c0566b8034fc723e8e0f7ffdf2f6db70c>
- [elm-test](https://package.elm-lang.org/packages/elm-explorations/test/latest)
- [elm-program-test](https://package.elm-lang.org/packages/avh4/elm-program-test/latest)

*Note: ellie-app does not support splitting out your code into modules and files. So there is no ellie link for this chapter.*

We will be using a newer Elm package called [elm-program-test](https://package.elm-lang.org/packages/avh4/elm-program-test/latest/). It allows us to test our application as a whole. It will stand up the application and allow us to test it as if a user were clicking through the application.

## Some Refactoring

In order to test our program we need to expose some of our functions in `Main.elm`.

```elm
module Main exposing (Model, Msg, init, main, update, view)
```

We also need to make our elm program use `Browser.document` instead of `Browser.element` since we will be using `ProgramTest.createDocument`.

Elm has different ways to create a program. `Browser.element` is good for creating a small elm application that you embed into the page on a specific DOM node. What if you want Elm to take over the whole page? That is what `Browser.document` is for. See the [elm-guide](https://guide.elm-lang.org/webapps/) for more information about `Browser.element` and `Browser.document`.

*Note: Since creating this book, I have since learned that you can use `ProgramTest.createElement` instead and we wouldn't need to do this refactor.*

Refactoring is lovely in Elm. Our first step is to start at the highest level of our refactor and let the compiler tell us what to change. So start by changing the `main` function to return a `Browser.document` instead of a `Browser.element`.

The only thing we need to change for this refactor is the `view` function to return a `Browser.Document` instead of `Html`.

The difference with `Browser.Document` is that the view function now needs a record with a `title` and a `body` field. We can place our previous view html stuffs inside the body field.

```elm
view : Model -> Browser.Document Msg
view model =
    { title = "Elm Calculator"
    , body =
        [ div []
            [ h1 [ class "h1" ] [ text "RPN Calculator" ]
            , ...
```

## Write the test

First we need to install everything we need. We need the `elm-test` command line program because we need something to launch and execute our tests. This is our test runner if you have used something like pytest.

```bash
npm install --save-dev elm-test
```

We also need to install the corresponding elm packages as well.

```bash
elm install elm-explorations/test
elm install avh4/elm-program-test
```

To get a simple example test run `elm-test init` in your project folder.

```bash
npx elm-test init
```

Now run the test you just created.

```bash
npx elm-test
```

You should get a test report.

Create a new file in the tests directory called `CalculatorTest.elm`.

The test is short (less than 40 lines of code). I'll walk through the most interesting part.

```elm
all : Test
all =
    describe "basic arithmetic"
        [ test "20 × 3 = 60" <|
            \() ->
                start
                    |> clickCalcBtn "2"
                    |> clickCalcBtn "0"
                    |> clickCalcBtn "←"
                    |> clickCalcBtn "3"
                    |> clickCalcBtn "×"
                    |> expectViewHas
                        [ text "60"
                        ]
        ]
```

This simulates a user clicking on the number and operator buttons. It then checks that the number 60 is somewhere on the page. Try playing with this and adding another test.

The next and last chapter will cover deploying our Elm application to netlify. If you got this far, congratulations! We're almost finished. I get a lot of satisfaction with web projects because they are so easy to share with the world. I'll show you how in the next chapter.
