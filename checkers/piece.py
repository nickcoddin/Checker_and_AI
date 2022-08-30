from .constants import DARK_BROWN, SQUARE_SIZE ,GRAY, CROWN
import pygame

class Piece:
    PADDING = 20
    OUTLINE = 2

    #1. initiate variables
    def __init__(self, row, col , color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_pos()

    #2. Calculating positions inside Suqare!
    def calc_pos(self):

        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    #3. defining KING!
    def make_king(self):
        self.king = True

    #4. Drowing pieces inside the suqares
    def draw(self, window):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(window, GRAY, (self.x ,self.y), radius + self.OUTLINE )
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
        if self.king:
            window.blit(CROWN,(self.x - CROWN.get_width()//2, self.y - CROWN.get_height()//2) )

    #5. Creating move method
    def move(self, row, col):
        self.row = row
        self.col = col
        self.calc_pos()

    #.Representation for debugging
    def __repr__(self):
        return str(self.color)
