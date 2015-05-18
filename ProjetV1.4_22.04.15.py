# -*- coding: utf-8 -*-
"""
Projet jeu 1 affichage chiffre
"""

import pygame
import random
from pygame.locals import *

# def fenetre_d_accueil(fenetre):



# choix fond de couleur
def choix_fond_de_couleur(fenetre):
    numero_fond = random.randint(1,4)
    if numero_fond == 1:
        #Chargement et collage du fond
        fond = pygame.image.load("./fond/fondjaune.jpg").convert()

    elif numero_fond == 2:
        fond = pygame.image.load("./fond/fondbleu.jpg").convert()

    elif numero_fond == 3:
        fond = pygame.image.load("./fond/fondrose.jpg").convert()

    else:
        fond = pygame.image.load("./fond/fondrose2.jpg").convert()

    fenetre.blit(fond, (0,0))  # placement dans la fenetre avec coordonnées




# choix du nombre de gauche (nombre numero1)
def choix_nb_1 (fenetre):
    
    # choix chiffre hasard entre 0 et 9 inclus
    numero_nombre = random.randint(0,9)
    
    if numero_nombre == 0 :
        #Chargement et collage du numero
        numero1 = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()
        # convert_alpha pour image sur fond transparent         
    elif numero_nombre ==1 :
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
    
    fenetre.blit(numero1, (130,5))  # placement dans la fenêtre avec coordonnées
    return numero_nombre # correspond au chiffre de gauche




# choix du nombre numero 2
def choix_nb_2( fenetre):
    
    # choix chiffre hasard entre 0 et 9 inclus
    numero_nombre2 = random.randint(0,9)

    if numero_nombre2 == 0 :
        numero2 = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()
        
    elif numero_nombre2 == 1 :
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
        
    fenetre.blit(numero2, (370,5))#placement dans la fenêtre avec coordonnées
    return numero_nombre2 # correspond au chiffre de droite





def choix_des_signes_et_boutons(fenetre):
    # choix chiffre hasard entre 1 et 2 inclus
    numero_signe = random.randint(1,2)
    print(numero_signe)
    if numero_signe == 1:
        signe = pygame.image.load("./signe/signe_plus.png").convert_alpha()
    else:
        signe = pygame.image.load("./signe/signe_fois.png").convert_alpha()
    print(signe)
    fenetre.blit(signe, (250,20))
    
    sign_egal = pygame.image.load("./signe/signe_egal.png").convert_alpha()
    fenetre.blit(sign_egal,(100,150))

    signe_correct = pygame.image.load("./Boutons/BoutonRightpasEnfonce.png").convert_alpha()
    signe_incorrect = pygame.image.load("./Boutons/BoutonWrongpasEnfonce.png").convert_alpha()
    fenetre.blit(signe_correct,(10,300))#placement dans la fenêtre avec coordonnées
    fenetre.blit(signe_incorrect,(470,300))#placement dans la fenêtre avec coordonnées
    
    return numero_signe, signe_correct, signe_incorrect






def calcul_resultat(nb_1, nb_2, signe):
    print(signe)
    if signe == 1:
       result = nb_2 + nb_1
    else:
        result = nb_2 * nb_1
    print(result)
    return result  # resultat juste de l'opération soit nb1 + nb2 soit nb1*nb2
    





def decomposition_resultat(result,fenetre):
    # création d'une liste dans laquelle on stockera la décomposition du nombre resultat_jeu
    liste_chiffre = []
    # resultat qu'on affiche est soit = vrai resultat + 1 soit  vrai resultat - 1
    # cela remplace les probabilités
    result_plus_un = result + 1
    result_moins_un = result -1
    
    choix_result = random.randint(1,3)
    if choix_result == 1 :
        resultat_jeu = result
    elif choix_result == 2 :
        resultat_jeu = result_plus_un
    else :
        resultat_jeu = result_moins_un
    resultat_jeu_nb = resultat_jeu # on fait cela pour récupérer resultat_jeu à la fin de la fonction
    resultat_jeu = str(resultat_jeu_nb) # transforme int en str *pour la boucle for*
    for chiffre in resultat_jeu:
        liste_chiffre.append(int(chiffre))  # transforme str en int
    print(liste_chiffre)
    
    return liste_chiffre, resultat_jeu_nb  # = liste de décomposition // = resultat changé, celui qui sera affiché à l'écran






def affichage_resultat(liste_chiffre,fenetre):
    a = 200
    for chiffre in liste_chiffre:
    
        if chiffre == 0 :
            chiffre_affich = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()
            
        elif chiffre == 1 :
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
        
        
        fenetre.blit(chiffre_affich, (a,160))#placement dans la fenêtre avec coordonnées
        a += 125 # décalage pour affichage du deuxieme chiffre






def evenement(fenetre,resultat_jeu_nb, result):
    #BOUCLE INFINIE
    pygame.display.init()

    yninja = 590
    bon = False

    i = 0 # compteur
    continuer = True
    while continuer:
        
        for event in pygame.event.get():	#Attente des événements
            if event.type == QUIT:  # on quitte la partie par la croix
                continuer = False
            if event.type == KEYDOWN and i < 1: # KEYDOWN => on appuie sur une touche // i < 1 on ne peut enfoncé qu'un seul bouton
                if event.key == K_LEFT: # appuie sur la touche fleche gauche
                        #fenetre.blit(background, position, position) 
                    bouton_reponse = pygame.image.load("./Boutons/BoutonRightEnfonce.png").convert_alpha()
                    fenetre.blit(bouton_reponse,(10,300))#placement dans la fenêtre avec coordonnées
                    bouton_enfonce = 1
                elif event.key == K_RIGHT and i < 1:
                    bouton_reponse = pygame.image.load("./Boutons/BoutonWrongEnfonce.png").convert_alpha()
                    fenetre.blit(bouton_reponse,(470,300))#placement dans la fenêtre avec coordonnées
                    bouton_enfonce = 2
                else:
                
                    bouton_enfonce = 3 
                    
                i += 1 
                pygame.display.flip()    #Rafraîchissement de l'écran

                if resultat_jeu_nb == result and bouton_enfonce == 1:
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme,(250, yninja))
                        pygame.display.flip()
                        
                        if yninja == 400:
                            bon = False
              
                elif  resultat_jeu_nb != result and bouton_enfonce == 2:
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True
                    
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme,(250, yninja))
                        pygame.display.flip()
                        
                        if yninja == 400:
                            bon = False
                    
                else:
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageWrong.png").convert_alpha()
                    bon = True 
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme,(250, yninja))
                        pygame.display.flip()
                        
                        if yninja == 400:
                            bon = False
                
  



        pygame.display.flip()
    pygame.quit()
    return bouton_reponse, bouton_enfonce






"""
def verification_reponse(fenetre,resultat_jeu_nb, result,bouton_enfonce):

    if resultat_jeu_nb == result and bouton_enfonce == 1:
        affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()

    elif  resultat_jeu_nb != result and bouton_enfonce == 2:
        affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
        
    else:
        affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageWrong.png").convert_alpha()
    surface.blit(affichage_bonhomme,(150,150))

    pygame.display.flip() 

"""


    
def main():
    pygame.init()
    pygame.display.init() 
    #Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((640, 590))
 
    choix_fond_de_couleur(fenetre)
    nb_1 = choix_nb_1(fenetre)# nb de gauche
    nb_2 = choix_nb_2(fenetre)# nb de droite
    signe = choix_des_signes_et_boutons(fenetre)# le signe de l'opération
    pygame.display.flip()
    result = calcul_resultat( nb_1,nb_2,signe)
    liste_chiffre , resultat_jeu_nb = decomposition_resultat(result,fenetre)
    affichage_resultat (liste_chiffre , fenetre)
    bouton_reponse, bouton_enfonce = evenement(fenetre, resultat_jeu_nb, result)
    #verification_reponse(fenetre,resultat_jeu_nb, result,bouton_enfonce)

    #Rafraîchissement de l'écran
    pygame.display.flip()        

main()
