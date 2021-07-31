import pygame

pygame.font.init()
font = pygame.font.SysFont("Sans Serif", 30)


class Player:
    """
    This class is mainly for switching turns and calculating remaining turn for individual players
    """

    def __init__(self, color):
        self.color = color
        self.time = 15 * 60  # converting it to second
        if self.color == "white":
            self.turn = True
        else:
            self.turn = False
        self.clock_tick = 0
        self.time_over = False

    def switchTurn(self):
        self.turn = not self.turn

    def displayRemainingTime(self, window, position):
        """
        Calculate and display remaining time
        """
        if self.turn:
            self.clock_tick += 1
            if self.clock_tick >= 10:
                self.clock_tick = 0
                seconds = self.time - 1
                self.time -= 1
            else:
                seconds = self.time
        else:
            seconds = self.time
        if self.time <= 0:  # player looses if his time is over
            self.time_over = True
        minutes = seconds // 60
        seconds -= minutes * 60
        if minutes < 1:
            minutes = "00"
        elif minutes < 10:
            minutes = "0" + str(minutes)
        else:
            minutes = str(minutes)
        if seconds < 1:
            seconds = "00"
        elif seconds < 10:
            seconds = "0" + str(seconds)
        else:
            seconds = str(seconds)
        text = font.render(
            f"Remaining Time: {minutes}:{seconds}", False, (255, 255, 255)
        )
        window.blit(text, (position[0], position[1]))
