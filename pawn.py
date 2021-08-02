from piece import Piece
from queen import Queen
from knight import Knight
from bishop import Bishop
from rook import Rook


class Pawn(Piece):
    def findAllMoves(self, board):
        moves = []
        if self.color == "white":
            if self.row == 6:
                if (board[5][self.column].piece != None) or (
                    board[4][self.column].piece != None
                ):
                    pass
                else:
                    moves.append((self.row - 2, self.column))

            if self.row - 1 >= 0 and (board[self.row - 1][self.column].piece == None):
                moves.append((self.row - 1, self.column))
            if self.row - 1 >= 0:  # diagonal attack
                if self.column + 1 < 8:
                    if (
                        board[self.row - 1][self.column + 1].piece != None
                        and board[self.row - 1][self.column + 1].piece.color == "black"
                    ):
                        moves.append((self.row - 1, self.column + 1))
                if self.column - 1 >= 0:
                    if (
                        board[self.row - 1][self.column - 1].piece != None
                        and board[self.row - 1][self.column - 1].piece.color == "black"
                    ):
                        moves.append((self.row - 1, self.column - 1))
        else:
            if self.row == 1:
                if (board[2][self.column].piece != None) or (
                    board[3][self.column].piece != None
                ):
                    pass
                else:
                    moves.append((self.row + 2, self.column))

            if self.row + 1 < 8 and (board[self.row + 1][self.column].piece == None):
                moves.append((self.row + 1, self.column))
            if self.row + 1 < 8:  # diagonal attack
                if self.column + 1 < 8:
                    if (
                        board[self.row + 1][self.column + 1].piece != None
                        and board[self.row + 1][self.column + 1].piece.color == "white"
                    ):
                        moves.append((self.row + 1, self.column + 1))
                if self.column - 1 >= 0:
                    if (
                        board[self.row + 1][self.column - 1].piece != None
                        and board[self.row + 1][self.column - 1].piece.color == "white"
                    ):
                        moves.append((self.row + 1, self.column - 1))

        return moves

    def promote(self, board):
        """
        Promote the Pawn to Queen/Knight/Bishop/Rook
        """

        import pygame

        run = True
        color = self.color[0].upper()
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if chr(event.key) == "q":
                        board[self.row][self.column].piece = Queen(
                            self.row, self.column, color + "-q"
                        )
                        return
                    elif chr(event.key) == "k":
                        board[self.row][self.column].piece = Knight(
                            self.row, self.column, color + "-k"
                        )
                        return
                    elif chr(event.key) == "b":
                        board[self.row][self.column].piece = Bishop(
                            self.row, self.column, color + "-b"
                        )
                        return
                    elif chr(event.key) == "r":
                        board[self.row][self.column].piece = Rook(
                            self.row, self.column, color + "-r"
                        )
                        return
                    else:
                        continue
