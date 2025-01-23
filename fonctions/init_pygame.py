import pygame
from pygame.locals import *


# Initialisation de Pygame
pygame.init()
pygame.font.init()

def init_pygame():

    LARGEUR, HAUTEUR = 1000, 700
    fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

    police = pygame.font.SysFont('Roboto', 35)
    police_survol = pygame.font.SysFont('Roboto', 35, True)

    BLANC = (255, 255, 255)
    NOIR = (0, 0, 0)
    ROUGE = (255, 0, 0)

    fichier_mots = "mots.txt"

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
    
    fichier_mots = "mots.txt"

    # Horloge
    FPS = pygame.time.Clock()

    # Ajouter une image de fond
    fond_ecran = pygame.image.load("image/fond_ecran.jpg")
    fond_ecran = pygame.transform.scale(fond_ecran, (LARGEUR, HAUTEUR))
    
    return fenetre, police, police_survol, fichier_mots, fond_ecran, NOIR, GRIS, BLANC, ROUGE, VERT, FPS