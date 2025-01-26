"""
Auteurs : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON
Date : 26/01/2025 23h14
But du programme :
    Créer un jeu de pendu en utilisant l'interface graphique PyGame.
Entrées : Lettres entrées au clavier par le joueur pour deviner le mot du pendu.
Sortie : Jeu du pendu avec l'interface graphique PyGame.
"""

from fonctions.init_pygame import *

from fonctions.bouton_jouer import bouton_jouer
from fonctions.bouton_arreter import bouton_arreter
from fonctions.bouton_difficile import bouton_difficile
from fonctions.bouton_ajout import bouton_ajout
from fonctions.partie import partie


def main():
    """
    Fonction principale du jeu.
    :return: ∅
    """
    en_cours = True
    affiche = True
    mot = "XXXX"  # Par défaut quand le mot n'est pas assigné
    devine = []
    lettres_fausses = []
    erreurs = 0
    accepte_lettres = False
    etat_difficulte = "normal"
    zone_texte = False
    nouveau_mot = ""

    while en_cours:

        fenetre.blit(fond_ecran, (0, 0))  # Place le fond d'écran

        # Bouton qui permet de lancer le jeu
        mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche = bouton_jouer(mot, devine, lettres_fausses,
                                                                                       erreurs, accepte_lettres,
                                                                                       affiche)

        if mot != "XXXX":  # Vérifie qu'un mot a été assigné au jeu avant de lancer
            accepte_lettres = partie(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche, etat_difficulte)

        if bouton_arreter():  # Bouton qui permet d'arrêter le jeu
            affiche = False
            devine = []
            lettres_fausses = []
            erreurs = 0
            accepte_lettres = True
            mot = "XXXX"

        etat_difficulte = bouton_difficile(etat_difficulte)  # Bouton de choix de la difficulté du jeu

        zone_texte, nouveau_mot = bouton_ajout(zone_texte, nouveau_mot)  # Bouton d'ajout d'un nouveau mot

        # Affiche le mot pour des tests #
        # text = police.render(f"mot: {mot}", True, VERT)
        # fenetre.blit(text, (400, 200))

        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

            elif evenement.type == pygame.KEYDOWN and "mot" != "XXXX":
                if accepte_lettres:
                    if evenement.unicode.isalpha():
                        lettre = evenement.unicode.upper()
                        if lettre in mot and lettre not in devine:
                            devine.append(lettre)
                        elif lettre not in mot and lettre not in lettres_fausses:
                            lettres_fausses.append(lettre)
                            erreurs += 1

        pygame.display.flip()
        FPS.tick(60)

    pygame.quit()


if __name__ == "__main__":  # Évite que le programme puisse être lancé depuis un autre programme.
    main()
