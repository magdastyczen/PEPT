# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:18:24 2017

@author: magda styczeń
"""

from detektor import Detektor
from promieniowanie import Promieniowanie
from ekran import Ekran

import math
import time
import collections

#start = time.time()

det = Detektor()

det.dodajSegment(48, 42.50, 0, math.radians(7.5))
det.dodajSegment(48, 46.75, math.radians(3.75), math.radians(7.5))
det.dodajSegment(96, 57.50, math.radians(1.875), math.radians(3.75))

SCYNTYLATORY = det.dajScyntylatory()
scyntylatory_id = [s._id for s in SCYNTYLATORY]
print("Scyntylatory: {}".format(scyntylatory_id))

n_promieni = 20

pr = Promieniowanie(n_promieni)
print(pr)
ekran = Ekran()
#ekran.rysujPunkty(pr)

ekran.rysujDetektor(det)
ekran.rysujPromienie(pr)

s_Icwiartka = []
s = []
promienie_histogram = [0]*n_promieni*4
kat_histogram = []
trafienia_histogram = {}

for i, prn in enumerate(pr._promienie):
    proste = prn.dajProste()
    trafione = det.dajScyntylatoryTrafione(proste)

    odbiteII = []
    odbiteIII = []
    odbiteIV = []
    for t in trafione:
        odbiteII += [SCYNTYLATORY[det.odbijScyntylatorII(t._id)]]
        odbiteIII += [SCYNTYLATORY[det.odbijScyntylatorIII(t._id)]]
        odbiteIV += [SCYNTYLATORY[det.odbijScyntylatorIV(t._id)]]

    promienie_histogram[i] = len(trafione)
    promienie_histogram[i*2] = len(odbiteII)
    promienie_histogram[i*3] = len(odbiteIII)
    promienie_histogram[i*4] = len(odbiteIV)

    kat_histogram += [int(math.degrees(prn._theta))]*len(trafione)

    if len(trafione) > 0:
        if len(trafione) not in trafienia_histogram:
            trafienia_histogram[len(trafione)] = []
        trafienia_histogram[len(trafione)] += [i._id for i in trafione]

    if len(odbiteII) > 0:
        if len(odbiteII) not in trafienia_histogram:
            trafienia_histogram[len(odbiteII)] = []
        trafienia_histogram[len(odbiteII)] += [i._id for i in odbiteII]

    s_Icwiartka += trafione
    #trafione += odbiteII + odbiteIII + odbiteIV
    s += trafione


print(trafienia_histogram)
s_id = [i._id for i in s]

ekran.rysujScyntylatory(s_Icwiartka)
ekran.rysujHistogramy(promienie_histogram, s_id, kat_histogram, trafienia_histogram)
ekran.pokaz()

with open("histogramy.csv", "w") as plik:
    plik.write(";".join(map(str, promienie_histogram)) + "\n")
    plik.write(";".join(map(str, s_id)) + "\n")
    plik.write(";".join(map(str, kat_histogram)) + "\n")
    for key, val in trafienia_histogram.iteritems():
        plik.write(";".join(map(str, val)) + "\n")

#end = time.time()
#print(end-start)
#/5)*5
