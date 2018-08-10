import numpy as np
import itertools as it

def appartient_liste_trie(nombre, liste):
    # marche si liste triée
    indice_min, indice_max = (0, len(liste) - 1)
    if nombre == liste[indice_min] or nombre == liste[indice_max]:
        return True
    if nombre < liste[indice_min] or nombre > liste[indice_max]:
            return False
    while indice_max - indice_min > 1  :
        indice_int = (indice_min + indice_max) // 2
        if nombre < liste[indice_int]:
            indice_max = indice_int
        elif nombre > liste[indice_int]:
            indice_min = indice_int
        else:
            return True
    return False

# nombre = somme de 2 nombres?
def somme_2_nombres(nombre, liste):
    longueur = len(liste)
    ppn = 0
    while nombre > liste[ppn] and ppn < longueur - 1:
        ppn += 1
    STOP = False
    resultat = False
    j = 0
    while not STOP:
        a = liste[j]
        b = liste[ppn]
        if nombre == a + b:
            STOP = True
            resultat = True
        elif nombre > a + b:
            j += 1
        else:
            ppn -= 1
        if ppn < j:
            STOP = True
    return resultat

#Détermination nombre premiers jusqu'à n
def nombres_premiers(n):
    j = 1
    if n < 2:
        return []
    L =[2]
    for i in range(3, n+1):
        a = 0
        longueur = 0
        while L[longueur] <= np.sqrt(i) and a == 0:
            if i % L[longueur] == 0:
                a = 1
            longueur += 1
        if a == 0:
            L.append(i)
    return np.array(L)

def diviseurs(n):
    #algo linéaire non optimisé
    if n % 2 == 1:
        L = [i for i in range(1, n // 2 + 1, 2) if n % i == 0]
    else:
        L = [i for i in range(1, n // 2 + 1) if n % i == 0]
    L.append(n)
    return L

# Détermination des diviseurs de n et de son nombre. Effet de bord attention
def diviseurs_bis_nombre_diviseur(n):
    if n <= 3:
        dico = {n: 1}
    else:
    # à finir, actuellement bien plus lent que le premier
        liste = nombres_premiers(int(np.sqrt(n)))
        dico = {}
        i = 0
        a = liste[i]
        while n >= a and i < len(liste):
            a = liste[i]
            while n % a == 0:
                if a in dico:
                    dico[a] += 1
                else:
                    dico[a] = 1
                n = n // a
            i += 1
        if n > 1:
            dico[n] = 1
    diviseurs = []
    for key, value in dico.items():
        diviseurs.append(tuple(key ** i for i in range(value + 1)))

    return [np.product(d) for d in it.product(*diviseurs)]


def factoriel(n):
    if n > 1:
        return n * factoriel(n - 1)
    else:
        return 1

