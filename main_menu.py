from PPlay.mouse import *
from button import Button


class MainMenu:
    def __init__(self):
        self.background = pygame.image.load("assets/war-mm.png").convert_alpha()
        self.start_game_img = pygame.image.load("assets/play.png").convert_alpha()
        self.start_game_btn = Button(650, 350, self.start_game_img)
        self.exit_game_img = pygame.image.load("assets/exit.png").convert_alpha()
        self.exit_game_btn = Button(650, 500, self.exit_game_img)
        self.rect = self.background.get_rect()

    def run(self, scr):
        scr.blit(self.background, self.rect)