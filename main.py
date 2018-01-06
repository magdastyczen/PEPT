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

start = time.time()

det = Detektor()

det.dodajSegment(48, 42.50, 0, math.radians(7.5))
det.dodajSegment(48, 46.75, math.radians(3.75), math.radians(7.5))
det.dodajSegment(96, 57.50, math.radians(1.875), math.radians(3.75))

pr = Promieniowanie(10**3)

#ekran = Ekran()
#ekran.rysujDetektor(det)
#ekran.rysujPromienie(pr)
#ekran.pokaz()

s = []

for prn in pr._promienie:
    p = prn.dajProstaKart()
    s += det.dajScyntylatoryTrafioneXY(p)
    #s += det.dajScyntylatoryZZakresu(p)
 

#ekran.rysujScyntylatory(s)
end = time.time()
print(end-start)