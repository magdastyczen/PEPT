# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:44:50 2017

@author: magda
"""
import scipy.stats as st
import math
import numpy as np
import matplotlib.pyplot as plt

from promien import Promien

class rozkladTheta(st.rv_continuous):
    def _pdf(self,x):
        return ((7.89875 * 10**7) - (630481 * x) -(15940.4 * x**2) + (147.356 * x**3))/(3.09892*10**9) # Normalized over its range, in this case [0,90]

class Promieniowanie:
    def __init__(self, n = 1000):
        self._promienie = []
        rozkladT = rozkladTheta(a=0, b=90, name='rozkladTheta')
        theta = np.deg2rad(rozkladT.rvs(size=(n, 1)))
        alpha = Promieniowanie.rozkladCos(n, 0, math.pi*2)
        phi = Promieniowanie.rozkladCos(n)
        r = np.random.uniform(low=0, high=58.45, size=(n,1))
        z = np.random.uniform(low=-25, high=25, size=(n,1))
        
        for r, p, z, t, a in zip(r, phi, z, theta, alpha):
            self._promienie.append(Promien(r, p, z, t, a))
            
        self._fig = plt.figure()

            
    def rysuj(self):
        for p in self._promienie:
            r, p, z, t, a = p.dajArg()
            self.rysujPromien(r, p, t)
        
        self._fig.show()

        
    def rysujPromien(self, r, phi, theta, length=10):
        x = r*math.cos(phi)
        y = r*math.sin(phi)
        angle = math.pi/2 - theta
        
        endy = length * math.sin(math.radians(angle))
        endx = length * math.cos(math.radians(angle))

        ax = plt.subplot(111)
        ax.set_ylim([0, 10])   # set the bounds to be 10, 10
        ax.set_xlim([0, 10])
        ax.plot([x, endx], [y, endy])

        
    @staticmethod
    def rozkladCos(n, a = 0, b = math.pi/2):
        srodek = (b-a)/2
        v = (np.random.rand(n, 1) * 2) - 1
        return a + srodek + srodek * v
        
        