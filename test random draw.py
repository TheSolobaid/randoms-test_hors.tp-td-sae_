l=[1,5,6,7,9,10,15,14,17,19,20,25,27]

def rechercheDichotomiqueRecursive(list, n, gauche, droite):
    if gauche > droite:
        return f"{n} n'existe pas dans la list"
    milieu = (gauche + droite) // 2
    if list[milieu] == n:
        return milieu
    elif list[milieu] > n:
        return rechercheDichotomiqueRecursive(list, n, gauche, milieu-1)
    else:
        return rechercheDichotomiqueRecursive(list, n, milieu+1, droite)

while True:
    x = int(input("valeur a chercher: "))
    print(rechercheDichotomiqueRecursive(l, x , 0 , len(l)))