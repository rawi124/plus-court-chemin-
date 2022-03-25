import tkinter as tk
import sys, time, numpy
import numpy as np

def affichage(canv, matrice, n):
    """
    affiche la matrice sur l'ecran avec des couleurs :
    blanc : -1
    yellow : petite valeur
    green : valeur moyenne
    blue : grande valeur
    """
    i = 0
    j = 1
    x = 0
    p = 0
    while x < n :
        i = 0
        while(i < 10*n):
            if matrice[x][p] == -1 :
                couleur ="white"
            elif matrice[x][p] <= 25 :
                couleur ="yellow"
            elif matrice[x][p] > 25 and matrice[x][p] < 50 :
                couleur = "green"
            elif matrice[x][p] >= 50 and matrice[x][p] < 75 :
                couleur = "blue"
            else :
                couleur = "black"
            canv.create_rectangle(i,j,i+10,j+10,fill=couleur, tags=(("clic",(x, p))))
            p = p + 1
            i = i + 10
        p = 0
        j = j + 10
        x = x + 1
    canv.addtag_withtag("clic", 1)
    



