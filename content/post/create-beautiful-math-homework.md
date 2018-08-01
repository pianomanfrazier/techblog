+++
title= "Create Beautiful Math Homework"
date= 2018-03-15T12:04:46-06:00
draft= false
markup= "mmark"
hasMath= true
+++

Throughout my Computer Science degree I have been doing a lot my homework in Latex. It has a steep learning curve but the results are amazing.

For my technical writing class I convinced my group to use Latex instead of Word or Google Docs. In hindsight this created a lot of extra work for me but I learned a lot about customizing a Latex document. See [here](https://github.com/pianomanfrazier/ENGR_3080_latex) for the Latex template I generated. The things I really liked about this setup was the ability to modularize the document and assign different team members a section. We then collaborated on the document using https://www.overleaf.com. Overleaf has git integration so I could edit the document on my laptop and push the changes back up to overleaf. The downside to this was that my other team members were not programmers and did not know how to use git and had to use the web interface for editing. Generating and managing the bibliography was also very easy using Bibliotex.

For my personal homework I have written a script that reads a config file for the class I am in that has data like the teacher, semester, class name and so forth and generates a new Latex project with a makefile. I have been using this system for 2 semesters and it has been working great. See [homework-generator](https://github.com/pianomanfrazier/homework-generator).

For my probability class this semester I have also wanted to produce graphs and charts. I have been using the python libraries [matplotlib](https://matplotlib.org) and [seaborn](https://seaborn.pydata.org/index.html) to create awesome graphs. My homework often looks better than my textbook.

Here are some highlights of the graphs I did for my homework. The visualizations helped me see what was going on with the math.

F>![Poisson distribution](/img/math_homework/poisson.svg)
Figure: Poisson Distribution where $$ \lambda = 10 $$ 
<br>[[download poisson.py]](/files/plots/poisson.py)

F>![Lognormal Distribution](/img/math_homework/lognorm.svg)
Figure: Lognormal Distribution $$ f(x) = \frac{1}{\sigma x \sqrt{2 \pi}} e^{- (\ln x - \mu)^2 / 2 \sigma^2 }$$ 
<br>[[download lognorm.py]](/files/plots/lognorm.py)

Using [moviepy](https://zulko.github.io/moviepy/) we can create a nice video of this graph where $$\sigma$$ varies over time.
[[download lognorm_video.py]](/files/plots/lognorm_video.py)

{{< video src="/video/lognormal.mp4" type="mp4" loop="true" autoplay="true">}}

F>![Normal Distribution of Velocity of a Particle](/img/math_homework/velocity.svg)
Figure: Normal Distribution of the Velocity of a Particle $$ f(x) = 2 \frac{mv}{\sigma \sqrt{2 \pi}} e^{- ( \frac{1}{2} mv^2 - \mu)^2 / 2 \sigma ^2} $$
<br>[[download velocity.py]](/files/plots/velocity.py)

F>![CDF](/img/math_homework/bivariate.svg)
Figure: Plot of a Bivariate Distribution $$f_{XY}(x,y) = x e^{-x(y+1)}$$.
<br>[[download bivariate.py]](/files/plots/bivariate.py)

And just for fun let's plot a torus and make a video out of it. [[download torus.py]](/files/plots/torus.py)

{{< video src="/video/torus.mp4" type="mp4" loop="true" autoplay="true">}}
