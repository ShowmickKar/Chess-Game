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
        ["W-r", "W-k", "W-b", "W-q", "W-K", "W-b", "W-k", "W-r"],
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
        self.turn = "white"

    def place(self, current_position, new_position):
        pass

    def switchTurn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    def getCellLocation(self, position):
        x, y = position[0] - 20, position[1] - 20
        for row in self.grid:
            for cell in row:
                if (
                    cell.row * cell.size <= y <= cell.row * cell.size + cell.size
                    and cell.column * cell.size
                    <= x
                    <= cell.column * cell.size + cell.size
                ):
                    return cell

    def selectCell(self, cell):
        # if cell == None:
        #     return
        for row in self.grid:  # checking for movement options
            for board_cell in row:
                if board_cell.selected:
                    selected = (cell.row, cell.column)
                    moves = board_cell.piece.moves
                    if selected in moves:  # move or capture the piece
                        board_cell.piece.move(board_cell, cell, self.grid)
                        self.unselectCell()
                        self.switchTurn()
                        return

        for row in self.grid:  # Checking for selection options
            for board_cell in row:
                if board_cell.selected:
                    board_cell.selected = False
                    if board_cell == cell:
                        self.unselectCell()
                        return
                    if (
                        cell != None
                        and cell.piece != None
                        and cell.piece.color == self.turn
                    ):
                        cell.selected = True
                    return
        if cell != None and cell.piece != None and cell.piece.color == self.turn:
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
