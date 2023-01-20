import numpy as np
import pandas   as pd
import  matplotlib.pyplot as plt
def rechercheDichotomiqueRecursive(liste, n, gauche = 0, droite = -2):
    if droite == -2:
            droite = len(liste) - 1
    if gauche > droite:
        return False
    else:
        milieu = (gauche + droite) // 2
        if liste[milieu] == int(n):
            return milieu
        elif liste[milieu] > int(n):
            return rechercheDichotomiqueRecursive(liste, n, gauche, milieu - 1)
        else:
            return rechercheDichotomiqueRecursive(liste, n, milieu + 1, droite)


def triFusion(list): 
    if len(list)>1:
        m = len(list) // 2     #trouve le milieu de la liste
        l = list[:m]           #créer une liste l (gauche) avec la partie gauche
        r = list[m:]           #créer une liste r (droite) avec la partie droite
        triFusion(l)        
        triFusion(r)
        i, j, k = 0, 0, 0
        while i < len(l) and j < len(r):    # [...] [...]
            if l[i] < r[j]:
                list[k] = l [i]
                i += 1
            else:
                list[k] = r[j]
                j += 1
            k += 1
        while i < len(l):                   # [...] []
            list[k] = l[i]
            i += 1
            k += 1
        while j < len(r):                   # [] [...]
            list[k] = r[j]
            j += 1
            k += 1  
    return list


def tirage(j):
    tirTotal = []
    for i in range(j):
        tir = np.random.choice(np.arange(1, 46), 5, replace=False)
        tirTotal.append(tir)
    return pd.DataFrame(tirTotal, columns=['1st nbr','2nd nbr','3rd nbr','4th nbr','5th nbr'])


def histogramme(df):
    totallist=[]
    for ligne in df.values:
        totallist += ligne.tolist()
    histo = [] # Create an empty list to store the histogram data
    for i in range(len(totallist)): # Iterate through each value in the flattened DataFrame
        index = rechercheDichotomiqueRecursive(histo, totallist[i]) # Search for the value in the histogram list
        if index is not False: # If the value is already in the list
            histo[index][1] += 1 # Increment the count
        else:
            histo.append([totallist[i], 1]) # If the value is not in the list, add it with a count of 1
            histo = triFusion(histo)
    plt.hist([x[0] for x in histo], bins=[x for x in range(1,46)], weights=[x[1] for x in histo], density=False, histtype='bar', align='mid', color='blue')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.title('Lottery Numbers Histogram')
    plt.show() # Show the chart


tir = tirage(14)
histogramme(tir)
