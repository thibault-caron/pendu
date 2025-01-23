import pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

police = pygame.font.SysFont('Roboto', 35)
police_survol = pygame.font.SysFont('Roboto', 35, True)

BLANC = (255, 255, 255)

# Dessiner les lettres
def affiche_texte(mot, devine, affiche):
    if affiche == True:
        affiche_mot = " ".join([lettre if lettre in devine else "_" for lettre in mot])
        texte = police.render(affiche_mot, True, BLANC)
        fenetre.blit(texte, (300, 650))
    
    return mot, devine