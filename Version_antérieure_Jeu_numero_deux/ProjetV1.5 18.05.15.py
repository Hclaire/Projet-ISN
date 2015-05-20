# -*- coding: utf-8 -*-
"""
Projet jeu 1 affichage chiffre
"""

import pygame
import random
from pygame.locals import *

# def fenetre_d_accueil(fenetre):

# choix fond de couleur


def choix_fond_de_couleur(fenetre, abscisse, ordonnee):
    numero_fond = random.randint(1, 4)
    if numero_fond == 1:
        # Chargement et collage du fond
        fond = pygame.image.load("./fond/fondjaune.jpg").convert()

    elif numero_fond == 2:
        fond = pygame.image.load("./fond/fondbleu.jpg").convert()

    elif numero_fond == 3:
        fond = pygame.image.load("./fond/fondrose.jpg").convert()

    else:
        fond = pygame.image.load("./fond/fondrose2.jpg").convert()

    fenetre.blit(fond, (abscisse, ordonnee))
    # placement dans la fenetre avec coordonnées


# choix du nombre de gauche (nombre numero1)
def choix_nb_1(fenetre, abscisse, ordonnee):

    # choix chiffre hasard entre 0 et 9 inclus
    numero_nombre = random.randint(0, 9)

    if numero_nombre == 0:
        # Chargement et collage du numero
        numero1 = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()
        # convert_alpha pour image sur fond transparent
    elif numero_nombre == 1:
        numero1 = pygame.image.load("./chiffre/chiffre_1.png").convert_alpha()

    elif numero_nombre == 2:
        numero1 = pygame.image.load("./chiffre/chiffre_2.png").convert_alpha()

    elif numero_nombre == 3:
        numero1 = pygame.image.load("./chiffre/chiffre_3.png").convert_alpha()

    elif numero_nombre == 4:
        numero1 = pygame.image.load("./chiffre/chiffre_4.png").convert_alpha()

    elif numero_nombre == 5:
        numero1 = pygame.image.load("./chiffre/chiffre_5.png").convert_alpha()

    elif numero_nombre == 6:
        numero1 = pygame.image.load("./chiffre/chiffre_6.png").convert_alpha()

    elif numero_nombre == 7:
        numero1 = pygame.image.load("./chiffre/chiffre_7.png").convert_alpha()

    elif numero_nombre == 8:
        numero1 = pygame.image.load("./chiffre/chiffre_8.png").convert_alpha()

    else:
        numero1 = pygame.image.load("./chiffre/chiffre_9.png").convert_alpha()

    fenetre.blit(numero1, (abscisse, ordonnee))
    # placement dans la fenêtre avec coordonnées

    return numero_nombre  # correspond au chiffre de gauche


# choix du nombre numero 2
def choix_nb_2(fenetre, abscisse, ordonnee):

    # choix chiffre hasard entre 0 et 9 inclus
    numero_nombre2 = random.randint(0, 9)

    if numero_nombre2 == 0:
        numero2 = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()

    elif numero_nombre2 == 1:
        # Chargement et collage du numero
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

    fenetre.blit(numero2, (abscisse, ordonnee))
    # placement dans la fenêtre avec coordonnées

    return numero_nombre2  # correspond au chiffre de droite


def choix_des_signes_et_boutons(fenetre, abscisse_signe, ordonnee_signe, abscisse_egal, ordonnee_egal, abscisse_bouton, ordonnee_bouton):
    # choix chiffre hasard entre 1 et 2 inclus
    numero_signe = random.randint(1, 2)
    print(numero_signe)
    if numero_signe == 1:
        signe = pygame.image.load("./signe/signe_plus.png").convert_alpha()
    else:
        signe = pygame.image.load("./signe/signe_fois.png").convert_alpha()
    fenetre.blit(signe, (abscisse_signe, ordonnee_signe))

    sign_egal = pygame.image.load("./signe/signe_egal.png").convert_alpha()
    fenetre.blit(sign_egal, (abscisse_egal, ordonnee_egal))

    signe_correct = pygame.image.load("./Boutons/BoutonRightpasEnfonce.png").convert_alpha()
    signe_incorrect = pygame.image.load("./Boutons/BoutonWrongpasEnfonce.png").convert_alpha()
    fenetre.blit(signe_correct, (abscisse_bouton, ordonnee_bouton))
    # placement dans la fenêtre avec coordonnées
    fenetre.blit(signe_incorrect, (abscisse_bouton + 320, ordonnee_bouton))
    # placement dans la fenêtre avec coordonnées

    return numero_signe


def calcul_resultat(nb_1, nb_2, signe):
    print(signe)
    if signe == 1:
        result = nb_2 + nb_1
    else:
        result = nb_2 * nb_1
    print(result)
    return result  # resultat juste de l'opération soit nb1 + nb2 soit nb1*nb2


def decomposition_resultat(result, fenetre):
    # création d'une liste dans laquelle
    # on stockera la décomposition du nombre resultat_jeu
    liste_chiffre = []
    # resultat qu'on affiche est soit = vrai resultat +1 soit  vrai resultat -1
    # cela remplace les probabilités
    if result != 0:
        result_choix_un = result + 1
        result_choix_deux = result-1

    else:
        result_choix_un = result + 1
        result_choix_deux = result + 2

    choix_result = random.randint(1, 3)
    if choix_result == 1:
        resultat_jeu = result
    elif choix_result == 2:
        resultat_jeu = result_choix_un
    else:
        resultat_jeu = result_choix_deux

    resultat_jeu_nb = resultat_jeu
    # on fait cela pour récupérer resultat_jeu à la fin de la fonction
    resultat_jeu = str(resultat_jeu_nb)
    # transforme int en str *pour la boucle for*
    for chiffre in resultat_jeu:
        liste_chiffre.append(int(chiffre))  # transforme str en int
    print(liste_chiffre)

    return liste_chiffre, resultat_jeu_nb
    # = liste de décomposition // = resultat changé, celui qui sera affiché à l'écran


def affichage_resultat(liste_chiffre, fenetre, ordonnee, abscisse):

    for chiffre in liste_chiffre:

        # Chargement et collage du numero
        if chiffre == 0:
            chiffre_affich = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()

        elif chiffre == 1:

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

        fenetre.blit(chiffre_affich, (abscisse, ordonnee))
        # placement dans la fenêtre avec coordonnées
        abscisse += 125  # décalage pour affichage du deuxieme chiffre


def evenement(fenetre, resultat_jeu_nb, result,yninja, abscisse_right, ordonnee,abscisse_ninja):
    # BOUCLE INFINIE
    pygame.display.init()

    bon = False

<<<<<<< HEAD
    i = 0  # compteur
    son_correct = pygame.mixer.Sound("./Son_touches/Sonright.wav")
    son_incorrect = pygame.mixer.Sound("./Son_touches/sonwrong.wav")
    son_quit_ecran = pygame.mixer.Sound("./Son_touches/quitecran.wav")
    son_appuiebouton = pygame.mixer.Sound("./Son_touches/sonappuiebouton.wav")

=======
>>>>>>> origin/master
    continuer = True
    while continuer:


        for event in pygame.event.get():  #Attente des événements
            if event.type == QUIT:  # on quitte la partie par la croix
                son_quit_ecran.play()
                continuer = False
<<<<<<< HEAD
 
            if event.type == KEYDOWN and i < 1:
                # KEYDOWN => on appuie sur une touche et i < 1
                # ---- > on ne peut enfoncé qu'un seul bouton
                son_appuiebouton.play()
                if event.key == K_LEFT:  # appuie sur la touche fleche gauche
=======
            elif event.type == KEYDOWN : # KEYDOWN => on appuie sur une touche // i < 1 on ne peut enfoncé qu'un seul bouton
                if event.key == K_LEFT: # appuie sur la touche fleche gauche
                        #fenetre.blit(background, position, position) 
>>>>>>> origin/master
                    bouton_reponse = pygame.image.load("./Boutons/BoutonRightEnfonce.png").convert_alpha()
                    fenetre.blit(bouton_reponse, (abscisse_right, ordonnee))
                    # placement dans la fenêtre avec coordonnées
                    bouton_enfonce = 1
<<<<<<< HEAD
                elif event.key == K_RIGHT:
=======
            
                elif event.key == K_RIGHT :
>>>>>>> origin/master
                    bouton_reponse = pygame.image.load("./Boutons/BoutonWrongEnfonce.png").convert_alpha()
                    abscisse_wrong = abscisse_right + 320
                    fenetre.blit(bouton_reponse, (abscisse_wrong, ordonnee))
                    # placement dans la fenêtre avec coordonnées
                    bouton_enfonce = 2
<<<<<<< HEAD
                else:

                    bouton_enfonce = 3

                i += 1
                pygame.display.flip()    # Rafraîchissement de l'écran
=======
            
                else :
                
                    bouton_enfonce = 3 
                 
                pygame.display.flip()    #Rafraîchissement de l'écran
>>>>>>> origin/master

                if resultat_jeu_nb == result and bouton_enfonce == 1:
                    son_correct.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme,(abscisse_ninja, yninja))
                        pygame.display.flip()

                        if yninja == 480:
                            bon = False

                elif resultat_jeu_nb != result and bouton_enfonce == 2:
                    son_incorrect.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True

                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme, (abscisse_ninja, yninja))
                        pygame.display.flip()

                        if yninja == 480:
                            bon = False

                else:
                    son_incorrect.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageWrong.png").convert_alpha()
                    bon = True
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme,(abscisse_ninja, yninja))
                        pygame.display.flip()

                        if yninja == 480:
                            bon = False
<<<<<<< HEAD

    pygame.quit()
    return bouton_reponse, bouton_enfonce

=======
                main()
                
            pygame.display.flip()
            
            
    pygame.quit()
    return bouton_reponse, bouton_enfonce

                  
>>>>>>> origin/master

def main():
    pygame.init()
    pygame.display.init()
    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((1150, 700))
    fond = pygame.image.load("./fond/fond.png").convert()
    fenetre.blit(fond, (0, 0))

    abscisse1 = 71
    abscisse2 = 612
    ordonnee = 150
    choix_fond_de_couleur(fenetre, abscisse1, ordonnee)
    choix_fond_de_couleur(fenetre, abscisse2, ordonnee)

    abscisse_nb_gauche_cadre_gauche = 130
    abscisse_nb_gauche_cadre_droit = 650
    ordonnee_nb_gauche = 140
    nb_1_cadre_gauche = choix_nb_1(fenetre, abscisse_nb_gauche_cadre_gauche, ordonnee_nb_gauche)# nb de gauche
    nb_1_cadre_droit = choix_nb_1(fenetre, abscisse_nb_gauche_cadre_droit, ordonnee_nb_gauche)

    abscisse_nb_droit_cadre_gauche = 355
    abscisse_nb_droit_cadre_droit = 900
    ordonnee_nb_droit = 140
    nb_2_cadre_gauche = choix_nb_2(fenetre, abscisse_nb_droit_cadre_gauche, ordonnee_nb_droit)# nb de gauche
    nb_2_cadre_droit = choix_nb_2(fenetre, abscisse_nb_droit_cadre_droit, ordonnee_nb_droit)

    abscisse_signe_cadre_gauche = 237
    abscisse_signe_cadre_droit = 771
    ordonnee_signe = 140
    abscisse_egal_cadre_gauche = 45
    abscisse_egal_cadre_droit = 625
    ordonnee_egal = 275
    abscisse_bouton_cadre_gauche = 65
    abscisse_bouton_cadre_droit = 605
    ordonnee_bouton = 470
    signe_gauche = choix_des_signes_et_boutons(fenetre,abscisse_signe_cadre_gauche, ordonnee_signe,abscisse_egal_cadre_gauche, ordonnee_egal, abscisse_bouton_cadre_gauche, ordonnee_bouton)# le signe de l'opération
    signe_droit = choix_des_signes_et_boutons(fenetre,abscisse_signe_cadre_droit, ordonnee_signe,abscisse_egal_cadre_droit, ordonnee_egal, abscisse_bouton_cadre_droit, ordonnee_bouton)

    pygame.display.flip()
<<<<<<< HEAD

    result1 = calcul_resultat( nb_1_cadre_gauche,nb_2_cadre_gauche,signe_gauche)
    result2 = calcul_resultat( nb_1_cadre_droit,nb_2_cadre_droit,signe_droit)

    liste_chiffre1 , resultat_jeu_nb1 = decomposition_resultat(result1,fenetre)
    liste_chiffre2 , resultat_jeu_nb2 = decomposition_resultat(result2,fenetre)

    ordonnee_affich = 300
    abscisse_affiche_gauche = 200
    abscisse_affiche_droit = 750
    affichage_resultat(liste_chiffre1 , fenetre, ordonnee_affich,abscisse_affiche_gauche)
    affichage_resultat(liste_chiffre2 , fenetre, ordonnee_affich,abscisse_affiche_droit)

    yninja_cadre_gauche = 700
    yninja_cadre_droit = 700
    abscisse_ninja_gauche = 190
    abscisse_ninja_droit = 738
    bouton_reponse1, bouton_enfonce1 = evenement(fenetre, resultat_jeu_nb1, result1, yninja_cadre_gauche, abscisse_bouton_cadre_gauche, ordonnee_bouton,abscisse_ninja_gauche)
    bouton_reponse2, bouton_enfonce2 = evenement(fenetre, resultat_jeu_nb2, result2, yninja_cadre_droit, abscisse_bouton_cadre_droit, ordonnee_bouton,abscisse_ninja_droit)
    # Rafraîchissement de l'écran

    pygame.display.flip()

=======
    result = calcul_resultat( nb_1,nb_2,signe)
    liste_chiffre , resultat_jeu_nb = decomposition_resultat(result,fenetre)
    affichage_resultat (liste_chiffre , fenetre)
    bouton_reponse, bouton_enfonce = evenement(fenetre, resultat_jeu_nb, result)
    #Rafraîchissement de l'écran
    
    pygame.display.flip()        
>>>>>>> origin/master
main()
