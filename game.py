from PPlay.gameimage import *
from PPlay.mouse import *
from button import Button
import globals

class Game:
    def __init__(self):
        self.background = GameImage("assets/war-map.png", 100, 100)
        self.mouse = Mouse()

    def run(self, wd):
        wd.width = 1920
        wd.height = 1033
        globals.WIDTH = 1920
        globals.HEIGHT = 1033
        self.background.draw()
