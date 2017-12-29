# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:16:07 2017

@author: magda
"""

import math

class Scyntylator:
    LICZBA = 0    
    
    def __init__(self):
        self._wierzcholki = []
        self._id = Scyntylator.LICZBA
        Scyntylator.LICZBA += 1
    
    def __init__(self, w):
        self._wierzcholki = w
    
    def wspWalc(self):
        return self._wierzcholki
        
    def wspKart(self):
        kart = []
        for p in self._wierzcholki:
            kart.append([p[0]*math.cos(math.radians(p[1])), p[0]*math.sin(math.radians(p[1])), p[2] )
        return kart