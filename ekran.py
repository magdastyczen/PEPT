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

    def rysujPromienieNaScyntylator(self, x, y):
        axes, plot = plt.subplots(1, 1,)
        plt.bar(x, y)
        plt.xlabel("ID scyntylatora")
        plt.ylabel("Liczba wygenerowanych promieni")

    def rysujHistogramy(self, histo1, histo2, histo3, histo4, s24, s12, s119):
        #plt.figure()
        fig, axes = plt.subplots(3, 1, sharey=True, tight_layout=True)
        axes[0].hist(histo1, max(histo1))
        #axes[0].axis([0, max(histo1), 0, len(histo1)])
        axes[0].grid(True)
        axes[0].set_title("Liczba trafien na promien")

        axes[1].hist(histo2, max(histo2))
        #axes[1].axis([0, max(histo2), 0, len(histo2)])
        axes[1].grid(True)
        axes[1].set_title("Liczba trafien w scyntylator")

        axes[2].hist(histo3, max(histo3))
        #axes[2].axis([0, max(histo3), 0, len(histo3)])
        axes[2].grid(True)
        axes[2].set_title("Kat trafienia")
        


        fig2, axes2 = plt.subplots(len(histo4), 1, sharey=True,
                                   tight_layout=True)

        i = 0
        for key, val in histo4.iteritems():
            #print(val)
            axes2[i].hist(val, max(val))
            #axes2[i].axis([0, max(val), 0, len(val)])
            axes2[i].grid(True)
            axes2[i].set_title("{} trafien".format(key))
            i += 1

        #range = 1 if len(s24) == 0 else max(s24)
        fig3, axes3 = plt.subplots(1, 1)
        axes3.hist(s24, 180)
        axes3.grid(True)
        axes3.set_title("Liczba trafien w scyntylator 24 w zaleznosci od theta")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Kat theta padajacego promienia")

        fig4, axes4 = plt.subplots(1, 1)
        axes4.hist(s12, max(s12)-1)
        axes4.grid(True)
        axes4.set_title("Liczba trafien w scyntylator 12 w zaleznosci od krotnosci")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Ile detektorow trafil promien")

        fig5, axes5 = plt.subplots(1, 1)
        axes5.hist(s119, max(s119)-1)
        axes5.grid(True)
        axes5.set_title("Liczba trafien w scyntylatory 119 + 120 w zaleznosci od krotnosci")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Ile detektorow trafil promien")