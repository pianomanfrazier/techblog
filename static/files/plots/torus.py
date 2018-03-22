#!../venv/bin/python

import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
from moviepy.video.fx.all import crop

plt.rc('text', usetex=True)

fig = plt.figure(figsize=(18,14))
ax1 = fig.add_subplot(121, projection='3d')
ax2 = fig.add_subplot(122, projection='3d')

# from https://scipython.com/book/chapter-7-matplotlib/examples/a-torus/
n = 100

theta = np.linspace(0, 2.*np.pi, n)
phi = np.linspace(0, 2.*np.pi, n)
theta, phi = np.meshgrid(theta, phi)
c, a = 2, 1
x = (c + a*np.cos(theta)) * np.cos(phi)
y = (c + a*np.cos(theta)) * np.sin(phi)
z = a * np.sin(theta)

def make_frame(t):
    for ax in (ax1, ax2):
        ax.clear()
        ax.grid(False)
        ax.axis("off")
        ax.plot_surface(x, y, z, rstride=5, cstride=5, edgecolors='w')
        ax.set_zlim(-3,3)
        if ax == ax1:
          ax.view_init(15, int(30*t))
        else:
          ax.view_init(int(30*t), 36)
    return mplfig_to_npimage(fig)

animation = VideoClip(make_frame, duration=6)
#animation.preview(fps=10)
#animation.show(1.5, interactive=True)
final  = crop(animation, x_center=900, y_center=700, width=1200, height=600)
#final.show(1.5, interactive=True)
#final.preview(fps=5)
final.write_videofile('torus.mp4', fps=30)

