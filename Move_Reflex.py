# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:16:25 2015

@author: sansomasoundara
"""

"""

Jeu n°1 :
Le joueur doit appuyer sur la même direction de la flèche affichée à l'écran
si le fond de la flèche est bleue sinon si le fond est rouge, il doit appuyer sur la direction inverse.
J1 = Joueur n°1 / J2 = Joueur n°2.
J1 joue avec les lettres esdf.
J2 joue avec les flèches.

"""
import pygame
import random
from pygame.locals import *
#importation des modules pygame.
pygame.init()
pygame.display.init()
#Initialisation de la bibliothèque pygame.
fenetre = pygame.display.set_mode((1150, 700)) #Ouverture de la fenetre pygame avec la résolution 1500x700
defaite_gauche = 0
defaite_droite = 0

#Initialisation des variables defaites

fond_general = pygame.image.load("./fond/fond.png").convert_alpha() #Chargement du fond d'écran.
fond_J1 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
fond_J2 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
#Chargement des fonds de chaque joueur

fenetre.blit(fond_general, (0,0))
fenetre.blit (fond_J1, (0,200))
fenetre.blit (fond_J2, (600,200))
#Collage du fond d'écran + des fonds de chaque joueur.
pygame.display.flip() #Rafraichissement de l'écran

       
"""
Fonction qui choisit au hasard la flèche qui sera affichée à l'écran.

Paramètres
----------
numero : int
         numero tiré au hasard dans la fonction principale

fenetre : fenetre principale

abscisse : int
           abscisse des flèches données dans la fonction principale
ordonnée : int
           ordonnée des fèches données dans la foncion principale.
Retour
------
None

"""
def choix_fleches(numero, fenetre, abscisse, ordonnee):

    if numero == 1:#Si numero = 1 alors:
    
        fleche = pygame.image.load("./fleches/fleche_bas_bleu.png").convert_alpha() #Chargement de la flèche BAS fond BLEUE.
    
    elif numero == 2: #Si numero = 2 alors:
    
        fleche = pygame.image.load("./fleches/fleche_droite_bleu.png").convert_alpha()#Chargement de la flèche DROITE fond BLEUE.
    #Même principe pour la suite:
        
    elif numero == 3:
    
        fleche = pygame.image.load("./fleches/fleche_haut_bleu.png").convert_alpha()#HAUT BLEUE
    
    elif numero == 4:
    
        fleche = pygame.image.load("./fleches/fleche_gauche_bleu.png").convert_alpha()#GAUCHE BLEUE
    
    elif numero == 5:
    
        fleche = pygame.image.load("./fleches/fleche_bas_rose.png").convert_alpha()#BAS ROUGE
    
    elif numero == 6:
    
        fleche = pygame.image.load("./fleches/fleche_droite_rose.png").convert_alpha()#DROITE ROSE
        
    elif numero == 7:
    
        fleche = pygame.image.load("./fleches/fleche_haut_rose.png").convert_alpha()#HAUT ROUGE
        
    
    else :
    
        fleche = pygame.image.load("./fleches/fleche_gauche_rose.png").convert_alpha() #GAUCHE ROUGE

    fenetre.blit(fleche,(abscisse, ordonnee))
    #Collage de la flèche selon l'abscisse et l'ordonnée passé en argument

"""
Fonction gère les événements du clavier. 

Paramètres
----------
defaite_gauche: int
                variable qui compte le nombre de défaite du joueur J1

defaite_droite : int
                 variable qui compte le nombre de défaite du joueur J2
fenetre : fenetre principale

numero_fleches_J1 : int
                    numéro de la flèche du joueur J1 tiré au hasard dans la focntion choix_fleches()
numero_fleches_J2 : int
                    numéro de la flèche du joueur J2 tiré au hasard dans la focntion choix_fleches()
            
Retour
------
defaite_gauche: int
                variable qui compte le nombre de défaite du joueur J1

defaite_droite : int
                 variable qui compte le nombre de défaite du joueur J2

"""    
def evenement(defaite_gauche, defaite_droite, numero_fleches_J1, numero_fleches_J2, fenetre):
    
    continuer = True #on crée une variable booléenne 
    son_correct = pygame.mixer.Sound("./Son_touches/son_correct.wav") 
    son_incorrect = pygame.mixer.Sound("./Son_touches/son_incorrect.wav")
    son_quit_ecran = pygame.mixer.Sound("./Son_touches/jeu_deux/quitteecran.wav")
    #Chargement des sons correct/incorrect + le son pour quitter l'écran.
    
    image_perdu = pygame.image.load("./fond/fond_panneau_perdu.png").convert_alpha()
    image_gagne = pygame.image.load("./fond/fond_panneau_gagne.png").convert_alpha()
    faux = pygame.image.load("./correct-incorrect/incorrect.png").convert_alpha()
    vrai = pygame.image.load("./correct-incorrect/correct.png").convert_alpha()
    fond_J1 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
    fond_J2 = pygame.image.load("./fond/fond_panneau.png").convert_alpha()
    #Chargement de toutes les images avant collage
    while continuer: #Tant que continuer est vrai, boucle infinie 
        
        for event in pygame.event.get():    #Attente des évènements
        
            if event.type == QUIT: #Si le joueur clique sur la croix pour fermer alors:
                son_quit_ecran.play()#On ajoute le son quitter écran à cet évenement.
                pygame.time.wait(500)#Attente de 0.5 sec
                continuer = False #On arrête le jeu et la boucle.
            
            elif event.type == KEYDOWN : #Si on appuie sur une touche du clavier alors:
                    
                if event.key == K_d: #Si le J1 appuie sur la flèche du bas alors :
                        
                    if numero_fleches_J1 == 1 or numero_fleches_J1 == 7: #Et si le numero de la flèche du J1 correspond à une flèche du bas fond bleu (n°1) ou flèche du haut fond rouge (n°7)

                        k_J1 = 1 #Dans ce cas J1 gagne, donc on initialise la variable k_J1 à 1 car J1 a gagné.  
                    else: #Sinon si le numero de la flèche du J1 ne correspond pas aux flèches qui lui sont attribués alors:
                        k_J1 = 0 #Dans ce cas J1 perd, donc on initialise la variable k_J1 à 0 car J1 a perdu.
                    
                elif event.key == K_s:#Même principe avec J1 appuyant sur flèche gauche.

                    if numero_fleches_J1 == 4 or numero_fleches_J1 == 6:

                        k_J1 = 1
            
                    else:
    
                        k_J1 = 0
                   

                elif event.key == K_e: #Même principe avec J1 appuyant sur flèche haut.
                        
                    if numero_fleches_J1 == 3 or numero_fleches_J1 == 5:
    
                        k_J1 = 1
                    else:
                        
                        k_J1 = 0

                elif event.key == K_f: #Même principe avec J1 appuyant sur flèche droite.
                    
                    if numero_fleches_J1 == 2 or numero_fleches_J1 == 8:

                        k_J1 = 1
                        
                    else: 
                   
                        k_J1 = 0
                else : #Condition sinon pour sortir de la boucle évenement du J1.
                    k_J1 = 3  #Fin du traitement des évenements du J1.

                if event.key == K_DOWN: #Début traitement évenements J2, si J2 appuie sur la flèche du bas alors : 
                        
                    if numero_fleches_J2 == 1 or numero_fleches_J2 == 7: #Et si le numero de la flèche du J2 correspond à une flèche du bas fond bleu (n°1) ou flèche du haut fond rouge (n°7)
                        
                        k_J2 = 1 #Dans ce cas J2 gagne, donc on initialise la variable k_J2 à 1 car J2 a gagné.  
                    else: #Sinon si le numero de la flèche du J2 ne correspond pas aux flèches qui lui sont attribués alors:

                        k_J2 = 0 #Dans ce cas J2 perd, donc on initialise la variable k_J2 à 0 car J2 a perdu.
                    
                elif event.key == K_RIGHT: #Même principe avec J2 appuyant sur la flèche droite.
                    
                    if numero_fleches_J2 == 2 or numero_fleches_J2 == 8:
                            
                        k_J2 = 1
                    else:

                        k_J2 = 0
                    
                elif event.key == K_LEFT: #Même principe avec J2 appuyant sur la flèche gauche.
                        
                    if numero_fleches_J2 == 4 or numero_fleches_J2 == 6:

                        k_J2 = 1
                    else:

                        k_J2 = 0
                
                elif event.key == K_UP:#Même principe avec J2 appuyant sur la flèche du haut.
                    
                    if numero_fleches_J2 == 3 or numero_fleches_J2 == 5:

                        k_J2 = 1
                    else:

                        k_J2 = 0
                else: #Condition sinon pour sortir de la boucle évenement du J2.
                    k_J2 = 3 #Fin du traitement des évenements du J2.

                if k_J1==1 : 
                    k_J2 = 0
                elif k_J1 == 0:
                    k_J2 = 1
                elif k_J2 == 1:
                    k_J1 = 0
                else:
                    k_J1 = 1
                #Ensemble de conditions pour que lorsque l'un des joueurs gagne, l'autre perd automatiquement le tour joué.

                if k_J1 == 1 and k_J2 ==0: #Si la condition J1 a gagné et que J2 a perdu le tour est vérifiée alors :
                    fenetre.blit(vrai, (160,300)) #Collage de l'image signe correct sur l'écran du J1.

                    pygame.time.wait(1000)#On attend 2secondes avant de continuer.
                    pygame.display.flip() #Rafraîchissement de l'écran.
                    son_correct.play() #On ajoute le son correct à cet évenement.

                    fenetre.blit(faux, (750,300)) #Collage de l'image signe incorrect sur l'écrand du J2.
                    pygame.time.wait(100)#On attend 2secondes avant de continuer.
                    pygame.display.flip() #Rafraîchissement de l'écran.
                    son_incorrect.play()#On ajoute le son incorrect à cet évenement.
                    defaite_droite += 1 #J2 a perdu donc on incrémente 1 à la variable défaite de J2.
                    
                    if defaite_droite == 1: #Condition si J2 a déjà eu 1 défaite dans les autres tours alors:
                        deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha() 
                        fenetre.blit (deux_vies, (600,200))
                        #Chargement et collage de l'image à 2 vies car on enlève une vie à J2.

                        if defaite_gauche == 1: #Condition si J1 a  lui aussi déjà eu 1 défaite dans les autres tours alors:
                            deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha() 
                            fenetre.blit (deux_vies, (0,200))
                            #Chargement et collage de l'image à 2 vies car on enlève une vie à J1.
                        elif defaite_gauche == 2: #Condition si J1 a déjà eu 2 défaites dans les autres tours alors:
                            une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                            fenetre.blit(une_vie, (0,200))
                            #Chargement et collage de l'image à 1 vie car on enlève une autre vie à J1.
                        elif defaite_gauche == 0:
                            fenetre.blit(fond_J1, (0,200))
                            #Collage de l'image à 3 vies si J1 n'a jamais perdu dans les tours précédents.

                        else: #Sinon si J1 a déjà accumulé 3 défaites dans les tours précédents alors:
                            fenetre.blit(image_perdu, (0,200))#Collage de l'image perdu dans l'écrand du J1.
                            fenetre.blit(image_gagne, (600, 200))#Collage de l'image gagné dans l'écrand du J2.
            
                    elif defaite_droite == 2:#Condition si J2 a déjà eu 2 défaites dans les autres tours alors:
                        une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                        fenetre.blit(une_vie,(600,200))
                        #Chargement et collage de l'image à 1 vie car on enlève une autre vie à J2.

                        if defaite_gauche == 1: 
                            deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha()
                            fenetre.blit (deux_vies, (0,200))
                        elif defaite_gauche == 2:
                            une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                            fenetre.blit(une_vie, (0,200))
                        elif defaite_gauche == 0:
                            fenetre.blit(fond_J1, (0,200))

                        else:
                            fenetre.blit(image_perdu, (0,200))
                            fenetre.blit(image_gagne, (600, 200))
                        #Même vérification que précedemment pour la situation de J1.
                    else:  #Sinon si J2 a déjà accumulé 3 défaites dans les tours précédents alors:
                        
                        fenetre.blit(image_gagne, (0, 200))#Collage de l'image perdu dans l'écrand du J2.
                        fenetre.blit(image_perdu, (600,200))#Collage de l'image gagné dans l'écrand du J1.
                        
                    pygame.display.flip()#Rafraîchissement de l'écran
                    pygame.time.wait(500)#Attente de 1sec
                
                else : #Si la condition J2 a gagné et que J1 a perdu le tour est vérifiée alors :
                    fenetre.blit(vrai, (750,300)) #Collage de l'image signe correct sur l'écran du J2.
                    pygame.time.wait(1000)#On attend 2secondes avant de continuer.
                    pygame.display.flip() #Rafraîchissement de l'écran.
                    son_correct.play() #On ajoute le son correct à cet évenement.

                    fenetre.blit(faux, (160,300)) #Collage de l'image signe incorrect sur l'écran du J2.
                    pygame.time.wait(100)#On attend 2secondes avant de continuer.
                    pygame.display.flip() #Rafraîchissement de l'écran.
                    son_incorrect.play()#On ajoute le son incorrect à cet évenement.

                    defaite_gauche += 1 #J1 a perdu donc on incrémente 1 à la variable défaite de J1.
                    
                    #Suite: même principe que les condictions au-dessus.
                    if defaite_gauche == 1:
                        deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha()
                        fenetre.blit (deux_vies, (0,200))
                        if defaite_droite == 1:
                            deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha()
                            fenetre.blit (deux_vies, (600,200))
                        elif defaite_droite == 2:
                            une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                            fenetre.blit(une_vie,(600,200))
                        elif defaite_droite == 0 :
                            fenetre.blit(fond_J2,(600,200))
                        else:
                            fenetre.blit(image_perdu, (600,200))
                            fenetre.blit(image_gagne, (0, 200))
                        pygame.display.flip()
                        pygame.time.wait(500)
                        
                    elif defaite_gauche == 2:
                        une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                        fenetre.blit(une_vie, (0,200))
                        if defaite_droite == 1:
                            deux_vies = pygame.image.load("./fond/fond_panneau_2vies.png").convert_alpha()
                            fenetre.blit (deux_vies, (600,200))
                        elif defaite_droite == 2:
                            une_vie = pygame.image.load("./fond/fond_panneau_1vie.png").convert_alpha()
                            fenetre.blit(une_vie,(600,200))
                        elif defaite_droite == 0 :
                            fenetre.blit(fond_J2,(600,200))
                        else:
                            fenetre.blit(image_perdu, (600,200))
                            fenetre.blit(image_gagne, (0, 200))
                        pygame.display.flip()
                        pygame.time.wait(500)
                        
                    else:
                        fenetre.blit(image_perdu, (0,200))
                        fenetre.blit(image_gagne, (600, 200))

                    pygame.display.flip()
                    pygame.time.wait(500)
                    pygame.display.flip()
                    
                while (defaite_gauche<3 and defaite_droite<3): #Tant que les féfaites de chacun des joueurs sont strcitement inférieures à 3 alors:
                    
                    defaite_gauche, defaite_droite = main_01(defaite_gauche, defaite_droite)# On continue de répeter tout le jeu et donc on appelle la fonction principale.
                
                pygame.display.flip()
    pygame.quit()#Rafraîchissement de l'écran.
    return defaite_gauche, defaite_droite #La fonction principale retourne le comptage des défaites de chaque joueur.
"""
Fonction principale qui execute toutes les autres fonctions.

Paramètres
----------
defaite_gauche: int
                variable qui compte le nombre de défaite du joueur J1

defaite_droite : int
                 variable qui compte le nombre de défaite du joueur J2
            
Retour
------
None

"""    

def main_01(defaite_gauche, defaite_droite): #Fonction principale.
    

    abscisse_fleche_J1 = 0 
    ordonnee_fleche_J1 = 200
    
    abscisse_fleche_J2 = 600
    ordonnee_fleche_J2 = 200

    #Initialisation de chaque abscisse/ordonnée de chaque flèche des joueurs.

    numero_fleches_J1 = random.randint(1,8)
    numero_fleches_J2 = random.randint(1,8)
    #Initialisation des nombres tirés au hasard pour choisir une flèche au hasard pour chaque joueur.
    
    choix_fleches(numero_fleches_J1, fenetre, abscisse_fleche_J1, ordonnee_fleche_J1)
    choix_fleches(numero_fleches_J2, fenetre,abscisse_fleche_J2, ordonnee_fleche_J2)
    #Appel des fonctions choix_fleches pour choisir une flèche au hasard pour chaque joueur.

    pygame.display.flip() #Rafraîchissement de l'écran

    defaite_gauche, defaite_droite = evenement(defaite_gauche, defaite_droite, numero_fleches_J1, numero_fleches_J2, fenetre)
    #Appel de la fonction evenement et affectation des variables défaites pour compter le nombre de défaites dans chaque tour
    
    pygame.display.flip() #Rafraichissement de l'écran
main_01(defaite_gauche, defaite_droite) #Appel de la fonction main()
