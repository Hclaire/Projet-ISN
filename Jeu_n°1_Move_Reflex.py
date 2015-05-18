# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:16:25 2015

@author: sansomasoundara
"""

"""

Jeu n°1 : 
L'utilisateur doit appuyer sur la flèche qui correspond à l'écran
si le fond de la flèche est bleu sinon il doit appuyer la flèche inverse.

"""
import pygame
import random
from pygame.locals import *


def choix_fond(fenetre):
    numero = random.randint(1,4)
    if numero == 1:
    
        fond = pygame.image.load("fondrouge.jpg").convert()

    elif numero == 2:
        fond = pygame.image.load("fondbleu.jpg").convert()

    elif numero == 3:
        fond = pygame.image.load("fondviolet.jpg").convert()

    else:
        fond = pygame.image.load("fondvert.jpg").convert()

    fenetre.blit (fond, (0,0))


def choix_fleches(numero, fenetre):

    if numero == 1:
    
        fleche = pygame.image.load("fleche_bas_bleu.png").convert_alpha()
    
    elif numero == 2:
    
        fleche = pygame.image.load("fleche_droite_bleu.png").convert_alpha()
    
    elif numero == 3:
    
        fleche = pygame.image.load("fleche_haut_bleu.png").convert_alpha()
    
    elif numero == 4:
    
        fleche = pygame.image.load("fleche_gauche_bleu.png").convert_alpha()
    
    elif numero == 5:
    
        fleche = pygame.image.load("fleche_bas_rose.png").convert_alpha()
    
    elif numero == 6:
    
        fleche = pygame.image.load("fleche_droite_rose.png").convert_alpha()
        
    elif numero == 7:
    
        fleche = pygame.image.load("fleche_haut_rose.png").convert_alpha()
    
    else :
    
        fleche = pygame.image.load("fleche_gauche_rose.png").convert_alpha()

    fenetre.blit(fleche, (100,80))
    

def evenement(numero_fleches, fenetre):
    
    continuer = True

    while continuer:
        
        for event in pygame.event.get():	#Attente des événements
        
            if event.type == QUIT:
                
                continuer = False
            
                
            if event.type == KEYDOWN:
                    
                if event.key == K_DOWN: #Si "flèche bas"
                        
                    if numero_fleches == 1 or numero_fleches == 7:
                            
                        result = pygame.image.load("correct.png").convert_alpha()
                        

                    else:

                        result = pygame.image.load("incorrect.png").convert_alpha()

                elif event.key == K_LEFT:

                    if numero_fleches == 4 or numero_fleches == 6:

                        result = pygame.image.load("correct.png").convert_alpha()

                    else:

                        result = pygame.image.load("incorrect.png").convert_alpha()

                elif event.key == K_UP: #Si "flèche bas"
                        
                    if numero_fleches == 3 or numero_fleches == 5:
                            
                        result = pygame.image.load("correct.png").convert_alpha()
                            
                    else:
                            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                            
                elif event.key == K_RIGHT:
                    
                    if numero_fleches == 2 or numero_fleches == 8:
                            
                        result = pygame.image.load("correct.png").convert_alpha()

                    else:

                        result = pygame.image.load("incorrect.png").convert_alpha()

                fenetre.blit(result, (120,100))

                pygame.display.flip() #Rafraîchissement de l'écran
                
                i = 0
                while i<7:

                    main()
                    i= i + 1   
    pygame.quit()
         

def main():
        
    pygame.init() #Ouverture de la fenêtre Pygame

    fenetre = pygame.display.set_mode((640, 480))
        
    choix_fond(fenetre)
    pygame.display.flip() #Rafraîchissement de l'écran

    numero_fleches = 1
    
    choix_fleches(numero_fleches, fenetre)
    pygame.display.flip() #Rafraîchissement de l'écran

    evenement(numero_fleches, fenetre)
    pygame.display.flip() #Rafraîchissement de l'écran
 
main()