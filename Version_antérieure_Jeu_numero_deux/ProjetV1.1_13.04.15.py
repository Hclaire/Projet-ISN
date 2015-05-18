# -*- coding: utf-8 -*-
"""
Projet jeu 1 affichage chiffre
"""

import pygame
import random
from pygame.locals import *

pygame.init()

#Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))


def choix_fond_de_couleur():
    numero_fond = random.randint(1,4)
    if numero_fond == 1:
        #Chargement et collage du fond
        fond = pygame.image.load("fond\fondrouge.jpg").convert()

    elif numero_fond == 2:
        fond = pygame.image.load("fond\fondbleu.jpg").convert()

    elif numero_fond == 3:
        fond = pygame.image.load("fond\fondviolet.jpg").convert()

    else:
        fond = pygame.image.load("fond\fondvert.jpg").convert()

    fenetre.blit(fond, (0,0))



def choix_nb_1 ():
    numero_nombre = random.randint(1,10)
    if numero_nombre ==1 :
        #Chargement et collage du numero
        numero1 = pygame.image.load("chiffre\chiffre_1.png").convert_alpha()

    elif numero_nombre ==2:
        numero1 = pygame.image.load("chiffre\chiffre_2.png").convert_alpha()

    elif numero_nombre ==3:
        numero1 = pygame.image.load("chiffre\chiffre_3.png").convert_alpha()

    elif numero_nombre ==4:
        numero1 = pygame.image.load("chiffre\chiffre_4.png").convert_alpha()

    elif numero_nombre ==5:
        numero1 = pygame.image.load("chiffre\chiffre_5.png").convert_alpha()
    
    elif numero_nombre ==6:
        numero1 = pygame.image.load("chiffre\chiffre_6.png").convert_alpha()

    elif numero_nombre ==7:
        numero1 = pygame.image.load("chiffre\chiffre_7.png").convert_alpha()
    
    elif numero_nombre ==8:
        numero1 = pygame.image.load("chiffre\chiffre_8.png").convert_alpha()

    else:
        numero1 = pygame.image.load("chiffre\chiffre_9.png").convert_alpha()
    
    fenetre.blit(numero1, (50,100))




# choix du nombre numero 2
def choix_nombre_deux():
    numero_nombre2 = random.randint(1,10)
    if numero_nombre2 == 1 :
        #Chargement et collage du numero
        numero2 = pygame.image.load("chiffre\chiffre_1.png").convert_alpha()

    elif numero_nombre2 == 2:
        numero2 = pygame.image.load("chiffre\chiffre_2.png").convert_alpha()

    elif numero_nombre2 == 3:
        numero2 = pygame.image.load("chiffre\chiffre_3.png").convert_alpha()

    elif numero_nombre2 == 4:
        numero2 = pygame.image.load("chiffre\chiffre_4.png").convert_alpha()

    elif numero_nombre2 == 5:
        numero2 = pygame.image.load("chiffre\chiffre_5.png").convert_alpha()
    
    elif numero_nombre2 == 6:
        numero2 = pygame.image.load("chiffre\chiffre_6.png").convert_alpha()

    elif numero_nombre2 == 7:
        numero2 = pygame.image.load("chiffre\chiffre_7.png").convert_alpha()
    
    elif numero_nombre2 == 8:
        numero2 = pygame.image.load("chiffre\chiffre_8.png").convert_alpha()

    else:
        numero2 = pygame.image.load("chiffre\chiffre_9.png").convert_alpha()
        
    fenetre.blit(numero2, (250,100))
    return numero_nombre2

def choix_signe():
    numero_signe = random.randint(1,4)
    if numero_signe != 4:
        if numero_signe == 1:
            signe = pygame.image.load("signe\signe_plus.png").convert_alpha()
        elif numero_signe == 2:
            signe = pygame.image.load("signe\signe_moins.png").convert_alpha()
        else:
            signe = pygame.image.load("signe\signe_fois.png").convert_alpha()
        choix_nombre_deux()
    else:
        signe = pygame.image.load("signe\signe_div.png").convert_alpha()
        
        numero_nombre2 = choix_nombre_deux()
        while numero_nombre2 > numero_nombre:
            numero_nombre2 = choix_nombre_deux()
    
    fenetre.blit (signe, (150,100))
    return signe,numero_signe
        



def choix_signe_egal():
    sign_egal = pygame.image.load("signe\signe_egal.png").convert_alpha()
    fenetre.blit(sign_egal,(350,100))


def main():
    choix_fond_de_couleur()
    choix_nb_1()
    choix_nb_2()
    choix_signe()
    choix_signe_egal()

#Rafraîchissement de l'écran
    pygame.display.flip()

main()