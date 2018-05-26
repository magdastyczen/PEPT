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
    def __init__(self, n = 1000):
        self._promienie = []
        while len(self._promienie) < n:
            d = int(np.random.rand(1) * 196) #generacja nr detektpr
           
           
           
            i = (A * np.random.rand(1)) - A/2 #generacja punktu x o wsp w początku uk. wsp
            j = (B * np.random.rand(1)) - B/2 #generacja punktu y o wsp w początku uk. wsp
            
            
            
            
            
            if d < 48:
                return j + R1
            if d < 96:
                return j + R2
            else:
                return j + R3



            x= i * np.cos(2*np.pi - Scyntylator.(d_kat) )  - j * np.sin(2 * np.pi - Scyntylator.(d_kat))   # Odwolanie do kata!!!!!!
            x= i * np.sin(2*np.pi - Scyntylator.(d_kat) )  + j * np.cos(2 * np.pi - Scyntylator.(d_kat)) 
               
        for X, Y in zip(x, y):
            R = np.sqrt(X**2+Y**2)
            r.append(R)
            if X > 0:
                phi.append(np.arcsin(Y/R))
            else:
                phi.append(- np.arcsin(Y/R) + np.pi)        
               
               
            rozkladT = rozkladTheta(a=0, b=90, name='rozkladTheta')
            theta = np.deg2rad(rozkladT.rvs(size=(1, 1)))*random.sample(set([-1, 1]), 1)
            alpha = (np.arccos(2*np.random.rand(1)-1))*2
            z = np.random.uniform(low=0, high=25, size=(1,1))
            pr = Promien(r[0], phi[0], z[0], theta[0], alpha[0])
            
            if self.sprawdzDlugosc(pr):
                self._promienie.append(pr)
            else:
                print('glupiajestem')    
    

    def sprawdzDlugosc(self, scyntylator):   
        B = np.random.rand(1)
        P = abs(wps1 - wsp2)/ np.sqrt(A**2 + B**2)
        return B > P
    
    def przesunieciePunktu(self, promien):
    
    def obrotpunktu(self, promien):
        x = Promieniowanie.
        
        
        
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
