# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:28:00 2018

@author: magda
"""

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from promien2 import Promien

p = Promien(1, np.pi/4, 0, np.pi/4, np.pi/4) # x, y, z, Theta-> 90-Theta, 90-alpha

p1 = p.dajPunktKart()
p2 = p.dajPunkt2(p1)

x = [p1[0], p2[0]]
y = [p1[1], p2[1]]
z = [p1[2], p2[2]]



fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')


ax.set_ylim([-2, 2])   # set the bounds to be 10, 10
ax.set_xlim([-2, 2])
ax.set_zlim([-2, 2])
ax.set_aspect('equal')
plt.axes().set_aspect('equal')
print("Punkt 1: {}\nPunkt 2: {}".format(p1, p2))

plt.scatter(x, y, z, "r", "o")

plt.show()