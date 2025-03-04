#------------------------------------#
# Bibliothèque de fonctions diverses #
#------------------------------------#

import pygame
import variables as var
from variables import LIGHT_GREY, WHITE


# from variables import *

#----Fonction pour écrire à l'écran-------------------------------------------------------------------------------------
def ecrit(texte,couleur,size, x, y,police):

    if police == "":
        font = pygame.freetype.Font(None, size)
    else:
        font = pygame.freetype.Font("Assets/retro.ttf", size)

    text_surf2, text_rect2 = font.render(texte,couleur)     # font.render permet d'avoir une transparence
    var.ecran.blit(text_surf2, (x, y))

#----Fonction pour écrire à l'écran sur un fond-------------------------------------------------------------------------
def ecrit_menu(texte,x, y,longueur,largeur):
    pygame.draw.rect(var.ecran,LIGHT_GREY,pygame.Rect(x,y,longueur,largeur))
    font = pygame.freetype.Font("Assets/retro.ttf", 40)

    text_surf2, text_rect2 = font.render(texte,WHITE)     # font.render permet d'avoir une transparence
    var.ecran.blit(text_surf2, (x, y))