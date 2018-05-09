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

n_promieni = 200

pr = Promieniowanie(n_promieni)
print(pr)
ekran = Ekran()
#ekran.rysujPunkty(pr)

ekran.rysujDetektor(det)
ekran.rysujPromienie(pr)

s = []
promienie_histogram = [0]*n_promieni
kat_histogram = []
trafienia_histogram = {}

for i, prn in enumerate(pr._promienie):
    proste = prn.dajProste()
    trafione = det.dajScyntylatoryTrafione(proste)
    s += trafione
    promienie_histogram[i] = len(trafione)
    kat_histogram += [int(math.degrees(prn._theta))]*len(trafione)

    if len(trafione) > 0:
        if len(trafione) not in trafienia_histogram:
            trafienia_histogram[len(trafione)] = []
        trafienia_histogram[len(trafione)] += [i._id for i in trafione]


print(trafienia_histogram)
s_id = [i._id for i in s]

ekran.rysujScyntylatory(s)
ekran.rysujHistogramy(promienie_histogram, s_id, kat_histogram, trafienia_histogram)
ekran.pokaz()
#end = time.time()
#print(end-start)
#/5)*5