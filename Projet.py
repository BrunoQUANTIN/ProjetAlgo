"Projet de programmation, sujet 2, Bruno Quantin et Zacharie Seignibrard"



"Import des bibliothèques nécessaires"

import pandas as pd
import sys
import math
from math import*
from pylab import *
import matplotlib.pyplot as plt 
import numpy as np
sys.setrecursionlimit(15000)  #changement limite récursivité
from collections import Counter #pour trouver dans une liste l'élément le plus récurrent



"Chargement des données CSV"


#Bruno
projet=pd.read_csv("C:/Users/QUANTIN/ProjetAlgo1/EIVP_KM.csv", sep=";",index_col='sent_at',parse_dates=True)
"""
#Zacharie
projet=pd.read_csv("EIVP_KM.csv", sep=";",index_col='sent_at',parse_dates=True)
"""


"Fonctions outils de récupération de données"

def ss_projet(num):
    if num>6 or num<=0:
        print("les capteurs sont numérotés de 1 à 6")
    else:
        return projet[projet['id']==num]


def ss_colonne(colonne,num):
    if num>6 or num<=0:
        print("les capteurs sont numérotés de 1 à 6")
    else:
        return ss_projet(num)[colonne]
 
    
def ss_colonnedate(colonne,num,date):
    if num>6 or num<=0:
        print("les capteurs sont numérotés de 1 à 6")
    else:
        return ss_projet(num)[colonne][date]
        
        
def is_in(liste,a):
    r=0
    for i in range(len(liste)):
        if liste[i]==a:
            r+=1
            break
        else:
            continue
    return r==1
   
     
    
"Sous-projets de tests"

projet1=(projet[projet['id']==1])
projet2=(projet[projet['id']==2])
projet3=(projet[projet['id']==3])
projet4=(projet[projet['id']==4])
projet5=(projet[projet['id']==5])
projet6=(projet[projet['id']==6])
temp1=(projet1['temp'])
temp2=(projet2['temp'])
temp3=(projet3['temp'])
temp4=(projet4['temp'])
temp5=(projet5['temp'])
temp6=(projet6['temp'])
humidity1=(projet1['humidity'])
humidity2=(projet2['humidity'])
humidity3=(projet3['humidity'])
humidity4=(projet4['humidity'])
humidity5=(projet5['humidity'])
humidity6=(projet6['humidity'])
noise1=(projet1['noise'])
noise2=(projet2['noise'])
noise3=(projet3['noise'])
noise4=(projet4['noise'])
noise5=(projet5['noise'])
noise6=(projet6['noise'])






"Dans la suite figurent les codes d'analyses de données"



"Redimensionnement"

def shape_check(colonne):
    L=[]
    for i in range (1,7): #intervalle permettant de récupérer le 6 capteurs
        L.append((ss_colonne(colonne,i).shape)[0]) #liste du nombre de lignes de données enregistrées par chaque capteur 
    rang_min=0
    for j in range(len(L)):
        if L[j]<L[rang_min]:
            rang_min=j
        else:
            continue
    serie_a_etudier= ss_projet(rang_min+1)
    liste_nombre_mesures_jour=[]
    for k in range(11,26):  #les jours de mesures sont entre le 11 et le 25 aout 2019
        liste_nombre_mesures_jour.append(ss_colonnedate(colonne,rang_min+1,'2019-08-'+str(k)).shape[0])
    liste_jour_a_suppr=[]
    def nb_le_plus_rep(liste):
        l=Counter(liste).most_common(1)
        return l[0][0]
    for m in range (len(liste_nombre_mesures_jour)):
        if liste_nombre_mesures_jour[m]<(nb_le_plus_rep(liste_nombre_mesures_jour)):  #comparaison au nombre de mesure par jour le plus courant
            liste_jour_a_suppr.append(m+11) #+11 pour faire correspondre la position dans la série à la date correspondante
        else:
            continue
    new_projet=projet.loc['2019-08-'+str(liste_jour_a_suppr[0]+1):'2019-08-'+str(liste_jour_a_suppr[1]-1)] #récupère les jours compris entre deux jours à supprimer exclus
    n=len(liste_jour_a_suppr)
    for p in range(2,n):
        if liste_jour_a_suppr[p-1]+1==liste_jour_a_suppr[p]:
            continue
        else:
            new_projet.merge(projet.loc['2019-08-'+str(liste_jour_a_suppr[p-1]+1):'2019-08-'+str(liste_jour_a_suppr[p]-1)],how='right')   #on concatène tous les jours valables
    if liste_jour_a_suppr[n-1]==25:
        return(new_projet)
    else:
        return(new_projet.merge(projet.loc['2019-08-'+str(liste_jour_a_suppr[len(liste_jour_a_suppr)]+1):'2019-08-25'], how='right'))   #on ajoute les jours aprés le dernier erroné jusqu'au 25 aout dernier de notre liste
        
new_projet=shape_check('temp') 


def ajustement(serie1,serie2) :
    l1=list(serie1)
    l2=list(serie2)
    n1=len(l1)
    n2=len(l2)
    rang_min=min(n1,n2)
    liste_nombre_mesures_jour=[]
    if n1==n2:
        return [l1,l2]
    elif rang_min==n1:
        for k in range(11,26):  #les jours de mesures sont entre le 11 et le 25 aout 2019
            liste_nombre_mesures_jour.append(serie1['2019-08-'+str(k)].shape[0])
        liste_jour_a_suppr=[]
        def nb_le_plus_rep(liste):
            l=Counter(liste).most_common(1)
            return l[0][0]
        for m in range (len(liste_nombre_mesures_jour)):
            if liste_nombre_mesures_jour[m]<(nb_le_plus_rep(liste_nombre_mesures_jour)):
                liste_jour_a_suppr.append(m+11) 
            else:
                continue
        new_liste=serie2['2019-08-'+str(liste_jour_a_suppr[0]+1):'2019-08-'+str(liste_jour_a_suppr[1]-1)]
        n=len(liste_jour_a_suppr)
        for p in range(2,n):
            if liste_jour_a_suppr[p-1]+1==liste_jour_a_suppr[p]:
                continue
            else:
                new_liste.append(serie2['2019-08-'+str(liste_jour_a_suppr[p-1]+1):'2019-08-'+str(liste_jour_a_suppr[p]-1)])   #on concatène tous les jours valables
        if liste_jour_a_suppr[n-1]==25:
            return [ajustementlisteunique(serie1,liste_jour_a_suppr),list(new_liste)]
        else:
            return [ajustementlisteunique(serie1,liste_jour_a_suppr),list(new_liste.append(serie2['2019-08-'+str(liste_jour_a_suppr[len(liste_jour_a_suppr)]+1):'2019-08-25']))]
    else:
        for k in range(11,26):  #les jours de mesures sont entre le 11 et le 25 aout 2019
            liste_nombre_mesures_jour.append(serie2['2019-08-'+str(k)].shape[0])
        liste_jour_a_suppr=[]
        def nb_le_plus_rep(liste):
            l=Counter(liste).most_common(1)
            return l[0][0]
        for m in range (len(liste_nombre_mesures_jour)):
            if liste_nombre_mesures_jour[m]<(nb_le_plus_rep(liste_nombre_mesures_jour)):
                liste_jour_a_suppr.append(m+11) 
            else:
                continue
        new_liste=serie1['2019-08-'+str(liste_jour_a_suppr[0]+1):'2019-08-'+str(liste_jour_a_suppr[1]-1)]
        n=len(liste_jour_a_suppr)
        for p in range(2,n):
            if liste_jour_a_suppr[p-1]+1==liste_jour_a_suppr[p]:
                continue
            else:
                new_liste.append(serie1['2019-08-'+str(liste_jour_a_suppr[p-1]+1):'2019-08-'+str(liste_jour_a_suppr[p]-1)])   #on concatène tous les jours valables
        if liste_jour_a_suppr[n-1]==25:
            return [list(new_liste),ajustementlisteunique(serie2,liste_jour_a_suppr)]
        else:
            return [list(new_liste.append(serie1['2019-08-'+str(liste_jour_a_suppr[len(liste_jour_a_suppr)]+1):'2019-08-25'],ajustementlisteunique(serie2,liste_jour_a_suppr)))]  


def ajustementlisteunique(serie1,liste_jour_a_suppr) :
    l1=list(serie1)
    new_liste1=serie1['2019-08-'+str(liste_jour_a_suppr[0]+1):'2019-08-'+str(liste_jour_a_suppr[1]-1)]
    n=len(liste_jour_a_suppr)
    for p in range(2,n):
        if liste_jour_a_suppr[p-1]+1==liste_jour_a_suppr[p]:
            continue
        else:
            new_liste1.append(serie1['2019-08-'+str(liste_jour_a_suppr[p-1]+1):'2019-08-'+str(liste_jour_a_suppr[p]-1)])   #on concatène tous les jours valables
    if liste_jour_a_suppr[n-1]==25:
        return list(new_liste1)
    else:
        return list(new_liste1.append(serie1['2019-08-'+str(liste_jour_a_suppr[len(liste_jour_a_suppr)]+1):'2019-08-25']))
    
    
def ajustementgrossier(serie1,serie2) : #Risque de déformer les statistiques
    l1=list(serie1)
    l2=list(serie2)
    n1=len(l1)
    n2=len(l2)
    new_liste=[]
    if n2==n1:
        return liste1,liste2
    elif n2>n1:
        for i in range(n1):
            new_list[i]=l2[i]
        return l1,new_list
    else:
        for i in range(n2):
            new_list[i]=l1[i]
        return new_list,l2


    
"somme"

def somme(serie1,serie2):
    l1,l2=ajustement(serie1,serie2)[0],ajustement(serie1,serie2)[1]
    L=[] #SONT DE LA MM TAILLE
    for i in range(len(l1)):
        x=l1[i]+l2[i]
        L.append(x)
    return L



"min/max"

def calcul_min(serie_csv):
    serie=list(serie_csv)     
    mini=serie[0]
    n=len(serie) 
    for i in range(n-1) :
        if serie[i]<mini:
            mini=serie[i]
        else:
            continue
    return mini

    
def calcul_max(serie_csv):
    serie=list(serie_csv) 
    maxi=serie[0]
    n=len(serie)
    for i in range(n-1) :
        if serie[i+1]>maxi:
            maxi=serie[i+1]
        else:
            continue
    return maxi
 

   
"moyennes"

def moyenne_arithmetique(serie_csv):
    serie=list(serie_csv) 
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

 

"médiane"
"La fonction médiane ne peut s'appliquer qu'à une liste triée, on code alors une fonction de tri rapide"
       
def trirap(serie_csv):
    serie=list(serie_csv)        #pour temp, humi --> pour lumi changement limit récursivité --> pour noise diviser séparer la liste en fonction des id sinon crash 
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
    
        
def mediane(serie):   
    lon=len(serie)
    l2= trirap(serie)
    if lon%2!=0:
        return l2[(lon//2)]
    else:
        return (l2[lon//2]+l2[(lon//2)+1])/2
        


"Quartiles"

def PremierQuartile(serie):  
    listeordonnée=trirap(serie)
    q=int(len(serie)/4) 
    return listeordonnée[q-1]

def TroisièmeQuartile(serie): 
    listeordonnée=trirap(serie)
    q=int(len(serie)*3/4)
    return listeordonnée[q-1]

def InterQuartile(serie): 
    return TroisièmeQuartile(serie)-PremierQuartile(serie)



"variance et covariance"

def variance(serie):  #attention à la précision
    n=len(serie)
    somme=0
    m=moyenne_arithmetique(serie)
    for x in serie:
        somme+=(x-m)**2
    return somme/(n-1)


def covariance(serie1,serie2):
    SOM=somme(serie1,serie2)
    return variance(SOM)-variance(serie1)-variance(serie2)
 
    

"écart type"

def ecart_type(serie): #attention à la précision
    return sqrt(variance(serie))



"étendue"

def étendue(serie):
    return serie.max()-serie.min()


   
"humidex"

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
    listTair,listhumidite=list(listTair_csv),list(listhumidite_csv)    
    list_Humidex=[]
    for i in range(len(listTair)):
        list_Humidex.append(listTair[i] + 0.5555 * (6.11*exp(5417.7530*((1/273.16)-(1/(273.15 + Trosee(listTair,listhumidite)[i])))-10)))
    return list_Humidex


     
"courbes"

def courbe(serie1, serie2):
    serie1.plot()
    serie2.plot()
    plt.show()


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
        projet.loc[date1:date2,serie].plot()
        plt.show()
    
        
def courbe_intervalle_tps_division(serie,num,date1,date2,lettre_divisiontemporelle):
    ss_projet(num).loc[date1:date2, serie].resample(str(lettre_divisiontemporelle)).plot() 
    plt.show()   
     
    
def Diagrm_Comparaison(nom_serie,date):  
    listmoy=[]
    for i in range(1,7):
        listmoy.append(moyenne_arithmetique(ss_colonnedate(nom_serie,i,date)))
        ss_colonnedate(nom_serie,i,date).plot(label='capteur'+str(i))
    plt.legend()
    plt.show()
    Tableau=pd.DataFrame({"moyenne"+nom_serie:listmoy},index=['capteur1','capteur2','capteur3','capteur4','capteur5','capteur6'])
    Tableau.plot.bar()
    plt.show()
    
    
def Diagrm_boite(colonne): 
    L=[]
    for i in range (1,7):
        L.append(ss_colonne(colonne,i))
    plt.boxplot(L)
    plt.show()
    
    
    
"Etude des courbes"
   
def coef_var(serie):           #étude variabilité
    return ecart_type(serie)/abs(moyenne_arithmetique(serie))


def correlation(serie1,serie2):
    return covariance(serie1,serie2)/(ecart_type(serie1)*ecart_type(serie2)*2) 
    
    
def liste_forte_correlation(num):                   #corrélation entre colonne d'un même capteur
    tableau_corr=array(ss_projet(num).corr())
    l=[]
    dico={}
    for i in range(tableau_corr.shape[0]):
        for j in range(tableau_corr.shape[1]):
            if tableau_corr[i][j]>=0.5 and tableau_corr[i][j]!=1:
                if is_in(l,tableau_corr[i][j])== False:
                    dico['Les variables '+str(ss_projet(num).columns[i])+' et '+ str(ss_projet(num).columns[j]) + ' ont pour coefficient de corrélation'] = tableau_corr[i][j]
                    l.append(tableau_corr[i][j])
                else:
                    continue
            else:
                continue
    return dico 

    
def forte_correlation():
    dico={}
    for i in range(1,6):
        dico['capteur '+str(i)]=liste_forte_correlation(i)
    return dico
                           
            
def forte_correlation_intercapteur(colonne):     #corrélation pour une même variable de chaque capteur 
    dico={}
    l=[]
    for i in range(1,7):
        for j in range(1,7):
            if correlation(ss_colonne(colonne,i),ss_colonne(colonne,j))>=0.5 and correlation(ss_colonne(colonne,i),ss_colonne(colonne,j))!=1:
                if is_in(l,correlation(ss_colonne(colonne,i),ss_colonne(colonne,j)))==False:
                    dico['Les variables '+str(projet.columns[i])+' et '+ str(projet.columns[j]) + ' ont pour coefficient de corrélation'] = correlation(ss_colonne(colonne,i),ss_colonne(colonne,j))
                    l.append(correlation(ss_colonne(colonne,i),ss_colonne(colonne,j)))
                else:
                    continue
            else:
                continue
    return dico
                
            
    
    
                
    
    

    