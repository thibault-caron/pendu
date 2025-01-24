import pygame

from .init_pygame import init_pygame

# Initialisation de Pygame
pygame.init()
pygame.font.init()

fenetre, police, police_survol, fichier_mots, fond_ecran, NOIR, GRIS, BLANC, ROUGE, VERT, FPS = init_pygame()

def verifie_fin(mot, devine, erreurs, accepte_lettres, etat_difficulte):
    # Vérifications de fin de jeu
    if erreurs > 9 and etat_difficulte == "facile" or erreurs > 6 and etat_difficulte == "normal" or erreurs > 4 and etat_difficulte == "difficile":
        accepte_lettres = False
        text = police.render("Perdu !", True, ROUGE)
        fenetre.blit(text, (400, 300))
        text = police.render(f"mot à trouver: {mot}", True, ROUGE)
        fenetre.blit(text, (400, 200))

    elif all(lettre in devine for lettre in mot):
        accepte_lettres = False
        text = police.render("Gagné !", True, VERT)
        fenetre.blit(text, (400, 300))

    return accepte_lettres