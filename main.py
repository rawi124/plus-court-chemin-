#!/usr/bin/python
import tkinter as tk
import sys, time, numpy
import Matrice as m
import affichage as aff



if __name__ == "__main__" :

    root  = tk.Tk()#creation du root

    ftopl = tk.Toplevel(width=750, height=750)#creation d une toplevel
    ftopl.title('Chemin')

    fram =  tk.Frame(ftopl,width="150m",height="100m",borderwidth=4)#creation d une frame
    cadre2 = tk.Frame(ftopl)#creation d une deuxieme frame
    lab = tk.Label(cadre2,text="pour afficher un chemin appuyez sur deux endroits # de la matrice, A* : brown, dijkstra : yellow")#creation d un label

    lab.pack(side="left")
    cadre2.pack()
    fram.pack()

    C     = tk.Canvas(fram, width=600, height = 600, bg="grey",highlightthickness=2,highlightbackground="black")
    C.pack(padx=5, pady=5)

    matrice = m.Matrice(30, 100)
    aff.affichage_matrice_couleur(C, matrice.mat, 30, 100)
    l_cord = []#pour receptionner les coordonnees de la ou l utilisateur appuie sur la matrice

    def chemin(event):
        """pour faire l affichage du chemin sur la matrice
        """
        global l_cord
        id = C.find_withtag("current")
        tmp = (C.gettags(id)[1]).split(' ')
        if matrice.mat[int(tmp[0])][int(tmp[1])] != -1 :
            #pour verifier si on  est pas sur la bordure
            #valeur par defaut sur la bordure est -1
            l_cord.append((int(tmp[0]), int(tmp[1])))
        if len(l_cord) == 2  :
            aff.afficher_dijkstra(l_cord, matrice.mat, C)
            aff.afficher_astar(l_cord, matrice.mat, C)
            l_cord = []

    C.tag_bind("clic", "<1>", chemin)
    root.mainloop()

exit(0)
