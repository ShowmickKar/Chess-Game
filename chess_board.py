import pygame
from pygame import mixer
from board_cell import BoardCell
from player import Player

pygame.font.init()
mixer.init()
font = pygame.font.SysFont("Sans Serif", 30)


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

    HORIZONTAL_MAPPING = [chr(i) for i in range(ord("a"), ord("h") + 1)]
    VERTICAL_MAPPING = [i + 1 for i in range(8)]

    def __init__(self, width):
        self.width = width
        self.grid = [
            [
                BoardCell(self.width // 8, (i, j), self.board_blueprint[i][j])
                for j in range(8)
            ]
            for i in range(8)
        ]
        # self.current = None
        self.black = Player("black")
        self.white = Player("white")
        self.check = None
        self.winner = None
        self.check_alert = False
        self.__total_moves = 0

    def place(self, current_position, new_position):
        pass

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
        for row in self.grid:  # checking for movement options
            for board_cell in row:
                if board_cell.selected:
                    selected = (cell.row, cell.column)
                    moves = board_cell.piece.moves
                    if selected in moves:  # move or capture the piece
                        board_cell.piece.move(board_cell, cell, self)
                        self.__total_moves += 1
                        self.unselectCell()
                        self.white.switchTurn()
                        self.black.switchTurn()
                        return
        turn = "white" if self.white.turn else "black"
        for row in self.grid:  # Checking for selection options
            for board_cell in row:
                if board_cell.selected:
                    board_cell.selected = False
                    if board_cell == cell:
                        self.unselectCell()
                        return
                    if cell != None and cell.piece != None and cell.piece.color == turn:
                        cell.selected = True
                    return

        if cell != None and cell.piece != None and cell.piece.color == turn:
            cell.selected = True

    def unselectCell(self):
        for row in self.grid:
            for board_cell in row:
                if board_cell.selected:
                    board_cell.selected = False
                    return

    def draw(self, window):
        if self.white.time <= 0:
            self.winner = "black"
        if self.black.time <= 0:
            self.winner = "white"
        turn = "white" if self.white.turn else "black"
        all_possible_moves = []
        for row in self.grid:
            for cell in row:
                if cell.piece != None and cell.piece.color == turn:
                    moves = cell.piece.showAllMoves(window, self)
                    if len(moves):
                        all_possible_moves.extend(moves)
        # print(self.__total_moves, turn, all_possible_moves)
        if not len(all_possible_moves):
            if self.check == None:
                self.winner = "draw"
            else:
                self.winner = "white" if self.black.turn else "black"

        for i, h in enumerate(self.HORIZONTAL_MAPPING):
            text = font.render(h, False, (255, 255, 255))
            window.blit(text, (i * 70 + 50, 0))
            window.blit(text, (i * 70 + 50, 580))
        for j, v in enumerate(self.VERTICAL_MAPPING):
            text = font.render(str(v), False, (255, 255, 255))
            window.blit(text, (5, j * 70 + 50))
            window.blit(text, (585, j * 70 + 50))
        selected_cell = None
        for row in self.grid:
            for board_cell in row:
                board_cell.draw(window)
                if board_cell.selected:
                    selected_cell = board_cell
        if selected_cell is not None:
            selected_cell.draw(window)
            selected_cell.piece.showAllMoves(window, self)
        if self.winner != None:
            print("Game Finished")
            return
        self.white.displayRemainingTime(window, (760, 570))  # remaining time for white
        self.black.displayRemainingTime(window, (760, 10))  # remaining time for black
        large_font = pygame.font.SysFont("Sans Serif", 50)
        if self.white.turn:
            text = large_font.render("White's Turn", False, (255, 0, 0))
        else:
            text = large_font.render("Black's Turn", False, (255, 0, 0))
        window.blit(text, (700, 270))
        if self.check != None:
            if self.check_alert:
                pygame.mixer.music.load("Assets/music/Alert02.wav")
                pygame.mixer.music.play()
                self.check_alert = False
            medium_font = pygame.font.SysFont("Sans Serif", 45)
            check_alert_location = (750, 510) if self.check == "white" else (750, 90)
            alert = medium_font.render("CHECK!", False, (255, 0, 0))
            window.blit(alert, (check_alert_location))
