+++
title = "Courses"
lastUpdate = true
date = "2019-12-12"
+++

## Learn Elm by example --- Code a calculator using Elm from scratch

*Update March 14, 2020: I have decided to publish this book also here on my blog as a series of blog posts. See the ["elm calculator book"](/tags/elm-calculator-book/) tag for all published chapters. If you benefited from my work please support me by purchasing the book [on Gumroad](https://gum.co/NwMtt).*

![Elm Calculator Book Cover](/img/courses/elm-calculator-book-cover.jpg)

This book uses Elm version 0.19.

<script src="https://gumroad.com/js/gumroad.js"></script>
<a class="link-btn text-large bg-red" href="https://gumroad.com/l/NwMtt">Get the book</a>


- [Table of Contents](#table-of-contents)
- [PDF sample](/files/elm-calculator-sample.pdf)
- [Project demo](https://elm-calculator.netlify.com/)

### Final Calculator Demo

{{< vimeo 374995850 >}}

### Using the course materials

{{< vimeo 375031361 >}}


### Things covered in the course

- CSS with external style sheet
- elm-live development server
- custom keyboard input events
- key combo events (like alt-shift-delete)
- testing with elm-program-test and elm-test
- deploy the application with Netlify

### What's included?

1. You get an **ebook** (63 page PDF, mobi, and epub) explaining step by step how to build the app.
1. Each chapter has the resulting code in [ellie-app](https://ellie-app.com)
1. You get access to the **code**. Each chapter is tagged with git so you can see the app in its current state while we build it.
1. **HTML diffs**. You can see a diff of the code each chapter and see the changes as the app is developed.

### Table of Contents

-   Introduction
    -   Who am I?
    -   Learn by doing
    -   Who is this book for?
    -   What will be covered?
    -   How to use this book and provided
        resources
        -   How to use the git bundle
        -   What is ellie app?
    -   What are we going to build?
    -   The Stack
    -   Why is a traditional calculator
        harder?
    -   Binary and Syntax Trees
        -   Process the tree
        -   Process tree on the stack
-   Setup the project
    -   Setup your editor
    -   Initialize elm and npm
    -   The Html
    -   The CSS
    -   A Minimal Elm Program
    -   Run the project
    -   Setup Shortcut
-   The layout
    -   The buttons
    -   The buttons in Elm
    -   Elm Types for the win
    -   The Input box
    -   Putting it all together
-   Program Basic Operations
    -   Display the stack
    -   Input numbers
        -   Homework
    -   Push numbers onto the stack
    -   Operate on the stack
        -   Pattern match on a list
        -   Handle the model update
        -   `let ... in` blocks
        -   Get the operator function
    -   Your homework solutions
    -   Input larger numbers
    -   Clear and back buttons
-   Add Decimal Support
    -   Failed attempt still using
        floats
    -   Change inputNumber to String
        -   Parse float in JavaScript and
            Python
    -   The Maybe type
    -   Push the parsed float to the
        stack
    -   Input the decimal
-   Add Negative Number
-   Add Dirty State
-   Add Keypad Input
    -   Refactor to use Elm
        subscriptions
        -   Change to `Browser.element`
    -   Add subscriptions
    -   Handle the key events
-   Add Combination Keys
-   Testing
    -   Some Refactoring
    -   Write the test
-   Deploy with Netlify
    -   Add deploy script
    -   Configure Netlify 
