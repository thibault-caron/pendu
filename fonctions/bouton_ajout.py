from .init_pygame import *
from .ajouter_mot import ajouter_mot


def bouton_ajout(zone_texte, nouveau_mot):
    """
    Permet d'ajouter un nouveau mot au fichier contenant les mots.
    :param zone_texte: Permet d'ajouter un nouveau mot si True.
    :param nouveau_mot: Nouveau mot à ajouter à la liste des mots.
    :return: Le nouveau mot est ajouté au fichier et les paramètres du bouton sont réinitialisés.
    """
    souris = pygame.mouse.get_pos()  # Détecte la position de la souris en tuple (x, y)
        
    bouton_largeur = 170
    bouton_hauteur = 40
    bouton = pygame.image.load("image/acier2.jpg")
    bouton = pygame.transform.scale(bouton, (bouton_largeur, bouton_hauteur))
       
    if (bouton_hauteur/2 + 780 <= souris[0] <= bouton_hauteur/2 + 940 and bouton_largeur/2 + 210 <= souris[1]
            <= bouton_largeur/2 + 270):
        jouer = fenetre.blit(bouton, (800, 300))
        jouer = police_survol.render('Ajout mot', True, BLANC)
        fenetre.blit(jouer, (825, 310))
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.MOUSEBUTTONDOWN:
                zone_texte = True
                nouveau_mot = ""

    else: 
        jouer = fenetre.blit(bouton, (800, 300))        
        jouer = police.render('Ajout mot', True, NOIR)
        fenetre.blit(jouer, (825, 310))
    
    if zone_texte:
        pygame.draw.rect(fenetre, BLANC, (800, 340, 170, 50))
        texte_affiche = police.render(nouveau_mot, True, NOIR)
        fenetre.blit(texte_affiche, (810, 350))

        if pygame.time.get_ticks() % 1000 < 500:
            pygame.draw.line(fenetre, NOIR, (810 + texte_affiche.get_width(), 350),
                             (810 + texte_affiche.get_width(), 380), 2)

        for evenement in pygame.event.get():
            if evenement.type == pygame.KEYDOWN:

                if evenement.key == pygame.K_RETURN:

                    if nouveau_mot.strip():
                        ajouter_mot(fichier_mots, nouveau_mot.strip())

                    zone_texte = False  # Quitte le mode de dessin de la zone de texte

                elif evenement.key == pygame.K_BACKSPACE:  # Supprime les lettres mal entrées
                    nouveau_mot = nouveau_mot[:-1]

                else:
                    nouveau_mot += evenement.unicode

    return zone_texte, nouveau_mot
