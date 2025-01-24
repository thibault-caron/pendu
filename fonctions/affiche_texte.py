import pygame

from .init_pygame import init_pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

fenetre, police, police_survol, fichier_mots, fond_ecran, NOIR, GRIS, BLANC, ROUGE, VERT, FPS = init_pygame()

# Dessiner les lettres
def affiche_texte(mot, devine, affiche):
    if affiche == True:
        affiche_mot = " ".join([lettre if lettre in devine else "_" for lettre in mot])
        texte = police.render(affiche_mot, True, BLANC)
        fenetre.blit(texte, (300, 650))
    
    return mot, devine