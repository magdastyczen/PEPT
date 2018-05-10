# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:49:31 2018

@author: magda
"""
from detektor import Detektor
from promieniowanie import Promieniowanie
from promien import Promien
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import pyplot
import numpy as np
import plotly as py
import plotly.graph_objs as go


det = Detektor()

det.dodajSegment(48, 42.50, 0, np.radians(7.5))
det.dodajSegment(48, 46.75, np.radians(3.75), np.radians(7.5))
det.dodajSegment(96, 57.50, np.radians(1.875), np.radians(3.75))

fig = pyplot.figure()
ax = Axes3D(fig)

n_promieni = 500
pr = Promieniowanie(n_promieni)
X, Y, Z = [], [], []
for p in pr._promienie:
    wsp = p.dajPunktKart().tolist()
    X.append(wsp[0][0])
    Y.append(wsp[1][0])
    Z.append(wsp[2][0])

ax.scatter(X, Y, Z)
"""
n_promieni = 500
pr = Promieniowanie(n_promieni)
X, Y, Z = [], [], []
for p in pr._promienie:
    wsp = p.dajPunktKart().tolist()
    X.append(wsp[0][0])
    Y.append(wsp[1][0])
    Z.append(wsp[2][0])
ax.scatter(X, Y, Z)    
trace = go.Heatmap(X=[], Y=[], Z=[])
data=[trace]
py.iplot(data, filename='basic-heatmap')
# R = np.linspace(0, 5, 100)
# h = 5
# u = np.linspace(0,  2*np.pi, 100)
# dX = np.outer(R, np.cos(u))
# dY = np.outer(R, np.sin(u))
# ax.plot3D(dX, dY, h)
"""
scyntylatory = det.rzutuj3D()
for s in scyntylatory:
    ax.scatter(s[0], s[1], s[2], c='black')

pyplot.show()