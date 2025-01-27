from .init_pygame import *

# Variables dessinant chacune un morceau de la potence #

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


def dessine_potence(tour, etat_difficulte):
    """
    Permet de dessiner la potence.
    :param tour: Tour actuel du jeu.
    :param etat_difficulte: Niveau de difficulté choisi.
    :return: Dessine un nouveau morceau de la potence.
    """
    if etat_difficulte == "facile":
        if tour > 0:
            fenetre.blit(potence_base, (260, 430))
        if tour > 1:
            fenetre.blit(potence_verticale, (350, 30))
        if tour > 2:
            fenetre.blit(potence_horizontale, (370, 30))
        if tour > 3:
            fenetre.blit(corde1, (500, 30))
            fenetre.blit(potence_horizontale, (370, 30))
            
    elif etat_difficulte == "normal" or etat_difficulte == "difficile":
        if tour > 0:
            fenetre.blit(potence_base, (260, 430))
            fenetre.blit(potence_verticale, (350, 30))
            fenetre.blit(corde1, (500, 30))
            fenetre.blit(potence_horizontale, (370, 30))
    
    return tour
