from piece import Piece


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
