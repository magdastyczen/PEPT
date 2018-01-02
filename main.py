# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:18:24 2017

@author: magda styczeń
"""

from detektor import Detektor
from promieniowanie import Promieniowanie
from ekran import Ekran

import math

det = Detektor()

det.generujScyntylatory(48, 42.50, 0, math.radians(7.5))
det.generujScyntylatory(48, 46.75, math.radians(3.75), math.radians(7.5))
det.generujScyntylatory(96, 57.50, math.radians(1.875), math.radians(3.75))

pr = Promieniowanie(100)

ekran = Ekran()
ekran.rysujDetektor(det)
ekran.rysujPromienie(pr)

ekran.pokaz()

