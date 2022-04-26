#!/usr/bin/python
import tkinter as tk
import math
import numpy as np

import traitement_matrice as fct

AUCUN = -1  # aucun chemin possible

class Matrice:

    def __init__(self, n, val_max):
        """ le constructeur qui initialise une self.mat aleatoire avec une valeur max val_max """
        self.n = n
        self.mat = fct.arith_matrice(val_max, n)
        self.mat = fct.ajout_infranchissable(self.mat, n)
        #print(self.mat)
        self.val_max = val_max

    def get_n(self):
        return self.__n

    def set_n(self, n):
        self.__n = n

    def get_val_max(self):
        return self.__val_max

    def set_val_max(self, val_max):
        self.__val_max = val_max


    def afficher_matrice(self):
        """methode qui affiche une self.mat aleatoire """
        for line in self.mat:
            for elem in line:
                print("{0:4}".format(elem), end=" ")
            print()
