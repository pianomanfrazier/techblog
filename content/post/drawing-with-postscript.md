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

```postscript
%!PS

newpath %sets a drawing path
200 200 moveto % moves drawing point (x,y) to (200,200)
200 0 rlineto % draws a line relative to (200,200), so (400,200)
1 0 0 setrgbcolor % set color to red
closepath
stroke
```
![Red Line](/img/postscript/line.png)

```postscript
%!PS

% a function definition
/box {
    % the top of the stack will be the function parameter
    % duplicate the top of the stack 3 times
    dup dup dup
    0 rlineto % consumes a duplicate
    0 exch rlineto % swap 0 and top of stack
    neg 0 rline to % negates and consumes the duplicate
    neg 0 exch rlineto % negates, exchanges then consumes 3rd dup
} def

newpath
1 0 1 setrgbcolor
200 200 moveto
50 rotate
200 box % function call will 200 on the stack
closepath
stroke
```
![Purple Rotated Box](/img/postscript/line2.png)

Now something a little bit wackier.

```postscript
%!PS

0.5 0.5 scale

/box {
	dup dup dup
	0 rlineto
	0 exch rlineto
	neg 0 rlineto
	neg 0 exch rlineto
} def

% new function that wraps the box function
% takes 4 parameters on the stack
/mybox {
gsave
newpath
0.5 setrgbcolor % param 1 & 2, colors changing in for loop
400 400 moveto
rotate % param 3
box % param 4
closepath
stroke
grestore
} def

%for loop
% start increment end { ... } for
10 5 360 {
    % comments are as if first time through the loop
    dup % param 4, copy 10 to stack
    dup % param 3, copy 10 to stack
    360 div % param 2, put 360 on stack, divide 10/360 put back on stack
    dup % param 1, copy 10% of 360
    mybox % needs 4 params on the stack
} for
```
![Spiral Box](/img/postscript/spiral_box.png)

