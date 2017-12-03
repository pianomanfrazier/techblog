---
title: "First Steps With Elm"
date: 2017-12-01T14:16:23-07:00
draft: false
markup: "mmark"
---

For my computer languages class I decided to evaluate Elm. Having not spend as much time on functional languages I figured this would be a good oportunity to expand my functional programming brain. The apps are the result of doing the exercises found in the Elm documentation.

## Forms 

Here is a simple app I wrote to play around with Elm. I augmented the form tutorial from the [Elm Docs](https://guide.elm-lang.org/architecture/user_input/forms.html). The source can be found [here](https://github.com/pianomanfrazier/CS4700_language_evaluation/blob/master/form.elm).

The exercises in the tutorial were to augment the form in the following ways:

- Check that the password is longer than 8 characters.
- Make sure the password contains upper case, lower case, and numeric characters.
- Add an additional field for age and check that it is a number.
- Add a "Submit" button. Only show errors after it has been pressed.


{{< iframe src="https://pianomanfrazier.github.io/CS4700_language_evaluation/form.html" height="35em">}}


## Random Dice

The random tutorial can be found [here](https://guide.elm-lang.org/architecture/effects/random.html).

I augmented the example provided in the following ways:

- show image for dice
- take input from user and validate
- allow arbitrary number of dice each with it's own random number

Again the source is found on GitHub [here](https://github.com/pianomanfrazier/CS4700_language_evaluation/blob/master/random.elm).

{{< iframe src="https://pianomanfrazier.github.io/CS4700_language_evaluation/random.html" height="12em">}}

