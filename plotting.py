import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

plt.style.use('fivethirtyeight')

def animate(i):
    data = pd.read_csv('data.csv')
    x1 = data['x_value']
    y1 = data['y_value']
    x2 = data['frw_sensor']
    y2 = data['left_sensor']
    d = data['direction']
    obsx = data['obstacle_x']
    obsy = data['obstacle_y']

    plt.cla()

    ax = plt.gca()
    ax.set_xlim(-30,30)
    ax.set_ylim(-30,30)

    plt.scatter(x1, y1, label='Vehicle') 

    plt.plot(obsx, obsy, label='Obstacle')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()

