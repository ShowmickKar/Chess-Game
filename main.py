import pygame
from board_cell import BoardCell
from chess_board import ChessBoard

WIDTH, HEIGHT = (1200, 600)

BOARD_SIZE = 560


def render_graphics(window, board):
    window.fill((35, 35, 35))
    board.draw(window)
    pygame.display.update()


def get_cell_location(position, board):
    x, y = position[0] - 20, position[1] - 20
    for row in board.grid:
        for cell in row:
            if (
                cell.row * cell.size <= y <= cell.row * cell.size + cell.size
                and cell.column * cell.size <= x <= cell.column * cell.size + cell.size
            ):
                return cell


def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Online Chess Game")
    clock = pygame.time.Clock()
    board = ChessBoard(BOARD_SIZE)
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEMOTION:
                pass
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = get_cell_location(pygame.mouse.get_pos(), board)
                if event.button == 1:
                    board.selectCell(cell)
                if event.button == 3:
                    board.unselectCell()
        render_graphics(window, board)
        clock.tick(10)


if __name__ == "__main__":
    main()
