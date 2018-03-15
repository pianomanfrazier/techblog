#!../venv/bin/python

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def fun(x,y):
  return x * np.exp(-x * (y + 1)) 

plt.rc('text', usetex=True)

# from https://stackoverflow.com/a/9170879/9399825
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = y = np.arange(0, 6.0, 0.1)
X, Y = np.meshgrid(x, y)
zs = np.array([fun(x,y) for x,y in zip(np.ravel(X), np.ravel(Y))])
Z = zs.reshape(X.shape)

ax.plot_surface(X, Y, Z)

ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel(r'$\displaystyle f_{X,Y}(x,y)$')

plt.show()
#plt.savefig('figures/prob14.png', dpi=200)
