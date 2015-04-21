# -*- coding: utf-8 -*-
"""
Projet jeu 1 affichage chiffre
"""

import pygame
import random
from pygame.locals import *


def choix_fond_de_couleur(fenetre):
    numero_fond = random.randint(1,4)
    if numero_fond == 1:
        #Chargement et collage du fond
        fond = pygame.image.load("./fond/fondrouge.jpg").convert()

    elif numero_fond == 2:
        fond = pygame.image.load("./fond/fondbleu.jpg").convert()

    elif numero_fond == 3:
        fond = pygame.image.load("./fond/fondviolet.jpg").convert()

    else:
        fond = pygame.image.load("./fond/fondvert.jpg").convert()

    fenetre.blit(fond, (0,0))



def choix_nb_1 (fenetre):
    numero_nombre = random.randint(1,10)
    if numero_nombre ==1 :
        #Chargement et collage du numero
        numero1 = pygame.image.load("./chiffre/chiffre_1.png").convert_alpha()

    elif numero_nombre ==2:
        numero1 = pygame.image.load("./chiffre/chiffre_2.png").convert_alpha()

    elif numero_nombre ==3:
        numero1 = pygame.image.load("./chiffre/chiffre_3.png").convert_alpha()

    elif numero_nombre ==4:
        numero1 = pygame.image.load("./chiffre/chiffre_4.png").convert_alpha()

    elif numero_nombre ==5:
        numero1 = pygame.image.load("./chiffre/chiffre_5.png").convert_alpha()
    
    elif numero_nombre ==6:
        numero1 = pygame.image.load("./chiffre/chiffre_6.png").convert_alpha()

    elif numero_nombre ==7:
        numero1 = pygame.image.load("./chiffre/chiffre_7.png").convert_alpha()
    
    elif numero_nombre ==8:
        numero1 = pygame.image.load("./chiffre/chiffre_8.png").convert_alpha()

    else:
        numero1 = pygame.image.load("./chiffre/chiffre_9.png").convert_alpha()
    
    fenetre.blit(numero1, (50,100))
    return numero_nombre



# choix du nombre numero 2
def choix_nb_2( fenetre):
    numero_nombre2 = random.randint(1,10)
    if numero_nombre2 == 1 :
        #Chargement et collage du numero
        numero2 = pygame.image.load("./chiffre/chiffre_1.png").convert_alpha()

    elif numero_nombre2 == 2:
        numero2 = pygame.image.load("./chiffre/chiffre_2.png").convert_alpha()

    elif numero_nombre2 == 3:
        numero2 = pygame.image.load("./chiffre/chiffre_3.png").convert_alpha()

    elif numero_nombre2 == 4:
        numero2 = pygame.image.load("./chiffre/chiffre_4.png").convert_alpha()

    elif numero_nombre2 == 5:
        numero2 = pygame.image.load("./chiffre/chiffre_5.png").convert_alpha()
    
    elif numero_nombre2 == 6:
        numero2 = pygame.image.load("./chiffre/chiffre_6.png").convert_alpha()

    elif numero_nombre2 == 7:
        numero2 = pygame.image.load("./chiffre/chiffre_7.png").convert_alpha()
    
    elif numero_nombre2 == 8:
        numero2 = pygame.image.load("./chiffre/chiffre_8.png").convert_alpha()

    else:
        numero2 = pygame.image.load("./chiffre/chiffre_9.png").convert_alpha()
        
    fenetre.blit(numero2, (250,100))
    return numero_nombre2

def choix_des_signes(fenetre):
    numero_signe = random.randint(1,3)
    
    if numero_signe == 1:
        signe = pygame.image.load("./signe/signe_plus.png").convert_alpha()
    elif numero_signe == 2:
        signe = pygame.image.load("./signe/signe_moins.png").convert_alpha()
    else:
        signe = pygame.image.load("./signe/signe_fois.png").convert_alpha()
  
    fenetre.blit (signe, (150,100))
    
    sign_egal = pygame.image.load("./signe/signe_egal.png").convert_alpha()
    fenetre.blit(sign_egal,(350,100))

    return numero_signe


    

    
def calcul_resultat(nb_1, nb_2, signe):
    if signe == 1:
       result = nb_2 + nb_1
    elif signe == 2:
        result = nb_2 - nb_1
    else:
        result = nb_2 * nb_1
    print(result)
    return result
    
def decomposition_resultat(result,fenetre):
    liste_chiffre = []
    result = str(result)
    for chiffre in result:
        liste_chiffre.append(int(chiffre))
    print(liste_chiffre)

def affichage_resultat(chiffre,fenetre):

    for chiffre in liste_chiffre:
    
        if chiffre == 1 :
        #Chargement et collage du numero
            chiffre_affich = pygame.image.load("./chiffre/chiffre_1.png").convert_alpha()

        elif chiffre == 2:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_2.png").convert_alpha()

        elif chiffre == 3:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_3.png").convert_alpha()

        elif chiffre == 4:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_4.png").convert_alpha()

        elif chiffre == 5:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_5.png").convert_alpha()
    
        elif chiffre == 6:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_6.png").convert_alpha()

        elif chiffre == 7:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_7.png").convert_alpha()
    
        elif chiffre == 8:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_8.png").convert_alpha()

        else:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_9.png").convert_alpha()
        
        a = 450
        fenetre.blit(chiffre_affich, (a,100))
        a += 50

def main():
    pygame.init()
    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((640, 480))
    choix_fond_de_couleur(fenetre)
    nb_1 = choix_nb_1(fenetre)
    nb_2 = choix_nb_2(fenetre)
    signe = choix_des_signes(fenetre)
    result = calcul_resultat( nb_1,nb_2,signe)
    decomposition_resultat(result,fenetre)


    #Rafraîchissement de l'écran
    pygame.display.flip()        

main()