## min/max

def calcul_min(liste):
    min=liste[0]
    n=len(liste)
    for i in range(n-1) :
        if liste[i+1]<liste[i]:
            min=liste[i+1]
        else:
            continue
    return min
    
def calcul_max(liste):
    max=liste[0]
    n=len(liste)
    for i in range(n-1) :
        if liste[i+1]>liste[i]:
            max=liste[i+1]
        else:
            continue
    return max
    
## médianne/moyennes

def moyenne_arithmetique(liste):
    n=len(liste)
    somme=0
    for i in range(n):
        somme+=liste[i]
    return somme/n
    
def moyenne_geom(liste):
    n=len(liste)
    
def moyenne_harmo(liste):
    n=len(liste)
    somme=0
    for i in range(n):
        somme+=1/liste[i]
    return n/somme
    
    
def bubbleSort(liste_a_trier):
    n=len(liste_a_trier)
    while n>0:
        for i in range(n-1):
            if liste_a_trier[i]>liste_a_trier[i+1]:
                liste_a_trier[i], liste_a_trier[i+1] = liste_a_trier[i+1], liste_a_trier[i]
            else:
                continue
        n-=1
    return liste_a_trier  
    
      
def mediane(liste):
    lon=len(liste)
    l2= bubbleSort(liste)
    if lon%2!=0:
        return liste[(lon//2)]
    else:
        return (liste[lon//2]+liste[(lon//2)+1])/2

    
## variance/ écart-type



## courbe
from pylab import *

def courbe(liste_variable,t0,t1):
    n=len(liste_variable)
    t= linspace(t0,t1,n)
    x=liste_variable
    plot(t,x)
    show()
    

    
    
    
    
    

    