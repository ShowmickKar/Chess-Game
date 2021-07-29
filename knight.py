from piece import Piece


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
