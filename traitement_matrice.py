import numpy as np
import random as random

AUCUN = -1

def median(l):
    """
    une fonction qui calcule la mediane d'une liste
    """
    half = len(l) // 2
    l.sort()
    if not len(l) % 2:
        return (l[half - 1] + l[half]) / 2.0
    return l[half]

def bordure_matrice(matrice):
    """
    methode qui definit une valeur par defaut -1 pour la bordure
    """
    size = len(matrice)
    for i in range(size):
        matrice[0][i] = matrice[size - 1][i] = AUCUN
        matrice[i][0] = matrice[i][size - 1] = AUCUN
    return matrice

def arith_matrice(val_max, size):
    """ une methode qui calcule la moyenne arith entiere pour chaque
        valeur de la self.mat
    """
    i, n, moyenne = 1, 1, 0
    matrice = np.random.randint(val_max, size=(size, size))
    matrice = bordure_matrice(matrice)
    copie = np.zeros((size, size))
    copie = bordure_matrice(copie)
    l = []
    while i < (size - 1):
        j = 1
        while j < (size - 1):
            if matrice[i-1][j-1] != AUCUN :
                l.append(matrice[i-1][j-1])
            if matrice[i-1][j] != AUCUN :
                l.append(matrice[i-1][j])
            if matrice[i-1][j+1] != AUCUN :
                l.append(matrice[i-1][j+1])
            if matrice[i][j-1] != AUCUN :
                l.append(matrice[i][j-1])
            if matrice[i][j+1] != AUCUN :
                l.append(matrice[i][j+1])
            if matrice[i+1][j-1] != AUCUN :
                l.append(matrice[i+1][j-1])
            if matrice[i+1][j+1] != AUCUN :
                l.append(matrice[i+1][j+1])
            if matrice[i+1][j] != AUCUN :
                l.append(matrice[i+1][j])
            l.append(matrice[i][j])
            copie[i][j] = median(l)
            l = []
            moyenne = 0
            j = j +1
        i = i+ 1
    #print(copie, matrice)
    return copie

def ajout_infranchissable(matrice, size):
    """
    ajoute des obstacles a -1 dans la matrice aleatoirement
    """
    i = 1
    while i+3 < size :
        x = int(random.randint(1,size-2))
        matrice[i][x] = 1e6
        matrice[i-1][x] = 1e6
        matrice[i][x+1] = 1e6
        matrice[i][x-1] = 1e6
        x = int(random.randint(1,size-2))
        matrice[i][x] = 1e6
        matrice[i+1][x] = 1e6
        matrice[i][x+1] = 1e6
        matrice[i][x-1] = 1e6
        i += 2
    return matrice
