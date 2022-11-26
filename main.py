from tracemalloc import start

import pygame

from players_selection import PlayersSelection
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.window import *
from button import Button
import globals
from main_menu import MainMenu
from game import Game
import Partida

mainClock = pygame.time.Clock()
pygame.init()
pygame.display.set_caption('WAR')
screen = pygame.display.set_mode((1600, 900))

main_menu = MainMenu()
game = Game()
ps = PlayersSelection()

while globals.GAME_STATE != 50:
    pygame.event.get()
    if globals.GAME_STATE == 0:
        main_menu.run(screen)

        if main_menu.start_game_btn.draw(screen):
            globals.GAME_STATE = 1

        if main_menu.exit_game_btn.draw(screen):
            pygame.quit()
            sys.exit()

    elif globals.GAME_STATE == 1:
        while globals.IN_PLAYER_SELECT is True:
            try:
                ps.run(screen)
            except AttributeError:
                sys.exit()

            pygame.display.update()

    elif globals.GAME_STATE == 2:
        print('entrou')
        Partida.partida(ps.n_players, ps.cores_disponiveis, ps.cores_escolhidas)

    pygame.display.update()
    mainClock.tick(60)
