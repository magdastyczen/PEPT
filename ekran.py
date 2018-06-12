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
        fig, axes = plt.subplots(1, 1,)
        plt.bar(x, y)
        plt.xlabel("ID scyntylatora")
        plt.ylabel("Liczba wygenerowanych promieni")
        fig.savefig('detektoripromienie.png')
        plt.close(fig)
        


    def rysujHistogramy(self, histo1, histo2, histo3, histo4, s24, s12, s119120, s119, s120, s119i120, s59, s60, s59i60, s12t):
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
        fig.savefig('histogramy.png')   # save the figure to file
        plt.close(fig) 

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
        fig2.savefig('trafienia.png')   # save the figure to file
        plt.close(fig2) 
        
        #range = 1 if len(s24) == 0 else max(s24)
        fig3, axes3 = plt.subplots(1, 1)
        axes3.hist(s24, 180)
        axes3.grid(True)
        axes3.set_title("Liczba trafien w scyntylator 24 w zaleznosci od theta")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Kat theta padajacego promienia")
        fig3.savefig('Liczba_trafien_w_scyntylator_24_w_zaleznosci_od_theta.png')   # save the figure to file
        plt.close(fig3) 

        fig4, axes4 = plt.subplots(1, 1)
        axes4.hist(s12, max(s12)-1)
        axes4.grid(True)
        axes4.set_title("Liczba trafien w scyntylator 12 w zaleznosci od krotnosci")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Ile detektorow trafil promien")
        fig4.savefig('Liczba_trafien_w_scyntylator_12_w_zaleznosci_od_krotnosci.png')   # save the figure to file
        plt.close(fig4)         

        fig5, axes5 = plt.subplots(1, 1)
        axes5.hist(s119120, max(s119120)-1)
        axes5.grid(True)
        axes5.set_title("Liczba trafien w scyntylatory 119 lub 120 w zaleznosci od krotnosci")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Ile detektorow trafil promien")
        fig5.savefig('Liczba_trafien_w_scyntylator_119120_w_zaleznosci_od_krotnosci.png')   # save the figure to file
        plt.close(fig5)         
        
        fig6, axes6 = plt.subplots(1, 1)
        axes6.hist(s119, max(s119)-1)
        axes6.grid(True)
        axes6.set_title("Liczba trafien w scyntylatory 119  w zaleznosci od krotnosci")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Ile detektorow trafil promien")
        fig6.savefig('Liczba_trafien_w_scyntylator_119_w_zaleznosci_od_krotnosci.png')   # save the figure to file
        plt.close(fig6)         
        

        fig7, axes7 = plt.subplots(1, 1)
        axes7.hist(s120, max(s120)-1)
        axes7.grid(True)
        axes7.set_title("Liczba trafien w scyntylator 120 w zaleznosci od krotnosci")
        plt.ylabel("Liczba trafien")
        plt.xlabel("Ile detektorow trafil promien")        
        fig7.savefig('Liczba_trafien_w_scyntylator_120_w_zaleznosci_od_krotnosci.png')   # save the figure to file
        plt.close(fig7)         
        
#        fig8, axes8 = plt.subplots(1, 1)
#        axes8.hist(s119i120, max(s120)-1)
#        axes8.grid(True)
#        axes8.set_title("Liczba trafien w scyntylator 119 i 120 w zaleznosci od krotnosci")
#        plt.ylabel("Liczba trafien")
#        plt.xlabel("Ile detektorow trafil promien") 
#
#        fig9, axes9 = plt.subplots(1, 1)
#        axes9.hist(s120, max(s120)-1)
#        axes9.grid(True)
#        axes9.set_title("Liczba trafien w scyntylator 60 w zaleznosci od krotnosci")
#        plt.ylabel("Liczba trafien")
#        plt.xlabel("Ile detektorow trafil promien") 
#
#        fig10, axes10 = plt.subplots(1, 1)
#        axes10.hist(s120, max(s120)-1)
#        axes10.grid(True)
#        axes10.set_title("Liczba trafien w scyntylator 59 w zaleznosci od krotnosci")
#        plt.ylabel("Liczba trafien")
#        plt.xlabel("Ile detektorow trafil promien") 
#        
#        fig11, axes11 = plt.subplots(1, 1)
#        axes11.hist(s59i60, max(s120)-1)
#        axes11.grid(True)
#        axes11.set_title("Liczba trafien w scyntylator 59 i 60 w zaleznosci od krotnosci")
#        plt.ylabel("Liczba trafien")
#        plt.xlabel("Kat theta padajacego promienia")                 
#
#        fig12, axes12 = plt.subplots(1, 1)
#        axes12.hist(s12t, 180)
#        axes12.grid(True)
#        axes12.set_title("Liczba trafien w scyntylator 12 w zaleznosci od theta")
#        plt.ylabel("Liczba trafien")
#        plt.xlabel("Kat theta padajacego promienia")        