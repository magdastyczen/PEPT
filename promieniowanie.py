# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:44:50 2017

@author: magda
"""
import scipy.stats as st
from scipy.stats import cosine
import math
import numpy as np

from promien import Promien

class rozkladTheta(st.rv_continuous):
    def _pdf(self,x):
        return ((7.89875 * 10**7) - (630481 * x) -(15940.4 * x**2) + (147.356 * x**3))/(3.09892*10**9) # Normalized over its range, in this case [0,90]

class Promieniowanie:
    def __init__(self, n = 1000):
        self._promienie = []
        rozkladT = rozkladTheta(a=0, b=90, name='rozkladTheta')
        theta = np.deg2rad(rozkladT.rvs(size=(n, 1)))
        #alpha = Promieniowanie.rozkladCos(n, 0, math.pi/2)
        alpha = (np.arccos(2*np.random.rand(n)-1))*2
        phi = (np.arccos(2*np.random.rand(n)-1))/2
        r = np.random.uniform(low=0, high=58.45, size=(n,1))
        z = np.random.uniform(low=0, high=25, size=(n,1))
        
        
        for r, p, z, t, a in zip(r, phi, z, theta, alpha):
            self._promienie.append(Promien(r, p, z, t, a))
            
    def rzutuj2(self):
        lista_x = []
        lista_y = []
        for p in self._promienie:
            r, p, z, t, a = p.dajArg()
            x, y = self.wyznaczOdcinek(r, p, t)
            lista_x.append(x)
            lista_y.append(y)
        return (lista_x, lista_y)
#            
    def rzutuj(self):
        lista_x = []
        lista_y = []
        for p in self._promienie:
            p0 = p.dajPunktKart()
            p1 = p.dajPunkt2(p0, -200.0)
            p2 = p.dajPunkt2(p0, 200.0)
            x, y = ([p1[0], p2[0]], [p1[1], p2[1]])
            lista_x.append(x)
            lista_y.append(y)
        return (lista_x, lista_y)
        
    def wyznaczOdcinek(self, r, phi, theta, length=200):
        x = r*math.cos(phi)
        y = r*math.sin(phi)
        angle = math.pi/2 - theta
        
        leny = length * math.sin(angle)
        lenx = length * math.cos(angle)
        
        endx=x+lenx
        endy=y+leny
        x-=lenx
        y-=leny
        
        
        return ([x, endx], [y, endy])
        
    def wypiszPhi(self):
        for p in self._promienie:
            r, p, z, t, a = p.dajArg()
            print(p)


        
    @staticmethod
    def rozkladCos(n, a = 0, b = math.pi/2):
        srodek = (b-a)/2
        v = (np.random.rand(n, 1) * 2) - 1
        return a + srodek + srodek * v
        
        