def rechercheDichotomiqueRecursive( list, n, gauche = 0, droite = -1 ):
    if gauche == droite: 
        return False
    else:
        if droite == -1 : 
            droite = len(list)-1
        m = (gauche+droite)//2
        if list[m] == int(n) :
            return m
        elif list[m] > int(n) :
            return rechercheDichotomiqueRecursive(list, n, gauche, m-1)
        else :
            return rechercheDichotomiqueRecursive(list, n, m+1, droite)