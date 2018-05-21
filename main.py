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

# trafienia to lista 192 liczb
# indeks to id scyntylatora, a wartosc to liczba trafien
def normalizujTrafienia(trafienia, scyntylatory):
    trafienia_przeskalowane = []
    #iterujemy po wszystkich scyntylatorach i wymnazamy liczbe trafien przez odpowiedni wspolczynnik
    for trafienie, scyntylator in zip(trafienia, scyntylatory):
        trafienie_przeskalowane = skalujTrafienia(trafienie, scyntylator._kat)
    return trafienia_przeskalowane

def skalujTrafienia(liczbaTrafien, kat, A=0.7, B=1.9):
    # tutaj leci Twoja funkcja
    wsp = kat * A * B #czy cokolwiek tam ma byc
    return liczbaTrafien * wsp #Tu zwracamy juz przeskalowana liczbe trafien w zaleznosci od kata

det = Detektor()

det.dodajSegment(48, 42.50, 0, math.radians(7.5))
det.dodajSegment(48, 46.75, math.radians(3.75), math.radians(7.5))
det.dodajSegment(96, 57.50, math.radians(1.875), math.radians(3.75))

SCYNTYLATORY = det.dajScyntylatory()
scyntylatory_id = [s._id for s in SCYNTYLATORY]
print("Scyntylatory: {}".format(scyntylatory_id))

n_promieni = 100

pr = Promieniowanie(n_promieni)
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

s_id = [i._id for i in s]

#Obliczamy histogram liczby trafien - inicializujemy liste zerami
trafienia_na_scyntylator = [0]*len(SCYNTYLATORY)
#I uzupelniamy zgodnie z trafieniami
for id in s_id:
    trafienia_na_scyntylator[id] += 1

# Majac histogram, mozemy przekazac go dalej do funkcji skalujacej trafienia,
# ktora zwroci nam liste trafien znormalizowanych (index - id scyntylatora)
trafienia_znormalizowane = normalizujTrafienia(trafienia_na_scyntylator, SCYNTYLATORY)


ekran.rysujScyntylatory(s)
ekran.rysujHistogramy(promienie_histogram, s_id, kat_histogram, trafienia_histogram)
ekran.pokaz()

with open("histogramy.csv", "w") as plik:
    plik.write(";".join(map(str, promienie_histogram)) + "\n")
    plik.write(";".join(map(str, s_id)) + "\n")
    plik.write(";".join(map(str, kat_histogram)) + "\n")
    for key, val in trafienia_histogram.iteritems():
        plik.write(";".join(map(str, val)) + "\n")

with open("promienie.csv", "w") as plik:
    wsp = [";".join(map(str, p.dajPunktKart().tolist())) for p in pr._promienie]
    plik.write("\n".join(wsp))

#end = time.time()
#print(end-start)
#/5)*5
