+++
title= "Create Beautiful Math Homework"
date= 2018-03-15T12:04:46-06:00
draft= true
markup= "mmark"
+++

Throughout my Computer Science degree I have been doing all my homework in Latex. It has a learning curve but the results are amazing. For my probability class this semester I have also needed to produce graphs and charts. I have been using the python libraries [matplotlib](https://matplotlib.org) and [seaborn](https://seaborn.pydata.org/index.html) to create awesome graphs. My homework often looks better than my textbook.

For my homework I have written a script that reads a config file for the class I am in that has data like the teacher, semester, class name and so forth and generates a new Latex project with a makefile for me. I have been using this system for 2 semesters and it has been working great.

Here are some highlights.

F>![Poisson distribution](/img/math_homework/poisson.svg)
Figure: Poisson distribution where $$ \lambda = 10 $$

F>![Lognormal Distribution](/img/math_homework/lognorm.svg)
Figure: Lognormal distribution $$ f(x) = \frac{1}{\sigma x \sqrt{2 \pi}} e^{- (\ln x - \mu)^2 / 2 \sigma^2 }$$ 

F>![Normal Distribution of Velocity of a Particle](/img/math_homework/velocity.svg)
Figure: Normal Distribtuion of the Velocity of a Particle $$ f(x) = 2 \frac{mv}{\sigma \sqrt{2 \pi}} e^{- ( \frac{1}{2} mv^2 - \mu)^2 / 2 \sigma ^2} $$

F>![CDF](/img/math_homework/prob14.svg)
Figure: Plot of a Bivariate Distribution $$f_{XY}(x,y) = x e^{-x(y+1)}$$.
