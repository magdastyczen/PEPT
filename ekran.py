# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 14:21:18 2017

@author: magda
"""
import math
import matplotlib.pyplot as plt
import time
from detektor import Detektor

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

    def rysujScyntylatory(self, scyntylatory):
        x_ret = []
        y_ret = []
        for s in scyntylatory:
            (x, y) = s.wspKart2D()
            x_ret.extend(x)
            y_ret.extend(y)
        
            
        self._detektor.scatter(x_ret, y_ret, s=50, c='#aaff32')
        
    def rysujPromienie(self, p):
        (xl, yl) = p.rzutuj()
        for x, y in zip(xl, yl):
            self._detektor.plot(x, y)
    
    def rysujProsta(self, prosta, d = 1000):
        x = []
        y = []
        if prosta[1] == 0:
            x = [-prosta[2]/prosta[0], -prosta[2]/prosta[0]]
            y = [-d, d]
        else:
            x = [-d, d]
            y = [Detektor.liczProsta(prosta + (x[0],)), Detektor.liczProsta(prosta + (x[1],))]
                    
        self._detektor.plot(x,y)

    def pokaz(self):
        plt.show()
        
    def rysujPunktyGraniczne(self,phi):
        self._detektor.plot(57.5*math.cos(phi), 57.5*math.sin(phi),'ro')        
        
