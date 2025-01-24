from .init_pygame import *


# Dessiner les lettres
def affiche_texte(mot, devine, affiche):
    if affiche == True:
        affiche_mot = " ".join([lettre if lettre in devine else "_" for lettre in mot])
        texte = police.render(affiche_mot, True, BLANC)
        fenetre.blit(texte, (300, 650))
    
    return mot, devine