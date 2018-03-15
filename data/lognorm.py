#!../venv/bin/python3

import pymonad
import sys
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

@pymonad.curry
def normal(mu, sigma, x):
    return 1/(x * sigma * np.sqrt(2 * np.pi)) * \
    np.exp( - (np.log(x) - mu)**2 / (2 * sigma**2) )

from scipy.integrate import quad

#integrate to check CDF
mu, sigma = 0, 0.25 
end = mu+16*sigma
start = 0
print("check CDF")
print(quad(normal(mu,sigma), start, end)) 

sns.set()
plt.rc('text', usetex=True)

for s in [0.25, 0.5, 1, 1.25]:
    mu, sigma = 0, s 
    x = np.arange(0.01, mu+3* (1/s) *sigma, 0.01)
    y = list(map(normal(mu, sigma), x))
    plt.plot(x,y, label="$\displaystyle \sigma={}$".format(s))

plt.xlabel(r"$\displaystyle x$")
plt.ylabel(r"$\displaystyle f(x)$")
plt.legend()
#plt.show()
plt.savefig('figures/lognorm.svg', dpi=200)

