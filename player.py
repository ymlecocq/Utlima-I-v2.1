import pygame

from variables import *

from sprites import Load_sheet



# ----------------------------------------------------------------------------------------------------------------------
class Player(pygame.sprite.Sprite):
    def __init__(self, i, j,zoomtuile):
        super().__init__()
        self.sizex = 16                           # taille x du sprite
        self.sizey = 16                           # taille y du sprite
        self.animationstep = [2,2]
        self.imageslist = Load_sheet("Assets/player_16_16_2_2.png", self.animationstep, self.sizex,self.sizey, zoomtuile)
        self.slowframe = 0
        self.frame = 0              # frame pour Direction Est
        self.frame_max = 2         # Frame max & min adaptée pour regarder vers l'Est
        self.frame_min = 0
        self.rect = pygame.Rect((i, j, self.sizex*zoomtuile,self.sizey*zoomtuile))  # Rect adapté à la taille du sprite, zoom compris
        self.rect.x = i*tuile_size
        self.rect.y = j*tuile_size
        self.pos_i = i
        self.pos_j = j
        self.vel = 1


    def draw(self):                                         # function qui affiche le sprite
        self.slowframe += 1
        if self.slowframe > 10:
            self.slowframe = 0
            self.frame += 1
            if self.frame == self.frame_max:    # on a atteind la frame maximale
                self.frame = self.frame_min

        ecran.blit(self.imageslist[self.frame], (self.rect.x, self.rect.y))


    def frame_dir(self,direction):          # on affiche les bons sprites en fonction du changement de direction
        match direction:
            case 3:
                self.frame_max = 16
                self.frame_min = 12
                self.frame = self.frame_min
            case 2:
                self.frame_max = 12
                self.frame_min = 8
                self.frame = self.frame_min
            case 0:
                self.frame_max = 4
                self.frame_min = 0
                self.frame = self.frame_min
            case 1:
                self.frame_max = 8
                self.frame_min = 4
                self.frame = self.frame_min

    def update(self, rayon):
        print("update")
        # Captation des touches du clavier
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_UP] or joyup:  # press up : le joueur va en haut
            if self.pos_j > 0:
                self.pos_j -= 1
        if pressed_keys[pygame.K_DOWN] or joydown:  # press up : le joueur va en bas
            if self.pos_j < nbcases_y+rayon-5:
                print("i : ",self.pos_j)
                print("nbcases_y+rayon : ",nbcases_y+rayon-5)
                self.pos_j += 1
        if pressed_keys[pygame.K_LEFT] or motion[0]<0:  # press up : le joueur va à gauche
            if self.pos_i > 0:
                self.pos_i -= 1
        if pressed_keys[pygame.K_RIGHT] or motion[0]>0 :  # press up : le joueur va à droite
            if self.pos_i < nbcases_x:
                self.pos_i += 1

        if (pressed_keys[pygame.K_SPACE]):
            print("Exit")

