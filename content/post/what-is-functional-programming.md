+++
title = "What Is Functional Programming"
date = 2020-10-20T09:55:15-06:00
draft = false
markup = "mmark"
tags = ["functional programming", "javascript"]
+++

In my day to day work as a software engineer I do not have the luxury of using a functional language like Haskell or Elm, however I have learned a lot from Elm that has changed how I program in JavaScript or Python. Here is a run-down of some of the concepts I have learned from writing 3000+ lines of Elm code.

Here are some of my projects written entirely in Elm.

- [Know Your Theory](https://knowyourtheory.com/) - a music theory drill app
- [Elm Piano Teacher](https://elm-piano-teacher.netlify.app/) - a midi keyboard interactive tool
- [Music Scale Explorer](https://frazierpianostudio.com/resources/scale-explorer/) - interactive graph of musical scales
- [Circle of 5ths Explorer](https://frazierpianostudio.com/resources/circle-of-fifths-explorer/) - interactive circle of 5ths with key signatures and keyboard
- [Uke Chord Finder](https://frazierpianostudio.com/resources/ukulele-chord-finder/) - interactive Ukulele chord finder

## FP Vocabulary

Here is a list of common terms that come up when learning functional programming (FP). I will discuss many of them in this article.

- Pure Function
- Side Effect
- Referential Transparency
- Mutable/Immutable
- Currying
- Monad
- Algebraic Data Types
- Variant
- Lambda Calculus

## Pure Functions

What is a pure function?

A function is said to be pure if 1) given the same arguments it always returns the same result and 2) the function has no side effects.

```js
function add(a,b) {
    return a + b;
}

function impureAdd(a,b) {
    return a + b + c;
}

console.log(add(1,2)) // 3
// console.log(impureAdd(1,2)) // EXPLOSION!!!
c = 1
console.log(impureAdd(1,2)) // 4
c = 2
console.log(impureAdd(1,2)) // 5
```

## What is a side effect?

A side effect is something that occurs as a result of a function call that does not get returned from the function.

## Referential Transparency

An expression is said to be **referentially transparent** if the evaluation of the function can be replaced with its return value and not effect the program's behavior.

```js
result = add(2,3) + 5 // result == 10
result = 5 + 5 // result == 10
```

By contrast, if the function call cannot be replaced by the output then the function is said to be **referentially opaque**.

## No For Loops?

In a pure functional language like Haskell or Elm, you will notice there are no for loops. You must process all lists with `map`, `reduce`, and `filter` (among others).

```js
list = [1,2,3,4]

// Imperative
listTimesThree = []
for(i = 0; i < list.length; i++) {
    listTimesThree.push(list[i] * 3)
}

// Declarative
listTimesThree = list.map(x => x * 3)
```

What are all the things that could go wrong in a for loop?

- mental burden of parsing a for loop (What does it do? Is it correct?)
- thread mutate the processing list
- mutate the iterator variable `i`
- out of range list access

## Currying

> currying is the technique of converting a function that takes multiple arguments into a sequence of functions that each take a single argument.
> 
Quote: -- Wikipedia [Currying](https://en.wikipedia.org/wiki/Currying)

```js
add = a => b => a + b

addOne = add(1) // What does this return?

add(1)(2) // 3

list.map(x => addOne(x)) // [2,3,4,5]
```

How is currying useful?

How about providing different ways to render a list? Currying makes it easy to make functions from other functions.

```js
list = ['Fries', 'Hamburger', 'Shake']

latexListHead = x => `\\begin\{itemize\}\n${x}\n\\end\{itemize\}`
latexItem = x => `\\item ${x}`

htmlListHead = x => `<ul>\n${x}\n</ul>`
htmlItem = x => `<li>${x}</li>`

mdListHead = x => x // The identity function
mdItem = x => `- ${x}`

renderList = headFn => itemFn => list => headFn(list.map(x => itemFn(x)).join('\n'))

latexList = renderList(latexListHead)(latexItem) // LaTeX render function
webList = renderList(htmlListHead)(htmlItem) // HTML render function
mdList = renderList(mdListHead)(mdItem) // Markdown render function

console.log(webList(list))
console.log(latexList(list))
console.log(mdList(list))
```

Now what if you wanted several styles of lists, like a fancy web list.

```js
htmlListHead = classes => x => `<ul class='${classes.join(' ')}'>\n${x}\n</ul>`

bigBlueListHead = htmlListHead(['big', 'blue'])
smallRedListHead = htmlListHead(['small', 'red'])

webList = renderList(bigBlueListHead)(htmlItem)

console.log(webList(list))
```

There are other uses for currying like generating a range of math plots. See my post on [creating beautiful math homework](https://pianomanfrazier.com/post/create-beautiful-math-homework/). And here is the [python file](https://pianomanfrazier.com/files/plots/lognorm.py)

## Exception Throwing is a Side Effect

> The reasoning is that I consider exceptions to be no better than “goto’s”, considered harmful since the 1960s, in that they create an abrupt jump from one point of code to another. In fact they are significantly worse than goto’s
> 
> 1. **They are invisible in the source code.**
> 1. **They create too many possible exit points** for a function.
> 
Quote: -- Joel Spolsky at [Joel on Software](https://www.joelonsoftware.com/2003/10/13/13/)

I wrote about this topic in a previous blog post [Exceptions Considered Harmful](https://pianomanfrazier.com/post/exceptions-considered-harmful/).

## JavaScript helper libraries

JavaScript is notorious for an inconstant API. What functions are immutable? For example, `map()` creates a new array whereas `sort()` and `reverse()` *mutate* the array *in place* and returns the mutated array. This inconsistency is a mental burden. Therefore there is a need for libraries like [Ramda](https://ramdajs.com/docs/).

```js
list = [4,2,3,1]
sortedList = list.sort()
console.log(list) // [4,2,3,1] or [1,2,3,4]?
```

Compare with [Ramda's sort](https://ramdajs.com/docs/#sort).

### JS Libraries

- [Ramda](https://ramdajs.com/docs/)
- [neverthrow](https://github.com/supermacro/neverthrow)
- [immutableJS](https://immutable-js.github.io/immutable-js/docs/#/)

### TypeScript Libraries

- [purify-ts](https://gigobyte.github.io/purify/)
- [fp-ts](https://gcanti.github.io/fp-ts/)
- [true-myth](https://true-myth.js.org/)

## Other Resources

- [[Blog Post] A practical guide to functional programming](https://codewords.recurse.com/issues/one/an-introduction-to-functional-programming)
- [[YouTube] Why Isn't Functional Programming the Norm? – Richard Feldman](https://youtu.be/QyJZzq0v7Z4)
- [[Forum Post] Explain Monads Like I'm Five](https://dev.to/bobbypriambodo/comment/j27)
- [[YouTube] Lambda Calculus - Fundamentals of Lambda Calculus & Functional Programming in JavaScript](https://youtu.be/3VQ382QG-y4)
- [[Blog Post] Some good discussion and some resources](https://elmbits.com/issue-40-functional-programming/)