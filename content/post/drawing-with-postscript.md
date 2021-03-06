---
title: "Drawing With Postscript"
date: 2017-09-16T12:03:58-06:00
draft: false
---

For my programming languages class we started out by drawing pictures with Postscript. Since the documentation on how to do basic tasks is sparse on the internet I decided to jot down some of my explorations in the language. This should get anyone started drawing more than just a few squares.

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

## Parametric Equations

Now on to something even more complicated.

```postscript
%!PS

% implement parametric equation a circle
% x = t * cos t
% y = t * sin t

/box {
    dup dup dup
    0 rlineto
    0 exch rlineto
    neg 0 rlineto
    neg 0 exch rlineto
} def

% 3 params
% size of box, x, y, R 
/mybox {
    gsave
    newpath
    600 700 translate
    setrgbcolor
    moveto 
    box
    closepath
    fill
    grestore
} def

0.4 0.4 scale % fit on the page
1 1 720 {
    10 exch % size of boxes
    dup
    dup cos mul exch % x param, 1 * cos 1
    dup
    dup sin mul exch % y param, 1 * sin 1
    dup
    360 div exch % divide red color by 720
    dup
    720 div exch % divide green by 720
    180 div % blue
    mybox
} for
```
![Spiral Parametric Equation](/img/postscript/parametric.png)

### Hypotrochoid

[Hypotrochoid](https://en.wikipedia.org/wiki/Hypotrochoid)

Here are the two equations in stack form (i.e. RPN):

```postscript
a b sub t cos mul a b sub t mul b div cos d mul add % x
a b sub t sin mul a b sub t mul b div sin d mul sub % y
```

```postscript
%!PS

% implement parametric equation a circle
% x = cos t
% y = sin t

/box {
    dup dup dup
    0 rlineto
    0 exch rlineto
    neg 0 rlineto
    neg 0 exch rlineto
} def

% 3 params
% size of box, x, y, R 
/mybox {
gsave
newpath
setrgbcolor
moveto 
box
closepath
fill
grestore
} def

/a 50 def
/b 30 def
/d 50 def

% takes one argument t
/xpos {
    dup % we need two t's, t1 & t2
    a b sub exch
    cos % consumes t1
    mul exch
    a b sub exch
    mul % consumes t2
    b div
    cos d
    mul
    add % x
} def

% takes one argument t
/ypos {
    dup % t1 & t2 on stack
    a b sub exch
    sin % consumes t1
    mul exch
    a b sub exch
    mul % consumes t2
    b div 
    sin d 
    mul 
    sub % y
} def

% 4 parameters
% scale translateX translateY
/star {
    1 1 1080 {
        %dup 360 exch
        3 exch % size of boxes
        dup xpos exch
        dup ypos exch
        dup
        1080 div exch % divide red color by 720
        dup
        360 div exch % divide green by 720
        pop
        0 exch
        %720 div % blue
        mybox
    } for
} def

300 300 translate
2 2 scale
star
```
![Parametric Star](/img/postscript/star.png)
Try changing the variables `/a`, `/b`, and `/d` and see the different stars produces. You will also have to change how many times around the circle you have to go to complete the cycle.
![Parametric Star](/img/postscript/star2.png)
![Parametric Star](/img/postscript/star3.png)
We can then redraw it and translate it in a loop.
```postscript
/a 70 def
/b 30 def
/d 50 def

300 300 translate
1 1 360 {
    rotate
    star
} for

/a 50 def
/b 30 def
/d 50 def

star2
```
![Parametric Star](/img/postscript/star4.png)

## Conclusion

I learned a lot about working directly with the stack working with PostScript. I also learned the dangers of global variables. The code is hard to reason about because function calls are totally dependant on the state of the stack.

