import pygame
# --------------------------------------------------
# Fonctions & classes pour charger les sprites
# --------------------------------------------------
class Spritesheet():
    def __init__(self,image):
        self.spritesheet = image

    def getimage(self,frame, row, x,y,scale,color):    # x et y = taille du sprite à récupérer
        image = pygame.Surface((x,y)).convert_alpha()   # On crée une image vierge de la taille du sprite
        image.blit(self.spritesheet, (0,0),(frame * x,row * y,x,y))    # On colle sur l'image vierge la frame voulue
        image = pygame.transform.scale(image,(x*scale,y*scale))         # On zoom si besoin avec le paramètre scale
        image.set_colorkey(color)   # couleur transparence
        return image    # La fonction renvoie l'image du sprite extrait

#---Charge une liste d'images dans le sprite sheet, en 2 D, pour l'animation des sprites-------------------------------
def Load_sheet(nomspritesheet, animationstep, taille_sprite_x, taille_sprite_y, zoom):   # Fichier, découpage des animations, taille du sprite
    list = []
    sprite_sheet_image = pygame.image.load(nomspritesheet).convert_alpha()  # Charge spritesheet complet
    sprite_sheet = Spritesheet(sprite_sheet_image)  # appel la classe Spritesheet et charge l'image complète dans l'objet sprite_sheet
    for j in range(0,len(animationstep)):
        for i in range(0,animationstep[j]):
            image = sprite_sheet.getimage(i, j, taille_sprite_x, taille_sprite_y, zoom,(0, 0, 0))  # on stocke l'image découpée dans le spritesheet. Zoom = paramètre
            list.append(image)
    # Retourne la liste des images
    return list

#---Charge une liste d'images depuis le spritesheet pour créer le décor en tuiles-------------------------------------------------------------
def Load_spritesheet_tiles(nomspritesheet, nbcases_x, nbcasesy, taille_sprite_x, taille_sprite_y, zoom):   # Fichier, découpage des animations, taille du sprite, zoom
    list = []
    sprite_sheet_image = pygame.image.load(nomspritesheet).convert_alpha()  # Charge l'image du spritesheet complet
    sprite_sheet = Spritesheet(sprite_sheet_image)                          # appel la classe Spritesheet et charge l'image complète
    for j in range(0,nbcasesy):
        for i in range(0,nbcases_x):
                image = sprite_sheet.getimage(i, j, taille_sprite_x, taille_sprite_y, zoom,(0, 0, 0))  # on stocke l'image découpée dans le spritesheet. Zoom = paramètre
                list.append(image)
    # Retourne la liste des images
    return list
# Fonction qui charge les images des sprites--------------------------------------------------
def load_image(name):
    image = pygame.image.load(name)
    return image
# ----------------------------------------------------------------------------------------------------------------------