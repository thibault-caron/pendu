from .init_pygame import *


def affiche_mauvaises_lettres(lettres_fausses, affiche):
    """
    Affiche les lettres fausses entrées par le joueur.
    :param lettres_fausses: Liste dans laquelle sont ajoutées les fausses lettres.
    :param affiche: Permet l'affichage du jeu si True.
    :return: La liste lettres_fausses sera mise à jour est affichée à l'écran.
    """
    if affiche:
        liste_de_faux = police.render(f"mauvaises lettres: {' '.join(map(str, lettres_fausses))}", True, ROUGE)
        fenetre.blit(liste_de_faux, (50, 550))
        
    return lettres_fausses
