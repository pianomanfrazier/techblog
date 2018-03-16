+++
title= "Create Beautiful Math Homework"
date= 2018-03-15T12:04:46-06:00
draft= false
markup= "mmark"
+++

Throughout my Computer Science degree I have been doing a lot my homework in Latex. It has a learning curve but the results are amazing. For my probability class this semester I have also wanted to produce graphs and charts. I have been using the python libraries [matplotlib](https://matplotlib.org) and [seaborn](https://seaborn.pydata.org/index.html) to create awesome graphs. My homework often looks better than my textbook.

For my homework I have also written a script that reads a config file for the class I am in that has data like the teacher, semester, class name and so forth and generates a new Latex project with a makefile. I have been using this system for 2 semesters and it has been working great. See [homework-generator](https://github.com/pianomanfrazier/homework-generator).

Here are some highlights of the graphs I did for my homework. The visualizations sure helped figure out what was going on.

F>![Poisson distribution](/img/math_homework/poisson.svg)
Figure: Poisson Distribution where $$ \lambda = 10 $$ 
<br>[[download poisson.py]](/files/plots/poisson.py)

F>![Lognormal Distribution](/img/math_homework/lognorm.svg)
Figure: Lognormal Distribution $$ f(x) = \frac{1}{\sigma x \sqrt{2 \pi}} e^{- (\ln x - \mu)^2 / 2 \sigma^2 }$$ 
<br>[[download lognorm.py]](/files/plots/lognorm.py)

F>![Normal Distribution of Velocity of a Particle](/img/math_homework/velocity.svg)
Figure: Normal Distribution of the Velocity of a Particle $$ f(x) = 2 \frac{mv}{\sigma \sqrt{2 \pi}} e^{- ( \frac{1}{2} mv^2 - \mu)^2 / 2 \sigma ^2} $$
<br>[[download velocity.py]](/files/plots/velocity.py)

F>![CDF](/img/math_homework/bivariate.svg)
Figure: Plot of a Bivariate Distribution $$f_{XY}(x,y) = x e^{-x(y+1)}$$.
<br>[[download bivariate.py]](/files/plots/bivariate.py)
