# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:18:24 2017

@author: magda
"""

import math
from scyntylator import Scyntylator
import matplotlib.pyplot as plt

class Detektor:
    def __init__(self):
        self._scyntylatory = []
    
    def generujScyntylatory(self, n, r, theta0, theta_skok, z=0, w=0.35, h=0.95, d=25.0):
        theta1 = math.atan2(w, r)
        theta2 = math.atan2(w, r+h)        
        for i in range(0, n):
            wsp = []     
            wsp.append([r-h, theta0 - theta1 + theta_skok*i, z-d]) #A-
            wsp.append([r-h, theta0 - theta1 + theta_skok*i, z+d]) #A+
            wsp.append([r+h, theta0 - theta2 + theta_skok*i, z-d]) #B-
            wsp.append([r+h, theta0 - theta2 + theta_skok*i, z+d]) #B+
            wsp.append([r+h, theta0 + theta2 + theta_skok*i, z-d]) #C-
            wsp.append([r+h, theta0 + theta2 + theta_skok*i, z+d]) #C+
            wsp.append([r-h, theta0 + theta1 + theta_skok*i, z-d]) #D-
            wsp.append([r-h, theta0 + theta1 + theta_skok*i, z+d]) #D+
            self._scyntylatory.append(Scyntylator(wsp))
    
    def dajScyntylatory(self):
        return self._scyntylatory

    def __str__(self):
        s = "Detektor sklada sie z {} scyntylatorow.".format(len(self._scyntylatory))
        return s
        
    def rzutuj(self):
        x_ret = []
        y_ret = []
        for s in self._scyntylatory:
            (x, y) = s.wspKart2D()
            x_ret.extend(x)
            y_ret.extend(y)
        
        return (x_ret, y_ret)     
        
    def rysuj(self):
        (x, y) = self.rzutuj()
        plt.scatter(x, y)
        plt.show()
        