import numpy as np
import pandas as pd

def triInsertion(list):
    swap=True
    while swap:
        swap = False
        for i in range(len(list)):
            for j in range(i , -1 , -1):                    #recule dans la liste à partire de i jusqu'au début en allant de -1 en -1
                if list[j]>list[i]:
                    list[j], list[i] = list[i], list[j]
                    swap = True
    return list

def rechercheDichotomiqueRecursive(liste, n, gauche = 0, droite = -2):
    if droite == -2:
            droite = len(liste) - 1
    if gauche > droite:
        return None
    else:
        milieu = (gauche + droite) // 2
        if liste[milieu] == int(n):
            return milieu
        elif liste[milieu] > int(n):
            return rechercheDichotomiqueRecursive(liste, n, gauche, milieu - 1)
        else:
            return rechercheDichotomiqueRecursive(liste, n, milieu + 1, droite)


def tirage(j):
    tirTotal = []
    for i in range(j):
        tir = np.random.choice(np.arange(1, 46), 5, replace=False)
        tirTotal.append(tir)
    return pd.DataFrame(tirTotal, columns=['1st nbr','2nd nbr','3rd nbr','4th nbr','5th nbr'])


import matplotlib.pyplot as plt

def histogram(df):
    # Create a dictionary to store the frequency of each number
    frequency = {i:0 for i in range(1,46)}
    # Iterate through each row of the dataframe
    for i in range(len(df)):
        # Iterate through each number in the row
        for j in df.iloc[i]:
            # Increment the frequency of the number
            frequency[j] += 1
    # Create a histogram of the frequency of each number
    plt.bar(frequency.keys(), frequency.values())
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.title('Frequency of Numbers in Dataframe')
    plt.show()

iteration = 0
np.random.seed(int(2))
# Number of draws
num_draws = 14
tir=tirage(num_draws)
tritotal = []
for i in range(len(tir)):
    templist=tir.iloc[i].values.tolist()
    templist = triInsertion(templist)
    tir.iloc[i]=templist
print(tir)


histogram(tir)
