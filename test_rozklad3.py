# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 19:49:31 2018

@author: magda
"""
from detektor import Detektor
from promieniowanie import Promieniowanie
from promien import Promien
import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

det = Detektor()

det.dodajSegment(48, 42.50, 0, np.radians(7.5))
det.dodajSegment(48, 46.75, np.radians(3.75), np.radians(7.5))
det.dodajSegment(96, 57.50, np.radians(1.875), np.radians(3.75))

<<<<<<< HEAD
n_promieni = 10000
=======
n_promieni = 100
>>>>>>> 50aa5dda1f49d409d18ed2768e0d832bf38917fe
pr = Promieniowanie(n_promieni)
X, Y, Z = [], [], []
for p in pr._promienie:
    wsp = p.dajPunktKart().tolist()
    X.append(wsp[0][0])
    Y.append(wsp[1][0])
    Z.append(wsp[2][0])


<<<<<<< HEAD
plt.scatter(X, Y, c=Z, s=1, cmap='Reds')
=======
plt.scatter(X, Y, c=Z, s=10, cmap='Reds')
>>>>>>> 50aa5dda1f49d409d18ed2768e0d832bf38917fe
plt.xlim(0, 60)
plt.ylim(0, 60)
plt.show()
