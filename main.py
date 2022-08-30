import pygame
from checkers.game import Game
from checkers.constants import HEIGHT,WIDTH,SQUARE_SIZE, DARK_BROWN , LIGHT_WHITE
from checkers.board import Board
from minimax.algorithm import minimax

FPS = 60

#1. creating Display board!
DISPLAY = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Checkers")

#2 creating mouse row and column position!
def get_mouse_pos(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row,col

#3. defining main function!
def main ():
    run = True
    clock = pygame.time.Clock()
    game = Game(DISPLAY)



#4. creating event loop!
    while run:
        clock.tick(FPS)

        if game.turn == LIGHT_WHITE:
            value, new_board = minimax(game.get_board(), 6, LIGHT_WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            run = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_mouse_pos(pos)

                game.select(row,col)

        game.update()


    pygame.quit()

#4. calling main function!
main()
