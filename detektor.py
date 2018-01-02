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
        self._segmenty = []
    
    def generujScyntylatory(self, n, r, theta0, theta_skok, z=0, w=0.35, h=0.95, d=25.0):
        self._segmenty.append(Segment(r, theta_skok, theta0))        
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
            self._segmenty[-1].dodajScyntylator(wsp)

    def __str__(self):
        s = "Detektor sklada sie z {} segmentów.\n".format(len(self._segmenty))
        for segment in self._segmenty:
            segment._n
            s+="Segment składa się z {} scyntylatorów.\n".format(segment._n)
        return s
        
    def rzutuj(self):
        x_ret = []
        y_ret = []
        scyntylatory = []
        
        for s in self._segmenty:
            scyntylatory.extend(s._scyntylatory)
        
        for s in scyntylatory:
            (x, y) = s.wspKart2D()
            x_ret.extend(x)
            y_ret.extend(y)
        
        return (x_ret, y_ret)     
        
    def rysuj(self):
        (x, y) = self.rzutuj()
        plt.scatter(x, y)
        plt.show()
        
class Segment:
    def __init__(self, r=0, theta=0, theta0=0):
        self._scyntylatory = []    
        self._r = r
        self._theta = theta
        self._theta0 = theta0
        self._n = 0
        
    def dodajScyntylator(self, w):
        self._scyntylatory.append(Scyntylator(w))
        self._n += 1