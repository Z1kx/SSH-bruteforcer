import itertools as it

def generatorWordlist(chaine, longueur):
    for i in it.product(chaine, repeat=longueur):
        yield "".join(i)
    
mesLettres = "abcdefghijklmnopqrstuvwxyz"
compteur = 0

maWordlist = generatorWordlist(mesLettres, 4)
print(maWordlist)

for i in maWordlist:
    print(i)
    compteur +=1
print(compteur)

