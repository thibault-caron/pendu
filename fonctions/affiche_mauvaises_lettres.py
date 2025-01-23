import pygame

from .init_pygame import init_pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

fenetre, police, police_survol, fichier_mots, fond_ecran, NOIR, GRIS, BLANC, ROUGE, VERT, FPS = init_pygame()

def affiche_mauvaises_lettres(lettres_fausses, affiche):
    # affiche les mauvaises lettres utilisées
    if affiche == True:
        liste_de_faux = police.render(f"mauvaises lettres: {' '.join(map(str, lettres_fausses))}", True, ROUGE)
        fenetre.blit(liste_de_faux, (50, 550))
        
    return lettres_fausses