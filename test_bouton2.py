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
couleur_texte_survol = (255, 255, 0)  # Couleur du texte au survol (jaune)

# Définir la police
police = pygame.font.SysFont("Segoe script", 50)

# Coordonnées et noms des boutons
boutons = [
    {'position': (150, 110), 'texte': "JOUER", 'position2': (350, 110)},
    {'position': (150, 270), 'texte': "AJOUTER UN MOT", 'position2': (500, 270)},
    {'position': (150, 420), 'texte': "CHANGER DE DIFFICULTÉ", 'position2': (600, 420)},
    {'position': (150, 590), 'texte': "SCORES", 'position2': (350, 590)}
]

rayon_bouton = 40


# Fonction pour dessiner un bouton
def dessiner_bouton(bouton):
    souris_x, souris_y = pygame.mouse.get_pos()

    # Vérifier si la souris est au-dessus du bouton (cercle)
    distance_cercle = (souris_x - bouton['position'][0]) ** 2 + (souris_y - bouton['position'][1]) ** 2
    survol_bouton = distance_cercle <= rayon_bouton ** 2

    # Vérifier si la souris est sur le texte
    texte = police.render(bouton['texte'], True, BLANC)
    texte_rect = texte.get_rect(center=bouton['position2'])
    survol_texte = texte_rect.collidepoint(souris_x, souris_y)

    # Changer la couleur en fonction du survol (cercle ou texte)
    if survol_bouton or survol_texte:
        pygame.draw.circle(fenetre, couleur_survol, bouton['position'], rayon_bouton)
        # Dessiner le texte en survol (jaune)
        texte = police.render(bouton['texte'], True, couleur_texte_survol)
    else:
        pygame.draw.circle(fenetre, couleur_bouton, bouton['position'], rayon_bouton)
        # Dessiner le texte normal
        texte = police.render(bouton['texte'], True, BLANC)

    # Dessiner le texte centré sur le bouton
    fenetre.blit(texte, texte_rect)

    # Retourner si le bouton ou le texte est survolé
    return survol_bouton or survol_texte


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
            for bouton in boutons:
                distance_cercle = (souris_x - bouton['position'][0]) ** 2 + (souris_y - bouton['position'][1]) ** 2
                # Vérifier si le clic est sur le bouton (cercle) ou le texte
                texte = police.render(bouton['texte'], True, BLANC)
                texte_rect = texte.get_rect(center=bouton['position2'])
                if distance_cercle <= rayon_bouton ** 2 or texte_rect.collidepoint(souris_x, souris_y):
                    print(f"{bouton['texte']} cliqué !")

    # Remplir l'écran de noir
    fenetre.fill(NOIR)

    # Dessiner tous les boutons
    for bouton in boutons:
        dessiner_bouton(bouton)

    # Mettre à jour l'affichage
    pygame.display.flip()
