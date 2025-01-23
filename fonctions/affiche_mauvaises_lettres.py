import pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

police = pygame.font.SysFont('Roboto', 35)

ROUGE = (255, 0, 0)

def affiche_mauvaises_lettres(lettres_fausses, affiche):
    # affiche les mauvaises lettres utilisées
    if affiche == True:
        liste_de_faux = police.render(f"mauvaises lettres: {' '.join(map(str, lettres_fausses))}", True, ROUGE)
        fenetre.blit(liste_de_faux, (50, 550))
        
    return lettres_fausses