import pygame
import sys

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Pendu - Jinx Edition")

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
NEON_BLUE = (0, 200, 255)
NEON_PURPLE = (138, 43, 226)
RED = (255, 0, 0)

# Police
font = pygame.font.Font(None, 60)

# Chargement des assets
background_img = pygame.image.load("image/fond-ecran.webp")  # Ajouter une image de fond
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))
jinx_head = pygame.image.load("image/jinx.webp")  # Ajouter une image de la tête de Jinx
jinx_head = pygame.transform.scale(jinx_head, (100, 100))

# Dessiner la potence
def draw_gallows():
    pygame.draw.line(screen, NEON_PURPLE, (200, 600), (400, 600), 8)  # Base
    pygame.draw.line(screen, NEON_PURPLE, (300, 600), (300, 200), 8)  # Poteau vertical
    pygame.draw.line(screen, NEON_PURPLE, (300, 200), (450, 200), 8)  # Poteau horizontal
    pygame.draw.line(screen, NEON_PURPLE, (450, 200), (450, 300), 8)  # Corde

# Dessiner Jinx
def draw_jinx(stage):
    if stage > 0:  # Tête
        screen.blit(jinx_head, (400, 300))
    if stage > 1:  # Corps
        pygame.draw.line(screen, NEON_BLUE, (450, 400), (450, 500), 6)
    if stage > 2:  # Bras gauche
        pygame.draw.line(screen, NEON_BLUE, (450, 450), (400, 400), 6)
    if stage > 3:  # Bras droit
        pygame.draw.line(screen, NEON_BLUE, (450, 450), (500, 400), 6)
    if stage > 4:  # Jambe gauche
        pygame.draw.line(screen, NEON_BLUE, (450, 500), (400, 550), 6)
    if stage > 5:  # Jambe droite
        pygame.draw.line(screen, NEON_BLUE, (450, 500), (500, 550), 6)

# Dessiner les lettres
def draw_text(word, guessed):
    display_word = " ".join([letter if letter in guessed else "_" for letter in word])
    text = font.render(display_word, True, WHITE)
    screen.blit(text, (300, 650))

# Jeu principal
def main():
    clock = pygame.time.Clock()
    word = "POWDER"  # Mot à deviner
    guessed = []
    mistakes = 0
    running = True

    while running:
        screen.blit(background_img, (0, 0))  # Ajouter le fond
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
            screen.blit(text, (400, 100))
        elif all(letter in guessed for letter in word):
            text = font.render("Gagné !", True, NEON_PURPLE)
            screen.blit(text, (400, 100))

        pygame.display.flip()
        clock.tick(30)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
