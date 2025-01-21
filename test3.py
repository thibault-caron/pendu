import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Pendu - Edition spéciale Jinx")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEON_BLUE = (0, 200, 255)
NEON_PURPLE = (138, 43, 226)
RED = (255, 0, 0)

# Police
font = pygame.font.Font(None, 60)

############ Chargement des assets
# Ajouter une image de fond
fond_ecran_img = pygame.image.load("image/fond_ecran.jpg")
fond_ecran_img = pygame.transform.scale(fond_ecran_img, (LARGEUR, HAUTEUR))

#Base
potence_base_img = pygame.image.load("image/acier2.jpg")
potence_base_img = pygame.transform.scale(potence_base_img, (200, 20))

# Poteau vertical
potence_vert_img = pygame.image.load("image/acier2.jpg")
potence_vert_img = pygame.transform.scale(potence_vert_img, (20, 400))

# Poteau horizontal
potence_horz_img = pygame.image.load("image/acier2.jpg")
potence_horz_img = pygame.transform.scale(potence_horz_img, (200, 20))

# Corde
corde_img = pygame.image.load("image/corde.png")
corde_img = pygame.transform.scale(corde_img, (100, 180))

corde2_img = pygame.image.load("image/corde2.png")
corde2_img = pygame.transform.scale(corde2_img, (100, 180))

# Dessiner Jinx
jinx_tete = pygame.image.load("image/jinx_head.webp")
jinx_tete = pygame.transform.scale(jinx_tete, (353/2, 1276/2))

jinx_corps = pygame.image.load("image/jinx_body.webp")
jinx_corps = pygame.transform.scale(jinx_corps, (353/2, 1276/2))

jinx_bras_droit = pygame.image.load("image/jinx_right_arm.webp") 
jinx_bras_droit = pygame.transform.scale(jinx_bras_droit, (353/2, 1276/2))

jinx_bras_gauche = pygame.image.load("image/jinx_left_arm.webp")
jinx_bras_gauche = pygame.transform.scale(jinx_bras_gauche, (353/2, 1276/2))

jinx_jambe_droite = pygame.image.load("image/jinx_right_leg.webp")
jinx_jambe_droite = pygame.transform.scale(jinx_jambe_droite, (353/2, 1276/2))

jinx_jambe_gauche = pygame.image.load("image/jinx_left_leg.webp")
jinx_jambe_gauche = pygame.transform.scale(jinx_jambe_gauche, (353/2, 1276/2))

# Dessiner la potence
def draw_gallows():
    fenetre.blit(potence_base_img, (260, 430))
    fenetre.blit(potence_vert_img, (350, 30))
    fenetre.blit(corde_img, (500, 30))
    fenetre.blit(potence_horz_img, (370, 30))
    

# Dessiner Jinx
def draw_jinx(stage):
    if stage > 0:  # Tête
        fenetre.blit(jinx_tete, (460, 115))
    if stage > 1:  # Corps
        fenetre.blit(jinx_corps, (460, 115))
        fenetre.blit(corde2_img, (500, 30))
        fenetre.blit(jinx_tete, (460, 115))
    if stage > 2:  # Bras gauche
        fenetre.blit(jinx_bras_droit, (460, 115))
    if stage > 3:  # Bras droit
        fenetre.blit(jinx_bras_gauche, (460, 115))
    if stage > 4:  # Jambe gauche
        fenetre.blit(jinx_jambe_droite, (460, 115))
    if stage > 5:  # Jambe droite
        fenetre.blit(jinx_jambe_gauche, (460, 115))
        
        
# Dessiner les lettres
def draw_text(word, guessed):
    display_word = " ".join([letter if letter in guessed else "_" for letter in word])
    text = font.render(display_word, True, WHITE)
    fenetre.blit(text, (300, 650))

# Jeu principal
def main():
    clock = pygame.time.Clock()
    word = "POWDER"  # Mot à deviner
    guessed = []
    mistakes = 0
    running = True

    while running:
        fenetre.blit(fond_ecran_img, (0, 0))  # Ajouter le fond
        draw_gallows()
        draw_jinx(mistakes)
        draw_text(word, guessed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    letter = event.unicode.upper()
                    if letter in word and letter not in guessed:
                        guessed.append(letter)
                    elif letter not in word:
                        mistakes += 1

        # Vérifications de fin de jeu
        if mistakes > 5:
            text = font.render("Perdu !", True, RED)
            fenetre.blit(text, (400, 100))
        elif all(letter in guessed for letter in word):
            text = font.render("Gagné !", True, NEON_PURPLE)
            fenetre.blit(text, (400, 100))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
