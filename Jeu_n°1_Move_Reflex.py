"""

Jeu n°1 : 
L'utilisateur doit appuyer sur la flèche qui correspond à l'écran
si le fond de la flèche est bleu sinon il doit appuyer la flèche inverse.

"""
import pygame
import random
from pygame.locals import *

pygame.init() #Ouverture de la fenêtre Pygame

fenetre = pygame.display.set_mode((640, 480))

def choix_fond(numero):
    
    if numero == 1:
    
        fond = pygame.image.load("fondrouge.jpg").convert()

    elif numero == 2:
        fond = pygame.image.load("fondbleu.jpg").convert()

    elif numero == 3:
        fond = pygame.image.load("fondviolet.jpg").convert()

    else:
        fond = pygame.image.load("fondvert.jpg").convert()
        
    fenetre.blit (fond, (0,0))
    
def choix_fleches(numero):

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

    fleche.set_colorkey((250,250,250))
    fenetre.blit (fleche, (100,100))


def evenement (numero_fleches):
    
    continuer = 1
    
    while continuer:
        
        for event in pygame.event.get():
            #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
        
                continuer = 0  #On arrête la boucle
            elif event.type == KEYDOWN :    
                
                if numero_fleches == 1:
                
                    if event.key == K_DOWN: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))
        
                elif numero_fleches == 2:
        
                    if event.key == K_RIGHT: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))
        
                elif numero_fleches == 3:
        
                    if event.key == K_UP: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
            
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))
        
                elif numero_fleches == 4:
        
                    if event.key == K_LEFT: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
            
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))
        
                elif numero_fleches == 5:
        
                    if event.key == K_UP: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
            
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
                    
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))
        
                elif numero_fleches == 6:
        
                    if event.key == K_LEFT: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
            
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
                        
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))
            
                elif numero_fleches == 7:
        
                    if event.key == K_DOWN: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
            
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))
            
                elif numero_fleches == 8:
        
                    if event.key == K_RIGHT: 
            
                        result = pygame.image.load("correct.png").convert_alpha()
                        print("Gagné !")
            
                    else:
            
                        result = pygame.image.load("incorrect.png").convert_alpha()
                        print("Perdu !")
            
                    result.set_colorkey((250,250,250))
                    fenetre.blit (result, (120,100))

def main():
    
    numero_fond = random.randint(1,4)
    
    choix_fond(numero_fond)
    
    pygame.display.flip() #Rafraîchissement de l'écran

    numero_fleches = random.randint(1,8)
    
    choix_fleches(numero_fleches)
    
    pygame.display.flip() #Rafraîchissement de l'écran
    
    evenement(numero_fleches)
    
    pygame.display.flip() #Rafraîchissement de l'écran

 
main()