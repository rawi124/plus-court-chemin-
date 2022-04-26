#!/usr/bin/python
import tkinter as tk
import math

def point(px, py, pcoul,canva):
    """
    affichage dans le repère écran d'un point (px, py) 
    """
    canva.create_line(px, py, px, py+2, fill=pcoul)


def barycentre(xa, ya, xb, yb, xc, yc, xd, yd, t):
    """
    calcule le barycentre des deux points a(xa, xb) et b(xb, yb)
    """
    l = []
    l.append([(1-t)*xa + t*xb, (1-t)*ya + t*yb])
    l.append([(1-t)*xb + t*xc, (1-t)*yb + t*yc])
    l.append([(1-t)*xc + t*xd, (1-t)*yc + t*yd])
    l.append([(1-t)*l[0][0] + t*l[1][0], (1-t)*l[0][1] + t*l[1][1]])
    l.append([(1-t)*l[1][0] + t*l[2][0], (1-t)*l[1][1] + t*l[2][1]])
    l.append([(1-t)*l[2][0] + t*l[3][0], (1-t)*l[2][1] + t*l[3][1]])
    l.append([(1-t)*l[3][0] + t*l[4][0], (1-t)*l[3][1] + t*l[4][1]])
    return l[6][0], l[6][1]

def bezier_Algo(xA, yA, xB, yB, xC, yC, xD, yD , N, canva):
    """
    avec la methode algorithmique
    """
    pas = 1 / N # 1 / N pour savoir on fait varier t de combien ( selon le nombre N saisie par l utilisateur )
    t = 0

    while (t < 1):
        pt = barycentre(xA, yA, xB, yB, xC, yC, xD, yD, t)
        point(pt[0], pt[1], "black", canva)
        t = t + pas

def equation_X_Y(xa, ya, xb, yb, xc, yc, xd, yd, t):
    """
    prend en entree une liste contenant les coordonées des 4 points de la courbe de bezier
    et t qui est entre 0 et 1 , et renvoie x(t),y(t) sous forme de tuple
    """
    B3_0 = (1-t)**3
    B3_1 = 3*t -6*t**2 + 3*t**3
    B3_2 = 3*t**2 - 3*t**3
    B3_3 = t**3
    return B3_0 *xa + B3_1 *xb + B3_2*xc + B3_3*xd, B3_0 *ya + B3_1 *yb + B3_2*yc + B3_3*yd

def courbe_Bezier_Bernstein(xA, yA, xB, yB, xC, yC, xD, yD , N, canva, couleur):
    """
    prend en entree une liste contenant les coordonées des 4 points de la courbe de bezier
    et N ( nombre de points d’interpolation) et dessine la courbe correspondante avec la methode
    de Bernstein
    """
    pas = 1 / N # 1 / N pour savoir on fait varier t de combien ( selon le nombre N saisie par l utilisateur )
    t = 0

    while (t < 1):
        pt = equation_X_Y(xA, yA, xB, yB, xC, yC, xD, yD, t)
        point(pt[0], pt[1], couleur, canva)
        t = t + pas


def bezier_chemin(lis, N, canva, couleur):
    """
    dessine la courbe de bezier qui passe par tous les points de la liste en parametre
    tout en respectant la C1 continuité 
    """

    i = 0
    n = len(lis)
    while i+8 <=  n:
        #a chaque tour de boucle on prend 8 valeurs de la liste qui representent respectivement x0, y0, ...., x7, y7
        #on incremente i de 6 pour assurer la C0 contuinuité
        courbe_Bezier_Bernstein(lis[i]+4, lis[i+1]+4, lis[i+2]+4, lis[i+3]+4, lis[i+4]+4, lis[i+5]+4, lis[i+6]+4, lis[i+7]+4 , N, canva, couleur)

        i+= 6
    while i+2 < n :
        canva.create_line(lis[i]+4, lis[i+1]+4, lis[i+2]+4, lis[i+3], fill=couleur)
        i += 2

        

    
        

