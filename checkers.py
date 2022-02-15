import pygame
import sys

TAN = (210, 180, 140)
BLACK = (0, 0, 0)
RED = (200, 20, 20)
WHITE = (255, 255, 255)
SIZE = 800
ROWS, COLS = 8, 8
SQUARE_SIZE = SIZE // ROWS

class Board():
    def __init__(self):
        self.selected_block = None
        self.whites = 12
        self.blacks = 12
        self.board = []

    def draw_board(self, screen):
        screen.fill(BLACK)
        for row in range(8):
            for col in range(row%2, 8, 2):
                pygame.draw.rect(screen, TAN, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

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

class Piece():
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), SQUARE_SIZE // 3)

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


        b.draw_board(screen)
        b.draw_pieces(screen)

        pygame.display.flip()

if __name__ == '__main__': main()
