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


# choix d'un fond de couleur 
numero_fond = random.randint(1,4)
if numero_fond == 1:
    #Chargement et collage du fond
    fond = pygame.image.load("fondrouge.jpg").convert()

elif numero_fond == 2:
    fond = pygame.image.load("fondbleu.jpg").convert()

elif numero_fond == 3:
    fond = pygame.image.load("fondviolet.jpg").convert()

else:
    fond = pygame.image.load("fondvert.jpg").convert()

fenetre.blit(fond, (0,0))


# choix du nombre numero 1
numero_nombre = random.randint(1,10)
if numero_nombre ==1 :
        #Chargement et collage du numero
    numero1 = pygame.image.load("chiffre_1.png").convert_alpha()

elif numero_nombre ==2:
    numero1 = pygame.image.load("chiffre_2.png").convert_alpha()

elif numero_nombre ==3:
    numero1 = pygame.image.load("chiffre_3.png").convert_alpha()

elif numero_nombre ==4:
    numero1 = pygame.image.load("chiffre_4.png").convert_alpha()

elif numero_nombre ==5:
    numero1 = pygame.image.load("chiffre_5.png").convert_alpha()
    
elif numero_nombre ==6:
    numero1 = pygame.image.load("chiffre_6.png").convert_alpha()

elif numero_nombre ==7:
    numero1 = pygame.image.load("chiffre_7.png").convert_alpha()
    
elif numero_nombre ==8:
    numero1 = pygame.image.load("chiffre_8.png").convert_alpha()

else:
    numero1 = pygame.image.load("chiffre_9.png").convert_alpha()
    
numero1.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
fenetre.blit(numero1, (150,100))


# choix du nombre numero 2
numero_nombre2 = random.randint(1,10)
if numero_nombre2 == 1 :
        #Chargement et collage du numero
    numero2 = pygame.image.load("chiffre_1.png").convert_alpha()

elif numero_nombre2 == 2:
    numero2 = pygame.image.load("chiffre_2.png").convert_alpha()

elif numero_nombre2 == 3:
    numero2 = pygame.image.load("chiffre_3.png").convert_alpha()

elif numero_nombre2 == 4:
    numero2 = pygame.image.load("chiffre_4.png").convert_alpha()

elif numero_nombre2 == 5:
    numero2 = pygame.image.load("chiffre_5.png").convert_alpha()
    
elif numero_nombre2 == 6:
    numero2 = pygame.image.load("chiffre_6.png").convert_alpha()

elif numero_nombre2 == 7:
    numero2 = pygame.image.load("chiffre_7.png").convert_alpha()
    
elif numero_nombre2 == 8:
    numero2 = pygame.image.load("chiffre_8.png").convert_alpha()

else:
    numero2 = pygame.image.load("chiffre_9.png").convert_alpha()

numero2.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
fenetre.blit(numero2, (350,100))

numero_signe = random.randint(1,4)
if numero_signe == 1:
    signe = pygame.image.load("signe_plus.png").convert_alpha()
elif numero_signe == 2:
    signe = pygame.image.load("signe_moins.png").convert_alpha()
elif numero_signe == 3:
    signe = pygame.image.load("signe_fois.png").convert_alpha()
else:
    signe = pygame.image.load("signe_div.png").convert_alpha()

signe.set_colorkey((255,255,255))
fenetre.blit (signe, (250,100))


#Rafraîchissement de l'écran
pygame.display.flip()

