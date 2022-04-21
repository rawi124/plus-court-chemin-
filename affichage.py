import tkinter as tk
import sys, time, numpy
import numpy as np
import math

import dijkstra as dj
import bezier as bz

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
            if matrice[x][p] == -1 :
                couleur ="white"
                canv.create_rectangle(i,j,i+20,j+20,fill=couleur, outline="", tags=(("clic",(x, p))))
            elif matrice[x][p] <= val_max/4 :
                couleur = '#BBBF95'
                canv.create_rectangle(i,j,i+20,j+20,fill=couleur, outline="", tags=(("clic",(x, p))))
            elif matrice[x][p] > val_max/4 and matrice[x][p] < val_max*3.5/10:
                couleur = '#0486DB'
                canv.create_rectangle(i,j,i+20,j+20,fill=couleur, outline="", tags=(("clic",(x, p))))
            elif matrice[x][p] >= val_max*3.5/10 and matrice[x][p] < val_max/2:
                couleur = '#05ACD3'
                canv.create_rectangle(i,j,i+20,j+20,fill=couleur, outline="", tags=(("clic",(x, p))))
            elif matrice[x][p] >= val_max/2 and matrice[x][p] < val_max*2/3 :
                couleur = '#012172'
                canv.create_rectangle(i,j,i+20,j+20,fill=couleur, outline="", tags=(("clic",(x, p))))
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
    s = dj.dijkstra(matrice, l_cord[0], l_cord[1], 30)
    s = [i*20 for i in s]#pour faire une sorte de projection 
    s.reverse()
    i = 0
    n = len(s)
    while i+2 < n :
        canv.create_oval(s[i], s[i+1], s[i]+7, s[i+1]+7 , fill="aqua")
        i += 2
    canv.create_oval(s[n-2], s[n-1], s[n-2]+7, s[n-1]+7 , fill="aqua")
    #pour ajouter le dernier point si le nombre de point est impair
    if len(s) > 8 :
        bz.bezier_chemin(s, 250, canv)



