# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:21:18 2017

@author: magda
"""

import matplotlib.pyplot as plt
import time

class Ekran:
    def __init__(self):
        self._detektor = plt.subplot(111)
        self._detektor.set_ylim([-80, 80])   # set the bounds to be 10, 10
        self._detektor.set_xlim([-80, 80])
        self._detektor.set_aspect('equal')
        plt.axes().set_aspect('equal')

    def rysujDetektor(self, d):
        (x, y) = d.rzutuj()
        self._detektor.scatter(x, y)
        
    def rysujPromienie(self, p):
        (xl, yl) = p.rzutuj()
        for x, y in zip(xl, yl):
            self._detektor.plot(x, y)

    def pokaz(self):
        plt.show()