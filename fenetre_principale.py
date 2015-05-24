# -*- coding: utf-8 -*-

"""
fenetre principale du jeu dans lequel ils  aura l'apparition des deux jeux
"""
import pygame
import random
from pygame.locals import *


from ProjetV1_7_23_05_15 import main_02

defaite_gauche = 0
defaite_droite = 0
while defaite_gauche <4 or defaite_droite <4:
    defaite_gauche, defaite_droite = main_02(defaite_gauche,defaite_droite)
    pygame.time.wait(2000)
       
