def ajouter_mot(fichier, mot):
    """
    Ajout un nouveau mot au fichier texte contenant la liste de mots du jeu.
    :param fichier: Fichier texte contenant la liste de mots du jeu.
    :param mot: Mot à ajouter au fichier.
    :return: ∅
    """

    def existence_mot(nouveau_mot):
        """
        Vérifie si le mot est déjà présent dans le fichier.
        :param nouveau_mot: Mot à ajouter au fichier.
        :return: True si le mot est déja dans le fichier, sinon None.
        """
        liste_mots = []
        with open(fichier, "r") as pendu:
            for ligne in pendu:
                unite = ligne[:-1]
                liste_mots.append(unite)
        for mots in liste_mots:
            if nouveau_mot == mots:
                return True

    if not existence_mot(mot):
        with open(fichier, "a") as mots_pendu:
            mots_pendu.write(f"\n{mot}")
