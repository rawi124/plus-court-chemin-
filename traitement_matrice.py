import numpy as np

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
    """ methode qui definit une valeur par defaut -1 pour la bordure """
    size = len(matrice)
    for i in range(size):
        matrice[0][i] = matrice[size - 1][i] = AUCUN
        matrice[i][0] = matrice[i][size - 1] = AUCUN
    return matrice 

def arith_matrice(val_max, size):
    """ une methode qui calcule la moyenne arith entiere pour chaque
        valeur de la self.mat """
    i, n, moyenne = 1, 1, 0
    matrice = np.random.randint(val_max, size=(size, size))
    matrice = bordure_matrice(matrice)
    copie = np.zeros((size, size))
    copie = bordure_matrice(matrice)
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
    return copie




    
