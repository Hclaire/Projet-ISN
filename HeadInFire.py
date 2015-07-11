# -*- coding: utf-8 -*-
"""
Mini jeu numéro deux "Head In Fire"
du jeu "The Best KingReflex
"""

import pygame
import random
from pygame.locals import *
"""
choix fond de couleur 
+affichage dans l'écran

Paramètres
----------
fenetre :
abscisse : int     
         abscisse des sous fenêtres (cadre gauche et cadre droit)
ordonnée :int
         ordonnée des sous fenêtres (cadre gauche et cadre droit)

"""         
def choix_fond_de_couleur(fenetre, abscisse, ordonnee):
    # nombre aléatoire entre 1 et 4 inclus
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

    # placement dans la fenetre avec coordonnées
    fenetre.blit(fond, (abscisse, ordonnee))


"""
choix du nombre de gauche (nombre numero1)
+affichage dans l'écran

Paramètres
----------
fenetre :
abscisse : int     
         abscisse du nombre de gauche dans le cadre du joueur 1
         et dans celui du joueur 2
ordonnée :int
         ordonnée du nombre de gauche dans le cadre du joueur 1
         et dans celui du joueur 2
return
------
numero_nombre : int
        nombre choisi au hasard
"""   

def choix_nb_1(fenetre, abscisse, ordonnee):

    # choix chiffre hasard entre 0 et 9 inclus
    numero_nombre = random.randint(0, 9)

    if numero_nombre == 0:
        # Chargement et collage du numero
        # convert_alpha pour image sur fond transparent
        numero1 = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()

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

    # placement dans la fenêtre avec coordonnées
    fenetre.blit(numero1, (abscisse, ordonnee))


    return numero_nombre  # correspond au chiffre de gauche

"""
choix du nombre de gauche (nombre numero1) 
+affichage dans l'écran

Paramètres
----------
fenetre :
abscisse : int     
         abscisse du nombre de droite dans le cadre du joueur 1
         et dans celui du joueur 2
ordonnée :int
         ordonnée du nombre de droite dans le cadre du joueur 1
         et dans celui du joueur 2
return
------
numero_nombre2: int
        nombre choisi au hasard
"""   

# choix du nombre de droit (numero2)
def choix_nb_2(fenetre, abscisse, ordonnee):

    # choix chiffre hasard entre 0 et 9 inclus
    numero_nombre2 = random.randint(0, 9)

    # Chargement et collage du numero
    if numero_nombre2 == 0:
        numero2 = pygame.image.load("./chiffre/chiffre_0.png").convert_alpha()

    elif numero_nombre2 == 1:
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
        
    # placement dans la fenêtre avec coordonnées
    fenetre.blit(numero2, (abscisse, ordonnee))

    return numero_nombre2  # correspond au chiffre de droite

"""
choix des signes et boutons 
+affichage dans l'écran

Paramètres
----------
fenetre :
abscisse_signe : int     
         abscisses du nombre de droite dans le cadre du joueur 1
         et dans celui du joueur 2
         
ordonné_signe :int
         ordonnées du nombre de droite dans le cadre du joueur 1
         et dans celui du joueur 2
         
abscisse_egal:int
            abscisses des signes "égal" dans le cadre du joueur1
            et dans celui du joueur2
        
ordonnee_egal:int
            ordonnées des signes "égal" dans le cadre du joueur1
            et dans celui du joueur2
            
abscisse_bouton:int
             abscisses des boutons vrais/ faux dans les deux cadres
ordonnee_bouton:int
             abscisses des boutons vrais/ faux dans les deux cadres
             
return
------
numero_signe :int
            numero qui correspond au signe
"""   

def choix_des_signes_et_boutons(fenetre, abscisse_signe, ordonnee_signe, abscisse_egal, ordonnee_egal, abscisse_bouton, ordonnee_bouton):
    # choix chiffre hasard entre 1 et 2 inclus
    numero_signe = random.randint(1, 2)
    if numero_signe == 1:
        signe = pygame.image.load("./signe/signe_plus.png").convert_alpha()
    else:
        signe = pygame.image.load("./signe/signe_fois.png").convert_alpha()
    # abscisse_signe, ordonnée_signe donnée dans la fonction main
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

"""
calcul du resultat vrai

Paramètres
----------
fenetre :
nb_1 : int     
         nombre de gauche
nb_2 : int
         nombre de droite
return
------
result: int
        somme ou produit des deux nombres
"""   
def calcul_resultat(nb_1, nb_2, signe):
    if signe == 1:
        result = nb_2 + nb_1
    else:
        result = nb_2 * nb_1

    return result  # resultat juste de l'opération soit nb1 + nb2 soit nb1*nb2

"""
décomposition du résultat en une liste

paramètres
----------
result : int
         resultat du calcul précédent
fenetre : fenetre principale

return
------
liste_chiffre : list
            liste du résultat, décomposée

resultat_jeu_nb :int
             resultat changé, celui qui sera affiché à l'écran

"""
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

    return liste_chiffre, resultat_jeu_nb
    # = liste de décomposition // = resultat changé, celui qui sera affiché à l'écran

"""
affichage du résultat

paramètres
----------
liste_chiffre :list
            correspond à la liste du résultat décomposé
fenetre :fenetre principale
ordonnee : int
        ordonnée de l'affichage du resultat
abscisse : int 
        abscisse de l'affichage du resultat

"""
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

        # placement dans la fenêtre avec coordonnées
        fenetre.blit(chiffre_affich, (abscisse, ordonnee))

        abscisse += 125  # décalage pour affichage du deuxieme chiffre

"""
Fonction qui gère les évènements du clavier.
recupère les defaites du JOUEUR GAUCHE et du JOUEUR DROIT

Paramètres
----------
defaite_gauche: int
                variable qui compte le nombre de défaite du joueur J1

defaite_droite : int
                 variable qui compte le nombre de défaite du joueur J2
                 
resultat_jeu_nb_gauche : int
                    resultat affiché à l'écran qui a été récupéré précédemment
                    
resultat_jeu_nb_droit :int
                    resultat affiché à l'écran qui a été récupéré précédemment
                    
result_gauche :int
            (vrai)resultat de l'opération  cadre gauche
            
result_droit :int
            (vrai)resultat de l'opération cadre droit
            
yninja:int
        ordonnée du ninja
        
abscisse_bouton_cadre_gauche:int
                        abscisse du bouton vrai/faux cadre GAUCHE
                        
abscisse_bouton_cadre_droit:int
                        abscisse du bouton vrai/faux cadre DROIT
                        
ordonnee: int
        ordonnée du bouton vrai/faux
        
abscisse_ninja_gauche:int
                    abscisses du ninja qui s'affiche
                    dans le cadre GAUCHE
                    
abscisse_ninja_droit:int    
                    abscisses du ninja qui s'affiche
                    dans le cadre DROIT

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
def evenement(defaite_gauche,defaite_droite,fenetre, resultat_jeu_nb_gauche,resultat_jeu_nb_droit, result_gauche, result_droit ,yninja,abscisse_bouton_cadre_gauche,abscisse_bouton_cadre_droit, ordonnee,abscisse_ninja_gauche, abscisse_ninja_droit):

    pygame.display.init()

    bon = False


    compteur = 0  
    son_correct = pygame.mixer.Sound("./Son_touches/jeu_deux/son_rightJ2.wav")
    son_incorrect = pygame.mixer.Sound("./Son_touches/jeu_deux/son_wrongJ2.wav")
    son_quit_ecran = pygame.mixer.Sound("./Son_touches/jeu_deux/quitteecran.wav")
    son_appuiebouton = pygame.mixer.Sound("./Son_touches/jeu_deux/appuie_bouton.wav")
    
    # BOUCLE INFINIE
    continuer = True
    while continuer:

        

        for event in pygame.event.get():  #Attente des événements
            if event.type == QUIT:  # on quitte la partie par la croix
                son_quit_ecran.play()
                pygame.time.wait(500)
                continuer = False

          

            if event.type == KEYDOWN and compteur < 1:
                # KEYDOWN => on appuie sur une touche et compteur < 1
                # ---- > on ne peut enfoncé qu'un seul bouton par partie
                son_appuiebouton.play()
                if event.key == K_LEFT:  # appuie sur la touche fleche gauche (bouton vrai du joueur de droite)
                    bouton_reponse = pygame.image.load("./Boutons/BoutonRightEnfonce.png").convert_alpha()
                    fenetre.blit(bouton_reponse, (abscisse_bouton_cadre_droit, ordonnee))
                    bouton_enfonce = 1 # le bouton enfonce est vrai (joueur droite)
                    compteur +=1 # incrémente le compteur 
                elif event.key == K_s:  # appuie sur la touche S (bouton vrai du joueur de gauche)
                    bouton_reponse = pygame.image.load("./Boutons/BoutonRightEnfonce.png").convert_alpha()
                    fenetre.blit(bouton_reponse, (abscisse_bouton_cadre_gauche, ordonnee))
                    bouton_enfonce = 3 # le bouton enfonce est vrai (joueur de droite)
                    compteur +=1
                elif event.key == K_RIGHT:  # appuie sur la touche fleche droite (bouton faux du joueur de droite)
                    bouton_reponse = pygame.image.load("./Boutons/BoutonWrongEnfonce.png").convert_alpha()
                    # placement dans la fenêtre avec coordonnées
                    # 320 c'est la distance qui sépare bouton vrai du bouton faux
                    fenetre.blit(bouton_reponse, (abscisse_bouton_cadre_droit + 320, ordonnee))
                    bouton_enfonce = 2  # le bouton enfonce est faux (joueur gauche)
                    compteur +=1
                elif event.key == K_f:  # appuie sur la touche F (bouton faux du joueur de gauche
                    bouton_reponse = pygame.image.load("./Boutons/BoutonWrongEnfonce.png").convert_alpha()
                    fenetre.blit(bouton_reponse, (abscisse_bouton_cadre_gauche + 320, ordonnee))
                    # placement dans la fenêtre avec coordonnées
                    bouton_enfonce = 4  # le bouton enfonce est faux (Joueur de gauche) 
                    compteur+=1
                else:
                    bouton_enfonce = 5  # aucun des boutons proposés
                
               
              
                pygame.display.flip()    # Rafraîchissement de l'écran

                if (resultat_jeu_nb_gauche == result_gauche and bouton_enfonce == 3):
                    # si resultat affiché à l'écran est égal au (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur vrai. (POUR JOUEUR GAUCHE)
                    son_correct.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True # Booléen
                    
                    while bon:
                        yninja -= 1  # pour déplacer le ninja vers le haut
                        fenetre.blit(affichage_bonhomme,(abscisse_ninja_gauche, yninja))
                        pygame.display.flip()

                        if yninja == 480:  # s'il arrive à un ce nombre, alors le bonhomme s'arrête.
                            bon = False
                            
                elif (resultat_jeu_nb_gauche != result_gauche and bouton_enfonce == 4):
                    # si resultat affiché à l'écran est différent du (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur faux. (POUR JOUEUR GAUCHE)
                    son_correct.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True
                  
                    while bon:
                        yninja -= 1  # pour déplacer le ninja vers le haut 
                        fenetre.blit(affichage_bonhomme, (abscisse_ninja_gauche, yninja))
                        pygame.display.flip()

                        if yninja == 480:  # s'il arrive à un ce nombre, alors le bonhomme s'arrête.
                            bon = False


                elif (resultat_jeu_nb_gauche == result_gauche and bouton_enfonce == 4) or (resultat_jeu_nb_gauche != result_gauche and bouton_enfonce == 3) :
                    # si resultat affiché à l'écran est egal au (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur faux. (POUR JOUEUR GAUCHE)
                    # OU
                    # si resultat affiché à l'écran est différent du (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur vrai. (POUR JOUEUR GAUCHE)
                    son_incorrect.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageWrong.png").convert_alpha()
                    bon = True
                    
                    defaite_gauche += 1  # il perd une fois de plus car il s'est trompé (JOUEUR GAUCHE)
                    if defaite_gauche == 1:
                        flamme = pygame.image.load("./vie-flamme/flamme.png").convert_alpha()
                    elif defaite_gauche == 2:
                        flamme = pygame.image.load("./vie-flamme/flamme2.png").convert_alpha()
                    else:
                        flamme = pygame.image.load("./vie-flamme/flamme3.png").convert_alpha()
                    fenetre.blit(flamme,(65,50))
                    
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme, (abscisse_ninja_gauche, yninja))
                        pygame.display.flip()

                        if yninja == 480:  # s'il arrive à un ce nombre, alors le bonhomme s'arrête.
                            bon = False                    

                            
                elif (resultat_jeu_nb_droit == result_droit and bouton_enfonce == 1):
                    # si resultat affiché à l'écran est égal du (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur vrai. (POUR JOUEUR DROIT)
                    son_correct.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True
                      
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme,(abscisse_ninja_droit, yninja))
                        pygame.display.flip()

                        if yninja == 480:  # s'il arrive à un ce nombre, alors le bonhomme s'arrête.
                            bon = False
                            
                elif (resultat_jeu_nb_droit != result_droit and bouton_enfonce == 2):
                    # si resultat affiché à l'écran est différent du (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur vrai. (POUR JOUEUR DE DROITE)

                    son_correct.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageRight.png").convert_alpha()
                    bon = True
                           
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme, (abscisse_ninja_droit, yninja))
                        pygame.display.flip()

                        if yninja == 480:  # s'il arrive à un ce nombre, alors le bonhomme s'arrête.
                            bon = False

                elif (resultat_jeu_nb_droit != result_droit and bouton_enfonce == 1) or (resultat_jeu_nb_droit == result_droit and bouton_enfonce == 2):
                    # si resultat affiché à l'écran est différent au (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur faux. (POUR JOUEUR DE DROITE)
                    # OU
                    # si resultat affiché à l'écran est égal du (vrai)resultat de l'opération et que le joueur
                    # a appuyé sur vrai. (POUR JOUEUR DE DROITE)
                    son_incorrect.play()
                    affichage_bonhomme = pygame.image.load("./ImageBonhomme/imageWrong.png").convert_alpha()
                    bon = True

                    defaite_droite  += 1  # il perd une fois de plus car il s'est trompé (JOUEUR DE DROITE)
                    if defaite_droite == 1 :
                        flamme = pygame.image.load("./vie-flamme/flamme.png").convert_alpha()
                        fenetre.blit(flamme,(1015,50))                           
                    elif defaite_droite == 2:
                        flamme = pygame.image.load("./vie-flamme/flamme2.png").convert_alpha()
                        fenetre.blit(flamme,(950,50))                        
                    else:
                        flamme = pygame.image.load("./vie-flamme/flamme3.png").convert_alpha()
                        fenetre.blit(flamme,(885,50))
                    while bon:
                        yninja -= 1
                        fenetre.blit(affichage_bonhomme, (abscisse_ninja_droit, yninja))
                        pygame.display.flip()

                        if yninja == 480:  # s'il arrive à un ce nombre, alors le bonhomme s'arrête.
                            bon = False                            
                else :
                    print("vous vous êtes trompés de touche")
                pygame.display.flip()

         
                while (defaite_gauche < 3 and defaite_droite < 3):  # tant que l'un des deux n'a pas perdu
                    # on perd quand on a 3flammes)
                    # on relance le programme en gardant les variables "défaites" des parties précédentes
                    defaite_gauche, defaite_droite = main_02(defaite_gauche, defaite_droite)
        
    pygame.quit()
    return defaite_gauche, defaite_droite
"""
fonction principale
"""
def main_02(defaite_gauche,defaite_droite):
    pygame.init()  # initialiser la page
    pygame.display.init()   #initialise le module display
    # Ouverture de la fenêtre Pygame
    fenetre = pygame.display.set_mode((1150, 700))
    fond = pygame.image.load("./fond/fondjeux_deux.png").convert()
    fenetre.blit(fond, (0, 0))

    # abscisses et ordonnée des sous fenêtres (cadre gauche et cadre droit)
    # avec les différentes couleurs
    abscisse_gauche = 71
    abscisse_droite = 612
    ordonnee = 150
    choix_fond_de_couleur(fenetre, abscisse_gauche, ordonnee)
    choix_fond_de_couleur(fenetre, abscisse_droite, ordonnee)

    # abscisses et ordonnées du nombre de gauche dans le cadre du joueur 1
    # et dans celui du joueur 2
    abscisse_nb_gauche_cadre_gauche = 130
    abscisse_nb_gauche_cadre_droit = 650
    ordonnee_nb_gauche = 140
    nb_1_cadre_gauche = choix_nb_1(fenetre, abscisse_nb_gauche_cadre_gauche, ordonnee_nb_gauche)  # nb de gauche
    nb_1_cadre_droit = choix_nb_1(fenetre, abscisse_nb_gauche_cadre_droit, ordonnee_nb_gauche)

    # abscisses et ordonnées du nombre de droite dans le cadre du joueur 1
    # et dans celui du joueur 2
    abscisse_nb_droit_cadre_gauche = 355
    abscisse_nb_droit_cadre_droit = 900
    ordonnee_nb_droit = 140
    nb_2_cadre_gauche = choix_nb_2(fenetre, abscisse_nb_droit_cadre_gauche, ordonnee_nb_droit)  # nb de gauche
    nb_2_cadre_droit = choix_nb_2(fenetre, abscisse_nb_droit_cadre_droit, ordonnee_nb_droit)

    # abscisse et ordonnée des signes (opération, égal) dans le cadre du joueur1
    # et dans celui du joueur2
    # + abscisses et ordonnée des boutons vrais/ faux dans les deux cadres
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

    # (Vrai) résultats du cadre gauche et du cadre droit
    result_gauche = calcul_resultat( nb_1_cadre_gauche,nb_2_cadre_gauche,signe_gauche)
    result_droit = calcul_resultat( nb_1_cadre_droit,nb_2_cadre_droit,signe_droit)

    # = liste de décomposition des vrai resultats pour l'affichage (CADRE G et D)
    # = resultat changé, celui qui sera affiché à l'écran (CADRE G et D)
    liste_chiffre_gauche , resultat_jeu_nb_gauche = decomposition_resultat(result_gauche,fenetre)
    liste_chiffre_droit , resultat_jeu_nb_droit = decomposition_resultat(result_droit,fenetre)

    # abscisses et ordonnée du resultat affiché à l'écran (CADRE G et D)
    ordonnee_affich = 300
    abscisse_affiche_gauche = 200
    abscisse_affiche_droit = 750
    affichage_resultat(liste_chiffre_gauche , fenetre, ordonnee_affich,abscisse_affiche_gauche)
    affichage_resultat(liste_chiffre_droit , fenetre, ordonnee_affich,abscisse_affiche_droit)
    
    pygame.display.flip()

    # abscisses et ordonnée du ninja qui s'affiche
    # dans le cadre GAUCHE et DROIT
    yninja= 700
    abscisse_ninja_gauche = 190
    abscisse_ninja_droit = 738
    # recupère les defaites du JOUEUR GAUCHE et du JOUEUR DROIT
    defaite_gauche, defaite_droite = evenement(defaite_gauche,defaite_droite,fenetre, resultat_jeu_nb_gauche,resultat_jeu_nb_droit, result_gauche, result_droit ,yninja, abscisse_bouton_cadre_gauche,abscisse_bouton_cadre_droit, ordonnee_bouton,abscisse_ninja_gauche, abscisse_ninja_droit)
    pygame.display.flip()


#variables globales 
defaite_gauche = 0  
defaite_droite = 0
main_02(defaite_gauche, defaite_droite)  # appel de la fonction principale
