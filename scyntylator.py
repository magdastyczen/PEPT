# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:16:07 2017

@author: magda
"""

import math

class Scyntylator:
    LICZBA = 0

    def __init__(self, w, kat):
        self._wierzcholki = w
        self._kat = kat
        self._id = Scyntylator.LICZBA
        Scyntylator.LICZBA += 1

#    def _str_(self):
#        ret = w.wspKart()
#        for w in self._wierzcholki:
#            ret_str +=  str(w)
#        return ret   

    def __str__(self):
        ret_str = "Scyntylator {}\t".format(self._id)
        wsp = self.wspKart()
        for w, nazwa in zip(wsp, ["A-", "A+", "B-", "B+", "C-", "C+", "D-", "D+"]):
            ret_str += "{}:({:.2f}, {:.2f}, {:.2f})\t".format(nazwa, w[0], w[1], w[2])
        return ret_str
        
        
    def wspWalc(self):
        return self._wierzcholki

    def wspKart(self):
        kart = []
        for p in self._wierzcholki:
            kart.append((p[0]*math.sin(p[1]), p[0]*math.cos(p[1]), p[2]))
        return kart
         

    def wspKart2D(self):
        x = []
        y = []
        for p in self._wierzcholki:
            x.append(p[0]*math.sin(p[1]))
            y.append(p[0]*math.cos(p[1]))
        return (x, y)
    def wspKart3D(self):
        x = []
        y = []
        z = []
        for p in self._wierzcholki:
            x.append(p[0]*math.sin(p[1]))
            y.append(p[0]*math.cos(p[1]))
            z.append(p[2])
        return (x, y, z)
