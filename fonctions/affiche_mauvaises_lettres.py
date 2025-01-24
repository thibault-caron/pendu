from .init_pygame import *


def affiche_mauvaises_lettres(lettres_fausses, affiche):
    # affiche les mauvaises lettres utilisées
    if affiche == True:
        liste_de_faux = police.render(f"mauvaises lettres: {' '.join(map(str, lettres_fausses))}", True, ROUGE)
        fenetre.blit(liste_de_faux, (50, 550))
        
    return lettres_fausses