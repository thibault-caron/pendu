import pygame
import random

from .init_pygame import init_pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

fenetre, police, police_survol, fichier_mots, fond_ecran, NOIR, GRIS, BLANC, ROUGE, VERT, FPS = init_pygame()

def bouton_jouer(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche):  
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
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                # assigne un mot à trouver depuis le fichier 'mot.txt'
                with open("./mots.txt", "r") as file:
                    mots = file.read().split("\n")
                    mot = random.choice(mots).upper()

                devine = []
                lettres_fausses = []
                erreurs = 0
                accepte_lettres = True
                affiche = True
    else: 
        jouer = fenetre.blit(bouton, (800, 60))        
        jouer = police.render('jouer' , True , NOIR)
        fenetre.blit(jouer, (850, 70))
        
    return mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche