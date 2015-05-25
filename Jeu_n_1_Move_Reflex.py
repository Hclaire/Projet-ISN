# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:16:25 2015

@author: sansomasoundara
"""

"""

Jeu n掳1 : 
L'utilisateur doit appuyer sur la fl猫che qui correspond 脿 l'茅cran
si le fond de la fl猫che est bleu sinon il doit appuyer la fl猫che inverse.

"""
import pygame
import random
from pygame.locals import *

pygame.init() #Ouverture de la fen锚tre Pygame

fenetre = pygame.display.set_mode((1150, 700))  
defaite_gauche = 0
defaite_droite = 0
fond_accueil = pygame.image.load("./fond/fond1.png").convert_alpha()
image_regle_jeu = pygame.image.load("./fond/reglejeu.png").convert_alpha()
fenetre.blit(fond_accueil, (0,0))
pygame.display.flip() #Rafra卯chissement de l'茅cran
pygame.time.wait(4000)
fond_general = pygame.image.load("./fond/fond.png").convert_alpha()
fond_J1 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
fond_J2 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
    


fenetre.blit(fond_general, (0,0))
fenetre.blit (fond_J1, (0,200))
fenetre.blit (fond_J2, (600,200))

pygame.display.flip() #Rafra卯chissement de l'茅cran


"""
i = 0
while i < 50:
    
    image_cliquez = pygame.image.load("./fond/image_clignote.png").convert_alpha()
    fenetre.blit(image_cliquez, (0,0))
    pygame.display.flip()

    image_regle_jeu = pygame.image.load("./fond/reglejeu.png").convert_alpha()
    fenetre.blit(image_regle_jeu, (0,0))
    pygame.display.flip()
    pygame.time.wait(4000)
    
    i += 1
    
"""            

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

    
def evenement(defaite_gauche, defaite_droite, numero_fleches_J1, numero_fleches_J2, fenetre):
    
    continuer = True
    son_correct = pygame.mixer.Sound("./Son_touches/son_correct.wav")
    son_incorrect = pygame.mixer.Sound("./Son_touches/son_incorrect.wav")
    compteur = 0
    
    image_perdu = pygame.image.load("./fond/fond_panneau_perdu.png").convert_alpha()
    image_gagne = pygame.image.load("./fond/fond_panneau_gagne.png").convert_alpha()
    while continuer:
        
        for event in pygame.event.get():    #Attente des 茅v茅nements
        
            if event.type == QUIT:
                
                continuer = False
            
            elif event.type == KEYDOWN and compteur < 1 :
                    
                if event.key == K_d: #Si "fl猫che bas"
                        
                    if numero_fleches_J1 == 1 or numero_fleches_J1 == 7:

                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                        k_J1 = 1
                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                        k_J1 = 0
                    compteur +=1

                    fenetre.blit(result, (160,300))
                    

                elif event.key == K_s:

                    if numero_fleches_J1 == 4 or numero_fleches_J1 == 6:

                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                        k_J1 = 1
            
                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                        k_J1 = 0
                    compteur +=1
                    fenetre.blit(result, (160,300))

                elif event.key == K_e: 
                        
                    if numero_fleches_J1 == 3 or numero_fleches_J1 == 5:
                            
                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()       
                        k_J1 = 1
                    else:
                            
                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                        k_J1 = 0
                    fenetre.blit(result, (160,300))

                elif event.key == K_f:
                    
                    if numero_fleches_J1 == 2 or numero_fleches_J1 == 8:
                            
                        result = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                        k_J1 = 1
                    else:

                        result = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()                   
                        k_J1 = 0
                    compteur +=1
                    fenetre.blit(result, (160,300))
                else:
                    k_J1 = 3

                pygame.display.flip()
                if k_J1 == 0:
                    defaite_gauche += 1
                    if defaite_gauche == 1:
                        deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha()

                        fenetre.blit (deux_vies, (0,200))
                    elif defaite_gauche == 2:
                        une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                        fenetre.blit(une_vie,(0,200))
                    else:
                        
                        fenetre.blit(image_perdu,(0,200))
                    pygame.display.flip()
                    pygame.time.wait(2000)

                if event.key == K_DOWN: #Si "fl猫che bas"
                        
                    if numero_fleches_J2 == 1 or numero_fleches_J2 == 7:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()  
                        k_J2 = 1
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                        k_J2 = 0
                    compteur +=1
                    fenetre.blit(result1, (750,300))
                    
                elif event.key == K_RIGHT:
                    
                    if numero_fleches_J2 == 2 or numero_fleches_J2 == 8:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                        k_J2 = 1
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                        k_J2 = 0
                    compteur +=1
                    fenetre.blit(result1, (750,300))
                    
                elif event.key == K_LEFT: 
                        
                    if numero_fleches_J2 == 4 or numero_fleches_J2 == 6:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play() 
                        k_J2 = 1
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                        k_J2 = 0
                    compteur +=1
                    fenetre.blit(result1, (750,300))
                    
                elif event.key == K_UP:
                    
                    if numero_fleches_J2 == 3 or numero_fleches_J2 == 5:
                            
                        result1 = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
                        son_correct.play()
                        k_J2 = 1
                    else:

                        result1 = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
                        son_incorrect.play()
                        k_J2 = 0
                    compteur +=1
                    fenetre.blit(result1, (750,300))
                else :
                    k_J2 = 3
    
 
                if k_J2 == 0 :
                    
                    defaite_droite += 1
                    if defaite_droite == 1:
                        deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha()
                        fenetre.blit (deux_vies, (600,200))
                    elif defaite_droite == 2:
                        une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                        fenetre.blit(une_vie,(600,200))
                    else:
                        fenetre.blit(image_perdu,(600,200))
                        
                pygame.display.flip()
                pygame.time.wait(2000)
                
         
                while (defaite_gauche<4 or defaite_droite<4):
                    defaite_gauche, defaite_droite = main_01(defaite_gauche, defaite_droite)
                
    
    pygame.quit()
    return defaite_gauche, defaite_droite
def main_01(defaite_gauche, defaite_droite):
    

    abscisse_fleche_J1 = 0
    ordonnee_fleche_J1 = 200
    
    abscisse_fleche_J2 = 600
    ordonnee_fleche_J2 = 200


    numero_fleches_J1 = random.randint(1,8)
    numero_fleches_J2 = random.randint(1,8)
    
    choix_fleches(numero_fleches_J1, fenetre, abscisse_fleche_J1, ordonnee_fleche_J1)
    choix_fleches(numero_fleches_J2, fenetre,abscisse_fleche_J2, ordonnee_fleche_J2  )

    pygame.display.flip() #Rafra卯chissement de l'茅cran

    defaite_gauche, defaite_droite = evenement(defaite_gauche, defaite_droite, numero_fleches_J1, numero_fleches_J2, fenetre)

    pygame.display.flip() #Rafra卯chissement de l'茅cran
main_01(defaite_gauche, defaite_droite)
