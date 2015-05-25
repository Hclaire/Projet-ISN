# -*- coding: utf-8 -*-

"""
fenetre principale du jeu dans lequel ils  aura l'apparition des deux jeux
"""
import pygame
import random
from pygame.locals import *

"""
Fonction qui affiche le menu principal du jeu.
Paramètres
----------
None
Retour
------
fenetre : fenetre principale
"""
def affichage_menu(): 
    pygame.init()
    pygame.display.init()
    #Initialisation de la bibliothèque pygame.
    
    fenetre = pygame.display.set_mode((1150, 700)) #Ouverture de la fenetre pygame avec la résolution 1500x700
    fond_ecran_jeu = pygame.image.load("./fond/fond_kingreflex.png").convert_alpha() #Chargement du fond d'écrand du jeu THE BEST KINGREFLEX.
    menu = pygame.image.load("./fond/menu.png").convert()#Chargement du menu à choix multiples du jeu THE BEST KINGREFLEX.
    fenetre.blit(fond_ecran_jeu, (0,0))#Collage du fond d'écrand du jeu THE BEST KINGREFLEX.
    pygame.display.flip()#Rafraîchissement de la fenêtre pygame
    pygame.time.wait(2000)#Attente de 2sec
    fenetre.blit(menu, (0,0))#Collage du menu à choix multiples du jeu THE BEST KINGREFLEX.
    pygame.display.flip()#Rafraîchissement de la fenêtre pygame
    

    return fenetre #La fonction retourne la fenêtre de pygame sur laquelle on va jouer.
"""
Fonction qui en focntion du jeu choisit, entre dans le jeu.
Paramètres
----------
fenetre : fenetre principalefenetre : fenetre principale
Retour
------

None
"""

def choix_menu(fenetre):
    continuer = True #on crée une variable booléenne.
    while continuer: #Tant que c'est vrai on continue
        son_quit_ecran = pygame.mixer.Sound("./Son_touches/jeu_deux/quitteecran.wav")
        for event in pygame.event.get():  #Attente des événements
            if event.type == QUIT:  # on quitte la partie par la croix
                son_quit_ecran.play()#On ajoute le son quitter écran à cet évenement.
                pygame.time.wait(500)#Attente de 0.5 sec
                continuer = False #On arrête le jeu et la boucle.
            if event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 391.5 and event.pos[0] < 1076.5 and event.pos[1] < 451 and event.pos[1] > 300:
            #Condition si on clique sur le jeu MOVE REFLEX alors:

                
                fond_accueil = pygame.image.load("./fond/fond1.png").convert_alpha() #Chargement du premier fond d'écran du jeu MOVE REFLEX.
                fenetre.blit(fond_accueil, (0,0)) #Collage du premier fond d'écran du jeu MOVE REFLEX.
                pygame.display.flip()#Rafraîchissement de la fenêtre pygame
                pygame.time.wait(700)
                
                continuer_2 = True #on crée une variable booléenne.
                while continuer_2: #Tant que c'est vrai on continue
                    i = 0 #Initialisation du compteur à 0.
                    while i < 20: #Tant que le comteur est <0 alors:
                        image_cliquez = pygame.image.load("./fond/image_clignote.png").convert_alpha()
                        fenetre.blit(image_cliquez, (0,0))
                        pygame.display.flip()
                        pygame.time.wait(700)        
                        image_regle_jeu = pygame.image.load("./fond/reglejeu.png").convert_alpha()
                        fenetre.blit(image_regle_jeu, (0,0))
                        pygame.display.flip()
                        pygame.time.wait(700)  
                        i += 1
                        #Ensemble de chargement et collage d'images permettant de faire clignoter les images du menus.
                        for event in pygame.event.get():	#Attente des événements
                            if event.type == QUIT: # on quitte la partie par la croix
                                
                                son_quit_ecran.play()#On ajoute le son quitter écran à cet évenement.
                                pygame.time.wait(500)#Attente de 0.5 sec
                                continuer = False #On arrête le jeu et la boucle.
                                
                            elif event.type == MOUSEBUTTONDOWN:
                            
                                if event.button == 1:#Condition si on clique n'importe où pour continuer le jeu alors:
                                       
                                        from Move_Reflex import main_01 #On lance le jeu MOVE REFLEX.
                pygame.quit() #Permet de quitter pygame.

            elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[0] > 391.5 and event.pos[0] < 1076.5 and event.pos[1] < 663.7 and event.pos[1] > 487.4:
                #Condition si on clique sur le jeu Head In Fire alors:
                pygame.init() #Ouverture de la fenetre Pygame

                fond_accueil = pygame.image.load("./fond/fondJEU02.png").convert_alpha() #Chargement du premier fond d'écran du jeu.
                fenetre.blit(fond_accueil, (0,0))#Collage du premier fond d'écran du jeu Head In Fire.
                pygame.display.flip()#Rafraîchissement de la fenêtre pygame
                
                son_fond = pygame.mixer.Sound("./Son_touches/jeu_deux/feu_jeu.wav")
                son_fond.play()
                pygame.time.wait(700)
                continuer = True#on crée une variable booléenne.
                while continuer:#Tant que c'est vrai on continue
                    i = 0#Initialisation du compteur à 0.
                    while i < 20:#Tant que le comteur est <0 alors:
 
                        image_cliquez = pygame.image.load("./fond/fondJEU02_regle_clignote.png").convert_alpha()
                        fenetre.blit(image_cliquez, (0,0))
                        pygame.display.flip()
                        pygame.time.wait(700)
                        image_regle_jeu = pygame.image.load("./fond/fondJEU02_regle.png").convert_alpha()
                        fenetre.blit(image_regle_jeu, (0,0))
                        pygame.display.flip()
                        pygame.time.wait(700)
                        
                        i += 1
                        #Ensemble de chargement et collage d'images permettant de faire clignoter les images du menus.
                        for event in pygame.event.get():	#Attente des événements
                            if event.type == QUIT:# on quitte la partie par la croix
                                son_quit_ecran.play()#On ajoute le son quitter écran à cet évenement.
                                pygame.time.wait(500)#Attente de 0.5 sec
                                continuer == False  #On arrête le jeu et la boucle
                            elif event.type == MOUSEBUTTONDOWN:
                                if event.button == 1:  #Condition si on clique n'importe où pour continuer le jeu alors:
                                    from HeadInFire import main_02  #On lance le jeu Head In Fire   
                #Permet de quitter pygame.
                pygame.display.flip()
    pygame.quit()
        

def main():#Fonction principale
    fenetre = affichage_menu()#Appel de la fonction affichage_menu()
    choix_menu(fenetre)#Appel de la fonction choix_menu()


main()#Appel de la fonction principale
    
