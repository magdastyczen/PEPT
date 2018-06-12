# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:18:24 2017

@author: magda styczeń
"""

from detektor import Detektor
from promieniowanie import Promieniowanie
from ekran import Ekran
import numpy as np

import math
import time
import collections

#start = time.time()

# trafienia to lista 192 liczb
# indeks to id scyntylatora, a wartosc to liczba trafien
def normalizujTrafienia(trafienia, scyntylatory):
    trafienia_przeskalowane = []
    #iteruje po wszystkich scyntylatorach i wymnazam liczbe trafien przez odpowiedni wspolczynnik
    for trafienie, scyntylator in zip(trafienia, scyntylatory):
        trafienie_przeskalowane = skalujTrafienia(trafienie, scyntylator._kat)
    return trafienia_przeskalowane

def skalujTrafienia(liczbaTrafien, kat, A=0.7, B=1.9):
    wsp = A / np.cos(np.pi-kat) 
    return liczbaTrafien * wsp

det = Detektor()

det.dodajSegment(48, 42.50, 0, math.radians(7.5))
det.dodajSegment(48, 46.75, math.radians(3.75), math.radians(7.5))
det.dodajSegment(96, 57.50, math.radians(1.875), math.radians(3.75))


#współrzedne detektora generownae do pliku
#with open("detektor.txt", "w") as logfile:
#    logfile.write(str(det))
    
#print(det)

# SCYNTYLATORY[id] = lista scyntylatorow [s1 ... s 192]
SCYNTYLATORY = det.dajScyntylatory()



scyntylatory_id = [s._id for s in SCYNTYLATORY]
print("Scyntylatory: {}".format(scyntylatory_id))

n_promieni = 20000

pr = Promieniowanie(n_promieni, SCYNTYLATORY)
print(pr)
ekran = Ekran()
#ekran.rysujPunkty(pr)

ekran.rysujDetektor(det)
ekran.rysujPromienie(pr)

s_Icwiartka = []
s = []
promienie_histogram = [0]*n_promieni
kat_histogram = []
trafienia_histogram = {}
s24_trafienia = [] #katy trafien w scyntylator 24
s12_krotnosc_trafien = []
s119_120_krotnosc_trafien = []
s119_krotnosc_trafien = []
s120_krotnosc_trafien = []
s119i120_krotnosc_trafien = []
s59_krotnosc_trafien = []
s60_krotnosc_trafien = []
s59i60_krotnosc_trafien = []
s12_trafienia = []

for i, prn in enumerate(pr._promienie):
    proste = prn.dajProste()
    trafione = det.dajScyntylatoryTrafione(proste)

    promienie_histogram[i] = len(trafione)
    kat_histogram += [int(math.degrees(prn._theta))]*len(trafione)
    if len(trafione) > 0:
        if len(trafione) not in trafienia_histogram:
            trafienia_histogram[len(trafione)] = []
        trafienia_histogram[len(trafione)] += [i._id for i in trafione]
    s += trafione

    # Zliczenie trafien w scyntylator 24
    # Z promieni wygenerowanych poza jego obrebem
    id_trafionych = [ts._id for ts in trafione]
    if prn._idScyntylatora != 24:
        if 24 in id_trafionych:
            s24_trafienia += [np.rad2deg(prn._theta)]

    id_trafionych = [ts._id for ts in trafione]
    if prn._idScyntylatora != 12:
        if 12 in id_trafionych:
            s12_trafienia += [np.rad2deg(prn._theta)]



    # Krotnosc trafien
    if 12 in id_trafionych:
        s12_krotnosc_trafien += [len(trafione)]
    if 119 in id_trafionych or 120 in id_trafionych:
        s119_120_krotnosc_trafien += [len(trafione)]
    if 119 in id_trafionych:
        s119_krotnosc_trafien += [len(trafione)]
    if 120 in id_trafionych:
        s120_krotnosc_trafien += [len(trafione)]
    if 119 in id_trafionych and 120 in id_trafionych:
        s119i120_krotnosc_trafien += [len(trafione)]
    if 59 in id_trafionych:
        s59_krotnosc_trafien += [len(trafione)]
    if 60 in id_trafionych:
        s60_krotnosc_trafien += [len(trafione)]
    if 60 in id_trafionych and 59 in id_trafionych:
        s59i60_krotnosc_trafien += [len(trafione)]

        
s_id = [i._id for i in s]

#ile promieni generowanych jest w danym scyntylatorze
x_promienie_na_scyntylator = range(len(SCYNTYLATORY))
y_promienie_na_scyntylator = [0]*len(SCYNTYLATORY)
for prn in pr._promienie:
    y_promienie_na_scyntylator[prn._idScyntylatora] += 1
ekran.rysujPromienieNaScyntylator(x_promienie_na_scyntylator, y_promienie_na_scyntylator)

#Obliczam histogram liczby trafien 
trafienia_na_scyntylator = [0]*len(SCYNTYLATORY)
for id in s_id:
    trafienia_na_scyntylator[id] += 1

# Histogram przekazuje do funkcji skalujacej trafienia i  zwroci liste trafien znormalizowanych (index - id scyntylatora)
trafienia_znormalizowane = normalizujTrafienia(trafienia_na_scyntylator, SCYNTYLATORY)

ekran.rysujScyntylatory(s)
ekran.rysujHistogramy(promienie_histogram, s_id, kat_histogram, trafienia_histogram,
                      s24_trafienia, s12_krotnosc_trafien, s119_120_krotnosc_trafien, s119_krotnosc_trafien, s120_krotnosc_trafien,
                      s119i120_krotnosc_trafien, s59_krotnosc_trafien, s59_krotnosc_trafien, s59i60_krotnosc_trafien, s12_trafienia)
ekran.pokaz()

with open("promienie_histogram.csv", "w") as plik:
    plik.write("\n".join(map(str, promienie_histogram)) + "\n")
    
with open("s_id.csv", "w") as plik:
    plik.write("\n".join(map(str, s_id)) + "\n")
    
with open("kat_histogram.csv", "w") as plik:
    plik.write("\n".join(map(str, kat_histogram)) + "\n")
    
with open("s24_trafienia.csv", "w") as plik: 
    plik.write("\n".join(map(str, s24_trafienia)) + "\n")
    
with open("s12_krotnosc_trafien.csv", "w") as plik:
    plik.write("\n".join(map(str, s12_krotnosc_trafien)) + "\n")
    
with open("s119_120_krotnosc_trafien.csv", "w") as plik:
    plik.write("\n".join(map(str, s119_120_krotnosc_trafien)) + "\n")

with open("s119_krotnosc_trafien.csv", "w") as plik:    
    plik.write("\n".join(map(str, s119_krotnosc_trafien)) + "\n")    

with open("s120_krotnosc_trafien.csv", "w") as plik:
    plik.write("\n".join(map(str, s120_krotnosc_trafien)) + "\n")

with open("s119i120_krotnosc_trafien.csv", "w") as plik:
    plik.write("\n".join(map(str, s119i120_krotnosc_trafien)) + "\n")

with open("s59_krotnosc_trafien.csv", "w") as plik:
    plik.write("\n".join(map(str, s59_krotnosc_trafien)) + "\n")

with open("s60_krotnosc_trafien.csv", "w") as plik:
    plik.write("\n".join(map(str, s60_krotnosc_trafien)) + "\n") 

with open("s59i60_krotnosc_trafien.csv", "w") as plik:
    plik.write("\n".join(map(str, s59i60_krotnosc_trafien)) + "\n")

with open("s12_trafienia.csv", "w") as plik:
    plik.write("\n".join(map(str, s12_trafienia)) + "\n")   
    
with open("trafienia_histogram.csv", "w") as plik:    
    for key, val in trafienia_histogram.iteritems():
        plik.write(";".join(map(str, val)) + "\n")

with open("rozkladpromieniowaniaosx.csv", "w") as plik:    
    plik.write("\n".join(map(str, x_promienie_na_scyntylator)) + "\n")     
with open("rozkladpromieniowaniaosy.csv", "w") as plik:    
    plik.write("\n".join(map(str, y_promienie_na_scyntylator)) + "\n") 



#end = time.time()
#print(end-start)

