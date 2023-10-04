import pygame
import os
from alert_popup import alert


class Piece:
    def __init__(self, row, column, piece_info):
        print(f"piece_info: {piece_info}")
        self.row, self.column = row, column
        self.color = "white" if piece_info[0] == "W" else "black"
        self.image = pygame.transform.scale(
            pygame.image.load(os.path.join("Assets", piece_info + ".svg")), (70, 70)
        ) # Issue: this hard coded piece size needs to be fixed. Piece size should depend of the board cell size.
        self.moves = []

    def showAllMoves(self, window, grid):
        board = grid.grid
        """
        Show all possible moves of a currently selected piece
        """
        self.moves = []
        """
        Remove some possible moves if they will lead to a CHECK
        """
        temp_moves = self.findAllMoves(board)
        for move in temp_moves:
            current_cell = board[self.row][self.column]
            new_cell = board[move[0]][move[1]]
            """
            Temporarily mutating the board
            """
            self.row, self.column = new_cell.row, new_cell.column
            previous_piece = new_cell.piece  # storing what is currently in the new cell
            new_cell.piece = self
            current_cell.piece = None
            # first find the king's location
            kings_location = (0, 0)
            all_possible_opponent_moves = []
            for row in board:
                for cell in row:
                    if cell.piece != None and cell.piece.color == self.color:
                        piece_type = str(type(cell.piece))
                        if piece_type == "<class 'king.King'>":
                            kings_location = (
                                cell.piece.row,
                                cell.piece.column,
                            )
                            # print("[Alert]: King found")
                            # print(f"[King's Location]: {kings_location}")
                    if cell.piece != None and cell.piece.color != self.color:
                        opponent_moves = cell.piece.findAllMoves(board)
                        if len(opponent_moves):
                            all_possible_opponent_moves.extend(opponent_moves)
            """
            Reverting the temporary move
            """
            self.row, self.column = current_cell.row, current_cell.column
            current_cell.piece = self
            new_cell.piece = previous_piece  # restoring the piece if there's any
            if kings_location not in all_possible_opponent_moves:
                self.moves.append(move)

        color = (65, 105, 225) if self.color == "white" else (222, 49, 99)
        for move in self.moves:
            pygame.draw.circle(window, color, (move[1] * 70 + 56, move[0] * 70 + 56), 9)
        return self.moves

    def move(self, current_cell, new_cell, grid):  # for moving and capturing pieces
        board = grid.grid
        """
        Move the piece if it's a valid move and no possibility of checkmate
        look for castling
        """
        capture = False
        if new_cell.piece != None:
            capture = True

        # First handle castling if there's any
        if (
            str(type(self)) == "<class 'king.King'>"
            and abs(current_cell.column - new_cell.column) > 1
        ):  # Castle
            row = 7 if self.color == "white" else 0
            rook = board[row][7].piece
            board[row][7].piece.column -= 2
            board[row][5].piece = rook
            board[row][7].piece = None

        self.row, self.column = new_cell.row, new_cell.column
        new_cell.piece = self
        current_cell.piece = None

        if (
            str(type(self)) == "<class 'king.King'>"
            or str(type(self)) == "<class 'rook.Rook'>"
        ):
            self.moved = True

        "First Handle Pawn Promotion/ En Passant if there's any"
        if str(type(self)) == "<class 'pawn.Pawn'>":
            if self.row == 0 or self.row == 7:
                alert()  # Creating a pop up window
                self.promote(board)  # promoting the Pawn

        """
        If the opposing player is in check, alert that here
        """
        all_attacking_positions = []
        opposing_kings_location = (-1, -1)
        opposing_player = "black" if self.color == "white" else "white"
        for row in board:
            for cell in row:
                if cell.piece != None:
                    if cell.piece.color != self.color:
                        piece_type = str(type(cell.piece))
                        if piece_type == "<class 'king.King'>":
                            opposing_kings_location = (
                                cell.piece.row,
                                cell.piece.column,
                            )
                            # print("[Alert]: Opponent King Found")
                            # print(
                            #     f"[Opponent King Location]: {opposing_kings_location}"
                            # )

                    else:
                        positions = cell.piece.findAllMoves(board)
                        if len(positions):
                            all_attacking_positions.extend(positions)
        if opposing_kings_location in all_attacking_positions:
            # print("[Alert]: Check")
            grid.check = opposing_player
            grid.check_alert = True
            return
        grid.check = None

        movement_sound = (
            pygame.mixer.Sound("Assets/music/capture.wav")
            if capture
            else pygame.mixer.Sound("Assets/music/move.wav")
        )
        movement_sound.play()

    def render(self, window):
        window.blit(self.image, (self.column * 70 + 20, self.row * 70 + 18))
