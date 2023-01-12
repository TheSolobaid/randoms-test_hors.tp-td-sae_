l=[1,5,6,7,9,10,15,14,17,19,20,25,27]

def recherche(list, n):
    début = 0
    fin = len(list)
    trouvé = False
    while début<=fin and not trouvé :
        milieu = (début+fin)//2
        if list[milieu] == n:
            trouvé=True
        elif list[milieu]<x:
            début = milieu+1
        else:
            fin = milieu-1
    if trouvé:
        return(milieu)
    else:
        return(f"{n} n'existe pas dans la list")


while True:
    x = int(input("valeur a chercher dans la liste: "))
    print(recherche(l, x))
    