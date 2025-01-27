from .init_pygame import *


# Dessiner les lettres
def affiche_texte(mot, devine, affiche):
    """
    Affichage du mot que l'on essaye de deviner.
    :param mot: Mot à deviner.
    :param devine: Liste des lettres devinées qui s'affichent à l'écran.
    :param affiche: Permet l'affichage du jeu si True.
    :return: Met à jour l'affichage à l'écran du mot en fonction de lettre entrée par le joueur.
    """
    if affiche:
        affiche_mot = " ".join([lettre if lettre in devine else "_" for lettre in mot])
        texte = police.render(affiche_mot, True, BLANC)
        fenetre.blit(texte, (300, 650))
    
    return mot, devine
