# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:19:40 2017

@author: magda
"""

class Promien:
    def __init__(self, r = 0, phi = 0, z = 0, theta = 0, alpha = 0):
        self._phi = phi
        self._theta = theta
        self._alpha = alpha
        self._r = r
        self._z = z
        
    def dajArg(self):
        return (self._r, self._phi, self._z, self._theta, self._alpha)


"""
import math
import numpy
import numpy as np
import scipy
import scipy.stats as st
from scipy.stats import rv_continuous
import matplotlib.pyplot as plt


# Wielomian odpowiadajcy rozkladowi mionow
class my_pdf(st.rv_continuous):
    def _pdf(self,x):
        return ((7.89875 * 10**7) - (630481 * x) -(15940.4 * x**2) + (147.356 * x**3))/(3.09892*10**9) # Normalized over its range, in this case [0,90]


n = 100

#Zdefiniowanie gestosc prawdopodobienstwa katow   
rozkladkata = my_pdf(a=0, b=90, name='my_pdf')

#Generujemy n katow Theta (nachylenie wzgledem osi pionowej)
theta = rozkladkata.rvs(size=(n, 1))

#Generujemy n katow Theta (kat w plasczyznie XY)
#alpha = np.random.rand(n, 1)alpha = cunifavariate(math.pi/4, math.pi/4)
a = np.random.rand(n, 1)
alpha = (math.pi/4 + math.pi/4 * (a - 0.5)) % math.pi

#generujemy rozklad punktow zaczepienia w osi OX od 0 do R 
anchor_point_R = np.random.uniform(low=0, high=57.5, size=(n,1))

#Generujemy n punktow zaczepienia w osi OY od 0 do 90 stopni  0.785398163
anchor_point_FI = np.random.uniform(low=0, high=1.570796327, size=(n,1))
# np.random.rand(n,2)
z = np.random.rand(n, 1)
#Laczymy w macierz nx5   theta=alpha
rays = np.concatenate((anchor_point_FI, anchor_point_R, theta, alpha, z), axis=1)
np.savetxt('test.out', theta, delimiter=',')
#print rays[1:3, :]
#-----------------------------------------------------------------------------

#test czy rozklad jest wlasciwy

def testrozkladu(r_list, fi_list, beta_list):
    punktprzeciecia = []
    for r, fi, beta in zip(r_list, fi_list, beta_list):
        x = r * math.cos(fi)
        y = r * math.sin(fi)
        A = math.atan(1.570796327 - beta)
        D = math.tan(0.7)
        C = -y + A*x
        z = -(C/A)
        if 0 <= z and z <= 57.5:
  
            punktprzeciecia.append([z, beta]) 
         
    return np.asarray(punktprzeciecia) #przed zwroceniem wartosci, konwertuje jeszcze liste do macierzy NumPy 

#Wywolujemy funkcje z odpowiednimi argumentami, a jej wynik od razu przypisujemy do macierzy punktprzeciecia:
punktprzeciecia = testrozkladu(r_list = rays[:,1], fi_list = rays[:,0], beta_list = rays[:,2]) 



def obszarszukania(a, b, c1, c2):
    obszar = []
    while m < n:        
        m=0
        r = rays[m, 1]
        fi = rays[m, 0]
        theta = rays[m, 2]
        x = r * math.cos(fi)
        y = r * math.sin(fi)
       
 #Prosta AX+BY+C=0; B=-1, A=tg(beta)-> wyliczenie C     
        d = 1.0124
        b = -1
        a = math.tan(theta)
        c = y - a*x

#prosta y prechodzaca przez punkt x,y pod katem beta
        y = a*x + c
        #x1 = (2*c) / (2*a + 2)
        #x2 = (-2*c) / (2 - 2*a)

        #y1 = a * x1 + c 
        #y2 = a * x2 + c
#dwie proste ograniczajajace pole poszukiwania
 #wzor na odleglosc punktu od prostej => tutaj wzor na prosta w odleglosci pol przekontnej detektora od wylosowanego punktu, a jest stale zmienne C
    
        c1 = d * math.sqrt( a**2 + b**2 ) - a * x - b * y 
        c2 = d * math.sqrt( a**2 + b**2 ) + a * x + b * y 
        obszar.append([a, b, c1, c2])
        m = m + 1
    return obszar
#print(obszar)



#print(wierzcholek1plus)

#wyznaczenie prostej w przestrzeni
def plaszczyznaXY():
    XY = []
    while m < n:        
        m=0
        r = rays[m, 1]
        fi = rays[m, 0]
        theta = rays[m, 2]
        alpha = 90 - theta
        x = r * math.cos(fi)
        y = r * math.sin(fi)
       
 #Prosta AX+BY+C=0; B=-1, A=tg(beta)-> wyliczenie C     
        B=-1
        A= math.tan(alpha)
         C= -A*x - y
#prosta y prechodzaca przez punkt x,y pod katem beta
        y = a*x + c
        #x1 = (2*C) / (2*A + 2)
        #x2 = (-2*C) / (2 - 2*A)

        #y1 = a * x1 + c 
        #y2 = a * x2 + c
#dwie proste ograniczajajace pole poszukiwania
 #wzor na odleglosc punktu od prostej => tutaj wzor na prosta w odleglosci pol przekontnej detektora od wylosowanego punktu, a jest stale zmienne C
    
        c1 = d * math.sqrt( a**2 + b**2 ) - a * x - b * y 
        c2 = d * math.sqrt( a**2 + b**2 ) + a * x + b * y 
        obszar.append([a, b, c1, c2])
        m = m + 1
    return obszar
"""