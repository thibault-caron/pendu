import pygame
from pygame.locals import *
import random


# Initialisation de Pygame
pygame.init()
pygame.font.init()

# Taille de la fenêtre de jeu
LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

# Choix de la police
police = pygame.font.SysFont('Roboto', 35)
police_survol = pygame.font.SysFont('Roboto', 35, True)

# Fichier de stockage des mots
fichier_mots = "mots.txt"

# Couleurs
NOIR = (0, 0, 0)
GRIS = (127, 127, 127)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 100, 0)

# Horloge
FPS = pygame.time.Clock()

# Ajouter une image de fond
fond_ecran = pygame.image.load("image/fond_ecran.jpg")
fond_ecran = pygame.transform.scale(fond_ecran, (LARGEUR, HAUTEUR))
