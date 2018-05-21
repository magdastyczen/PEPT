# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:18:24 2017

@author: magda
"""

import math
import numpy as np
from scyntylator import Scyntylator
import matplotlib.pyplot as plt

class Detektor:
    def __init__(self, w_scyn = 0.7, h_scyn=1.9, d_scyn=50.0):
        self._segmenty = []
        self._w_scyn = w_scyn
        self._h_scyn = h_scyn
        self._d_scyn = d_scyn
        self._plot = plt.subplot(111)
        self._plot.set_ylim([-80, 80])   # set the bounds to be 10, 10
        self._plot.set_xlim([-80, 80])
        self._plot.set_aspect('equal')
        plt.axes().set_aspect('equal')

    def dodajSegment(self, n, r, theta0, theta_skok, z=0):
        self._segmenty.append(Segment(r, theta_skok, theta0))
        theta1 = math.atan2(self._w_scyn/2, r-self._h_scyn/2)
        theta2 = math.atan2(self._w_scyn/2, r+self._h_scyn/2)
        for i in range(0, n):
            wsp = []
            wsp.append([r-self._h_scyn/2, theta0 - theta1 + theta_skok*i, z-self._d_scyn/2]) #A-
            wsp.append([r-self._h_scyn/2, theta0 - theta1 + theta_skok*i, z+self._d_scyn/2]) #A+
            wsp.append([r+self._h_scyn/2, theta0 - theta2 + theta_skok*i, z-self._d_scyn/2]) #B-
            wsp.append([r+self._h_scyn/2, theta0 - theta2 + theta_skok*i, z+self._d_scyn/2]) #B+
            wsp.append([r+self._h_scyn/2, theta0 + theta2 + theta_skok*i, z-self._d_scyn/2]) #C-
            wsp.append([r+self._h_scyn/2, theta0 + theta2 + theta_skok*i, z+self._d_scyn/2]) #C+
            wsp.append([r-self._h_scyn/2, theta0 + theta1 + theta_skok*i, z-self._d_scyn/2]) #D-
            wsp.append([r-self._h_scyn/2, theta0 + theta1 + theta_skok*i, z+self._d_scyn/2]) #D+
            self._segmenty[-1].dodajScyntylator(wsp, theta0 + theta_skok*i)

    def dajScyntylatory(self):
        scyntylatory = []
        for segment in self._segmenty:
            scyntylatory += segment._scyntylatory
        return scyntylatory


    @staticmethod
    def odbijScyntylatorII(id):
        if id < 25:
            return 24 - id
        elif id < 48:
            return 48 + 24 - id
        elif id < 72:
            return 47 + 72 - id
        elif id < 96:
            return 96 - id + 71
        elif id < 144:
            return 95 + 144 - id
        else:
            return 192 - id + 143

    @staticmethod
    def odbijScyntylatorIII(id):
        if id < 23:
            return id + 14
        elif id < 25:
            return id - 14
        elif id < 72:
            return id + 24
        elif id < 96:
            return id - 24
        elif id < 144:
            return id + 48
        else:
            return id - 48

    @staticmethod
    def odbijScyntylatorIV(id):
        if id < 48:
            return 48 - id
        elif id < 96:
            return 48 + (95 - id)
        else:
            return 96 + (191 - id)


    def __str__(self):
        s = "Detektor sklada sie z {} segmentów.\n".format(len(self._segmenty))
        for segment in self._segmenty:
            segment._n
            s+="Segment składa się z {} scyntylatorów.\n".format(segment._n)
        return s

    def dajScyntylatoryTrafioneXY(self, prosta):
        scyntylatory = self.dajScyntylatoryZZakresu(prosta)
        ret = []
        for s in scyntylatory:
            if Detektor.testXY(s, prosta):
                ret += [s]
        return ret

    def dajScyntylatoryTrafione(self, proste):
        pxy = proste[:3]
        pyz = proste[3:]
        scyntylatory = self.dajScyntylatoryTrafioneXY(pxy)
        ret = []
        for s in scyntylatory:
            if Detektor.testYZ(s, pyz):
                ret += [s]
        return ret


   # def dajWszystkiescyntylatory(self):
   #     scyntylatory = self.dajScyntylatoryTrafione
    #    ret = []
    #    i._id for i in scyntylatory
     #   if i._id < 49:
      #      ret +=[50- i._id]


    def dajScyntylatoryZZakresu(self, prosta, zakres=2.05):
        z1, z2 = Detektor.liczZakres(prosta, zakres)
        #self.rysujProsta(prosta)
        #self.rysujProsta(z1)
        #self.rysujProsta(z2)
        scyntylatory = []
        for segment in self._segmenty:
            x1_seg = []
            x1_seg.extend(Detektor.punktyPrzeciecia(z1,segment._r - self._h_scyn/2))
            x1_seg.extend(Detektor.punktyPrzeciecia(z1,segment._r + self._h_scyn/2))
            x2_seg = []
            x2_seg.extend(Detektor.punktyPrzeciecia(z2,segment._r - self._h_scyn/2))
            x2_seg.extend(Detektor.punktyPrzeciecia(z2,segment._r + self._h_scyn/2))

            y_seg = map(Detektor.liczProsta, [z1 + (x,) for x in x1_seg])
            y_seg += (map(Detektor.liczProsta, [z2 + (x,) for x in x2_seg]))

            x_seg = x1_seg + x2_seg

            pprost = Detektor.prostaProstopadla(z1)
            #self.rysujProsta(pprost)
            zakres1 = []
            zakres2 = []


            for x, y in zip(x_seg, y_seg):
                if y < Detektor.liczProsta(pprost + (x,)):
                    zakres1.append((x,y))
                else:
                    zakres2.append((x,y))



            phi = []
            if len(zakres1) == 4 and len(zakres2) == 4:
                phi1 = map(Detektor.liczPhi, zakres1)
                phi2 = map(Detektor.liczPhi, zakres2)
                phi = [Detektor.wyznaczSkrajnePhi(phi1), Detektor.wyznaczSkrajnePhi(phi2)]
            elif len(zakres1) + len(zakres2) <= 1:
                continue
            else:
                phi1 = map(Detektor.liczPhi, zakres1 + zakres2)
                phi = [Detektor.wyznaczSkrajnePhi(phi1)]
#                for p in zakres1:
#                    self._plot.scatter(p[0], p[1], s=50, c='r')
#                for p in zakres2:
#                    self._plot.scatter(p[0], p[1], s=50, c='y')
            """
            for p in zakres1:
                self._plot.scatter(p[0], p[1], s=50, c='r')
            for p in zakres2:
                self._plot.scatter(p[0], p[1], s=50, c='y')
            """
            for kat in phi:
                scyntylatory += self.dajScyntylator(kat, segment)
            #return [(math.degrees(phi1_min), math.degrees(phi1_max)),(math.degrees(phi2_min), math.degrees(phi2_max))]

        return scyntylatory

    @staticmethod
    def testXY(scyntylator, promienXY):
        wsp = list(set(scyntylator.wspKart()))
        pnad, ppod = (0, 0)
        for w in wsp:
            if w[1] < Detektor.liczProsta(promienXY + (w[0],)):
                ppod += 1
            else:
                pnad += 1

        if ppod > 0 and pnad > 0:
            return True
        else:
            return False

    @staticmethod
    def testYZ(scyntylator, promienYZ):
        wsp = list(set(scyntylator.wspKart()))
        pnad, ppod = (0, 0)
        for w in wsp:
            if w[2] < Detektor.liczProsta(promienYZ + (w[1],)):
                ppod += 1
            else:
                pnad += 1

        if ppod > 0 and pnad > 0:
            return True
        else:
            return False


    def dajScyntylator(self, zakres_phi, seg): #zakres_phi = (min, max)
        phi1 = 2*math.pi - seg._theta0 if zakres_phi[0] - seg._theta0 < 0 else zakres_phi[0] - seg._theta0
        phi2 = 2*math.pi - seg._theta0 if zakres_phi[1] - seg._theta0 < 0 else zakres_phi[1] - seg._theta0

        i1 = int(math.ceil((phi1)/seg._theta))
        i2 = int(math.floor((phi2)/seg._theta))

        if phi1 > phi2 and abs(phi1-phi2) > math.pi:
            #print("Segment {}: phi0 = {}, phi1 = {}".format(seg._r, phi1, phi2))
            #print("Segment {}: Scyntylatory[{}:{}] + Scyntylatory[{}:{}]".format(seg._r, i1,'', '', i2+1))
            return seg._scyntylatory[i1:] + seg._scyntylatory[:i2+1]
        else:
            #print("Segment {}: phi0 = {}, phi1 = {}".format(seg._r, phi1, phi2))
            #print("Segment {}: Scyntylatory[{}:{}]".format(seg._r, i1,i2+1))
            return seg._scyntylatory[min(i1,i2):max(i1,i2)+1]



    @staticmethod
    def wyznaczSkrajnePhi(katy): # zwraca graniczne kąty zakresu (min, max)
        katy = np.array(katy)
        kmin = min(katy)
        kmax = max(katy)
        if kmax <= math.pi or kmin > math.pi: # sprawdzić czy nie <
            return (min(katy),max(katy))
        else:
            return (min(katy[katy>math.pi]), max(katy[katy<=math.pi]))


    def rysujProsta(self, prosta, d = 1000):
        x = []
        y = []
        if prosta[1] == 0:
            x = [-prosta[2]/prosta[0], -prosta[2]/prosta[0]]
            y = [-d, d]
        else:
            x = [-d, d]
            y = [Detektor.liczProsta(prosta + (x[0],)), Detektor.liczProsta(prosta + (x[1],))]
        self._plot.plot(x,y)

    @staticmethod
    def prostaProstopadla(prosta):
        ret = None
        if prosta[0] == 0:
            ret = (1.0, 0, 0)
        else:
            ret = (-prosta[1]/prosta[0], 1.0, 0)
        return ret

    @staticmethod
    def rownanieKwadratowe(a, b, c):
        x = []
        d = b**2-4*a*c
        if d == 0:
            x = [-b / (2 * a)]
        elif d > 0:
            x1 = (-b+math.sqrt(d))/(2*a)
            x2 = (-b-math.sqrt(d))/(2*a)
            x = [x1, x2]
        return x

    @staticmethod
    def punktyPrzeciecia(prosta, r):
        wynik = []
        if prosta[1] == 0:
            wynik = [-prosta[2]]
        else:
            a = 1 + ((prosta[0]**2)/(prosta[1]**2))
            b = (2 * prosta[0] * prosta[2])/(prosta[1]**2)
            c = (prosta[2]**2)/(prosta[1]**2) - r**2
            wynik = Detektor.rownanieKwadratowe(a, b, c)
        return wynik

    @staticmethod
    def liczProsta(prosta): #(A, B, C, x)
        if prosta[1] == 0:
            return -prosta[2]/prosta[0]
        else:
            return -(prosta[0]*prosta[3] + prosta[2])/prosta[1]

    @staticmethod
    def liczZakres(prosta, zakres):
        a = prosta[0]
        b = prosta[1]
        c = prosta[2]

        c1 = c - zakres * math.sqrt(a**2 + b**2)
        c2 = c + zakres * math.sqrt(a**2 + b**2)
        return ((a, b, min(c1,c2)), (a, b, max(c1,c2)))

    @staticmethod
    def liczPhi(p): # (x, y)
        phi = math.atan2(p[0],p[1])
        phi = phi if phi >= 0 else phi + 2*math.pi
        return phi

    def rzutuj(self, scyntylatory = []):
        x_ret = []
        y_ret = []

        if len(scyntylatory) == 0:
            for s in self._segmenty:
                scyntylatory.extend(s._scyntylatory)

        for s in scyntylatory:
            (x, y) = s.wspKart2D()
            x_ret.extend(x)
            y_ret.extend(y)

        return (x_ret, y_ret)

    def rzutuj3D(self, scyntylatory=[]):
        lista = []
        if len(scyntylatory) == 0:
            for s in self._segmenty:
                scyntylatory.extend(s._scyntylatory)
        for s in scyntylatory:
            lista.append(s.wspKart3D())
        return lista

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

    def dodajScyntylator(self, w, kat):
        self._scyntylatory.append(Scyntylator(w, kat))
        self._n += 1
