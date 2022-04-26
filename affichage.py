import tkinter as tk
import sys, time, numpy
import numpy as np
import math

import dijkstra as dj
import bezier as bz
import astar as ast

def affichage_matrice_couleur(canv, matrice, n, val_max):
    """
    affiche la matrice sur l'ecran avec des couleurs degradé
    """
    i = 0
    j = 1
    x = 0
    p = 0
    coord = []
    l = []
    while x < n :
        i = 0
        while(i < 20*n):
            if matrice[x][p] == -1 or matrice[x][p] == 1e6 :
                couleur ="red"
            elif matrice[x][p] <= val_max/4 :
                couleur = '#BBBF95'
            elif matrice[x][p] > val_max/4 and matrice[x][p] < val_max*3.5/10:
                couleur = '#0486DB'
            elif matrice[x][p] >= val_max*3.5/10 and matrice[x][p] < val_max/2:
                couleur = '#05ACD3'
            elif matrice[x][p] >= val_max/2 and matrice[x][p] < val_max*2/3 :
                couleur = '#012172'
            elif matrice[x][p] >= val_max*2/3 and matrice[x][p] < val_max :
                couleur = '#1F1641'
            canv.create_rectangle(i,j,i+20,j+20,fill=couleur, outline="", tags=(("clic",(x, p))))
            p = p + 1
            i = i + 20
        p = 0
        j = j + 20
        x = x + 1
    canv.addtag_withtag("clic", 1)

def afficher_dijkstra(l_cord, matrice, canv):
    """
    affiche sur la matrice du canva le chemin de bezier avec
    la courbe de bezier
    """

    dij = dj.dijkstra(matrice, l_cord[0], l_cord[1], 30)
    dij = [i*20 for i in dij]#pour faire une sorte de projection
    dij.reverse()
    i = 0
    n = len(dij)
    while i+2 < n :
        canv.create_oval(dij[i], dij[i+1], dij[i]+5, dij[i+1]+5 , fill="aqua")
        i += 2
    canv.create_oval(dij[n-2], dij[n-1], dij[n-2]+5, dij[n-1]+5 , fill="aqua")
    #pour ajouter le dernier point si le nombre de point est impair
    if len(dij) > 8 :
        bz.bezier_chemin(dij, 250, canv, "yellow")


def afficher_astar(l_cord, matrice, canv):
    """
    affiche sur la matrice du canva le chemin en suivant astar avec
    la courbe de bezier
    """
    astr = ast.astar(matrice, l_cord[0], l_cord[1], 30)
    astr = [i*20 for i in astr]#pour faire une sorte de projection
    astr.reverse()
    i = 0
    n = len(astr)
    while i+2 < n :
        canv.create_oval(astr[i], astr[i+1], astr[i]+5, astr[i+1]+5 , fill="rosybrown")
        i += 2
    canv.create_oval(astr[n-2], astr[n-1], astr[n-2]+5, astr[n-1]+5 , fill="rosybrown")
    #pour ajouter le dernier point si le nombre de point est impair
    if len(astr) > 8 :
        bz.bezier_chemin(astr, 250, canv,"brown")
