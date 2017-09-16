---
title: "Drawing With Postscript"
date: 2017-09-16T12:03:58-06:00
draft: false
---

Some notes about drawing with PostScript. The documentation is pretty sparse out on the web. Here I will document some basic usage to get you drawing more than just a couple of squares.

## Getting started

If you are on Linux, then just write a `.ps` file and open it with `evince` or `xreader` or whatever your default document reader is. You can also get some debugging information by opening your file in the command line with ghost script.

```bash
gs <filename.ps>
```

## Resources

- [quick ps tutorial](http://www.mostlymaths.net/2008/12/quick-postscript-programming-tutorial.html?m=1)
- [Programming L-systems](http://www.cs.unh.edu/~charpov/programming-lsystems.html)

## The Stack

The biggest thing to realize is that PostScript is a really simple language. Everything is done on the stack. So most commands are written in postfix notation `a b plus`. This command pushes `a` and `b` to the stack and then the interpreter sees the `plus` keyword. It pops off two values from the stack and adds them. Then the result is put back on the stack.

So when something more complicated comes up it is important to think about what is happening on the stack. Let's walk through a bit of this command. This is from [Hypotrochoid](https://en.wikipedia.org/wiki/Hypotrochoid).

```postscript
a b sub t cos mul a b sub t mul b div cos d mul add
```

- `a` and `b` are pushed to the stack
- `sub` pops off two values, then puts `a - b` on the stack.
- `t` is pushed to the stack
- `cos` pops the two values `a - b` and `t` off the stack and pushes the result back to the stack
- and so forth

The thing to remember is that the amount of arguments that the function takes is the number of items it will pop off the stack. The result will then be pushed back to the stack. This will become even more important when writing functions.

## Lines, Squares, and Functions
