#!/usr/bin/python
import tkinter as tk
import sys, time, numpy
import Matrice as m
import fenetre as fnt


if __name__ == "__main__" :
    root  = tk.Tk()#creation du root
    ftopl = tk.Toplevel(width=400, height=400)#creation d une toplevel
    ftopl.title('Chemin')
    fram =  tk.Frame(ftopl,width="150m",height="100m",borderwidth=4)#creation d une frame
    fram.pack()
    C     = tk.Canvas(fram, width=500, height=300, bg="grey",highlightthickness=2,highlightbackground="black")
    cadre = tk.Frame(ftopl,width="50m",height="40m",borderwidth=2)#creation d une frame
    cadre.pack(fill="x")
    matrice = m.Matrice(1000,100)
    #matrice.afficher_matrice()
    fnt.affichage(C, matrice.mat)

    C.pack(padx=5, pady=5)
    root.mainloop()
    
exit(0)