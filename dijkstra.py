import numpy as np
import math

import traitement_matrice as ttt_mat

AUCUN = -1
infini = 10000

def voisin(matrice, point, size):
    """
    renvoie une liste qui contient les voisins de mon sommet courant
    sans prendre en compte les voisins sur la bordure
    """
    val = []
    i = point[0]
    j = point[1]

    if ( i-1 > 0 and j-1 > 0) and matrice[i-1][j-1] != AUCUN  :
        val.append((i-1,j-1))
    if ( i-1 > 0 and j > 0) and matrice[i-1][j] != AUCUN  :
        val.append((i-1,j))
    if ( i-1 > 0 and j+1 < size) and matrice[i-1][j+1] != AUCUN :
        val.append((i-1,j+1))
    if ( i > 0 and j-1 > 0) and  matrice[i][j-1] != AUCUN :
        val.append((i,j-1))
    if ( i > 0 and j+1 < size) and matrice[i][j+1] != AUCUN :
        val.append((i,j+1))
    if ( i+1 < size and j-1 > 0)  and matrice[i+1][j-1] != AUCUN  :
        val.append((i+1,j-1))
    if ( i+1 < size and j+1 < size) and matrice[i+1][j+1] != AUCUN :
        val.append((i+1,j+1))
    if ( i+1 < size and j < size  ) and matrice[i+1][j] != AUCUN :
        val.append((i+1, j))
    return val

def rechercher_min(F, dist):
    """
    rechercher dans F "si" tq dist[si] soir minimale
    """
    mini = 1e6 # zone infranchisable
    for el in F :
        if dist[el[0]][el[1]] < mini and dist[el[0]][el[1]] != AUCUN:
            mini = dist[el[0]][el[1]]
            si = el
    return si


def predecessuer(T, point):
    """
    recherche le predecesseur du point en parametre
    et ceci pour pouvoir remonter dans l arbre couvrant
    minimal et repartir du point d arrivée vers celui
    d'arrivé
    """
    z = 0
    while z < len(T):
        w = 0
        while w < len(T):
            if z == point[0] and w == point[1] :
                #print(T[z][w],' est le predecessur de ', z, w)
                x = T[z][w]
                return x[0], x[1]

            w += 1
        z += 1


def cout(sj, si, matrice):
    """
    pour un voisin sj de si, si sj se trouve sur la diagonale de si
    alors le cout de sj devient egale a sj*racine_carré de 2
    """
    x_j, y_j = sj[0], sj[1]
    x_i, y_i = si[0], si[1]

    if y_i == (y_j + 1) or y_i == (y_j - 1):
        return matrice[x_j][y_j]*math.sqrt(2)
    else :
        return matrice[x_j][y_j]


def relacher(sj, si, matrice, T, dist):
    """
    effectue le relachement des sommets
    """
    x_j, y_j = sj[0], sj[1]
    x_i, y_i = si[0], si[1]

    cout_sj = cout(sj, si, matrice)

    dist_sj, dist_si = dist[x_j][y_j], dist[x_i][y_i]
    if dist_sj > (dist_si + cout_sj):
        dist[x_j][y_j] = dist_si + cout_sj
        T[x_j][y_j] = si

        
def remonter(arrive, depart, T):
    """
    part du point d arrivee et remonte en suivant les predecesseur jusqu'au
    point d arrivee
    """
    chemin = []
    chemin.append(arrive[0])
    chemin.append(arrive[1])
    while arrive != depart :
        arrive = predecessuer(T, arrive)
        chemin.append(arrive[0])
        chemin.append(arrive[1])
    return chemin

def dijkstra(matrice, depart, arrive, size):

    """
    prend matrice en entree, un point de depart et un autre d arrivÃ©e
    et retourne une liste qui contient les corrdonnes du plus court chemin
    en suivant l'algorithme de dijkstra
    """
    
    #partie des initialisations
    d = [[infini]*size]*size
    dist = ttt_mat.bordure_matrice(np.array(d)) #liste des distances de chaque sommet init a +inf
    dist[depart[0]][depart[1]] = 0
    #print('au depart l ensemble dist est initilisé ainsi \n',dist,'\n')

    t = [[(0, 0) ]*size]*size
    T = ttt_mat.bordure_matrice(np.array(t))
    #print('au depart l ensemble T est initilisé ainsi \n',T,'\n')

    #initialise l ensemble F qui va contenir tous les coordonnes de la matrice
    #partant de (0,0) a (size-1, size-1)
    F = set()
    cpt = 0
    i = 0
    j = 0
    while cpt < (size)* (size) :
        F.add((i, j))
        j+= 1
        if j == size  :
            i += 1
            j = 0
        cpt += 1

    si = depart
    t = []

    longeur = size*size - (size-2)*(size-2)#pour ne pas prendre les bordures 
    while len(F) > longeur :

        #si le sommet de plus petite distance
        si = rechercher_min(F, dist)

        #supprime le sommet min de F
        F.discard(si)

        #succ contiendra les voisins de si
        succ = voisin(matrice, si, size)

        #Relacher
        for sj in succ :
            relacher(sj, si, matrice, T, dist)
        
    return remonter(arrive, depart, T)


