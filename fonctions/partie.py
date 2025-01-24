from .init_pygame import *
from .dessine_jinx import dessine_jinx
from .desssine_potence import dessine_potence
from .affiche_mauvaises_lettres import affiche_mauvaises_lettres
from .affiche_texte import affiche_texte
from .verifie_fin import verifie_fin


def partie(mot, devine, lettres_fausses, erreurs, accepte_lettres, affiche, etat_difficulte):

    dessine_potence(erreurs, etat_difficulte)
    dessine_jinx(erreurs, etat_difficulte)

    affiche_mauvaises_lettres(lettres_fausses, affiche)
    affiche_texte(mot, devine, affiche)

    accepte_lettres = verifie_fin(mot, devine, erreurs, accepte_lettres, etat_difficulte)

    return accepte_lettres