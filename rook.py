from piece import Piece


class Rook(Piece):
    def __init__(self, row, column, piece_info):
        super().__init__(row, column, piece_info)
        self.moved = False  # required for castling

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
