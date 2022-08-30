import pygame
from .constants import BLACK, ROWS, BROWN, SQUARE_SIZE, COLS , LIGHT_WHITE , DARK_BROWN
from .piece import Piece
class Board():
    def __init__(self):

    #1. defining board and pieces
        self.board = []
        self.brown_piece = self.white_piece = 12
        self.brown_kings = self.white_kings = 0
        self.creating_board()

    #2. Drawing squares on the Main board!
    def draw_sqr(self,window):

        window.fill(BLACK)

        for row in range(ROWS):
            for col in range (row % 2 , ROWS, 2):
                pygame.draw.rect(window, BROWN, (row*SQUARE_SIZE, col*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

#################################################################################################################
                                            # AI CODES

    ###1. Creating Evaluation method!

    def evaluation(self):
        return self.white_piece - self.brown_piece + (self.white_kings * 0.5 - self.brown_kings * 0.5)

    ###2. from board check the piece and color!

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

##################################################################################################################

    #3. Creating moves!
    def move(self, piece, row, col):
        self.board[piece.row][piece.col], self.board[row][col] = self.board[row][col], self.board[piece.row][piece.col]
        piece.move(row,col)


        # making King
        if row == ROWS-1 or row == 0:
            piece.make_king()
            if piece.color == LIGHT_WHITE:
                self.white_kings +=1
            else:
                self.brown_kings +=1


    #4. Getting piece for the main!
    def get_piece(self, row, col):
        return self.board[row][col]



    #5. Creating Board and Pieces!
    def creating_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col , LIGHT_WHITE ))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, DARK_BROWN))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    #6. putting  Pieces on the board!
    def draw(self, window):
        self.draw_sqr(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece !=0:
                    piece.draw(window)

    #7. Creating piece remove method!
    def remove(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece !=0:
                if piece.color == DARK_BROWN:
                    self.brown_piece -=1
                else:
                    self.white_piece -=1

    #8. Creating Winner method!
    def winner(self):
        if self.brown_piece <=0:
            return LIGHT_WHITE
        elif self.white_piece <=0:
            return DARK_BROWN

        return None


    #9. Creating  valid moves for pieces
    def get_valid_moves(self, piece):
        moves ={}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == DARK_BROWN or piece.king:
            moves.update(self._move_left(row - 1, max(row -3, -1), -1, piece.color, left))
            moves.update(self._move_right(row - 1, max(row - 3, -1), -1, piece.color, right))

        if piece.color == LIGHT_WHITE or piece.king:
            moves.update(self._move_left(row + 1, min(row + 3, ROWS), 1, piece.color, left))
            moves.update(self._move_right(row + 1, min(row + 3, ROWS), 1, piece.color, right))


        return moves

    ##### Main game Logic #####
    #10. Creating left movement!
    def _move_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range (start,stop,step):
            if left < 0:
                break
            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)] = last + skipped
                else:
                    moves[(r,left)] = last

                if last:
                    if step == -1:
                        row = max (r -3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self._move_left(r+step, row ,step, color,left-1, skipped=last))
                    moves.update(self._move_right(r + step, row, step, color, left + 1, skipped=last))
                break
            elif current.color == color:
                break

            else:
                last = [current]

            left -= 1

        return moves


     # 11. Creating right movement!
    def _move_right(self,start, stop, step, color, right, skipped =[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break
            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r - 3, 0)
                    else:
                        row = min(r + 3, ROWS)
                    moves.update(self._move_left(r + step, row, step, color, right - 1, skipped=last))
                    moves.update(self._move_right(r + step, row, step, color, right + 1, skipped=last))
                break
            elif current.color == color:
                break

            else:
                last = [current]

            right += 1

        return  moves






