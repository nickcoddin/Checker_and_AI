import pygame
from .board import Board
from .constants import DARK_BROWN, LIGHT_WHITE, SQUARE_SIZE, BLUE


class Game:

    #1. Defining Board options!
    def __init__(self, window):
         self._init()
         self.window = window

    #2. Creating update method!
    def update(self):
        self.board.draw(self.window)
        self.draw_moves(self.valid_moves)
        pygame.display.update()

    #3. Creating Board option (private)!
    def _init(self):
        self.selected_piece = None
        self.board = Board()
        self.turn = DARK_BROWN
        self.valid_moves = {}

    # 4. Defining Winner!
    def winner(self):
       return self.board.winner()

    #5. Creating reset method for restarting game!
    def reset(self):
        self._init()

    #6. Creating Select mode!
    def select(self,row, col):
        if self.selected_piece:
            result = self._move(row, col)
            if not result:
                self.selected_piece = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected_piece = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    #7. Creating Move mode (private)!
    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected_piece and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected_piece,row,col)
            skipped = self.valid_moves[(row,col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False

        return True

    #8. Creating dots for showing moves
    def draw_moves(self,moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.window, BLUE, (col*SQUARE_SIZE + SQUARE_SIZE//2, row*SQUARE_SIZE + SQUARE_SIZE//2), 8)


    #9. Creating turn changing method!
    def change_turn(self):
        self.valid_moves = {}
        if self.turn == DARK_BROWN:
            self.turn = LIGHT_WHITE
        else:
            self.turn = DARK_BROWN

    #10. function that returns board!
    def get_board(self):
        return self.board

    #11. function that updates board after every AI move!
    def ai_move(self, board):
        self.board = board
        self.change_turn()



