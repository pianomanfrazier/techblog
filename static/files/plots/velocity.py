#!../venv/bin/python3

import pymonad
import sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
import seaborn as sns

m = 1

@pymonad.curry
def normal(mu, sigma, v):
    return 2*m*v/(sigma * np.sqrt(2 * np.pi)) * \
    np.exp( - (0.5 * m * v**2 - mu)**2 / (2 * sigma**2) )

#integrate to check CDF
mu, sigma = 0, 0.25 
start, end = 0, mu+16*sigma
print("check the integral of the CDF is 1")
print(quad(normal(mu,sigma), start, end)) 

sns.set()
plt.rc('text', usetex=True)

for s in [0.25, 0.5, 1, 1.25]:
    mu, sigma = 0, s 
    x = np.arange(0, mu+3* (1/s) *sigma, 0.01)
    y = list(map(normal(mu, sigma), x))
    plt.plot(x,y, label="$\displaystyle \sigma={}$".format(s))

plt.xlabel(r"$\displaystyle v$")
plt.ylabel(r"$\displaystyle f_V(|v|)$")
plt.legend()
#plt.show()
plt.savefig('figures/velocity.svg')
