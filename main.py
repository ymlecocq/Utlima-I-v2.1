import pygame
from sprites import *
import csv
import player

from variables import *

class Case(object):
    def __init__(self, a,posx,posy):
        super().__init__()
        self.image = tuilesspritesheet[a].convert_alpha()  # Charge image dans le spritesheet
        # on agrandi l'image par le zoom demandé
        self.taille_image = self.image.get_size()  # Renvoie un tuple (x,y) ex.: taille_image[0] = 16
        self.big_image = pygame.transform.scale(self.image, (int(self.taille_image[0] * 2), int(self.taille_image[1] * 2)))
        # on agrandi l'image par le zoom demandé
        self.rect = pygame.Rect(posx, posy, 16,16)

    def draw(self):                                         # function qui affiche le sprite
        ecran.blit(self.image,(self.rect.x, self.rect.y))

#------------------------------------------------------------
def tbl_from_map(map,nbcolx,nbcoly):
    x, y = 0, 0
    for i in range(nbcolx * nbcoly):  # on parcourt l'ensemble des cases du tableau
        a = val_map(map, x, y)  # valeur de la map à ces coordonnées x y
        case = Case(a,x * tuile_size,y * tuile_size)
        tableau.append(case)
        x += 1
        if x == nbcolx:
            x = 0
            y += 1
    return(tableau)
#------------------------------------------------------------
def aff_tableau_txt(tableau):
    z = 0
    for i in range(nbcases_x*nbcases_y):  # on parcourt l'ensemble des cases du tableau
        print(' .', end='')
        z += 1
        if z == nbcases_x:
            print()     # passage à la ligne
            z = 0
#------------------------------------------------------------
#------------------------------------------------------------
def aff_global_map(map,tuilesspritesheet, nbcolx,nbcoly,zoom):
    x, y = 0, 0
    for i in range(0, nbcolx * nbcoly):
        a = val_map(map, x, y)
        image = tuilesspritesheet[a].convert_alpha()  # Charge image dans le spritesheet
        taille_image = image.get_size()     # Renvoie un tuple (x,y) ex.: taille_image[0] = 16
        # on agrandi l'image par le zoom demandé
        big_image = pygame.transform.scale(image, (int(taille_image[0] * zoom), int(taille_image[1] * zoom)))
        ecran.blit(big_image,(x * (tuile_size*zoom), y * (tuile_size * zoom)))
        pygame.draw.rect(ecran, LIGHT_GREY, (x * (tuile_size * zoom), y * (tuile_size * zoom), tuile_size*zoom, tuile_size*zoom), 1)
        x += 1
        if x == nbcolx:
            x = 0
            y += 1
    pygame.display.update()  # on affiche le tout
# ----------------------------------------------------------------------------------------------------------------------
def read_csv(filename):
    map = []
    with open(filename,newline='') as data:
        data = csv.reader(data, delimiter=',')
        for row in data:
            # print(list(row))
            map.append(list(row))
    return map
#--Aff global tableau-------------------------------------
def aff_global_tableau(tableau,zoom):
    ecran.fill(BLACK)  # efface l'écran
    # Affichage des cases
    for i in range(0,len(tableau)):
        image = tableau[i].image
        taille_image = image.get_size()  # Renvoie un tuple (x,y) ex.: taille_image[0] = 16
        # # on agrandi l'image par le zoom demandé
        big_image = pygame.transform.scale(image, (int(taille_image[0] * zoom), int(taille_image[1] * zoom)))
        ecran.blit(big_image, (tableau[i].rect.x*zoom,tableau[i].rect.y*zoom))
    pygame.display.update()  # on affiche le tout
#--Aff tableau-------------------------------------
def aff_tableau(tableau,zoom):
    ecran.fill(BLACK)  # efface l'écran
    # Affichage des cases
    for i in range(0,len(tableau)):
        ecran.blit(tableau[i].big_image,(tableau[i].rect.x*zoom,tableau[i].rect.y*zoom))
        # image = tableau[i].image
        # taille_image = image.get_size()  # Renvoie un tuple (x,y) ex.: taille_image[0] = 16
        # # # on agrandi l'image par le zoom demandé
        # big_image = pygame.transform.scale(image, (int(taille_image[0] * zoom), int(taille_image[1] * zoom)))
        # ecran.blit(big_image, (tableau[i].rect.x*zoom,tableau[i].rect.y*zoom))

    for player in all_player:
        player.draw()

    clock.tick(clocktimer)
    pygame.display.update()  # on affiche le tout
# ----------------------------------------------------------------------------------------------------------------------
def val_map(map,i,j):      # Affiche la valeur du tableau aux coordonnées i / j
    a = int(map[j][i])
    return a
#-----------------------------------------------------------------------------------------------------------------------
def aff_player(player):
    ecran.fill(BLACK)  # efface l'écran
    for player in all_player:
        player.draw()

    clock.tick(clocktimer)
    pygame.display.update()  # on affiche le tout
#-----------------------------------------------------------------------------------------------------------------------
#-Programme principal---------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

map = read_csv("Assets/map1.csv")       # Lecture du fichier contenant la map

tuilesspritesheet = Load_spritesheet_tiles("Assets/Spritesheet_Map4_4.png",4,4,tuile_size,tuile_size,1)     # chargement des sprites du spritesheet de la map

tableau = tbl_from_map(map,nbcases_x,nbcases_y)
print(tableau[33].rect.y)

player = player.Player(20,20,2)
all_player.add(player)
all_sprites_list.add(player)

continuer = True

while continuer:

    # Boucle qui tourne pendant le jeu en dehors de la gestion des évènements-------------------------------------------
    # aff_global_map(map, tuilesspritesheet, 32, 32,2)
    aff_tableau(tableau,2)


    # captation des évènements-----------------------------------------------------------------
    for event in pygame.event.get():

        pressed = pygame.key.get_pressed()          # captation des évèvements claviers sous forme de liste
                                                    # permet de capter la répétition des frappes de touches

        if event.type == pygame.JOYAXISMOTION:      # détection stick analogique du joystick
            if event.axis < 2:
                motion[event.axis] = event.value

        # Clic sur la croix fermeture de la fenetre
        if event.type == pygame.QUIT:
            continuer = False
            pygame.quit()

        # Evènements clavier-------------------------------------------------------------------------
        # KEYDOWN permet de savoir si une touche a été pressée
        # moins rapide que get_pressed, permet de n'avoir qu'une seule touche pressée
        if event.type == pygame.KEYDOWN:  # Utilisateur presse une touche
            exit()

