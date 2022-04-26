import numpy as np
import math as math

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

def cout_dist(sj, si, matrice):
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



def distance(x, y, x1, y1):
    """
    calcule la distance estimée entre deux points de coordonnees respectives
    x,y et x1,y1
    ===> c est l heurestique des distances
    """
    return math.sqrt((x-x1)*(x-x1) + (y-y1)*(y-y1));
    
def nb_obst(matrice, size):
    i = 0
    cpt = 0
    while i < size :
        j = 0
        while j < size :
            if matrice[i][j] == -1 :
                cpt +=1
            j +=1
        i += 1
    return cpt
def astar(matrice, depart, arrive, size):

    """
    prend matrice en entree, un point de depart et un autre d arrivÃ©e
    et retourne une liste qui contient les corrdonnes du plus court chemin
    en suivant l'algorithme de dijkstra
    """

    #partie des initialisations
    d = [[0]*size]*size
    cout = ttt_mat.bordure_matrice(np.array(d)) #liste des distances de chaque sommet init a +inf
    #print('au depart l ensemble dist est initilisé ainsi \n',dist,'\n')

    open_list = set()#open_list
    closed_list = set()#closed_list

    open_list.add((depart[0], depart[1]))#ajouter le point de depart a open_list

    u = depart

    t = [[(0, 0) ]*size]*size
    T = ttt_mat.bordure_matrice(np.array(t))

    while open_list :
        mini = infini
        #recherche dans open_list u tq cout u soit minimale
        #car la liste open_list est consideree une FilePrioritaire
        for el in open_list :
            if cout[el[0]][el[1]] < mini and cout[el[0]][el[1]] != AUCUN:
                mini = cout[el[0]][el[1]]
                u = el
        open_list.discard(u)#supprime le sommet min de open_list
                            #equivalent a faire open_list.defiler()
        if u == arrive :
            chemin = []
            chemin.append(arrive[0])
            chemin.append(arrive[1])
            while arrive != depart :
                arrive = predecessuer(T, arrive)
                chemin.append(arrive[0])
                chemin.append(arrive[1])
            return chemin
        succ = voisin(matrice, u, size)

        #pour chaque voisin v de u dans G
        for v in succ :
            cout_tmp = cout[u[0]][u[1]] + cout_dist(u, v, matrice)
            if not (v in closed_list or (v in open_list and cout_tmp > cout[v[0]][v[1]])):
                cout[v[0]][v[1]] = cout[u[0]][u[1]] + cout_dist(u, v, matrice) + distance(v[0], v[1], arrive[0], arrive[1])
                T[v[0]][v[1]] = u
                open_list.add(v)
        closed_list.add(u)
    #print('application de dijkstra a partir du sommet de depart ',depart,'pour la matrice ','\n\n',matrice,'\n\n','est ',T)

    return False

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
