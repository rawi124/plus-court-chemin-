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

def dijkstra(matrice, depart, arrive, size):

    """
    prend matrice en entree, un point de depart et un autre d arrivÃ©e
    et retourne une liste qui contient les corrdonnes du plus court chemin
    depart est de type entier et non pas tuple
    """


    #partie des initialisations
    d = [[infini]*size]*size
    dist = ttt_mat.bordure_matrice(np.array(d)) #liste des distances de chaque sommet init a +inf
    dist[depart[0]][depart[1]] = 0
    #print('au depart l ensemble dist est initilisé ainsi \n',dist,'\n')


    t = [[(0, 0) ]*size]*size
    T = ttt_mat.bordure_matrice(np.array(t))
    #print('au depart l ensemble T est initilisé ainsi \n',T,'\n')
    
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
        
    #print('au depart l ensemble F est initialisé ainsi \n',F,'\n')
    
    si = depart
    t = []

    longeur = size*size - (size-2)*(size-2)
    #print('la longeur est ', longeur)
    while len(F) > longeur :
        mini = infini
        #recherche dans F si tq dist[si] soit minimale 
        for el in F :
            if dist[el[0]][el[1]] < mini and dist[el[0]][el[1]] != AUCUN:
                mini = dist[el[0]][el[1]]
                si = el
            
        #print('le sommet courant qu on traite c est ',si)
        
        F.discard(si)#supprime le sommet min de F
        #print('maintenant F est' , F)
        
        succ = voisin(matrice, si, size)
        #print('les voisins de mon sommet courant ',si,' sont ', succ)

        #Relacher
        for sj in succ :
            relacher(sj, si, matrice, T, dist)
    #print('application de dijkstra a partir du sommet de depart ',depart,'pour la matrice ','\n\n',matrice,'\n\n','est ',T)
    chemin = [arrive]
    while arrive != depart :
        arrive = predecessuer(T, arrive)
        chemin.append(arrive)
    return chemin

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
    

















    
