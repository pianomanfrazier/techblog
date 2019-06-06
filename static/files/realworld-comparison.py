import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

x = ['Svelte/Sapper', 'Stencil', 'Angular', 'React/Redux', 'Vue', 'Elm']
y = [43.54, 120.06, 551.97, 1024.00, 218.13, 90.52]
xlabel = 'Framework'
ylabel = 'JS Bundle Size'
df = pd.DataFrame(data={xlabel:x, ylabel:y})

sns.set(style='whitegrid')
sns.barplot(x=xlabel,y=ylabel,data=df,palette='bright')
plt.savefig('../img/new-web-tech-2019/compare.svg')
