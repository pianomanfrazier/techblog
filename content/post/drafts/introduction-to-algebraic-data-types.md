+++
title = "Introduction to Algebraic Data Types"
date = 2020-07-07T08:46:15-06:00
draft = true
markup = "mmark"
tags = ["typescript", "functional programming", "elm"]
+++

The demo code:

- Elm on [ellie-app](https://ellie-app.com/9my7fGjW3Rsa1)
- TypeScript on [TypeScript playground](https://www.typescriptlang.org/play/#code/IYIwzgLgTsDGEAJYBthjAgggOwJYFthkEBvAKAEhRIZ4EwAHAU2AGsAKASgC57pdsAcwDcZAL5kyKNBgDCwREwAeEJtgAmGHASKlKjFhx58oAwXooUoTCAFco2BACJ8TAPYB3J6IoSJU1HQEABE3c2VVDS08QmJyCgM2Ll4aMwsrG3tHJxBgKFZvSj9JMgB6UqRgbAByREJWJgQqpvBoOERtWLKK2DdsSAR8AE9O3QBeBGwmDywYoi5RXv66oflECamZtYXJJbA3ZCYAOmQw9mG1o8SjTlEyADNbbHhcPoR7piZ1UeR2Kp1kLwfsZUkILNY7A5nBAABZVVgYe5uKAIWGNJFudQAQmcCAA1E05sgrswkrdxLs+vtDiczh8vj9zqsFJxyWQBKooPc4I0fgAlJi9KDqCwQIbMAD6QKJPmwwFcKX4QlE-j2iA+yFwSmlAIFQpFE3iYslvE2CG2nAANJQ5QrnAAxJiapROa1iURAA#)

One of the concepts in functional programming that trips up beginners is Algebraic Data Types (ADT). I am going to go through some examples and relate it to some concepts that would be familiar to Object Oriented Programming (OOP).

For this introduction I will be using TypeScript for the OOP examples and Elm for the functional examples.

Let's start with an example.

```elm
type Animal = Cat | Dog
```

An `Animal` can be either a `Cat` or a `Dog`, but you can't just be an animal. You need to be a type of an animal, the classic "is a" relationship. This is a bit similar to abstract classes in OOP languages.

```ts
abstract class Animal {
	abstract speak(): string;
}

class Cat extends Animal {
	speak(): string {
		return "meow";
	}
}

class Dog extends Animal {
	speak(): string {
		return "bark";
	}
}

// can't make an abstract Animal
// const myAnimal = new Animal();
const myCat = new Cat();

console.log(myCat.speak());
```

Now you could make a function that generically takes any type of `Animal` as an argument.

```ts
function feedAnimal(animal: Animal): string {
	return "thanks for the food! " + animal.speak(); 
}

console.log(feedAnimal(myCat));
```

Similarly, let's translate this to Elm.

```elm
animalSpeak : Animal -> string
animalSpeak animal =
    case animal of
        Cat ->
            "meow"

        Dog ->
            "bark"
```

```elm
feedAnimal : Animal -> string
feedAnimal animal =
    "thanks for the food! " ++ animalSpeak(animal)
```

## Why are they useful?

- Easy refactors. You can catch problems at compile time.
- Can constrain the problem domain by types. See [Making Impossible States Impossible](https://www.youtube.com/watch?v=IcgmSRJHu_8).

You can do this by leveraging classes and using them as types but it is a lot easier and compact to have a robust type system built into the language. There is usually a lot of boiler code needed to get some better type safety in languages like Java or TypeScript. See [this stackoverflow question](https://stackoverflow.com/questions/21034017/how-do-you-emulate-adts-and-pattern-matching-in-typescript).

```elm
zoo : List Animal
zoo = [ Cat, Dog ]

feedZoo : List Animal -> List String
```

## Animal Names

Since there are no classes or member variables in a language like Elm we use records instead.

```elm
type alias AnimalRecord =
    { type_ : Animal
    , name : String
    }

felix = AnimalRecord Cat "Felix"
```

When I write TypeScript I actually prefer using interfaces instead of defining classes. The reason for this preference is that I like to separate the structure of the data from the operations on that data.

> I will, in fact, claim that the difference between a bad programmer 
and a good one is whether he considers his code or his data structures 
more important. Bad programmers worry about the code. Good programmers 
worry about data structures and their relationships.
>
Quote: -- Linux Torvalds, see https://lwn.net/Articles/193245/

So it would look like this:

```ts
interface AnimalRecord {
    type_ : Animal;
    name : string;
}

const felix : AnimalRecord = {
    type_: new Cat(),
    name : "Felix",
};
```

## Immutability

- for classes https://www.typescriptlang.org/docs/handbook/classes.html#readonly-modifier
- for interfaces https://www.typescriptlang.org/docs/handbook/utility-types.html#readonlyt

## An example with error handling

I wrote about this in another post [Exceptions considered harmful](https://pianomanfrazier.com/post/exceptions-considered-harmful/).

Let's use the `Either` type from [purify-ts](https://gigobyte.github.io/purify/adts/Either) to deal with errors in our code. The TypeScript compiler can help us if we give it the right information.

```ts
// might be one of an Error or a result string
function getUsernameFromDB(id : number) : Either<Error, string> {
    const username : string;
    const error : Error;
    try {
        username = DB.getUserById(id);
    } catch(e) {
        error = e;
    }

    if (error) {
        return Left(error); // error values are always Left
    } else {
        return Right(username); // Right is "right" or the correct value
    }
    // could use Either.encase instead https://gigobyte.github.io/purify/adts/Either#encase
    // return Either.encase(() => DB.getUserByID(id));
}

const result = getUsernameFromDB(1);
// now the compiler forces you to deal with the error
result.caseOf({
    Left: error => error.toString(),
    Right: value => value,
})
```

caseOf statements for
- Either https://gigobyte.github.io/purify/adts/Either#caseOf
- Maybe https://gigobyte.github.io/purify/adts/Maybe#caseOf
