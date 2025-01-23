"""
Auteurs : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON
Date : 21/01/2025 15h53
But du programme :
    Créer un jeu de pendu en utilisant l'interface graphique PyGame
Entrée :
Sortie :
"""

import pygame
from pygame.locals import *
import sys
import random

# Initialisation de Pygame
pygame.init()
pygame.font.init()

# Dimensions de la fenêtre (classe)
LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Pendu - Edition spéciale Jinx")

police = pygame.font.SysFont('Roboto', 35)
police_survol = pygame.font.SysFont('Roboto', 35, True)

# Couleurs
NOIR = (0, 0, 0)
GRIS = (127, 127, 127)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Horloge
FPS = pygame.time.Clock()

# AFFICHAGE DES OBJETS #

# Ajouter une image de fond
fond_ecran = pygame.image.load("image/fond_ecran.jpg")
fond_ecran = pygame.transform.scale(fond_ecran, (LARGEUR, HAUTEUR))

# Base
potence_base = pygame.image.load("image/acier2.jpg")
potence_base = pygame.transform.scale(potence_base, (200, 20))

# Poteau vertical
potence_verticale = pygame.image.load("image/acier2.jpg")
potence_verticale = pygame.transform.scale(potence_verticale, (20, 400))

# Poteau horizontal
potence_horizontale = pygame.image.load("image/acier2.jpg")
potence_horizontale = pygame.transform.scale(potence_horizontale, (200, 20))

# Corde
corde1 = pygame.image.load("image/corde.png")
corde1 = pygame.transform.scale(corde1, (50, 90))

corde2 = pygame.image.load("image/corde2.png")
corde2 = pygame.transform.scale(corde2, (50, 90))

# Jinx
jinx_tete = pygame.image.load("image/jinx_head.webp")
jinx_tete = pygame.transform.scale(jinx_tete, (353 / 4, 1276 / 4))

jinx_corps = pygame.image.load("image/jinx_body.webp")
jinx_corps = pygame.transform.scale(jinx_corps, (353 / 4, 1276 / 4))

jinx_bras_droit = pygame.image.load("image/jinx_right_arm.webp")
jinx_bras_droit = pygame.transform.scale(jinx_bras_droit, (353 / 4, 1276 / 4))

jinx_bras_gauche = pygame.image.load("image/jinx_left_arm.webp")
jinx_bras_gauche = pygame.transform.scale(jinx_bras_gauche, (353 / 4, 1276 / 4))

jinx_jambe_droite = pygame.image.load("image/jinx_right_leg.webp")
jinx_jambe_droite = pygame.transform.scale(jinx_jambe_droite, (353 / 4, 1276 / 4))

jinx_jambe_gauche = pygame.image.load("image/jinx_left_leg.webp")
jinx_jambe_gauche = pygame.transform.scale(jinx_jambe_gauche, (353 / 4, 1276 / 4))


# Dessiner la potence
def dessine_potence(tour, difficulte):
    if difficulte == "facile":
        if tour > 0:
            fenetre.blit(potence_base, (260, 430))
        if tour > 1:
            fenetre.blit(potence_verticale, (350, 30))
        if tour > 2:
            fenetre.blit(potence_horizontale, (370, 30))
        if tour > 3:
            fenetre.blit(corde1, (500, 30))
            fenetre.blit(potence_horizontale, (370, 30))
            
    elif difficulte == "moyen" or difficulte == "difficile":
        if tour > 0:
            fenetre.blit(potence_base, (260, 430))
            fenetre.blit(potence_verticale, (350, 30))
            fenetre.blit(corde1, (500, 30))
            fenetre.blit(potence_horizontale, (370, 30))


# Dessiner Jinx
def dessine_jinx(tour, difficulte):
    if difficulte == "facile":
        if tour > 4:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 5:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 6:  # Bras gauche
            fenetre.blit(jinx_bras_droit, (480, 70))
        if tour > 7:  # Bras droit
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 8:  # Jambe gauche
            fenetre.blit(jinx_jambe_droite, (480, 70))
        if tour > 9:  # Jambe droite
            fenetre.blit(jinx_jambe_gauche, (480, 70))
            
    elif difficulte == "moyen":
        if tour > 1:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 2:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 3:  # Bras gauche
            fenetre.blit(jinx_bras_droit, (480, 70))
        if tour > 4:  # Bras droit
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 5:  # Jambe gauche
            fenetre.blit(jinx_jambe_droite, (480, 70))
        if tour > 6:  # Jambe droite
            fenetre.blit(jinx_jambe_gauche, (480, 70))
            
    elif difficulte == "difficile":
        if tour > 1:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 2:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 3:  # Bras
            fenetre.blit(jinx_bras_droit, (480, 70))
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 4:  # Jambes
            fenetre.blit(jinx_jambe_droite, (480, 70))
            fenetre.blit(jinx_jambe_gauche, (480, 70))

            
# Dessiner les lettres
def affiche_texte(mot, devine):
    affiche_mot = " ".join([lettre if lettre in devine else "_" for lettre in mot])
    texte = police.render(affiche_mot, True, BLANC)
    fenetre.blit(texte, (300, 650))
   
# Dessiner les boutons
def bouton_jouer():  
    # Détecte la postion de la souris en tuple [x, y]
    souris = pygame.mouse.get_pos()
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))
       
    if bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 - 40 <= souris[1] <= bouton_largeur/2 + 20: 
        jouer = fenetre.blit(bouton, (800, 60))
        jouer = police_survol.render('jouer' , True , BLANC)
        fenetre.blit(jouer, (850, 70)) 
    else: 
        jouer = fenetre.blit(bouton, (800, 60))        
        jouer = police.render('jouer' , True , NOIR)
        fenetre.blit(jouer, (850, 70))

def bouton_arreter():
    # Détecte la postion de la souris en tuple [x, y]
    souris = pygame.mouse.get_pos()
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur)) 
    
    if bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 + 60 <= souris[1] <= bouton_largeur/2 + 100:
        arreter = fenetre.blit(bouton, (800, 140))
        arreter = police_survol.render("arrêter", True, BLANC)
        fenetre.blit(arreter, (845, 150)) 
    else:
        arreter = fenetre.blit(bouton, (800, 140))
        arreter = police.render("arrêter", True, NOIR)
        fenetre.blit(arreter, (845, 150)) 

fichier_mots = "mots.txt"

def verifie_fin(mot, devine, erreurs, difficulte, accepte_lettres):
    # Vérifications de fin de jeu
    if erreurs > 9 and difficulte == "facile" or erreurs > 6 and difficulte == "moyen" or erreurs > 4 and difficulte == "difficile":
        accepte_lettres = False
        text = police.render("Perdu !", True, ROUGE)
        fenetre.blit(text, (400, 100))
        text = police.render(f"mot à trouver: {mot}", True, ROUGE)
        fenetre.blit(text, (400, 200))

    elif all(lettre in devine for lettre in mot):
        accepte_lettres = False
        text = police.render("Gagné !", True, VERT)
        fenetre.blit(text, (400, 100))

    return accepte_lettres


def main():
    """"""
    # assigne un mot à trouver depuis le fichier 'mot.txt'
    # with open("./mots.txt", "r") as file:
    #     mots = file.read().split("\n")
    #     mot = random.choice(mots).upper()
    mot = "POWDER"
    difficulte = "moyen"
    devine = []
    lettres_fausses = []
    erreurs = 0
    en_cours = True
    accepte_lettres = True
    while en_cours:

        fenetre.blit(fond_ecran, (0, 0))
        dessine_potence(erreurs, difficulte)
        bouton_jouer()
        bouton_arreter()
        dessine_jinx(erreurs, difficulte)

        # affiche les mauvaises lettres utilisées
        liste_de_faux = police.render(f"mauvaises lettres: {' '.join(map(str, lettres_fausses))}", True, ROUGE)
        fenetre.blit(liste_de_faux, (50, 550))

        affiche_texte(mot, devine)

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

            elif evenement.type == pygame.KEYDOWN:
                if accepte_lettres:
                    if evenement.unicode.isalpha():
                        lettre = evenement.unicode.upper()
                        if lettre in mot and lettre not in devine:
                            devine.append(lettre)
                        elif lettre not in mot and lettre not in lettres_fausses:
                            lettres_fausses.append(lettre)
                            erreurs += 1

        accepte_lettres = verifie_fin(mot, devine, erreurs, difficulte, accepte_lettres)

        pygame.display.flip()
        FPS.tick(60)

    pygame.quit()


if __name__ == "__main__":  # Evite que le programme puisse être lancé depuis un autre programme.

    # nouveau_mot = "tuyau"
    # ajouter_mot(fichier_mots, nouveau_mot)
    main()