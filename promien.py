

# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:19:40 2017

@author: magda
"""

import numpy as np

class Promien:
    def __init__(self, r = 0, phi = 0, z = 0, theta = 0, alpha = 0, id = 0):
        self._phi = phi
        self._theta = theta
        self._alpha = alpha
        self._r = r
        self._z = z
        self._idScyntylatora = id

    def dajPunktKart(self):
        return np.array([self._r * np.cos(self._phi),
                         self._r * np.sin(self._phi),
                         self._z])


        return np.array([self._r * np.cos(self._phi),
                         self._r * np.sin(self._phi),
                         self._z])

    def dajProstaKart(self):      
        a = (np.tan(np.pi/2 - self._theta))
        return (a, -1, np.sin(self._phi)*self._r - a*self._r*np.cos(self._phi))

    def dajPunkt2(self, p1, d=1.0):
        x2=  d*np.cos(np.pi/2 -self._theta)*np.sin(self._alpha)
        y2 = d*np.sin(np.pi/2 - self._theta)
        z2 = d*np.cos(np.pi/2 - self._theta)*np.cos(self._alpha)
        p2 = np.array([x2, y2, z2]) + p1
        return p2

    def dajProste(self):
        p1 = self.dajPunktKart()
        p2 = self.dajPunkt2(p1)
        a = (p1[1] - p2[1])/(p1[0] - p2[0])
        b = p2[1] - a*p2[0]
        c = (p1[2] - p2[2])/(p1[1]-p2[1])
        d = p2[2] - c * p2[1]
        return (a, -1, b, c, -1, d)

    def dajArg(self):
         return (self._x, self._y, self._z, self._theta, self._alpha)
