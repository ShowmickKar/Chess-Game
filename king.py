from piece import Piece


class King(Piece):
    def __init__(self, row, column, piece_info):
        super().__init__(row, column, piece_info)
        self.moved = False  # required for castling

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
            """
            Weird bug with king moves. It appends some extra moves to list
            Haven't found the bug yet but the the next two lines fix that
            """
            if abs(move[0] - self.row) > 1 or abs(move[1] - self.column) > 1:
                continue
            piece = board[move[0]][move[1]].piece
            """
            Append to final_moves if it's a valid move
            """
            if piece == None or piece.color != self.color:
                final_moves.append(move)
        if not self.moved:
            castling_cell = board[self.row][self.column + 3]
            if (
                castling_cell.piece != None
                and str(type(castling_cell.piece)) == "<class 'rook.Rook'>"
                and board[self.row][self.column + 1].piece == None
                and board[self.row][self.column + 2].piece == None
            ):
                final_moves.append((self.row, self.column + 2))
        return final_moves
