import pygame
from pygame.locals import *

from .init_pygame import init_pygame
from .ajouter_mot import ajouter_mot

# Initialisation de Pygame
pygame.init()
pygame.font.init()

fenetre, police, police_survol, fichier_mots, fond_ecran, NOIR, GRIS, BLANC, ROUGE, VERT, FPS = init_pygame()


def bouton_ajout(zone_texte, nouveau_mot):
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
                zone_texte = True
                nouveau_mot = ""

    else: 
        jouer = fenetre.blit(bouton, (800, 300))        
        jouer = police.render('Ajout mot' , True , NOIR)
        fenetre.blit(jouer, (825, 310))
    
    if zone_texte:
        pygame.draw.rect(fenetre, BLANC, (800, 340, 170, 50))
        texte_affiche = police.render(nouveau_mot, True, NOIR)
        fenetre.blit(texte_affiche, (810, 350))
        
        # Afficher le curseur
        if pygame.time.get_ticks() % 1000 < 500:
            pygame.draw.line(fenetre, NOIR, (810 + texte_affiche.get_width(), 350), (810 + texte_affiche.get_width(), 380), 2)

        for evenement in pygame.event.get():
            if evenement.type == pygame.KEYDOWN:
                # Validation avec Entrée
                if evenement.key == pygame.K_RETURN:
                    # Si le mot n'est pas vide
                    if nouveau_mot.strip():
                        ajouter_mot(fichier_mots, nouveau_mot.strip())
                        # Quitte le mode de dessin de la zone de texte
                    zone_texte = False
                # Supprime les lettres mal entrées
                elif evenement.key == pygame.K_BACKSPACE:
                    nouveau_mot = nouveau_mot[:-1]
                # Ajout des caractères
                else:
                    nouveau_mot += evenement.unicode
        
        
    return zone_texte, nouveau_mot