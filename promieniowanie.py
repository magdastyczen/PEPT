# -*- coding: utf-8 -*-
"""
Created on Sat Dec 30 12:44:50 2017

@author: magda
"""
import scipy.stats as st
from scipy.stats import cosine
import math
import numpy as np
import random

from scyntylator import Scyntylator
from promien import Promien

class rozkladTheta(st.rv_continuous):
    def _pdf(self,x):
        return ((7.89875 * 10**7) - (630481 * x) -(15940.4 * x**2) + (147.356 * x**3))/(3.09892*10**9) # Normalized over its range, in this case [0,90]

class Promieniowanie:
    A = 0.7
    B = 1.9
    R1 = 42.5
    R2 = 46.75
    R3 = 57.5
    R = 58.15
    def __init__(self, n = 1000, scyntylatory = []):
        self._promienie = []
        liczba_scyntylatorow = len(scyntylatory)
        while len(self._promienie) < n:
            d = int(np.random.rand(1) * liczba_scyntylatorow) #generacja nr detektpr
            wylosowany_scyntylator = scyntylatory[d]
            if not self.sprawdzDlugosc(wylosowany_scyntylator):
                print("Odrzucamy promien")
                continue

            i = (Promieniowanie.A * np.random.rand(1)) - Promieniowanie.A/2 #generacja punktu x o wsp w początku uk. wsp
            j = (Promieniowanie.B * np.random.rand(1)) - Promieniowanie.B/2 #generacja punktu y o wsp w początku uk. wsp

            przesuniecieY = 0
            if d < 48:
                przesuniecieY = j + Promieniowanie.R1
            if d < 96:
                przesuniecieY = j + Promieniowanie.R2
            else:
                przesuniecieY = j + Promieniowanie.R3

            x = i * np.cos(2*np.pi - wylosowany_scyntylator._kat )  - przesuniecieY * np.sin(2 * np.pi - wylosowany_scyntylator._kat)   # Odwolanie do kata!!!!!!
            y = i * np.sin(2*np.pi - wylosowany_scyntylator._kat )  + przesuniecieY * np.cos(2 * np.pi - wylosowany_scyntylator._kat)

            r = np.sqrt(x**2+y**2)
            if x > 0:
                phi = (np.arcsin(y/r))
            else:
                phi = (- np.arcsin(y/r) + np.pi)

            rozkladT = rozkladTheta(a=0, b=90, name='rozkladTheta')
            theta = np.deg2rad(rozkladT.rvs(size=(1, 1))) * random.sample(set([-1, 1]), 1) #odbicie rozkldu theta
            alpha = (np.arccos(2*np.random.rand(1)-1))*2
            z = np.random.uniform(low=0, high=25, size=(1,1))
            pr = Promien(r[0], phi[0], z[0][0], theta[0][0], alpha[0])
            self._promienie.append(pr)
            print("Dodajemy promien {}".format(pr))


    def sprawdzDlugosc(self, s):
        wsp = s.wspKart() # [w1 ... w8]
        Ax = wsp[0][0]
        Cx = wsp[4][0]
        B = np.random.rand(1)
        P = abs(Ax - Cx)/ np.sqrt(Promieniowanie.A**2 + Promieniowanie.B**2)
        return B > P



#    def sprawdzRozklad(self, promien):
#            # Y=sqrt(R^2-x1^2) d=2Y
#            #p= a/ cos(pi/2- kat) ;kat=0 i pi -> p=a; kat =pi/2 i 3/2 pi -> p=b
#            #if (k < (1-(d/2R)* (p/b) ))\
#        wsp = promien.dajPunktKart()
#        y1 = np.sqrt(Promieniowanie.R**2 - wsp[0]**2)
#       # K=((2*np.sqrt(Promieniowanie.R**2-wsp[0]**2))/(np.pi*Promieniowanie.R**2))
#        K = 1-(2*abs(y1)/(2*Promieniowanie.R))
#        B = np.random.rand(1)
#        print(K,B)
#        return B > K

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
