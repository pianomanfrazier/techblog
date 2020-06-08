+++
title = "Exceptions Considered Harmful"
date = 2020-06-05T13:32:21-06:00
draft = false
markup = "mmark"
+++

> The reasoning is that I consider exceptions to be no better than “goto’s”, considered harmful since the 1960s, in that they create an abrupt jump from one point of code to another. In fact they are significantly worse than goto’s
> 
> 1. **They are invisible in the source code.**
> 1. **They create too many possible exit points** for a function.
> 
Quote: -- Joel Spolsky at [Joel on Software](https://www.joelonsoftware.com/2003/10/13/13/)

How do we deal with uncertainty in our code?

If something goes wrong in our code we need to know about it, preferably without crashing our program. When I come back to the code months later or I am using someone elses code I want the compiler to help me handle errors gracefully.

Here are several patterns that I have seen, my own code included.

## Pattern 1 - return true or false

```ts
function doWork() : boolean {
    // do some SIDE EFFECT
    let result = doWork();
    this.some_member_variable = result;
    
    let success = result !== null;
    if (success) {
        return true;
    } else {
        return false;
    }
}
```

Side effect's make it harder to reason about what your code does. Pure functions, side effect free functions, are also easier to test. Also if there was a failure you can't send a message to the function caller.

## Pattern 2 - return null if failed

In the next examples, let's assume that our database stuff are synchronous to make things a bit simpler.

Instead of returning true or false we could return the value or a null value.


```ts
import DB from 'my-synchronous-database';

function getUser(id : UserID) : User | null {
    const user = DB.getUserById(id);

    if (user) {
        return user;
    } else {
        return null;
    }
}
```
This is slightly better, now that we don't have a side effect. However we still have no error message and we better make sure to handle that returned `null` value or our program will explode.

This eliminates the side effect but now creates a new problem.

> I call it my billion-dollar mistake. It was the invention of the null reference in 1965. At that time, I was designing the first comprehensive type system for references in an object oriented language (ALGOL W). My goal was to ensure that all use of references should be absolutely safe, with checking performed automatically by the compiler. But I couldn't resist the temptation to put in a null reference, simply because it was so easy to implement. This has led to innumerable errors, vulnerabilities, and system crashes, which have probably caused a billion dollars of pain and damage in the last forty years.
Quote: -- Tony Hoare at QCon London 2009, see [wikipedia](https://en.wikipedia.org/wiki/Tony_Hoare#Apologies_and_retractions)


## Pattern 3 - throw exception

Our other choice is to throw an exception.

```ts
import DB from 'my-synchronous-database';

function getUser(id : UserID) : User {
    const user = DB.getUserById(id);

    if (user) {
        return user;
    } else {
        throw new Error(`Cannot find the user by id ${id}`);
    }
}
```

Now we have an error message but now we introduced another side effect: the exception. If you don't catch the exception, in most cases, your program will crash. 

In JavaScript there is no way I can tell by using a function if it will throw or not. Java helps because the tooling will warn you that you are using a throwable function. Still no one likes seeing a `nullExceptionPointer` in Java land. Not fun.

## Pattern 4 - return a result type

What if we wanted to both return an error message if something goes wrong and also not introduce side effects.

This is the `Result` type. This is also called the `Maybe` type.

This thing is baked into the standard library of newer programming languages like Rust and Elm. We have [std::result](https://doc.rust-lang.org/std/result/) in Rust and the [Maybe Type](https://guide.elm-lang.org/error_handling/maybe.html) in Elm. Most newer languages don't implement exceptions and treat **errors as data** like [Go](https://blog.golang.org/go1.13-errors), [Rust](https://doc.rust-lang.org/book/ch09-00-error-handling.html), and [Elm](https://guide.elm-lang.org/error_handling/).

Since this article is using TypeScript, I'm going to use the library [neverthrow](https://github.com/supermacro/neverthrow) but there are others to choose from. This will also work in plain JavaScript too.

Let's look at neverthrow's `Result` type.

From the neverthrow [docs](https://github.com/supermacro/neverthrow#synchronous-api):


```ts
type Result<T, E> = Ok<T, E> | Err<T, E>
```

`Ok<T, E>`: contains the success value of type `T`

`Err<T, E>`: contains the failure value of type `E`

And here it is in action.

```ts
import { Result, ok, err } from 'neverthrow';
import DB from 'my-synchronous-database';

type DBError = string; // type alias for error message

function getUser(id : UserID) : Result<User, DBError> {
    const user = DB.getUserById(id);

    if (user) {
        return ok(user); // return instance of OK
    } else {
        return err(`Cannot find the user by id ${id}`); // return instance of Err
    }
}
```

This is an improvement because there are now **no side effects** and we can return an **error message** if something goes wrong. I know that when I use this function I will always get a `Result`.

```ts
const userID = 1;
const userResult : Result<User, DBError> = getUser(userID);

if (userResult.isOK()) {
    console.log(userResult.value);
} else {
    console.log(userResult.error);
}
```

If you try to retrieve `userResult.value` before you have checked `isOK()` the TS compiler won't let you. Pretty awesome.

## JavaScript tooling

[tslint-immutable](https://github.com/jonaskello/tslint-immutable) is a plugin for TSlint that has several options to prevent throwing exceptions. See this set of functional programming rules for TSlint [here](https://github.com/jonaskello/tslint-immutable#no-throw). Enable `no-throw` and `no-try`.

And [here](https://github.com/jonaskello/eslint-plugin-functional) is a similar set of rules for eslint.

## Other libraries and languages

These ideas are also being explored in other languages. Here are some libraries I found.

[C++ std::optional](https://en.cppreference.com/w/cpp/utility/optional), `optional<T>`, is a safer way than just returning `null`.  The optional can be empty or it can hold a value of type `T`. It does not hold an error message.

[C++ Result](https://github.com/oktal/result) is a header only library that implements Rust's `Result<T, E>` type. This type can hold the value or an error.

[Python result](https://github.com/dbrgn/result) another Rust inspired result type.

If you want to explore more typed functional programming in TypeScript, check out [fp-ts](https://gcanti.github.io/fp-ts/).
