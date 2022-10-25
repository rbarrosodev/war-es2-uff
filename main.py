from tracemalloc import start
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.window import *
from button import Button
import globals
from main_menu import MainMenu
from game import Game

window = Window(globals.WIDTH, globals.HEIGHT)
main_menu = MainMenu()
game = Game()

while globals.GAME_STATE != 5:
    if globals.GAME_STATE == 0:
        main_menu.run()
    elif globals.GAME_STATE == 1:
        game.run(window)
    
    window.update()

