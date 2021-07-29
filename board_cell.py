import pygame
from king import King
from queen import Queen
from bishop import Bishop
from knight import Knight
from rook import Rook
from pawn import Pawn

WHITE = (240, 240, 255)
BLACK = (135, 206, 235)


class BoardCell:
    def __init__(self, size, index, contains):
        self.size = size
        self.row = index[0]
        self.column = index[1]
        if not len(contains):
            self.piece = None
        else:
            self.piece = self.__assignPiece(contains)

        self.__assignColor()
        self.selected = False

    def __assignColor(self):
        if self.row % 2 == 0:
            if self.column % 2 == 0:
                self.color = WHITE
            else:
                self.color = BLACK
        else:
            if self.column % 2 == 0:
                self.color = BLACK
            else:
                self.color = WHITE

    def __assignPiece(self, contains):
        if contains[2] == "K":
            return King(self.row, self.column, contains)
        elif contains[2] == "q":
            return Queen(self.row, self.column, contains)
        elif contains[2] == "b":
            return Bishop(self.row, self.column, contains)
        elif contains[2] == "k":
            return Knight(self.row, self.column, contains)
        elif contains[2] == "r":
            return Rook(self.row, self.column, contains)
        elif contains[2] == "p":
            return Pawn(self.row, self.column, contains)

    def draw(self, window):
        if self.selected:
            if self.piece.color == "white":
                color = (65, 105, 225)
            else:
                color = (222, 49, 99)
            pygame.draw.rect(
                window,
                color,
                (
                    self.column * self.size + 17,
                    self.row * self.size + 17,
                    self.size + 6,
                    self.size + 6,
                ),
            )

        pygame.draw.rect(
            window,
            self.color,
            (
                self.column * self.size + 20,
                self.row * self.size + 20,
                self.size,
                self.size,
            ),
        )
        if self.piece is not None:
            self.piece.render(window)
