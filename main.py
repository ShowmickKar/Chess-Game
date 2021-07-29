import pygame
from chess_board import ChessBoard

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = (1000, 600)

BOARD_SIZE = 560


def render_graphics(window, board):
    window.fill((35, 35, 35))
    pygame.draw.rect(window, (100, 149, 237), (0, 0, HEIGHT, HEIGHT))
    board.draw(window)
    pygame.display.update()

def end_screen(window, board, winner):
    pygame.draw.rect(window, (91,96,100), (601, 0, WIDTH - BOARD_SIZE, HEIGHT))
    small_font = pygame.font.SysFont("Sans Serif", 30)
    large_font = pygame.font.SysFont("Sans Serif", 50)
    restart_message = small_font.render("Press ANY KEY to restart", False, (255, 0, 0))
    window.blit(restart_message, (700, 10))
    if winner == "draw":
        message = large_font.render("STALEMATE!", False, (0, 0, 0))
        window.blit(message, (700, 250))
    else:
        winner.upper()
        message = (
            large_font.render("WHITE Wins!", False, (0, 0, 0))
            if winner == "white"
            else large_font.render("BLACK Wins!", False, (0, 0, 0))
        )
        window.blit(message, (700, 250))
    pygame.display.update()


def main():
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Chess Game")
    clock = pygame.time.Clock()
    board = ChessBoard(BOARD_SIZE)
    render_graphics(window, board)
    run = True
    while run:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                cell = board.getCellLocation(pygame.mouse.get_pos())
                if event.button == 1:
                    board.selectCell(cell)
                if event.button == 3:
                    board.unselectCell()
            if event.type == pygame.KEYDOWN:
                if board.winner != None:
                    """
                    Restart the Game
                    """
                    pygame.time.delay(2000)
                    main()
        if board.winner != None:
            end_screen(window, board, board.winner)
            continue

        render_graphics(window, board)


if __name__ == "__main__":
    main()
