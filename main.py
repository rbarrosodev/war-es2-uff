from tracemalloc import start

import pygame

from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.window import *
from button import Button
import globals
from main_menu import MainMenu
from game import Game

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('WAR')
screen = pygame.display.set_mode((1600, 900))

main_menu = MainMenu()
game = Game()

while globals.GAME_STATE != 5:
    if globals.GAME_STATE == 0:
        main_menu.run(screen)
    if main_menu.start_game_btn.draw(screen):
        globals.GAME_STATE = 1
    if main_menu.exit_game_btn.draw(screen):
        pygame.quit()
        sys.exit()

    elif globals.GAME_STATE == 1:
        game.run(screen)

    pygame.display.update()
    mainClock.tick(60)

