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
def dessine_potence():
    fenetre.blit(potence_base, (260, 430))
    fenetre.blit(potence_verticale, (350, 30))
    fenetre.blit(corde1, (500, 30))
    fenetre.blit(potence_horizontale, (370, 30))


# Dessiner Jinx
def dessine_jinx(tour):
    if tour > 0:  # Tête
        fenetre.blit(jinx_tete, (480, 70))
    if tour > 1:  # Corps
        fenetre.blit(jinx_corps, (480, 70))
        fenetre.blit(corde2, (500, 30))
        fenetre.blit(jinx_tete, (480, 70))
    if tour > 2:  # Bras gauche
        fenetre.blit(jinx_bras_droit, (480, 70))
    if tour > 3:  # Bras droit
        fenetre.blit(jinx_bras_gauche, (480, 70))
    if tour > 4:  # Jambe gauche
        fenetre.blit(jinx_jambe_droite, (480, 70))
    if tour > 5:  # Jambe droite
        fenetre.blit(jinx_jambe_gauche, (480, 70))


# Dessiner les lettres
def affiche_texte(mot, devine):
    affiche_mot = " ".join([lettre if lettre in devine else "_" for lettre in mot])
    texte = police.render(affiche_mot, True, BLANC)
    fenetre.blit(texte, (300, 650))
    
# Dessiner les boutons
def affiche_bouton():
    # Détecte la postion de la souris en tuple [x, y]
    # souris = pygame.mouse.get_pos()
    
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))
    # if bouton_largeur/2 <= souris[0] <= bouton_largeur/2+800 and bouton_hauteur/2 <= souris[1] <= bouton_hauteur/2+60: 
    #     jouer = fenetre.blit(bouton, (800, 60))
    #     arreter = fenetre.blit(bouton, (800, 140))
    
    #     jouer = police_survol.render('jouer' , True , BLANC)
    #     fenetre.blit(jouer, (850, 70))
    
    #     arreter = police_survol.render("arrêter", True, BLANC)
    #     fenetre.blit(arreter, (845, 150)) 
          
    # else: 
    jouer = fenetre.blit(bouton, (800, 60))
    arreter = fenetre.blit(bouton, (800, 140))
    
    jouer = police.render('jouer' , True , NOIR)
    fenetre.blit(jouer, (850, 70))
    
    arreter = police.render("arrêter", True, NOIR)
    fenetre.blit(arreter, (845, 150)) 
    
 

fichier_mots = "mots.txt"

touches_alphabet = {K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e", K_f: "f", K_g: "g", K_h: "h", K_i: "i", K_j: "j",
                    K_k: "k", K_l: "l", K_m: "m", K_n: "n", K_o: "o", K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t",
                    K_u: "u", K_v: "v", K_w: "w", K_x: "x", K_y: "y", K_z: "z"}


def main():
    """"""
    mot = "POWDER"  # Mot à deviner
    devine = []
    erreurs = 0
    en_cours = True
    while en_cours:

        fenetre.blit(fond_ecran, (0, 0))
        dessine_potence()
        affiche_bouton()
        dessine_jinx(erreurs)
        affiche_texte(mot, devine)

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False
            if evenement.type == pygame.KEYDOWN:
                if evenement.unicode.isalpha():
                    lettre = evenement.unicode.upper()
                    if lettre in mot and lettre not in devine:
                        devine.append(lettre)
                    elif lettre not in mot:
                        erreurs += 1

        # Vérifications de fin de jeu
        if erreurs > 5:
            text = police.render("Perdu !", True, ROUGE)
            fenetre.blit(text, (400, 100))
        elif all(lettre in devine for lettre in mot):
            text = police.render("Gagné !", True, VERT)
            fenetre.blit(text, (400, 100))

            # if evenement.type == pygame.KEYDOWN:
                # if evenement.key == pygame.K_r:
                    # couleur = ROUGE

        pygame.display.flip()
        FPS.tick(60)

    pygame.quit()


if __name__ == "__main__":  # Evite que le programme puisse être lancé depuis un autre programme.

    # nouveau_mot = "tuyau"
    # ajouter_mot(fichier_mots, nouveau_mot)
    main()
