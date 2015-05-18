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
    fond_general = pygame.image.load("./fond/fond.png").convert_alpha()
    fond = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
    fond1 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
    fenetre.blit(fond_general, (0,0))
    fenetre.blit (fond, (0,200))
    fenetre.blit (fond1, (750,200))
    

def choix_fleches(numero, fenetre):

    if numero == 1:
    
        fleche = pygame.image.load("./fleches/fleche_bas_bleu.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_bas_bleu.png").convert_alpha()
    
    elif numero == 2:
    
        fleche = pygame.image.load("./fleches/fleche_droite_bleu.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_droite_bleu.png").convert_alpha()
    
    elif numero == 3:
    
        fleche = pygame.image.load("./fleches/fleche_haut_bleu.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_haut_bleu.png").convert_alpha()
    
    elif numero == 4:
    
        fleche = pygame.image.load("./fleches/fleche_gauche_bleu.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_gauche_bleu.png").convert_alpha()
    
    elif numero == 5:
    
        fleche = pygame.image.load("./fleches/fleche_bas_rose.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_bas_rose.png").convert_alpha()
    
    elif numero == 6:
    
        fleche = pygame.image.load("./fleches/fleche_droite_rose.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_droite_rose.png").convert_alpha()
        
    elif numero == 7:
    
        fleche = pygame.image.load("./fleches/fleche_haut_rose.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_haut_rose.png").convert_alpha()
        
    
    else :
    
        fleche = pygame.image.load("./fleches/fleche_gauche_rose.png").convert_alpha()
        fleche1 = pygame.image.load("./fleches/fleche_gauche_rose.png").convert_alpha()

    fenetre.blit(fleche, (50,200))
    fenetre.blit(fleche1, (800,200))
    

def evenement(numero_fleches, fenetre):
    
    continuer = True

    while continuer:
        
        for event in pygame.event.get():	#Attente des événements
        
            if event.type == QUIT:
                
                continuer = False
            
            elif event.type == KEYDOWN:
                    
                if event.key == K_DOWN: #Si "flèche bas"
                        
                    if numero_fleches == 1 or numero_fleches == 7:

                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()

                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                    fenetre.blit(result, (170,300))

                elif event.key == K_LEFT:

                    if numero_fleches == 4 or numero_fleches == 6:

                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()

                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                    fenetre.blit(result, (170,300))

                elif event.key == K_UP: 
                        
                    if numero_fleches == 3 or numero_fleches == 5:
                            
                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                            
                    else:
                            
                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                    fenetre.blit(result, (170,300))

                elif event.key == K_RIGHT:
                    
                    if numero_fleches == 2 or numero_fleches == 8:
                            
                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()

                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        
                    fenetre.blit(result, (170,300))
                
                elif event.key == K_s: #Si "flèche bas"
                        
                    if numero_fleches == 1 or numero_fleches == 7:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                    fenetre.blit(result1, (900,300))
                elif event.key == K_q:

                    if numero_fleches == 4 or numero_fleches == 6:

                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()

                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                    fenetre.blit(result1, (900,300))
                elif event.key == K_z: 
                        
                    if numero_fleches == 3 or numero_fleches == 5:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                            
                    else:
                            
                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        
                    fenetre.blit(result1, (900,300))
                elif event.key == K_d:
                    
                    if numero_fleches == 2 or numero_fleches == 8:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()

                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                
                    fenetre.blit(result1, (900,300))

                pygame.display.flip() #Rafraîchissement de l'écran
                pygame.time.wait(4000)
                
                main()
        
    pygame.quit()
         

def main():
        
    pygame.init() #Ouverture de la fenêtre Pygame

    fenetre = pygame.display.set_mode((2500, 1600))
        
    choix_fond(fenetre)
    pygame.display.flip() #Rafraîchissement de l'écran

    numero_fleches = random.randint(1,8)
    
    choix_fleches(numero_fleches, fenetre)
    pygame.display.flip() #Rafraîchissement de l'écran

    evenement(numero_fleches, fenetre)
    pygame.display.flip() #Rafraîchissement de l'écran
 
main()