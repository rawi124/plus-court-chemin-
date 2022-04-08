import tkinter as tk
import sys, time, numpy
import numpy as np
import math

def affichage(canv, matrice, n, val_max):
    """
    affiche la matrice sur l'ecran avec des couleurs degradé
    """
    i = 0
    j = 1
    x = 0
    p = 0
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
            elif matrice[x][p] == 1500 :
                couleur = '#D50B53'
                canv.create_oval(i+7,j+7,i+15,j+15,fill=couleur, outline="", tags=(("clic",(x, p))))
            p = p + 1
            i = i + 20
        p = 0
        j = j + 20
        x = x + 1
    canv.addtag_withtag("clic", 1)
