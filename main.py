import math
import numpy
import numpy as np
import scipy
import scipy.stats as st
from scipy.stats import rv_continuous
import matplotlib.pyplot as plt

# Wielomian odpowiadajcy rozkladowi mionow
class my_pdf(st.rv_continuous):
    def _pdf(self,x):
        return ((7.89875 * 10**7) - (630481 * x) -(15940.4 * x**2) + (147.356 * x**3))/(3.09892*10**9) # Normalized over its range, in this case [0,90]


n = 100

#Zdefiniowanie gestosc prawdopodobienstwa katow   
rozkladkata = my_pdf(a=0, b=90, name='my_pdf')

#Generujemy n katow Theta (nachylenie wzgledem osi pionowej)
theta = rozkladkata.rvs(size=(n, 1))

#Generujemy n katow Theta (kat w plasczyznie XY)
#alpha = np.random.rand(n, 1)alpha = cunifavariate(math.pi/4, math.pi/4)
a = np.random.rand(n, 1)
alpha = (math.pi/4 + math.pi/4 * (a - 0.5)) % math.pi

#generujemy rozklad punktow zaczepienia w osi OX od 0 do R 
anchor_point_R = np.random.uniform(low=0, high=57.5, size=(n,1))

#Generujemy n punktow zaczepienia w osi OY od 0 do 90 stopni  0.785398163
anchor_point_FI = np.random.uniform(low=0, high=1.570796327, size=(n,1))
# np.random.rand(n,2)
z = np.random.rand(n, 1)
#Laczymy w macierz nx5   theta=alpha
rays = np.concatenate((anchor_point_FI, anchor_point_R, theta, alpha, z), axis=1)
np.savetxt('test.out', theta, delimiter=',')
#print rays[1:3, :]
#-----------------------------------------------------------------------------

#test czy rozklad jest wlasciwy
"""
def testrozkladu(r_list, fi_list, beta_list):
    punktprzeciecia = []
    for r, fi, beta in zip(r_list, fi_list, beta_list):
        x = r * math.cos(fi)
        y = r * math.sin(fi)
        A = math.atan(1.570796327 - beta)
        D = math.tan(0.7)
        C = -y + A*x
        z = -(C/A)
        if 0 <= z and z <= 57.5:
  
            punktprzeciecia.append([z, beta]) 
         
    return np.asarray(punktprzeciecia) #przed zwroceniem wartosci, konwertuje jeszcze liste do macierzy NumPy 

#Wywolujemy funkcje z odpowiednimi argumentami, a jej wynik od razu przypisujemy do macierzy punktprzeciecia:
punktprzeciecia = testrozkladu(r_list = rays[:,1], fi_list = rays[:,0], beta_list = rays[:,2]) 
"""
#print '\n'.join(map(str, beta))
#np.savetxt('test.out', beta, delimiter=',')
#Rysowanie wykresu
#plt.plot(punktprzeciecia[:, 0], punktprzeciecia[:, 1], 'ro');
#----------------------------------------------------------------
#zdefiniowanie polozenia detektorow
def polozeniedetektoraI(r, theta, z): #to jest deklaracja - nazwa_funkcji(argumenty). zaczyna sie od slowa kluczowego "def"
    #deklarujemy pusta liste wspolrzednych, gdyz bedziemy do niej dodawac nowe elementy w petli
    wspolrzedne = []
    i = 0
    while i < 46:
        wspolrzedne.append([r, theta*i, z]) #uzywamy funkcji append: powoduje ona dodanie nowego elementu do listy
        i = i+1
       
    return wspolrzedne

wspolrzedne_detektora1 = polozeniedetektoraI(r=42.5, theta=7.5, z=0)
wspolrzedne_detektora2 = polozeniedetektoraI(r=46.75, theta=7.5, z=0)
#print(wspolrzedne_detektora2)
#print(wspolrzedne_detektora1)


def polozeniedetektoraIII(r3, theta3, z3): #to jest deklaracja - nazwa_funkcji(argumenty). zaczyna sie od slowa kluczowego "def"
    #deklarujemy pusta liste wspolrzednych, gdyz bedziemy do niej dodawac nowe elementy w petli
    wspolrzedneIII = []
    j = 0
    while j < 92:
        wspolrzedneIII.append([r3, theta3*j, z3]) #uzywamy funkcji append: powoduje ona dodanie nowego elementu do listy
        j = j+1
       
    return wspolrzedneIII

wspolrzedne_detektora3 = polozeniedetektoraIII(r3=57.5, theta3=3.75, z3=0)
#print(wspolrzedne_detektora2)
#print(wspolrzedne_detektora3)

def obszarszukania(a, b, c1, c2):
    obszar = []
    while m < n:        
        m=0
        r = rays[m, 1]
        fi = rays[m, 0]
        theta = rays[m, 2]
        x = r * math.cos(fi)
        y = r * math.sin(fi)
       
 #Prosta AX+BY+C=0; B=-1, A=tg(beta)-> wyliczenie C     
        d = 1.0124
        b = -1
        a = math.tan(theta)
        c = y - a*x

#prosta y prechodzaca przez punkt x,y pod katem beta
        y = a*x + c
        #x1 = (2*c) / (2*a + 2)
        #x2 = (-2*c) / (2 - 2*a)

        #y1 = a * x1 + c 
        #y2 = a * x2 + c
#dwie proste ograniczajajace pole poszukiwania
 #wzor na odleglosc punktu od prostej => tutaj wzor na prosta w odleglosci pol przekontnej detektora od wylosowanego punktu, a jest stale zmienne C
    
        c1 = d * math.sqrt( a**2 + b**2 ) - a * x - b * y 
        c2 = d * math.sqrt( a**2 + b**2 ) + a * x + b * y 
        obszar.append([a, b, c1, c2])
        m = m + 1
    return obszar
#print(obszar)

       
def wierzcholekDI(rI, thetaI, zI): #to jest deklaracja - nazwa_funkcji(argumenty). zaczyna sie od slowa kluczowego "def"
    #deklarujemy pusta liste wspolrzednych, gdyz bedziemy do niej dodawac nowe elementy w petli
    wierzcholek1D = []
    j=0
    while j < 48:
        wierzcholek1D.append([rI, 0.45 + thetaI*j, zI]) #uzywamy funkcji append: powoduje ona dodanie nowego elementu do listy
        j = j+1
       
    return wierzcholek1D

wsp_wierzcholkaD1plus = wierzcholekDI(rI=41.55, thetaI=7.5, zI=25)
wsp_wierzcholkaD1minus = wierzcholekDI(rI=41.55, thetaI=7.5, zI=-25)
#print(wspolrzedne_wierzcholkaD1plus)

def wierzcholekDII(rI, thetaI, zI): 
    wierzcholek2D = []
    j=0
    while j < 48:
        wierzcholek2D.append([rI, 4.20 + thetaI*j, zI]) 
        j = j+1
       
    return wierzcholek2D

wsp_wierzcholkaD2plus = wierzcholekDII(rI=45.8, thetaI=7.5, zI=25)
wsp_wierzcholkaD2minus = wierzcholekDII(rI=45.8, thetaI=7.5, zI=-25)
#print(wsp_wierzcholkaD2puls)
#
def wierzcholekDIII(rI, thetaI, zI): 
    wierzcholekD3 = []
    j=0
    while j < 96:
       wierzcholekD3.append([rI,2.325 + thetaI*j, zI])
       j = j+1
       
    return wierzcholekD3

wsp_wierzcholkaD3plus = wierzcholekDIII(rI=56.65, thetaI=3.75, zI=25)
wsp_wierzcholkaD3minus = wierzcholekDIII(rI=56.65, thetaI=3.75, zI=-25)
#print(wsp_wierzcholkaD3minus)

def wierzcholekAI(rI, thetaI, zI): 
    wierzcholekA1 = []
    j=0
    while j < 48:
        wierzcholekA1.append([rI, -0.45 + thetaI*j, zI]) 
        j = j+1
       
    return wierzcholekA1

wsp_wierzcholkaA1plus = wierzcholekAI(rI=41.55, thetaI=7.5, zI=25)
wsp_wierzcholkaA1minus = wierzcholekAI(rI=41.55, thetaI=7.5, zI=-25)

def wierzcholekAII(rI, thetaI, zI):
    wierzcholekA2 = []
    j=0
    while j < 48:
        wierzcholekA2.append([rI, 3.3 + thetaI*j, zI]) 
        j = j+1
       
    return wierzcholekA2

wsp_wierzcholkaA2plus = wierzcholekAII(rI=45.8, thetaI=7.5, zI=25)
wsp_wierzcholkaA2minus = wierzcholekAII(rI=45.8, thetaI=7.5, zI=-25)

def wierzcholekAIII(rI, thetaI, zI):
    wierzcholekA3 = []
    j=0
    while j < 96:
       wierzcholekA3.append([rI,1.425 + thetaI*j, zI])
       j = j+1
       
    return wierzcholekA3

wsp_wierzcholkaA3plus = wierzcholekAIII(rI=56.65, thetaI=3.75, zI=25)
wsp_wierzcholkaA3minus = wierzcholekAIII(rI=56.65, thetaI=3.75, zI=-25)
#print(wsp_wierzcholkaA3minus)


def wierzcholekCI(rI, thetaI, zI):
    wierzcholekC1 = []
    j=0
    while j < 48:
        wierzcholekC1.append([rI, 0.45 + thetaI*j, zI]) #uzywamy funkcji append: powoduje ona dodanie nowego elementu do listy
        j = j+1
       
    return wierzcholekC1

wsp_wierzcholkaC1plus = wierzcholekCI(rI=43.45, thetaI=7.5, zI=25)
wsp_wierzcholkaC1minus = wierzcholekCI(rI=43.45, thetaI=7.5, zI=-25)

def wierzcholekCII(rI, thetaI, zI): 
    wierzcholekC2 = []
    j=0
    while j < 48:
        wierzcholekC2.append([rI,4.20 + thetaI*j, zI]) 
        j = j+1
       
    return wierzcholekC2

wsp_wierzcholkaC2plus = wierzcholekCII(rI=47.7, thetaI=7.5, zI=25)
wsp_wierzcholkaC2minus = wierzcholekCII(rI=47.7, thetaI=7.5, zI=-25)

def wierzcholekCIII(rI, thetaI, zI): 
    wierzcholekC3 = []
    j=0
    while j < 96:
       wierzcholekC3.append([rI,2.325 + thetaI*j, zI])
       j = j+1
       
    return wierzcholekC3

wsp_wierzcholkaC3plus = wierzcholekCIII(rI=58.4, thetaI=3.75, zI=25)
wsp_wierzcholkaC3minus = wierzcholekCIII(rI=58.4, thetaI=3.75, zI=-25)

def wierzcholekBI(rI, thetaI, zI): 
    wierzcholekB1 = []
    j=0
    while j < 48:
        wierzcholekB1.append([rI,-0.45 + thetaI*j, zI]) 
        j = j+1
       
    return wierzcholekB1

wsp_wierzcholkaB1plus = wierzcholekBI(rI=43.45, thetaI=7.5, zI=25)
wsp_wierzcholkaB1minus = wierzcholekBI(rI=43.45, thetaI=7.5, zI=-25)


def wierzcholekBII(rI, thetaI, zI):
    wierzcholekB2 = []
    j=0
    while j < 48:
        wierzcholekB2.append([rI,3.3 + thetaI*j, zI]) 
        j = j+1
       
    return wierzcholekB2

wsp_wierzcholkaB2plus = wierzcholekBII(rI=47.7, thetaI=7.5, zI=25)
wsp_wierzcholkaB2minus = wierzcholekBII(rI=47.7, thetaI=7.5, zI=-25)



def wierzcholekBIII(rI, thetaI, zI):
    wierzcholekB3 = []
    j= 0
    while j < 96:
       wierzcholekB3.append([rI,1.425 + thetaI*j, zI])
       j = j+1
       
    return wierzcholekB3

wsp_wierzcholkaB3plus= wierzcholekBIII(rI=58.4, thetaI=3.75, zI=25)
wsp_wierzcholkaB3minus = wierzcholekBIII(rI=58.4, thetaI=3.75, zI=-25)


#wierzcholki A,B,C,D ksolejno w  1,2,3 rzedzie i o wartosci z rownej  +/-   25
wierzcholek1plus = np.concatenate((wsp_wierzcholkaA1plus, wsp_wierzcholkaB1plus, wsp_wierzcholkaC1plus, wsp_wierzcholkaD1plus), axis=0)

wierzcholek1minus = np.concatenate((wsp_wierzcholkaA1minus, wsp_wierzcholkaB1minus, wsp_wierzcholkaC1minus, wsp_wierzcholkaD1minus), axis=0)

wierzcholek2plus = np.concatenate((wsp_wierzcholkaA2plus, wsp_wierzcholkaB2plus, wsp_wierzcholkaC2plus, wsp_wierzcholkaD2plus), axis=0)

wierzcholek2minus = np.concatenate((wsp_wierzcholkaA2minus, wsp_wierzcholkaB2minus, wsp_wierzcholkaC2minus, wsp_wierzcholkaD2minus), axis=0)

wierzcholek3plus = np.concatenate((wsp_wierzcholkaA3plus, wsp_wierzcholkaB3plus, wsp_wierzcholkaC3plus, wsp_wierzcholkaD3plus), axis=0)

wierzcholek3minus = np.concatenate((wsp_wierzcholkaA3minus, wsp_wierzcholkaB3minus, wsp_wierzcholkaC3minus, wsp_wierzcholkaD3minus), axis=0)

wszystko = np.concatenate((wierzcholek1plus, wierzcholek2plus, wierzcholek3plus), axis=0)

def walcowyDoKart(punkty):
    x = []
    y = []
    for p in punkty:
        x.append( p[0]*math.cos(math.radians(p[1])) )
        y.append( p[0]*math.sin(math.radians(p[1])) )
    return (x, y)

(test_x, test_y) = walcowyDoKart(wszystko)

plt.scatter(test_x, test_y)
plt.show()


#print(wierzcholek1plus)

"""
#wyznaczenie prostej w przestrzeni
def plaszczyznaXY():
    XY = []
    while m < n:        
        m=0
        r = rays[m, 1]
        fi = rays[m, 0]
        theta = rays[m, 2]
        alpha = 90 - theta
        x = r * math.cos(fi)
        y = r * math.sin(fi)
       
 #Prosta AX+BY+C=0; B=-1, A=tg(beta)-> wyliczenie C     
        B=-1
        A= math.tan(alpha)
         C= -A*x - y
#prosta y prechodzaca przez punkt x,y pod katem beta
        y = a*x + c
        #x1 = (2*C) / (2*A + 2)
        #x2 = (-2*C) / (2 - 2*A)

        #y1 = a * x1 + c 
        #y2 = a * x2 + c
#dwie proste ograniczajajace pole poszukiwania
 #wzor na odleglosc punktu od prostej => tutaj wzor na prosta w odleglosci pol przekontnej detektora od wylosowanego punktu, a jest stale zmienne C
    
        c1 = d * math.sqrt( a**2 + b**2 ) - a * x - b * y 
        c2 = d * math.sqrt( a**2 + b**2 ) + a * x + b * y 
        obszar.append([a, b, c1, c2])
        m = m + 1
    return obszar
    """