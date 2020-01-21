+++
title = "Beginning Programming Curriculum"
date = 2019-07-25T20:36:51-06:00
draft = true
markup = "mmark"
+++

My 8 year old daughter has been begging me to teach her how to program. I am putting all my notes here of the different exercises I have given her.

I try to make it an exploratory process. I start by giving her a little information and then we play with it and see many different ways of using it.

The Mu Editor is very friendly. I let her explore the buttons and see what things do.

## Get the Mu Editor

See the [download page](https://codewith.mu/en/download) and follow the instructions.

When you get it up and running copy and paste lesson 1 into the window.

## Lesson 1

```py
# print out your name


# ask for someones name and then respond by saying hi to them


# count to 5 


# now count to 100


# when counting to 20
# if the number is 15 print something funny


# if the number is 5 print something else


# now count by 5s to 25


```

This introduces:

- print statements
- for loops
- getting input from the user
- if statements

### Solutions

```py
# print out your name
print('bob')
```

```py
# ask for someones name and then respond by saying hi to them
name = input('What is your name?')
print('Hi ', name)
```

```py
# count to 5 
print(1)
print(2)
print(3)
print(4)
print(5)

# or better
for number in range(1,6):
  print(number)
```

```py
# now count to 100
for number in range(1,101):
  print(number)
```

```py
# when counting to 20
# if the number is 15 print something funny
for number in range(1,21):
  if number == 15:
    print('Snurp')
  else:
    print(number)
```

```py
# if the number is 5 print something else
for number in range(1,21):
  if number == 15:
    print('Snurp')
  elif number == 5:
    print('Glarp')
  else:
    print(number)
```

```py
# now count by 5s to 25

# several ways to do this
# ----- 1 -----
# Use a while loop
num = 0
while num < 26:
  num = num + 5
  print(num)

# ----- 2 -----
# Use a for loop
for number in range(1,6):
  print(number * 5)

for number in range(1,30,5):
  print(number)

```

## Functions

You already know a function. `print()` is a function. You put something in and it does something.

In this case you put in a message and it prints it out for you.

Also `input()` is a function. Besides just printing something out, it also captures user input.

A function is a black box. Put something in one side and get and output on the other. It may do stuff as a result (a side effect) or just do something.

Here is the add 5 to any number box. Put in a number and spit out a number that has 5 added to it.



```py
def add5(num):
  return num + 5
```

How about add 2 numbers

```py
def add(num1, num2):
  return num1 + num2
```

Explore making functions and then combining them.

```py
add(5,add5(3))
```

What should this output? This is a basic math question.

What about this?

```py
add5(add(1,2))
```

## Text Adventure Game

By combining functions, if statements, and user input create a basic text adventure game.

```py
print('You are in a dark room. You see 2 doors.')
answer = input('Do you go right(r) or left(l)?')
if answer == 'l':
  print('You take the left door')
  print('You see a strange little man sitting on a chair.')
  answer = input('Do you talk to him?(y) or (n)')
    if answer == 'y':
      print('...')
    elif answer == 'n':
      print('...')
elif answer == 'r':
  print('You take the right door')
  answer = input('...')
  # and so forth
```

## Tic-Tac-Toe

Guide them through buiding up pieces of the game.

Here is what I start with.

```py
def print_grid(grid)
  print(' {} | {} | {} '.format(grid[0], grid[1], grid[2]))
  print('-----------')
  print(' {} | {} | {} '.format(grid[3], grid[4], grid[5]))
  print('-----------')
  print(' {} | {} | {} '.format(grid[6], grid[7], grid[8]))

# store answers
def get_user_input():
  print(' 0 | 1 | 2 ')
  print('-----------')
  print(' 3 | 4 | 5 ')
  print('-----------')
  print(' 6 | 7 | 8 ')
  answer = input('Where do you want to move?')
  return answer

grid = [' '] * 9
print_grid(grid)

# 1. put an 'x' or an 'o' in a spot in the grid
# 2. be able to ask for player 1 and player 2
# 3. don't let a player place a spot already taken
# 4. determine when the game is over
# 5. write a game loop to play the game
```

## Exploring The Mu Plotter

Start by plotting just a single number.

```py
import numpy as np
import random
from time import sleep

num = 5
while True:
  sleep(0.5) 
  print((num,))
```

Then change the number by incrementing it.

```py
num = 5
while True:
  num = num + 1
  sleep(0.5) 
  print((num,))
```

What happens when you add by a different number? Subtract? What if you increase the sleep time?

### Exercises

TODO: add some screen shots and have kids replicate the images.

- Plot a saw tooth wave by incrementing the number. When it gets too high reset it back to zero.
- Plot a square wave by incrementing up to a point and then decrement.
- Plot a sin wave with `np.sin()`
- Combine a sin wave plot with a square wave.

## Next Items

- worm game with PyGame
- break out game with PyGame
- augment previous games with sprites
- add some sounds on collision events
- add a game controller (can't be done with PyGame Zero)

