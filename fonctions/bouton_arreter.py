from .init_pygame import *


def bouton_arreter():
    """
    Bouton qui permet d'arrêter une partie en cours.
    :return: Arrête le jeu et réinitialise tous les paramètres pour pouvoir relancer une partie si souhaitée.
    """
    souris = pygame.mouse.get_pos()  # Détecte la position de la souris en tuple (x, y)
    clic = False
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur)) 
    
    if (bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 + 60 <= souris[1]
            <= bouton_largeur/2 + 100):
        arreter = fenetre.blit(bouton, (800, 140))
        arreter = police_survol.render("arrêter", True, BLANC)
        fenetre.blit(arreter, (845, 150))
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                clic = True
    else:
        arreter = fenetre.blit(bouton, (800, 140))
        arreter = police.render("arrêter", True, NOIR)
        fenetre.blit(arreter, (845, 150))
    
    return clic
