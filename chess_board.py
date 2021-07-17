import pygame
from board_cell import BoardCell


class ChessBoard:
    board_blueprint = [
        ["B-r", "B-k", "B-b", "B-q", "B-K", "B-b", "B-k", "B-r"],
        ["B-p", "B-p", "B-p", "B-p", "B-p", "B-p", "B-p", "B-p"],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", ""],
        ["W-p", "W-p", "W-p", "W-p", "W-p", "W-p", "W-p", "W-p"],
        ["W-r", "W-k", "W-b", "W-K", "W-q", "W-b", "W-k", "W-r"],
    ]

    def __init__(self, width):
        self.width = width
        self.grid = [
            [
                BoardCell(self.width // 8, (i, j), self.board_blueprint[i][j])
                for j in range(8)
            ]
            for i in range(8)
        ]
        self.current = None

    def place(self, current_position, new_position):
        pass

    def selectCell(self, cell):
        # if cell != None:
        #     moves = cell.piece.moves
        for row in self.grid:
            for board_cell in row:
                # if cell.row == board_cell.row and cell.column == board_cell.column and (cell.row, cell.column) in moves:
                #     self.place()
                if board_cell.selected:
                    board_cell.selected = False
                    if cell != None and cell.piece:
                        cell.selected = True
                    return
        if cell != None and cell.piece:
            cell.selected = True

    def unselectCell(self):
        for row in self.grid:
            for board_cell in row:
                if board_cell.selected:
                    board_cell.selected = False
                    return

    def draw(self, window):
        selected_cell = None
        for row in self.grid:
            for board_cell in row:
                board_cell.draw(window)
                if board_cell.selected:
                    selected_cell = board_cell
        if selected_cell is not None:
            selected_cell.draw(window)
            selected_cell.piece.showAllMoves(window, self.grid)
