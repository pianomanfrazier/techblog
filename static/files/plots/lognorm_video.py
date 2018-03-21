#!../venv/bin/python3

import pymonad
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage

@pymonad.curry
def normal(mu, sigma, x):
    return 1/(x * sigma * np.sqrt(2 * np.pi)) * \
    np.exp( - (np.log(x) - mu)**2 / (2 * sigma**2) )

sns.set()
plt.rc('text', usetex=True)

fig,ax = plt.subplots()
ax.set_xlabel(r"$\displaystyle x$")
ax.set_ylabel(r"$\displaystyle f(x)$")
ax.set_title("Lognormal distribution")

def make_frame(t):
    ax.clear()
    mu, sigma = 0, t 
    x = np.arange(0.01, 3, 0.01)
    y = list(map(normal(mu, sigma), x))
    ax.set_ylim(-0.1,4)
    ax.set_xlim(-0.1,3)
    ax.plot(x,y, label="$\displaystyle \sigma={:03.2f}$".format(sigma))
    ax.legend()
    return mplfig_to_npimage(fig)

animation = VideoClip(make_frame, duration=3)
#animation.preview(fps=10)
#animation.show(1.5, interactive=True)
#animation.write_gif('lognormal.gif', fps=10)
animation.write_videofile('lognormal.mp4', fps=30)
