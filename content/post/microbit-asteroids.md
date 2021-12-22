+++
title = "Microbit Asteroids"
date = 2021-12-21T14:24:22-07:00
draft = false
markup = "mmark"
+++

We will be using the [Mu Editor](https://codewith.mu/).

Here is the final version of this simple game.

{{< video src="/img/microbit_asteroids/final_demo.mp4" type="mp4" loop="false" autoplay="false">}}

Here is our plan of attack.

- create controllable rocket
- make astroid fall from the sky
- check if game over (astroid collides with our rocket)

## TLDR;

Go to the bottom and copy and paste my code into your microbit.

## Light up an LED

First we need to know how to light up individual lights on the 5x5 grid. We can use the function `display.set_pixel(x,y,b)`.

```py
from microbit import *

display.set_pixel(0,0,9)
```

{{< figure
  src="/img/microbit_asteroids/light_led.png"
  alt="Microbit LED 0,0"
  title="Microbit LED 0,0"
  caption="Lighting LED 0,0 on the grid"
>}}

## The LED grid

The 5x5 grid can be addressed with the cartesian coordinates with the origin starting at the top left.

{{< figure
  src="/img/microbit_asteroids/led_grid.png"
  alt=""
  title="Microbit LED grid"
  caption="The LED cartesian grid start at the top right"
>}}

As an exercise try to light up each of the four corners of the grid.

What happens if you try to light up an LED that isn't on the grid like (0,5)?

## Button Input

We are going to need to control our rocket with the A and B buttons. So let's make a simple program where a pixel lights up if we just push a button.

```py
from microbit import *

if button_a.is_pressed():
    display.set_pixel(0,0,9)
```

{{< figure
  src="/img/microbit_asteroids/led_button.png"
  alt=""
  title="Microbit LED grid"
  caption="The LED cartesian grid start at the top right"
>}}

Now if you run this you likely won't see anything happen. This is because the code is only run once. What we actually want to happen is for the microbit to keep checking if we have pushed a button and then respond to it. So we really need the code to always be running our code. The way we do that is with an **event loop**.

We also need to tell the microbit to turn the light off if we are not pushing the button. We'll use `display.clear()`. Otherwise once the light is turned on it will stay on whether we press the button again or not.

```py
from microbit import *

# event loop hack
while True:
    if button_a.is_pressed():
        display.set_pixel(0,0,9)
    else:
        display.clear()
```

## Making our rocket

Now we need to be able to control our rocket (the pixel) with the buttons. We want our rocket to be on the bottom so the available positions of our rocket will be (0,4), (1,4), (2,4), (3,4), and (4,4).

If you'll notice the Y position stays the same and the X position moves. So we should make a variable in our code for the part that changes. We'll combine what we know about checking for buttons and drawing pixels to the grid.

```py
from microbit import *

# this part changes based on button pushes
rocketX = 0
# this doesn't change
rocketY = 4

while True:
    if button_a.is_pressed():
        # move the rocket to the left by 1
        rocketX = rocketX - 1
    if button_b.is_pressed():
        # move the rocket to the right by 1
        rocketX = rocketX + 1
    
    # draw the rocket
    display.clear()
    display.set_pixel(rocketX,rocketY,9)
```

The program kind of works but it has some problems. Can you find them? There are 2.

## Problem 1

The program runs really fast so when we push a button our rocket shoots of the screen and then there is an error. We can fix this by slowing down our event loop with the `sleep` function. Since we are only checking the buttons every so often now we should switch to checking if there have been any button presses with `button_a.get_presses()`


```py
from microbit import *

rocketX = 0
rocketY = 4

while True:
    sleep(200)
    if button_a.get_presses():
        rocketX = rocketX - 1
    if button_b.get_presses():
        rocketX = rocketX + 1
    
    display.clear()
    display.set_pixel(rocketX,rocketY,9)
```

## Problem 2

Ok. So we've fixed that but we can still run our rocket off the screen.

{{< video src="/img/microbit_asteroids/overflow_error.mp4" type="mp4" loop="false" autoplay="false">}}

We need a way to make sure that you can't move your rocket off the screen and crash our program. In order to do that we need to guarantee that `rocketX` is never greater than 4 or less than 0.

```py
from microbit import *

rocketX = 0
rocketY = 4

while True:
    sleep(200)
    if button_a.get_presses() and rocketX > 0:
        rocketX = rocketX - 1
    if button_b.get_presses() and rocketX < 4:
        rocketX = rocketX + 1
    
    display.clear()
    display.set_pixel(rocketX,rocketY,9)
```

{{< video src="/img/microbit_asteroids/overflow_fix.mp4" type="mp4" loop="false" autoplay="false">}}

## Asteroids

Now that we have a controllable rocket we need some asteroids to dodge.

The idea is that an asteroid will start at a random place on the top and fall towards the bottom.

Try to draw a random pixel to the screen.

```py
from microbit import *
from random import randint

rocketX = 0
rocketY = 4

asteroidX = randint(0, 4)
asteroidY = 0

while True:
    sleep(200)
    if button_a.get_presses() and rocketX > 0:
        rocketX = rocketX - 1
    if button_b.get_presses() and rocketX < 4:
        rocketX = rocketX + 1
    
    display.clear()
    display.set_pixel(rocketX, rocketY, 9)
    # draw the asteroid
    display.set_pixel(asteroidX, asteroidY, 9)
```

Try reseting the microbit several times with the button on the back and notice how the asteroid starts at different positions.

Now we need the astroid to fall down and then when it goes off the screen start over at the top again. We also need to make sure that the astroid doesn't try to draw off screen or our program will crash just like our rocket crashed our program before.

```py
from microbit import *
from random import randint

rocketX = 0
rocketY = 4

asteroidX = randint(0, 4)
asteroidY = 0

while True:
    sleep(200)
    if button_a.get_presses() and rocketX > 0:
        rocketX = rocketX - 1
    if button_b.get_presses() and rocketX < 4:
        rocketX = rocketX + 1

    if asteroidY < 4:
        asteroidY = asteroidY + 1
    else:
        # reset the astroid
        asteroidY = 0
        asteroidX = randint(0,4)
    
    display.clear()
    display.set_pixel(rocketX, rocketY, 9)
    display.set_pixel(asteroidX, asteroidY, 9)
```

You'll notice now that we almost have a working game. We now need to detect if the astroid crashed into your rocket.

## Game Over

To do that we need to check if the asteroid is occupying the same space as our rocket.

```py
from microbit import *
from random import randint

rocketX = 0
rocketY = 4

asteroidX = randint(0, 4)
asteroidY = 0

while True:
    sleep(200)
    if button_a.get_presses() and rocketX > 0:
        rocketX = rocketX - 1
    if button_b.get_presses() and rocketX < 4:
        rocketX = rocketX + 1

    if asteroidY < 4:
        asteroidY = asteroidY + 1
    else:
        asteroidY = 0
        asteroidX = randint(0,4)
    
    # check the game over condition
    if asteroidX == rocketX and asteroidY == rocketY:
        display.scroll('GAME OVER')
    else:
        display.clear()
        display.set_pixel(rocketX, rocketY, 9)
        display.set_pixel(asteroidX, asteroidY, 9)
```

## Bonus

There are a bunch of other features you could add to this game. Here are some ideas.

- connect up a speaker and make music/sound on asteroid collision
- keep score (either a timer or number of astroids missed)
- add multiple astroids
- allow the rocket to shoot with A+B button presses
- use the microbit internal tilt sensor to control the rocket

## Add sound

Microbit verion 2 has better support for sounds, I only have version 1 so I'll make due with playing some music on game over.

```py
import music
...

# check the game over condition
if asteroidX == rocketX and asteroidY == rocketY:
    music.play(music.BADDY)
    display.scroll('GAME OVER')
```

## Keep Score

To keep store we'll count the astroids that go by. For this we need another variable to count the astroids.

```py
score = 0

while True:
    ...
    
    if asteroidX == rocketX and asteroidY == rocketY:
        # report the score to the player
        display.scroll('GAME OVER! SCORE: ' + score)
        # reset the score on game over
        score = 0
    else:
        score = score + 1
        display.clear()
        display.set_pixel(rocketX, rocketY, 9)
        display.set_pixel(asteroidX, asteroidY, 9)
```

## Multiple Asteroids

Multiple asteroids becomes trickier because we don't just want to copy and paste the asteroid code and keep track of all those variables. We need a way to abstract out the idea of an asteroid. We'll use a class. This is a more advanced topic so beware.

```py
from microbit import *
import music
from random import randint


# base class
class Point:
    x = 0
    y = 0
    brightness = 9

    def update(self):
        pass

    def draw(self):
        display.set_pixel(self.x, self.y, self.brightness)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Rocket(Point):
    brightness = 9

    def __init__(self):
        self.x = 2
        self.y = 4

    def update(self):
        if button_a.get_presses() and self.x > 0:
            self.x -= 1
        if button_b.get_presses() and self.x < 4:
            self.x += 1


class Asteroid(Point):
    def __init__(self):
        self.brightness = randint(3, 7)
        self.x = randint(0, 4)
        self.y = 0

    def update(self):
        if self.y < 4:
            self.brightness += randint(-2, 2)
            if self.brightness > 9:
                self.brightness = 9
            if self.brightness < 2:
                self.brightness = 2
            self.y += 1
        else:
            self.__init__()


def init():
    global rocket
    global asteroids
    global counter
    global num_asteroids
    global speed
    rocket = Rocket()
    asteroids = []
    counter = 0
    num_asteroids = 1
    speed = 200


init()
while True:
    # throttle the event loop
    sleep(speed)
    counter += 1

    # gradually add more asteroids
    if counter % 2 == 0 and len(asteroids) < num_asteroids:
        asteroids.append(Asteroid())
    if counter % 3 == 0 and len(asteroids) < num_asteroids:
        asteroids.append(Asteroid())
    
    # difficulty adjustment
    if counter > 13:
        num_asteroids = 2
    if counter > 37:
        num_asteroids = 3
    if counter > 53:
        speed = 170
    if counter > 71:
        speed = 150
    if counter > 93:
        speed = 120
    if counter > 111:
        num_asteroids = 4

    rocket.update()
    [x.update() for x in asteroids]

    # check the game over condition
    if True in [rocket == x for x in asteroids]:

        display.show(Image.ANGRY)
        music.play(music.BADDY)
        display.scroll(str(counter))

        # reset the game variables
        init()
    else:
        display.clear()
        rocket.draw()
        [x.draw() for x in asteroids]
```