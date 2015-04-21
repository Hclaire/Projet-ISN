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
    
    fenetre.blit(numero1, (150,20))
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
        
    fenetre.blit(numero2, (350,20))
    return numero_nombre2


def choix_des_signes_et_boutons(fenetre):
    numero_signe = random.randint(1,2)
    
    if numero_signe == 1:
        signe = pygame.image.load("./signe/signe_plus.png").convert_alpha()
    else:
        signe = pygame.image.load("./signe/signe_fois.png").convert_alpha()
  
    fenetre.blit (signe, (250,20))
    
    sign_egal = pygame.image.load("./signe/signe_egal.png").convert_alpha()
    fenetre.blit(sign_egal,(175,150))

    signe_correct = pygame.image.load("./Boutons/BoutonRightpasEnfonce.png").convert_alpha()
    signe_incorrect = pygame.image.load("./Boutons/BoutonWrongpasEnfonce.png").convert_alpha()
    fenetre.blit(signe_correct,(25,200))
    fenetre.blit(signe_incorrect,(350,200))
    
    return numero_signe


def calcul_resultat(nb_1, nb_2, signe):
    if signe == 1:
       result = nb_2 + nb_1
    else:
        result = nb_2 * nb_1
    print(result)
    return result
    

def decomposition_resultat(result,fenetre):
    liste_chiffre = []
    result_plus_un = result + 1
    result_moins_un = result -1 
    
    choix_result = random.randint(1,3)
    if choix_result == 1 :
        resultat_jeu = result
    elif choix_result == 2 :
        resultat_jeu = result_plus_un
    else :
        resultat_jeu = result_moins_un
    resultat_jeu_nb = resultat_jeu
    resultat_jeu = str(resultat_jeu_nb)
    for chiffre in resultat_jeu:
        liste_chiffre.append(int(chiffre))
    print(liste_chiffre)
    
    return liste_chiffre, resultat_jeu_nb


def affichage_resultat(liste_chiffre,fenetre):
    a = 250
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
        
        
        fenetre.blit(chiffre_affich, (a,150))
        a += 75


def evenement(fenetre, resultat_jeu_nb, result):
    #BOUCLE INFINIE
    i = 0 
    continuer = True
    while continuer:
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:
                continuer = False
            if event.type == KEYDOWN and i < 1:
                if event.key == K_LEFT:
                        #fenetre.blit(background, position, position) 
                        bouton_reponse = pygame.image.load("./Boutons/BoutonRightEnfonce.png").convert_alpha()
                        fenetre.blit(bouton_reponse,(25,200))
                        bouton_reponse = 1
                elif event.key == K_RIGHT and i < 1:
                        bouton_reponse = pygame.image.load("./Boutons/BoutonWrongEnfonce.png").convert_alpha()
                        fenetre.blit(bouton_reponse,(350,200))
                        bouton_reponse = 2
                i += 1 
            pygame.display.flip()
    pygame.quit()

#def verification_reponse(bouton_reponse,):
        
    
def main():
    pygame.init()
    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((640, 480))
    choix_fond_de_couleur(fenetre)
    nb_1 = choix_nb_1(fenetre)
    nb_2 = choix_nb_2(fenetre)
    signe = choix_des_signes_et_boutons(fenetre)
    result = calcul_resultat( nb_1,nb_2,signe)
    liste_chiffre , resultat_jeu_nb = decomposition_resultat(result,fenetre)
    affichage_resultat (liste_chiffre , fenetre)
    evenement(fenetre, resultat_jeu_nb, result)

    #Rafraîchissement de l'écran
    pygame.display.flip()        

main()