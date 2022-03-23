import tkinter as tk
import sys, time, numpy
import numpy as np

def affichage(canv, matrice):
    """
    affiche une matrice sous forme de couleur
    """
    i = 0
    j = 1
    x = 0
    while x < 30 :
        i = 0
        while(i < 490):
            if matrice[x][i] < 30 :
                couleur ="yellow"
            elif matrice[x][i] >= 30 and matrice[x][i] < 60 :
                couleur = "green"
            else :
                couleur = "red"
            canv.create_rectangle(i,j,i+10,j+10,fill=couleur, tags=(("clic",matrice[x][i])))
            i = i + 10
        j = j + 10
        x = x + 1
    canv.addtag_withtag("clic", 1)


