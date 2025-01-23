def ajouter_mot(fichier, nouveau_mot):
    """
    Ajout un nouveau mot au fichier texte contenant la liste de mots du jeu.
    :param fichier: Fichier texte contenant la liste de mots du jeu.
    :param mot: Mot à ajouter au fichier.
    :return: ∅
    """
    with open(fichier, "a") as mots_pendu:
        mots_pendu.write(f"\n{nouveau_mot}")
