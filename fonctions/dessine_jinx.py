from .init_pygame import *

# Variables dessinant chacune un morceau du jinx #

jinx_tete = pygame.image.load("image/jinx_head.webp")
jinx_tete = pygame.transform.scale(jinx_tete, (353 / 4, 1276 / 4))

corde2 = pygame.image.load("image/corde2.png")
corde2 = pygame.transform.scale(corde2, (50, 90))

jinx_corps = pygame.image.load("image/jinx_body.webp")
jinx_corps = pygame.transform.scale(jinx_corps, (353 / 4, 1276 / 4))

jinx_bras_droit = pygame.image.load("image/jinx_right_arm.webp")
jinx_bras_droit = pygame.transform.scale(jinx_bras_droit, (353 / 4, 1276 / 4))

jinx_bras_gauche = pygame.image.load("image/jinx_left_arm.webp")
jinx_bras_gauche = pygame.transform.scale(jinx_bras_gauche, (353 / 4, 1276 / 4))

jinx_jambe_droite = pygame.image.load("image/jinx_right_leg.webp")
jinx_jambe_droite = pygame.transform.scale(jinx_jambe_droite, (353 / 4, 1276 / 4))

jinx_jambe_gauche = pygame.image.load("image/jinx_left_leg.webp")
jinx_jambe_gauche = pygame.transform.scale(jinx_jambe_gauche, (353 / 4, 1276 / 4))


def dessine_jinx(tour, etat_difficulte):
    """
    Permet de dessiner le jinx (bonhomme du jeu).
    :param tour: Tour actuel du jeu.
    :param etat_difficulte: Niveau de difficulté choisi.
    :return: Dessine un nouveau morceau du jinx.
    """
    if etat_difficulte == "facile":
        if tour > 4:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 5:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 6:  # Bras gauche
            fenetre.blit(jinx_bras_droit, (480, 70))
        if tour > 7:  # Bras droit
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 8:  # Jambe gauche
            fenetre.blit(jinx_jambe_droite, (480, 70))
        if tour > 9:  # Jambe droite
            fenetre.blit(jinx_jambe_gauche, (480, 70))
            
    elif etat_difficulte == "normal":
        if tour > 1:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 2:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 3:  # Bras gauche
            fenetre.blit(jinx_bras_droit, (480, 70))
        if tour > 4:  # Bras droit
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 5:  # Jambe gauche
            fenetre.blit(jinx_jambe_droite, (480, 70))
        if tour > 6:  # Jambe droite
            fenetre.blit(jinx_jambe_gauche, (480, 70))
            
    elif etat_difficulte == "difficile":
        if tour > 1:  # Tête
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 2:  # Corps
            fenetre.blit(jinx_corps, (480, 70))
            fenetre.blit(corde2, (500, 30))
            fenetre.blit(jinx_tete, (480, 70))
        if tour > 3:  # Bras
            fenetre.blit(jinx_bras_droit, (480, 70))
            fenetre.blit(jinx_bras_gauche, (480, 70))
        if tour > 4:  # Jambes
            fenetre.blit(jinx_jambe_droite, (480, 70))
            fenetre.blit(jinx_jambe_gauche, (480, 70))
    
    return tour
