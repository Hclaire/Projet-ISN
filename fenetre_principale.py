# -*- coding: utf-8 -*-

"""
fenetre principale du jeu dans lequel ils  aura l'apparition des deux jeux
"""
import pygame
import random
from pygame.locals import *

def affichage_menu():
    pygame.init()
    pygame.display.init()
    fenetre = pygame.display.set_mode((1150, 700))
    menu = pygame.image.load("./fond/menu.png").convert()
    fenetre.blit(menu, (0,0))
    pygame.display.flip()
def choix_menu():
    continuer = True
    while continuer:

        for event in pygame.event.get():  #Attente des événements
            if event.type == QUIT:  # on quitte la partie par la croix
                son_quit_ecran.play()
                pygame.time.wait(500)
                continuer = False    
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] < 386.75 and event.pos[0] > 138.13 and event.pos[1] < 331.5 and event.pos[1] > 196.84:
                from ProjetV1_8_24_05_15 import main_02

def main():
    affichage_menu()
    choix_menu()


main()
    
