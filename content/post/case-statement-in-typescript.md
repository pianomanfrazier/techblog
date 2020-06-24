+++
title = "Case Statement in Typescript"
date = 2020-06-24T12:33:03-06:00
draft = false
markup = "mmark"
tags = ["typescript", "functional programming"]
+++

One of my favorite features of functional languages like Elm is pattern matching. Here is an example:

```elm
type State
	= Loading
	| Error
	| Ok

stateToString : State -> String
stateToString state =
	case state of
		Loading ->
			"Loading ..."

		Error ->
			"Something went wrong."

		Ok ->
			"It's all good"

```

I found a simple way to provide an action for every case of a TypeScript enum.

```ts
enum State {
	Loading,
	Error,
	Ok,
}

const STATE_MAP = {
	[State.Loading] : () => "Loading ...",
	[State.Error] : () => "Something went wrong.",
	[State.Ok] : () => "It's all good",
}

function stateToString(state : State) : string {
	return STATE_MAP[state]();
}

```
[Link to TypeScript playground](https://www.typescriptlang.org/play/#code/KYOwrgtgBAygLgQzsKBvAUASADIHsEAmAliAOYA0WAogE4242WYDyA1pQL7roDGuIAZziwAKgEERVAPoBZMQAUoAXjRYA2vCTAAdHkIlSAXSgAuKAAoAlMoB8UAER7iZKNrf2mGxMm216NYzMrWwcYXAhgOAALAygAd1BhOPoybQ91TR82QItrJTt7AEk4AHIBKAQAG0qoUlxcAnSudAAzMBAeOCJ+KCEtEVx4GgNzPuRTWG9gazMhYZcMTBpIsBoQUQlpOXk1MeBDKwBudGa+QVxKnUrcUlGpgaGRzJ0nA0tLQ6A)

Usually TypeScript won't allow bracket notation to access properties of an object. In this case the compiler knows that all cases of `State` are accounted for and can thus be used to index into the object.

Try removing one of the states from `STATE_MAP` and the TypeScript compiler will yell at you.

```txt
Element implicitly has an 'any' type because expression of type 'State' can't be used to index type '{ 0: () => string; 1: () => string; }'.
  Property '[State.Ok]' does not exist on type '{ 0: () => string; 1: () => string; }'.
```
