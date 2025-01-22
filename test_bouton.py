import pygame

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre
fenetre = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Bouton rond Pygame")

# Définir les couleurs
NOIR = (0, 0, 0)
BLANC = (255, 255, 255)
couleur_bouton = (0, 128, 255)
couleur_survol = (0, 255, 255)

# Définir la police
police = pygame.font.SysFont("Segoe script", 50)

# Coordonnées des boutons
bouton_1 = (150, 110)
bouton_2 = (150, 270)
bouton_3 = (150, 420)
bouton_4 = (150, 590)
rayon_bouton = 40


# Fonction pour dessiner le bouton
def dessiner_bouton(bouton):
    # Récupérer la position de la souris
    souris_x, souris_y = pygame.mouse.get_pos()

    # Vérifier si la souris est au-dessus du bouton
    if (souris_x - bouton[0]) ** 2 + (souris_y - bouton[1]) ** 2 <= rayon_bouton ** 2:
        pygame.draw.circle(fenetre, couleur_survol, bouton, rayon_bouton)
    else:
        pygame.draw.circle(fenetre, couleur_bouton, bouton, rayon_bouton)


# Boucle principale du jeu
while True:
    # Gestion des événements
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Détection du clic de souris
        if event.type == pygame.MOUSEBUTTONDOWN:
            souris_x, souris_y = pygame.mouse.get_pos()
            if (souris_x - bouton_1[0]) ** 2 + (souris_y - bouton_1[1]) ** 2 <= rayon_bouton ** 2:
                print("Bouton 1 cliqué !")
            elif (souris_x - bouton_2[0]) ** 2 + (souris_y - bouton_2[1]) ** 2 <= rayon_bouton ** 2:
                print("Bouton 2 cliqué !")
            elif (souris_x - bouton_3[0]) ** 2 + (souris_y - bouton_3[1]) ** 2 <= rayon_bouton ** 2:
                print("Bouton 3 cliqué !")
            elif (souris_x - bouton_4[0]) ** 2 + (souris_y - bouton_4[1]) ** 2 <= rayon_bouton ** 2:
                print("Bouton 4 cliqué !")

    # Remplir l'écran de noir
    fenetre.fill(NOIR)

    # Dessiner le bouton
    dessiner_bouton(bouton_1)
    dessiner_bouton(bouton_2)
    dessiner_bouton(bouton_3)
    dessiner_bouton(bouton_4)

    texte_1 = police.render("JOUER", True, BLANC)
    fenetre.blit(texte_1, (250, 70))

    texte_2 = police.render("AJOUTER UN MOT", True, BLANC)
    fenetre.blit(texte_2, (250, 230))

    texte_3 = police.render("CHANGER DE DIFFICULTÉ", True, BLANC)
    fenetre.blit(texte_3, (250, 380))

    texte_4 = police.render("SCORES", True, BLANC)
    fenetre.blit(texte_4, (250, 550))

    # Mettre à jour l'affichage
    pygame.display.flip()
