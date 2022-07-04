import math
import pygame
import sys
import random

TAN = (210, 180, 140)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (200, 20, 20)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
SIZE = 800
ROWS, COLS = 8, 8
SQUARE_SIZE = SIZE // ROWS

class Board():
    def __init__(self):
        self.selected_block = None
        self.whites = 12
        self.reds = 12
        self.board = []
        self.turn = random.choice([1, -1])
        self.double_blocks = list()
        self.double_jump = False
        self.jumper = None

    def draw_board(self, screen):
        screen.fill(BLACK)
        for row in range(8):
            for col in range(row%2, 8, 2):
                pygame.draw.rect(screen, TAN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

            for col in range(row%2-1, 8, 2):
                if [row, col] == self.selected_block:
                    pygame.draw.rect(screen, GREEN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

            for col in range(row%2-1, 8, 2):
                if [row, col] in self.double_blocks:
                    pygame.draw.rect(screen, BLUE, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 3)

    def init(self):
        for i in range(8):
            self.board.append([0 for i in range(8)])
        for row in range(3):
            for col in range(8):
                if row%2 == 0 and col%2 == 1 or row%2 == 1 and col%2 == 0:
                    self.board[row][col] = Piece(row, col, RED)
        for row in range(5, 8):
            for col in range(8):
                if row%2 == 1 and col%2 == 0 or row%2 == 0 and col%2 == 1:
                    self.board[row][col] = Piece(row, col, WHITE)

    def draw_pieces(self, screen):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col] != 0:
                    self.board[row][col].draw(screen)

    def move_piece(self, screen, selected_block, row, col):
        #initialize the new piece that will be moved
        temp = self.board[selected_block[1]][selected_block[0]]
        temp.row = row
        temp.col = col
        temp.make_pos()

        # set the previous click to 0 so it will have no piece anymore
        self.board[selected_block[1]][selected_block[0]] = 0

        # set the new click to the new piece to move it
        self.board[row][col] = temp

    def correct_piece(self, piece_color, turn):
        if (
            (turn == 1 and piece_color == WHITE) or
            (turn == -1 and piece_color == RED)
        ):
            return True
        else:
            return False

    def check_double(self, row, col):
        piece = self.board[row][col]
        if piece.king == False:
            if piece.color == WHITE:

                # ** wip ** #

                # all the possible pieces that could be jumped
                possible = []
                if (row - 1 >= 0 and col + 1 < 8):
                    if self.board[row - 1][col + 1] != 0:
                        possible.append(self.board[row - 1][col + 1])
                if (row - 1 >= 0 and col - 1 >= 0):
                    if self.board[row - 1][col - 1] != 0:
                        possible.append(self.board[row - 1][col - 1])
                print(possible)
                for i in possible:
                    if i != 0:

                        # check if there is valid space on the board and if this space contains a piece for each if clause
                        if col+1 == i.col:
                            if i.col + 1 < 8 and i.row - 1 >= 0:
                                if self.board[i.row - 1][i.col + 1] == 0:
                                    self.double_blocks.append([i.col + 1, i.row - 1])
                        elif col-1 == i.col:
                            if i.col - 1 >= 0 and i.row - 1 >= 0:
                                if self.board[i.row - 1][i.col - 1] == 0:
                                    self.double_blocks.append([i.col - 1, i.row - 1])

            elif piece.color == RED:

                # all the possible pieces that could be jumped
                possible = []
                if (row + 1 < 8 and col + 1 < 8):
                    if self.board[row + 1][col + 1] != 0:
                        possible.append(self.board[row + 1][col + 1])
                if (row + 1 < 8 and col - 1 >= 0):
                    if self.board[row + 1][col - 1] != 0:
                        possible.append(self.board[row + 1][col - 1])
                print(possible)
                for i in possible:
                    if i != 0:

                        # check if there is valid space on the board and if this space contains a piece for each if clause
                        if col+1 == i.col:
                            if i.col + 1 < 8 and i.row + 1 < 8:
                                if self.board[i.row + 1][i.col + 1] == 0:
                                    self.double_blocks.append([i.col + 1, i.row + 1])
                        elif col-1 == i.col:
                            if i.col - 1 >= 0 and i.row + 1 < 8:
                                if self.board[i.row + 1][i.col - 1] == 0:
                                    self.double_blocks.append([i.col - 1, i.row + 1])



        elif piece.king == True:
            if (
                    self.board[row + 1][col + 1] != 0 or
                    self.board[row + 1][col - 1] != 0 or
                    self.board[row - 1][col + 1] != 0 or
                    self.board[row - 1][col - 1] != 0
                ):
                possible = []
                if (row + 1 < 8 and col + 1 < 8):
                    if self.board[row + 1][col + 1] != 0:
                        possible.append(self.board[row + 1][col + 1])
                if (row + 1 < 8 and col - 1 >= 0):
                    if self.board[row + 1][col - 1] != 0:
                        possible.append(self.board[row + 1][col - 1])
                if (row - 1 >= 0 and col + 1 < 8):
                    if self.board[row - 1][col + 1] != 0:
                        possible.append(self.board[row - 1][col + 1])
                if (row - 1 >= 0 and col - 1 >= 0):
                    if self.board[row - 1][col - 1] != 0:
                        possible.append(self.board[row - 1][col - 1])
                for i in possible:
                    if i != 0:
                        if col+1 == i.col:
                            if i.col + 1 < 8 and i.row + 1 < 8 and row + 1 == i.row:
                                if self.board[i.row + 1][i.col + 1] == 0:
                                    self.double_blocks.append([i.col + 1, i.row + 1])
                            if i.col + 1 < 8 and i.row - 1 >= 0 and row - 1 == i.row:
                                if self.board[i.row - 1][i.col + 1] == 0:
                                    self.double_blocks.append([i.col + 1, i.row - 1])

                        elif col-1 == i.col:
                            if i.col - 1 >= 0 and i.row + 1 < 8 and i.row == row + 1:
                                if self.board[i.row + 1][i.col - 1] == 0:
                                    self.double_blocks.append([i.col - 1, i.row + 1])

                            if i.col - 1 >= 0 and i.row - 1 >= 0 and i.row == row-1:
                                    if self.board[i.row - 1][i.col - 1] == 0:
                                        self.double_blocks.append([i.col - 1, i.row - 1])
        if len(self.double_blocks) > 0:
            self.jumper = self.board[row][col]




    def jump(self, row, col, prev_col, prev_row, screen):
        self.double_blocks.clear()
        if self.board[int((prev_row + row)/2)][int((prev_col + col)/2)].color == WHITE:
            self.whites -= 1
        else:
            self.reds -= 1
        self.board[int((prev_row + row)/2)][int((prev_col + col)/2)] = 0
        self.move_piece(screen, self.selected_block, row, col)
        self.selected_block.clear()
        self.check_double(row, col)
        self.double_jump = not (len(self.double_blocks) == 0)
        self.board[row][col].check_king()
        if self.double_jump == False:
            self.turn *= -1

    def select(self, screen, x, y):
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE
        if self.selected_block != None:

            prev_row = self.selected_block[1]
            prev_col = self.selected_block[0]
            previous_move = self.board[prev_row][prev_col]
            move = self.board[row][col]

            if previous_move != 0:
                if move == 0: #if there is a piece on the previous click and no piece on the new click (hence a valid move)
                    if not ((row % 2 == 0 and col % 2 == 0) or (row % 2 != 0 and col % 2 != 0)): # check if move square is black
                        if row - 1 == prev_row or row + 1 == prev_row:
                            if (
                                    (previous_move.king == True or
                                    (previous_move.color == WHITE and row + 1 == prev_row) or
                                    (previous_move.color == RED and row - 1 == prev_row)
                                    ) and self.double_jump == False
                                ):  # king or move forward

                                if self.correct_piece(previous_move.color, self.turn):
                                    self.move_piece(screen, self.selected_block, row, col)
                                    self.selected_block.clear()
                                    self.turn *= -1
                                    self.board[row][col].check_king()
                        elif (
                                (previous_move.king == True or
                                row - 2 == prev_row or row + 2 == prev_row) and
                                self.board[int((prev_row + row)/2)][int((prev_col + col)/2)] != 0
                              ):
                            if self.board[int((prev_row + row)/2)][int((prev_col + col)/2)].color != self.board[prev_row][prev_col].color:
                                if self.correct_piece(previous_move.color, self.turn) and self.double_jump == False:
                                    self.jump(row, col, prev_col, prev_row, screen)

                                if self.correct_piece and self.double_jump == True and [col, row] in self.double_blocks and self.jumper == self.board[prev_row][prev_col]:
                                    self.jump(row, col, prev_col, prev_row, screen)

        self.selected_block = [col, row]

class Piece():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.kingImg = pygame.image.load('star-removebg-preview.png')
        self.kingImg = pygame.transform.scale(self.kingImg, (30, 30))

        self.make_pos()

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), SQUARE_SIZE // 3)
        if self.king == True:
            screen.blit(self.kingImg, (self.x - 15, self.y - 15))

    def make_pos(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def check_king(self):
        if self.color == WHITE and self.row == 0:
            self.king = True
        if self.color == RED and self.row == 7:
            self.king = True

def main():
    pygame.init()
    screen = pygame.display.set_mode((SIZE, SIZE))
    pygame.display.set_caption('checkers')
    b = Board()
    b.init()
    while True:
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                sys.exit()
            if e.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                b.select(screen, x, y)

        b.draw_board(screen)
        b.draw_pieces(screen)

        pygame.display.flip()

if __name__ == '__main__': main()
