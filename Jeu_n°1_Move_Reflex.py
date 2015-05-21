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

pygame.init() #Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((1150, 700))  
fond_accueil = pygame.image.load("./fond/fond1.png").convert_alpha()
image_regle_jeu = pygame.image.load("./fond/reglejeu.png").convert_alpha()
fenetre.blit(fond_accueil, (0,0))
pygame.display.flip() #Rafraîchissement de l'écran
pygame.time.wait(4000)

i = 0
while i < 20:
    
    image_cliquez = pygame.image.load("./fond/image_clignote.png").convert_alpha()
    fenetre.blit(image_cliquez, (0,0))
    pygame.display.flip()

    image_regle_jeu = pygame.image.load("./fond/reglejeu.png").convert_alpha()
    fenetre.blit(image_regle_jeu, (0,0))
    pygame.display.flip()

    i += 1
               
def choix_fond(fenetre):

    fond_general = pygame.image.load("./fond/fond.png").convert_alpha()
    fond_J1 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
    fond_J2 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
    


    fenetre.blit(fond_general, (0,0))
    fenetre.blit (fond_J1, (0,200))
    fenetre.blit (fond_J2, (600,200))
    

def choix_fleches(numero, fenetre, abscisse, ordonnee):

    if numero == 1:
    
        fleche = pygame.image.load("./fleches/fleche_bas_bleu.png").convert_alpha()
    
    elif numero == 2:
    
        fleche = pygame.image.load("./fleches/fleche_droite_bleu.png").convert_alpha()
    
    elif numero == 3:
    
        fleche = pygame.image.load("./fleches/fleche_haut_bleu.png").convert_alpha()
    
    elif numero == 4:
    
        fleche = pygame.image.load("./fleches/fleche_gauche_bleu.png").convert_alpha()
    
    elif numero == 5:
    
        fleche = pygame.image.load("./fleches/fleche_bas_rose.png").convert_alpha()
    
    elif numero == 6:
    
        fleche = pygame.image.load("./fleches/fleche_droite_rose.png").convert_alpha()
        
    elif numero == 7:
    
        fleche = pygame.image.load("./fleches/fleche_haut_rose.png").convert_alpha()
        
    
    else :
    
        fleche = pygame.image.load("./fleches/fleche_gauche_rose.png").convert_alpha()

    fenetre.blit(fleche,(abscisse, ordonnee))

    
def evenement(numero_fleches_J1, numero_fleches_J2, fenetre):
    
    continuer = True
    son_correct = pygame.mixer.Sound("./Son_touches/son_correct.wav")
    son_incorrect = pygame.mixer.Sound("./Son_touches/son_incorrect.wav")
    while continuer:
        
        for event in pygame.event.get():    #Attente des événements
        
            if event.type == QUIT:
                
                continuer = False
            
            elif event.type == KEYDOWN :
                    
                if event.key == K_d: #Si "flèche bas"
                        
                    if numero_fleches_J1 == 1 or numero_fleches_J1 == 7:

                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                    fenetre.blit(result, (160,300))

                elif event.key == K_s:

                    if numero_fleches_J1 == 4 or numero_fleches_J1 == 6:

                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                    fenetre.blit(result, (160,300))

                elif event.key == K_e: 
                        
                    if numero_fleches_J1 == 3 or numero_fleches_J1 == 5:
                            
                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()                            
                    else:
                            
                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                    fenetre.blit(result, (160,300))

                elif event.key == K_f:
                    
                    if numero_fleches_J1 == 2 or numero_fleches_J1 == 8:
                            
                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()                        
                    fenetre.blit(result, (160,300))


                elif event.key == K_DOWN: #Si "flèche bas"
                        
                    if numero_fleches_J2 == 1 or numero_fleches_J2 == 7:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()                        
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                    fenetre.blit(result1, (750,300))
                    
                elif event.key == K_RIGHT:
                    
                    if numero_fleches_J2 == 2 or numero_fleches_J2 == 8:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                    fenetre.blit(result1, (750,300))
                    
                elif event.key == K_LEFT: 
                        
                    if numero_fleches_J2 == 4 or numero_fleches_J2 == 6:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()                        
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                    fenetre.blit(result1, (750,300))
                    
                elif event.key == K_UP:
                    
                    if numero_fleches_J2 == 3 or numero_fleches_J2 == 5:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                    fenetre.blit(result1, (750,300))
                   
                pygame.display.flip() #Rafraîchissement de l'écran
                pygame.time.wait(2000)
                abscisse_fleche_J1 = 0
                ordonnee_fleche_J1 = 200
    
                abscisse_fleche_J2 = 600
                ordonnee_fleche_J2 = 200

                choix_fond(fenetre)

                pygame.display.flip() #Rafraîchissement de l'écran

                numero_fleches_J1 = random.randint(1,8)
                numero_fleches_J2 = random.randint(1,8)
    
                choix_fleches(numero_fleches_J1, fenetre, abscisse_fleche_J1, ordonnee_fleche_J1)
                choix_fleches(numero_fleches_J2, fenetre,abscisse_fleche_J2, ordonnee_fleche_J2  )

                pygame.display.flip() #Rafraîchissement de l'écran

                evenement(numero_fleches_J1, numero_fleches_J2, fenetre)

                pygame.display.flip() #Rafraîchissement de l'écran
    
    pygame.quit()
    
def main():
    
    continuer = 1
    while continuer:
        for event in pygame.event.get():    #Attente des événements
            if event.type == QUIT:
                continuer = 0
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:    #Si clic gauche
                    abscisse_fleche_J1 = 0
                    ordonnee_fleche_J1 = 200
    
                    abscisse_fleche_J2 = 600
                    ordonnee_fleche_J2 = 200

                    choix_fond(fenetre)

                    pygame.display.flip() #Rafraîchissement de l'écran

                    numero_fleches_J1 = random.randint(1,8)
                    numero_fleches_J2 = random.randint(1,8)
    
                    choix_fleches(numero_fleches_J1, fenetre, abscisse_fleche_J1, ordonnee_fleche_J1)
                    choix_fleches(numero_fleches_J2, fenetre,abscisse_fleche_J2, ordonnee_fleche_J2  )

                    pygame.display.flip() #Rafraîchissement de l'écran

                    evenement(numero_fleches_J1, numero_fleches_J2, fenetre)

                    pygame.display.flip() #Rafraîchissement de l'écran
main()