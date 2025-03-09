import pygame

#-----------------------------------------------------------------------------------------------------------------------
#Variables--------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------

# Define some colors
BLACK = (0, 0, 0)
LIGHT_GREY = (0,50,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0, 0)
PINK = (255,85,255)
CYAN = (85,255,255)


# init joypad
pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
for joystick in joysticks:
    print(joystick.get_name())
motion = [0, 0]         # initialisation des mouvements du joystick
joybuttonx = False
motionx, motiony = 0,0
joyx, joyy, joyup, joydown = False, False, False, False

# Init écran graphique
SCREEN_X = 1024
SCREEN_Y = 768
pygame.init()
size = [SCREEN_X, SCREEN_Y]
ecran = pygame.display.set_mode(size)
pygame.display.set_caption("TbL2D")

clocktimer = 10     # vitesse rafraichissement écran
clock = pygame.time.Clock()

# init sprite groups
all_sprites_list = pygame.sprite.Group()
all_player = pygame.sprite.Group()
all_cases = pygame.sprite.Group()

# Déclaration du tableau bi-dimensionnel
tableau = []

# Taille du tableau
nbcases_x = 128
nbcases_y = 128
tuile_size = 16


