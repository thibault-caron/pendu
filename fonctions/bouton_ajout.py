import pygame
from pygame.locals import *

from .ajouter_mot import ajouter_mot

# Initialisation de Pygame
pygame.init()
pygame.font.init()

LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))

police = pygame.font.SysFont('Roboto', 35)
police_survol = pygame.font.SysFont('Roboto', 35, True)

BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
ROUGE = (255, 0, 0)

fichier_mots = "mots.txt"


def bouton_ajout():
        # Détecte la postion de la souris en tuple [x, y]
    souris = pygame.mouse.get_pos()
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))
       
    if bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 + 210 <= souris[1] <= bouton_largeur/2 + 270: 
        jouer = fenetre.blit(bouton, (800, 300))
        jouer = police_survol.render('Ajout mot' , True , BLANC)
        fenetre.blit(jouer, (825, 310))
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                # permet d'ajouter un mot dans le fichier 'mot.txt'
                nouveau_mot = "Entrez un nouveau mot"
                font = pygame.font.SysFont(None, 48)
                img = font.render(nouveau_mot, True, ROUGE)
                rect = img.get_rect()
                rect.topleft = (20, 20)
                cursor = Rect(rect.topright, (3, rect.height))
                if evenement.type == KEYDOWN:
                    if evenement.key == K_BACKSPACE:
                        if len(nouveau_mot)>0:
                            nouveau_mot = nouveau_mot[:-1]
                    else:
                        nouveau_mot += evenement.unicode
                    img = font.render(nouveau_mot, True, ROUGE)
                rect.size=img.get_size()
                cursor.topleft = rect.topright
                fenetre.blit(img, rect)
                ajouter_mot(fichier_mots, nouveau_mot)

    else: 
        jouer = fenetre.blit(bouton, (800, 300))        
        jouer = police.render('Ajout mot' , True , NOIR)
        fenetre.blit(jouer, (825, 310))    