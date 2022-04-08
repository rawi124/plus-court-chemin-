#!/usr/bin/python
import tkinter as tk
import sys, time, numpy
import Matrice as m
import fenetre as fnt
import dijkstra as dj


if __name__ == "__main__" :

    root  = tk.Tk()#creation du root
    ftopl = tk.Toplevel(width=400, height=400)#creation d une toplevel
    ftopl.title('Chemin')
    fram =  tk.Frame(ftopl,width="150m",height="100m",borderwidth=4)#creation d une frame
    fram.pack()
    C     = tk.Canvas(fram, width=600, height = 600, bg="grey",highlightthickness=2,highlightbackground="black")
    cadre = tk.Frame(ftopl,width="50m",height="40m",borderwidth=2)#creation d une frame
    cadre.pack(fill="x")
    matrice = m.Matrice(30, 100)
    C.pack(padx=5, pady=5)
    fnt.affichage(C, matrice.mat, 30, 100)
    l_cord = []
    def chemin(event):
        """pour faire l affichage du chemin sur la matrice
        """
        global l_cord
        id = C.find_withtag("current")
        tmp = (C.gettags(id)[1]).split(' ')
        x = (int(tmp[0]), int(tmp[1]))
        l_cord.append(x)
        if len(l_cord) == 2:
            s = dj.dijkstra(matrice.mat, l_cord[0], l_cord[1], 30)
            for el in s :
                matrice.mat[el[0]][el[1]] = 1500
        fnt.affichage(C, matrice.mat, 30, 100)
    C.tag_bind("clic", "<1>", chemin)

    root.mainloop()

exit(0)
