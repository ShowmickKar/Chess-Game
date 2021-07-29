from piece import Piece


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
