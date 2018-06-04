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

with open("detektor.txt", "w") as logfile:
    logfile.write(str(det))
#print(det)

# SCYNTYLATORY[id] = lista scyntylatorow [s1 ... s 192]
SCYNTYLATORY = det.dajScyntylatory()



scyntylatory_id = [s._id for s in SCYNTYLATORY]
print("Scyntylatory: {}".format(scyntylatory_id))

n_promieni = 500

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
s119_krotnosc_trafien = []

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
    #if prn._idScyntylatora != 24:
    if 24 in id_trafionych:
            s24_trafienia += [np.rad2deg(prn._theta)]

    # Krotnosc trafien
    if 12 in id_trafionych:
        s12_krotnosc_trafien += [len(trafione)]
    if 119 in id_trafionych or 120 in id_trafionych:
        s119_krotnosc_trafien += [len(trafione)]

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
                      s24_trafienia, s12_krotnosc_trafien, s119_krotnosc_trafien)
ekran.pokaz()

with open("histogramy.csv", "w") as plik:
    plik.write(";".join(map(str, promienie_histogram)) + "\n")
    plik.write(";".join(map(str, s_id)) + "\n")
    plik.write(";".join(map(str, kat_histogram)) + "\n")
    plik.write(";".join(map(str, trafienia_histogram)) + "\n")
    plik.write(";".join(map(str, s24_trafienia)) + "\n")
    plik.write(";".join(map(str, s12_krotnosc_trafien)) + "\n")
    plik.write(";".join(map(str, s119_krotnosc_trafien)) + "\n")
    for key, val in trafienia_histogram.iteritems():
        plik.write(";".join(map(str, val)) + "\n")

with open("promienie.csv", "w") as plik:
    wsp = [";".join(map(str, p.dajPunktKart().tolist())) for p in pr._promienie]
    plik.write("\n".join(wsp))

#end = time.time()
#print(end-start)

