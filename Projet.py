import pandas as pd
"""
projet=pd.read_excel("Documents/EIVP/IVP1/Algorihme et programmation/EIVP_KM.xlsx",index_col='id')
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

projet=pd.read_csv("EIVP_KM.csv", sep=";") #sep permet permet de délimiter chaque colonne en décrivant le sérateur qui les constitue

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
    b=liste[0]
    for i in range (1,n):
        b=b*liste[i]
    moygéo=b**(1/n)
    return moygéo
            
    
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
        


## variance/écart-type

def variance(liste):
    n=len(liste)
    somme=0
    m=moyenne_arithmetique(liste)
    for i in range(n):
        somme+=(i-m)**2
    return somme/n
    
def ecart_type(liste):
    return sqrt(variance(liste))
    
    
## humidex

#Domaine de validité: Formule de Heinrich Gustav Magnus-Tetens
# 
# 0<T<60 °C
# 0,01 (1 %)< phi < 1 (100 %)
# 0< T_{r} < 50 °C

def alpha(Tair,phi):
    a=17,27
    b=237,7                #constantes en celsius
    return (a*Tair)/(b+Tair) + ln(phi)

def Trosee(Tair,phi):       #phi donne l'humidité relative
    return (b*alpha(Tair,phi))/(a-alpha(Tair, phi))

      
def humidex(liste_Tair,liste_humidite):
    for i in range(len(liste_Tair)):
        return liste_Tair[i] + 0.5555 * (6.11*exp(5417,7530*((1/273.16)-(1/(273.15 + liste_Trosee[i])))-10))
    


## courbe
from pylab import *
import matplotlib.pyplot as plt
def courbe(colonne,t0,t1):
    n=colonne.shape[0]
    t= linspace(t0,t1,n)
    x=colonne
    plot(t,x)
    show()
    

    
    
    
    
    

    