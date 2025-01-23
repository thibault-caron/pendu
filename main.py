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

from fonctions.bouton_jouer import bouton_jouer
from fonctions.bouton_arreter import bouton_arreter
from fonctions.bouton_difficile import bouton_difficile
from fonctions.bouton_ajout import bouton_ajout
from fonctions.partie import partie

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

        



def main():
    """"""

    en_cours = True
    affiche = True
    mot = "XXXX"
    devine = []
    lettres_fausses = []
    erreurs = 0
    accepte_lettres = False
    etat_difficulte = "normal"

    while en_cours:

        fenetre.blit(fond_ecran, (0, 0))
        
        mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche = bouton_jouer(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche)

        if mot != "XXXX":
            accepte_lettres = partie(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche, etat_difficulte)

        if bouton_arreter():
            affiche = False
            devine = []
            lettres_fausses = []
            erreurs = 0
            accepte_lettres = True
            mot = "XXXX"
            
        etat_difficulte = bouton_difficile(etat_difficulte)
        
        bouton_ajout()

        text = police.render(f"mot: {mot}", True, VERT)
        fenetre.blit(text, (400, 200)) # pour test, affiche mot


        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

            elif evenement.type == pygame.KEYDOWN and "mot" is not "XXXX":
                    if accepte_lettres:
                        if evenement.unicode.isalpha():
                            lettre = evenement.unicode.upper()
                            if lettre in mot and lettre not in devine:
                                devine.append(lettre)
                            elif lettre not in mot and lettre not in lettres_fausses:
                                lettres_fausses.append(lettre)
                                erreurs += 1

        pygame.display.flip()
        FPS.tick(60)

    pygame.quit()


if __name__ == "__main__":  # Evite que le programme puisse être lancé depuis un autre programme.

    # nouveau_mot = "tuyau"
    # ajouter_mot(fichier_mots, nouveau_mot)
    main()