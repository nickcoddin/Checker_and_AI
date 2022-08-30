import pygame

#1. Dimentions
HEIGHT,WIDTH = 800, 800
ROWS, COLS = 8 , 8
SQUARE_SIZE = WIDTH//COLS

#2. colors
BROWN = (170,105,30)
DARK_BROWN = (95,27,27)
LIGHT_WHITE = (220,210,210)
BLACK = (0,0,0)
BLUE = (0,0,255)
GRAY = (148,148,148)

#3. creating kings crown
crown = pygame.image.load("checkers/crown.png")
CROWN = pygame.transform.scale(crown,(30,22))