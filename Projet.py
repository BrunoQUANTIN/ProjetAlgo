
import pandas as pd
import sys
import math
from math import*
from pylab import *
import matplotlib.pyplot as plt 
import numpy as np
sys.setrecursionlimit(15000)  #changement limite récursivité

"""
#Bruno
projet=pd.read_csv("C:/Users/QUANTIN/ProjetAlgo1/EIVP_KM.csv", sep=";",index_col='sent_at',parse_dates=True)
"""
#Zacharie
projet=pd.read_csv("EIVP_KM.csv", sep=";",index_col='sent_at',parse_dates=True)

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
        
    
     
"""
def dtFrame(colonne):
    Dicovid={}
    for i in range (1,7):
        Dicovid[colonne+str(i)]=list(ss_colonne(colonne,i))
    DtFrame=pd.DataFrame(Dicovid)
    return DtFrame 
"""
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

"Verification"
def shape_check(colonne):
    L=[]
    for i in range (1,7):
        L.append((ss_colonne(colonne,i).shape)[0]) #liste du nombre de lignes de données enregistrées par chaque capteur 
    print(L) #RETIRER
    rang_min=0
    for j in range(len(L)):
        if L[j]<L[rang_min]:
            rang_min=j
        else:
            continue
    print('le capteur '+str(rang_min+1)+' contient le moins de données.')      #compenser le fait que la liste commence à 0 et les capteurs à 1
    serie_a_etudier= ss_projet(rang_min+1)
    liste_nombre_mesures_jour=[]
    for k in range(11,26):  #les jours de mesures sont entre le 11 et le 25 aout 2019
        liste_nombre_mesures_jour.append(ss_colonnedate(colonne,rang_min+1,'2019-08-'+str(k)).shape[0])
    print(liste_nombre_mesures_jour)     #donne la liste du nombre de mesures par jour pour le capteur avec le min de données
    liste_jour_a_suppr=[]
    for m in range (len(liste_nombre_mesures_jour)):
        if liste_nombre_mesures_jour[m]<=95:
            liste_jour_a_suppr.append(m+11)
        else:
            continue
    print(liste_jour_a_suppr)     # donne liste jour avec erreurs sur ce capteur
    new_projet=projet.loc['2019-08-'+str(liste_jour_a_suppr[0]+1):'2019-08-'+str(liste_jour_a_suppr[1]-1)]
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
        
def mesures_par_jour(colonne):
    liste_nombre_mesures_jour=[]
    for i in range(1,7):
        for k in range(11,26):  #les jours de mesures sont entre le 11 et le 25 aout 2019
            liste_nombre_mesures_jour.append(ss_colonnedate(colonne,i,'2019-08-'+str(k)).shape[0])
    print(liste_nombre_mesures_jour)
    Dicomesure={'nombre_de_mesures':liste_nombre_mesures_jour}
    Datamesure=pd.DataFrame(Dicomesure)
    nombremesure=Datamesure['nombre_de_mesures'].value_counts()
    print(nombremesure)
    M=list(nombremesure)[0]
    s,i=0,0
    while s!=M:
        init=liste_nombre_mesures_jour[i]
        if x==init:
            s+=1
            i+=1
        else:
            i+=1
    print(x)
                    
            
   
    

"somme"

def somme(liste1,liste2):
    L=[] #SONT DE LA MM TAILLE
    for i in range(len(liste1)):
        x=liste1[i]+liste2[i]
        L.append(x)
    return L

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

def covariance(serie1,serie2):
    L1,L2=list(serie1),list(serie2)
    SOM=somme(L1,L2)
    return variance(SOM)-variance(serie1)-variance(serie2)
    
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

def courbe(serie1, serie2):
    serie1.plot()
    serie2.plot()
    plt.show()

##courbe

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
   
    
def Diagrm_boîte(colonne): 
    L=[]
    for i in range (1,7):
        L.append(ss_colonne(colonne,i))
    plt.boxplot(L)
    plt.show()
    
   
def coef_var(serie):           #étude variabilité
    return ecart_type(serie)/abs(moyenne_arithmetique(serie))

   
def correlation(serie1,serie2):
    return covariance(serie1,serie2)/(ecart_type(serie1)*ecart_type(serie2))  
    
    

    