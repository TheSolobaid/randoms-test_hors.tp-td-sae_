from random import randint

def simu(n):
    multsept = 0
    for k in range(1, 1+n):
        valeur = randint(1 , 1000)
        if valeur%7 == 0:
            multsept += 1
    return multsept/n

print ('tamère')