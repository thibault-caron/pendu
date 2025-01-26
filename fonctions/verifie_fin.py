from .init_pygame import *


def verifie_fin(mot, devine, erreurs, accepte_lettres, etat_difficulte):
    """
    Permet en fin de jeu de vérifier si le joueur a gagné ou perdu.
    :param mot: Mot à deviner.
    :param devine: Liste des lettres devinées qui s'affichent à l'écran.
    :param erreurs: Nombre d'erreurs commises par le joueur.
    :param accepte_lettres: Permet d'entrer des lettres pour deviner le mot si True.
    :param etat_difficulte: Niveau de difficulté choisi.
    :return: Affiche la défaite ou la victoire du joueur.
    """
    if erreurs > 9 and etat_difficulte == "facile" or erreurs > 6 and etat_difficulte == "normal" or erreurs > 4 and etat_difficulte == "difficile":
        accepte_lettres = False
        text = pygame.font.SysFont('Roboto', 55).render("Perdu !", True, ROUGE)
        fenetre.blit(text, (400, 300))
        text = police.render(f"mot à trouver: {mot}", True, ROUGE)
        fenetre.blit(text, (400, 200))

    elif all(lettre in devine for lettre in mot):
        accepte_lettres = False
        text = pygame.font.SysFont('Roboto', 55).render("Gagné !", True, VERT)
        fenetre.blit(text, (400, 300))

    return accepte_lettres
