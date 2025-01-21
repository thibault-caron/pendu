"""
Auteurs : Lorenzo OTTAVIANI, Olivier PORTAL et Thibault CARON
Date : 20/01/2025 15h48
But du programme :
    Créer un jeu de pendu en utilisant l'interface graphique PyGame
Entrée :
Sortie :
"""

import pygame
from pygame.locals import *

# Initialisation de Pygame
pygame.init()
pygame.font.init()

# Dimensions de la fenêtre
LARGEUR, HAUTEUR = 1000, 700
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
pygame.display.set_caption("Jeu du Pendu - Edition spéciale Jinx")

# Couleurs 
NOIR = (0, 0, 0)
GRIS = (127, 127, 127)
BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
VERT = (0, 255, 0)
BLEU = (0, 0, 255)
JAUNE = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

# Police
font = pygame.font.Font(None, 60)

############ Affichage des objets
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

# Le pendu => Jinx
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
def dessine_potence():
    fenetre.blit(potence_base_img, (260, 430))
    fenetre.blit(potence_vert_img, (350, 30))
    fenetre.blit(corde_img, (500, 30))
    fenetre.blit(potence_horz_img, (370, 30))
    

# Dessiner Jinx
def dessine_jinx(stage):
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

fichier_mots = "mots.txt"

touches_alphabet = {K_a: "a", K_b: "b", K_c: "c", K_d: "d", K_e: "e", K_f: "f", K_g: "g", K_h: "h", K_i: "i", K_j: "j",
                    K_k: "k", K_l: "l", K_m: "m", K_n: "n", K_o: "o", K_p: "p", K_q: "q", K_r: "r", K_s: "s", K_t: "t",
                    K_u: "u", K_v: "v", K_w: "w", K_x: "x", K_y: "y", K_z: "z"}

police = pygame.font.SysFont("Courier New", 32)
FPS = pygame.time.Clock()


def main():
    """"""
    en_cours = True    
    while en_cours:
        
        fenetre.blit(fond_ecran_img, (0, 0))
        dessine_potence()
        
        for evenement in pygame.event.get():
            if evenement.type == pygame.QUIT:
                en_cours = False

            if evenement.type == pygame.KEYDOWN:
                if evenement.key == pygame.K_r:
                    couleur = ROUGE
                elif evenement.key == pygame.K_v:
                    couleur = VERT
                    fenetre
                elif evenement.key == pygame.K_1:
                    police.render("Placeholder lance partie")
            
        pygame.display.update()
        FPS.tick(60)

    pygame.quit()


if __name__ == "__main__":  # Evite que le programme puisse être lancé depuis un autre programme.

    # nouveau_mot = "tuyau"
    # ajouter_mot(fichier_mots, nouveau_mot)
    main()


