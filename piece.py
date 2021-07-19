import pygame
import os


class Piece:
    def __init__(self, row, column, piece_info):
        self.row, self.column = row, column
        self.color = "white" if piece_info[0] == "W" else "black"
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", piece_info + ".svg")), (70, 70)
        )
        self.moves = []

    def showAllMoves(self, window, board):
        """
        Show all possible moves of a currently selected piece
        """
        self.moves = self.findAllMoves(board)
        color = (0, 0, 255) if self.color == "white" else (255, 0, 0)
        for move in self.moves:
            pygame.draw.circle(window, color, (move[1] * 70 + 56, move[0] * 70 + 56), 9)

    def move(self, current_cell, new_cell, board):  # for moving and capturing pieces
        """
        Move the piece if it's a valid move and no possibility of checkmate
        look for castling
        """
        self.row, self.column = new_cell.row, new_cell.column
        new_cell.piece = self
        current_cell.piece = None

    def render(self, window):
        window.blit(self.image, (self.column * 70 + 20, self.row * 70 + 18))


class King(Piece):
    def isCastlingAvailable(self):
        pass

    def isChecked(self):
        pass

    def findAllMoves(self, board):  # also check for castling and checks
        moves = []
        if self.row - 1 >= 0:
            moves.append((self.row - 1, self.column))
            if self.column - 1 >= 0:
                moves.append((self.row - 1, self.column - 1))
            if self.column + 1 < 8:
                moves.append((self.row - 1, self.column + 1))
        if self.row + 1 < 8:
            moves.append((self.row + 1, self.column))
            if self.column - 1 >= 0:
                moves.append((self.row + 1, self.column - 1))
            if self.column + 1 < 8:
                moves.append((self.row + 1, self.column + 1))
        if self.column - 1 >= 0:
            moves.append((self.row, self.column - 1))
            if self.row - 1 >= 0:
                moves.append((self.row - 1, self.column - 1))
            if self.row + 1 < 8:
                moves.append((self.row + 1, self.row - 1))
        if self.column + 1 < 8:
            moves.append((self.row, self.column + 1))
            if self.row - 1 >= 0:
                moves.append((self.row - 1, self.column + 1))
            if self.row + 1 < 8:
                moves.append((self.row + 1, self.column + 1))
        final_moves = []
        # remove moves if there's a chance of check
        for move in moves:
            piece = board[move[0]][move[1]].piece
            if piece == None or piece.color != self.color:
                final_moves.append(move)
        return final_moves


class Queen(Piece):
    def findAllMoves(self, board):
        moves = []
        i, j = self.row - 1, self.column - 1
        while i >= 0 and j >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
            j -= 1
        i, j = self.row + 1, self.column - 1
        while i < 8 and j >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
            j -= 1
        i, j = self.row + 1, self.column + 1
        while i < 8 and j < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
            j += 1
        i, j = self.row - 1, self.column + 1
        while i >= 0 and j < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
            j += 1
        i, j = self.row - 1, self.column
        while i >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
        i, j = self.row + 1, self.column
        while i < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
        i, j = self.row, self.column - 1
        while j >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j -= 1
        i, j = self.row, self.column + 1
        while j < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j += 1
        return moves


class Bishop(Piece):
    def findAllMoves(self, board):
        moves = []
        i, j = self.row - 1, self.column - 1
        while i >= 0 and j >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
            j -= 1
        i, j = self.row + 1, self.column - 1
        while i < 8 and j >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
            j -= 1
        i, j = self.row + 1, self.column + 1
        while i < 8 and j < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
            j += 1
        i, j = self.row - 1, self.column + 1
        while i >= 0 and j < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
            j += 1
        return moves


class Knight(Piece):
    def findAllMoves(self, board):
        moves = []
        if self.row - 1 >= 0:
            if self.column - 2 >= 0 and (
                board[self.row - 1][self.column - 2].piece == None
                or board[self.row - 1][self.column - 2].piece.color != self.color
            ):
                moves.append((self.row - 1, self.column - 2))
            if self.column + 2 < 8 and (
                board[self.row - 1][self.column + 2].piece == None
                or board[self.row - 1][self.column + 2].piece.color != self.color
            ):
                moves.append((self.row - 1, self.column + 2))
        if self.row - 2 >= 0:
            if self.column - 1 >= 0 and (
                board[self.row - 2][self.column - 1].piece == None
                or board[self.row - 2][self.column - 1].piece.color != self.color
            ):
                moves.append((self.row - 2, self.column - 1))
            if self.column + 1 < 8 and (
                board[self.row - 2][self.column + 1].piece == None
                or board[self.row - 2][self.column + 1].piece.color != self.color
            ):
                moves.append((self.row - 2, self.column + 1))
        if self.row + 1 < 8:
            if self.column - 2 >= 0 and (
                board[self.row + 1][self.column - 2].piece == None
                or board[self.row + 1][self.column - 2].piece.color != self.color
            ):
                moves.append((self.row + 1, self.column - 2))
            if self.column + 2 < 8 and (
                board[self.row + 1][self.column + 2].piece == None
                or board[self.row + 1][self.column + 2].piece.color != self.color
            ):
                moves.append((self.row + 1, self.column + 2))
        if self.row + 2 < 8:
            if self.column - 1 >= 0 and (
                board[self.row + 2][self.column - 1].piece == None
                or board[self.row + 2][self.column - 1].piece.color != self.color
            ):
                moves.append((self.row + 2, self.column - 1))
            if self.column + 1 < 8 and (
                board[self.row + 2][self.column + 1].piece == None
                or board[self.row + 2][self.column + 1].piece.color != self.color
            ):
                moves.append((self.row + 2, self.column + 1))
        return moves


class Rook(Piece):
    def findAllMoves(self, board):
        moves = []
        i, j = self.row - 1, self.column
        while i >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i -= 1
        i, j = self.row + 1, self.column
        while i < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            i += 1
        i, j = self.row, self.column - 1
        while j >= 0:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j -= 1
        i, j = self.row, self.column + 1
        while j < 8:
            if board[i][j].piece != None:
                if self.color != board[i][j].piece.color:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j += 1
        return moves


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
