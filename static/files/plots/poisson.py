#!../venv/bin/python3

import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

l = 10 
k = 20

def fact(n):
  if n < 1:
    return 1
  else:
    return fact(n-1) * n

def poisson(l,k):
    return ((l**k) * (np.e ** (-l)))/fact(k)

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
#plt.show()
plt.savefig('figures/poisson.svg')

