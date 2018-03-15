#!../venv/bin/python3

import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from helper import *

l = 10 
k = 20

def poisson(l,k):
    return ((l**k) * (math.e ** (-l)))/fact(k)

def p2(k):
    return poisson(l,k)

x = range(k)
y = list(map(p2, x))
sns.set()
plt.rc('text', usetex=True)
plt.bar(x,y,width=0.8)
plt.xticks(x)
plt.xlabel(r"$\displaystyle x$")
plt.ylabel(r"$\displaystyle P(X = x)$")
plt.show()
#plt.savefig('figures/poisson.png', dpi=200)

