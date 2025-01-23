import pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

police = pygame.font.SysFont('Roboto', 35)
police_survol = pygame.font.SysFont('Roboto', 35, True)

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)

def bouton_difficile(etat_difficulte):

    souris = pygame.mouse.get_pos()
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))

    # Détection de la souris sur le bouton
    if 800 <= souris[0] <= 800 + bouton_largeur and 220 <= souris[1] <= 240 + bouton_hauteur:
        fenetre.blit(bouton, (800, 220))
        texte = police_survol.render(etat_difficulte, True, BLANC)
        fenetre.blit(texte, (840, 230))

        # Vérification du clic
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                if etat_difficulte == "normal":
                    etat_difficulte = "difficile"
                elif etat_difficulte == "difficile":
                    etat_difficulte = "facile"
                elif etat_difficulte == "facile":
                    etat_difficulte = "normal"
    else:
        fenetre.blit(bouton, (800, 220))
        texte = police.render(etat_difficulte, True, NOIR)
        fenetre.blit(texte, (840, 230))
        
    return etat_difficulte