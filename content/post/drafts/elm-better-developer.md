+++
title = "Elm Can Make You A Better Developer"
date = 2020-02-06T23:47:42-07:00
draft = true
markup = "mmark"
+++

After writing Elm for over 2 years I have noticed a dramatic change in how I write code.

I write Java and JavaScript (VueJS, NodeJS, Electron) at work. I don't get to use elm. I'm working on it. However my elm skills have brought some good changes to my code.

- no for loops
- explicitly state all side effects
- the Type system
- small composable functions is easier to test

## What is Functional Programming (FP)

## Simple Tooling

- no webpack or complicated build processes (although you still can if you want to)
- elm-live (my own [elm-starter](https://github.com/pianomanfrazier/elm-starter) on GitHub)

Here are some stats on my Know Your Theory music app.

Ran `find . -name '*.elm' | xargs wc -l` in my `src` directory. 18421 lines of elm code.

243 lines of JavaScript. And some extra JS for netlify Lambda functions.


```txt
$ du -h --max-depth=1 ./ | sort -hr

470M	./
411M	./node_modules
39M	    ./functions
11M	    ./elm-stuff
4.6M	./.git
3.7M	./build
720K	./src
92K	    ./public
32K	    ./tests
8.0K	./.netlify
```

## Types

## Side Effects

## State Machines

## The Elm Architecture

Simple data flows.

Reduce duplication of state. One source of truth. Richard Feldman's [talk](https://www.youtube.com/watch?v=x1FU3e0sT1I)

## Modules

## Hard to always sell Elm 

Legacy projects. Existing code.

Administration nervous about new technology. Other developers fear of the unknown. Syntax looks foreign.

Worried about long term maintenance. They fear they might not find other Elm developers.

## Package Management and Dependencies

- 3rd party code can't have unintended side effects. Impossible to make a network request unless you call a side effect.
- secure by default
- versioning in Elm moves very slow and methodical. No breaking changes and churn every month.

## Community

- elm slack
- elm discourse
- twitter 

## Come participate

Really beginner friendly. Most conferences reserve spots for beginners.

Find good answers on slack and on Discourse. Some really well designed and thought out APIs in libraries like elm-css, remote-data, ...
