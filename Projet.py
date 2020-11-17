import pandas as pd
import sys
import math
from math import*
from pylab import *
import matplotlib.pyplot as plt 
import numpy
sys.setrecursionlimit(15000)  #changement limite récursivité


#Bruno
projet=pd.read_csv("C:/Users/QUANTIN/ProjetAlgo1/EIVP_KM.csv", sep=";",index_col='sent_at',parse_dates=True)
"""
#Zacharie
projet=pd.read_csv("EIVP_KM.csv", sep=";",index_col='sent_at',parse_dates=True)
"""

projet1=(projet[projet['id']==1])
projet2=(projet[projet['id']==2])
projet3=(projet[projet['id']==3])
projet4=(projet[projet['id']==4])
projet5=(projet[projet['id']==5])
projet6=(projet[projet['id']==6])
tempér1=(projet1['temp'])
tempér2=(projet2['temp'])
tempér3=(projet3['temp'])
tempér4=(projet4['temp'])
tempér5=(projet5['temp'])
tempér6=(projet6['temp'])
humidity1=(projet1['humidity'])
humidity2=(projet2['humidity'])
humidity3=(projet3['humidity'])
humidity4=(projet4['humidity'])
humidity5=(projet5['humidity'])
humidity6=(projet6['humidity'])

"""
projet.info()  
projet.head()  #5 premières lignes
projet.tail()  #dernières lignes
projet.shape   #attention sans parenthèse et renvoie le couple (nbr_ligne, nbr_colonne)
temp_projet=projet.append(projet)   #copie du double
temp_projet=temp_projet.drop_duplicates()   #copie en ayant retiré le double
temp_projet.drop_duplicates(inplace=True)   #modifie automatiquement
temp_projet.drop_duplicates( inplace = True , keep = False )    #False supprime les doublons, first idem sauf la 1ere occurence, last idem sauf la derniere
projet.columns   #donne index des colonnes
projet.rename(columns= {},inplace=True )  #pr renommer les colonnes
projet.columns = [col.lower() for col in projet]  #colonne en minuscule
projet. isnull (). sum()     #nombre de lignes nulles par colonne
projet. dropna ()  #supprime les lignes avec au moins une valeur nulle
projet. dropna ( axe = 1 )  #supprimes les colonnes avec des nulles
tempera = projet[ 'temp' ]    #assimile une colonne dans une variable --> c'est une série
tempera.head()
tempera_moy=tempera.mean()    #moyenne --> .mean(axis=1)
tempera. fillna ( tempera_moy , inplace = True )   #remplace les valeurs nulles par la moy
projet.describe()   #donne toutes les infos sur chaque colonnes, moy, std(écart-type), min, max, var, sum, prod et pour les lignes --> 
projet['temp'].describe()   #aussi pour les variables de catégories (type de films,...)
projet['temp'].value_counts().head(10)     #fréquence des 10 1éres catégories
projet.corr()          #corrélation des colonnes
type(tempera)        #type de données ici série
sous-ensemble=projet[['temp']]    #ici DataFrame car on a ajouté les crochets puis on peut faire une liste de colonnes
ligne1=projet.loc["2"]     #ensemble des lignes avec l'index= 2 donc ici l'id et on peut sliccer avec extrémité comprise
ligne2=projet.iloc[52]     #52ième ligne et on peut fair du sliccing avec extrémité exclue
condition=(projet['temp']==22.4)    #condition sur une colonne et renvoie true ou false pour chaque ligne
projet[projet['temp']==22.4]        #filtre les valeurs pour lesquelles c'est true
#on peut faire des condition avec des str aussi et mettre plusieurs condition avec | et & 
projet[ projet[ 'temp' ]. isin ([ 22.8, 25.3 ])] #ou utiliser .isin avec une liste des valeurs qui marchent
projet[ ((projet[ 'temp' ] > = 23 ) & (projet[ 'temp' ] <= 25 )) & ( projet[ 'lum' ] > 20.0 ) & ( projet[ 'co2' ] <projet[ 'co2' ].quantile ( 0.25 )) ]    #erreur mais où ?!
projet.apply(fonction)   # applique une fction à l'ensemble des données
projet.plot(kind='scatter', x='temp', y='lum', title='Température vs Lum');  # tracé mais marche pas...
projet[ 'temp' ]. plot ( kind = 'hist' , title = 'Température' );  #idem
projet['temp'].plot (kind='box');      #box
projet['colonne'].apply(lambda x: x+1)    #appliquer une fonction à une SERIE

"""




##Programmes

"min/max"

def calcul_min(serie_csv):
    serie=list(serie_csv)    #WORKS 
    mini=serie[0]
    n=len(serie) #pas nécessaire len(serie) devrait marcher
    for i in range(n-1) :
        if serie[i]<mini:
            mini=serie[i]
        else:
            continue
    return mini
    
def calcul_max(serie_csv):
    serie=list(serie_csv) #WORKS
    maxi=serie[0]
    n=len(serie)
    for i in range(n-1) :
        if serie[i+1]>maxi:
            maxi=serie[i+1]
        else:
            continue
    return maxi
    
"médianne/moyennes"

def moyenne_arithmetique(serie_csv):
    serie=list(serie_csv) #WORKS
    n=len(serie)
    somme=0
    for i in range(n):
        somme+=serie[i]
    return somme/n
    
def moyenne_geom(serie_csv):
    serie=list(serie_csv)
    n=len(serie)
    b=serie[0]
    for i in range (1,n):
        b=b*serie[i]
    moygéo=b**(1/n)
    return moygéo
            
    
def moyenne_harmo(serie_csv):
    serie=list(serie_csv)
    n=len(serie)
    somme=0
    for i in range(n):
        somme+=1/serie[i]
    return n/somme
    
def moy_nrgtique(serie_csv):
    serie=list(serie_csv)
    n=len(serie)
    s=abs(serie[0]-serie[1]/(log(serie[0])-log(serie[1])))
    for i in range(2,n):
        s=abs(s-serie[i]/(log(s)-log(serie[i])))
    return s
    
     
def trirap(serie_csv):
    serie=list(serie_csv)        #WORK pour temp, humi --> pour lumi changement limit récursivité --> pour noise diviser séparer la liste en fonction des id sinon crash 
    if len(serie)<=1:
        return serie
    else:
        n=len(serie)
        pivot=serie[0]
        Lg=[]
        Ld=[]
        for i in range (1,n):
            if serie[i] <= pivot:
                Lg.append(serie[i])
            else:
                Ld.append(serie[i])
        return trirap(Lg) + [pivot] + trirap(Ld)
   
      
def mediane(serie):  #WORK 
    lon=len(serie)
    l2= trirap(serie)
    if lon%2!=0:
        return l2[(lon//2)]
    else:
        return (l2[lon//2]+l2[(lon//2)+1])/2
        

"variance/écart-type"

def variance(serie):  #WORKS attention à la précision
    n=len(serie)
    somme=0
    m=moyenne_arithmetique(serie)
    for x in serie:
        somme+=(x-m)**2
    return somme/n
    
def ecart_type(serie): #WORKS attention à la précision
    return sqrt(variance(serie))


"étendue"

def étendue(serie):
    return serie.max()-serie.min()

"Quartiles"

def PremierQuartile(serie):  #WORKS
    listeordonnée=trirap(serie)
    q=int(len(serie)/4)
    #qsup=q+1 d'un point de vue du code, pas utile d'arrondir à l'entier supèrieur 
    return listeordonnée[q-1]

def TroisièmeQuartile(serie): #WORKS
    listeordonnée=trirap(serie)
    q=int(len(serie)*3/4)
    return listeordonnée[q-1]

def InterQuartile(serie): #WORKS
    return TroisièmeQuartile(serie)-PremierQuartile(serie)

   
"humidex"

#Domaine de validité: Formule de Heinrich Gustav Magnus-Tetens
# 
# 0<T<60 °C
# 0,01 (1 %)< phi < 1 (100 %)
# 0< T_{r} < 50 °C

"Varibles globales en celsisus"
a=17.27
b=237.7 

def alpha(Tair,humidite):
    return (a*Tair)/(b+Tair) + log(humidite)
     
def Trosee(listTair_csv,listhumidite_csv):
    listTair,listhumidite=list(listTair_csv),list(listhumidite_csv)
    list_Trosee=[]
    for i in range(len(listTair)):
        list_Trosee.append((b*alpha(listTair[i],listhumidite[i]))/(a-alpha(listTair[i],listhumidite[i])))
    return list_Trosee

def humidex(listTair_csv,listhumidite_csv):
    listTair,listhumidite=list(listTair_csv),list(listhumidite_csv)    #WORKS
    list_Humidex=[]
    for i in range(len(listTair)):
        list_Humidex.append(listTair[i] + 0.5555 * (6.11*exp(5417.7530*((1/273.16)-(1/(273.15 + Trosee(listTair,listhumidite)[i])))-10)))
    return list_Humidex
     
    

##courbe

def courbe(serie):
    serie.plot()
    plt.show()

##courbe en fonction jour

def courbe_jour(serie,date):
    if type(date)!=str:
        print ("La date est une chaîne de caractère!")
    else:
        serie[date].plot()
        plt.show()
  
def courbe_intervalle_tps(serie,date1,date2):
    if type(date1)!=str or type(date2)!=str:
        print ("La date est une chaîne de caractère!")
    else:
        serie[date1:date2].plot()
        plt.show()
  
    
    
    

    