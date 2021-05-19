# Trying to recreate 3blue1brown's "colliding blocks create pi" video
# -Im trying to work out collisions here in the hopes of eventually \
#   plugging it into my 2d block collision model
# 5/18/2021

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.patches import Rectangle
from supportingFunctions import v2f, v1f, plots
from numpy import *
from matplotlib.pyplot import *


n_particles = 2
f = []
# 0 for left, 1 for right
# these arrays store the properties of the blocks
x_position = np.zeros(n_particles)
x_velocity = np.zeros(n_particles)
mass = np.zeros(n_particles)

x_position[0] = 2.0
x_position[1] = 8.0

x_velocity[0] = 0
x_velocity[1] = -0.01

mass[0] = 1.0
mass[1] = 10000.0

counter=[]

fig = plt.figure()
fig.set_dpi(100)
fig.set_size_inches(7, 6.5)

size = 1.0
ax = plt.axes(xlim=(0, 10), ylim=(0, 10))
patch = plt.Rectangle((5, -5), size, size)
patch2 = plt.Rectangle((5, -5), size, size)




def init():
    patch.xy = (5, 5)
    patch2.xy = (5, 5)
    ax.add_patch(patch)
    ax.add_patch(patch2)
    return patch, patch2

# this is the animation part
def update(frame_number):

    number = 0
    x1, y1 = patch.xy
    x_position[0] += x_velocity[0]
    y1 = 0
    patch.xy = (x_position[0], y1)
    x2, y2 = patch2.xy
    x_position[1] += x_velocity[1]
    y2 = 0
    patch2.xy = (x_position[1], y2)

    length = len(counter)
    # this handles the collisions with left wall
    if x_position[1]  < 0.0:
        x_velocity[1] = -x_velocity[1]
        counter.append(1)
    if x_position[0] < 0.0:
        x_velocity[0] = -x_velocity[0]
        counter.append(1)


    # trying to handle block collisions, uses functions on other python sheet
    if (x_position[1]) <= (x_position[0]+size):
        initialVelocity = x_velocity[1]
        x_velocity[1] = v2f(x_velocity[0], initialVelocity, mass[0], mass[1])
        x_velocity[0] = v1f(x_velocity[0], initialVelocity, x_velocity[1], mass[0], mass[1])
        counter.append(1)

        # this is an attempts at making a continuously updating plot
        f = plots(x_velocity[0], initialVelocity, mass[0], mass[1])
        a = f[0]
        b = f[1]
        c = f[2]
        # this is a graph maker
        x = linspace(-2, 0, 5000)
        y = a * x ** 2 + b * x + c
        plot(x, y)

        #x_velocity[0] = -x_velocity[0]
        #x_velocity[1] = -x_velocity[1]

    # this tells when to print the collision counter, which is whenever it changes value
    if len(counter) != length:
        print("Number of collisions:", len(counter))
    return patch, patch2

animation = animation.FuncAnimation(fig, update, init_func=init, interval=10, blit=True)
plt.show()