from PPlay.gameimage import *
from PPlay.mouse import *
from button import Button
import globals

class MainMenu:
    def __init__(self):
        self.background = GameImage("assets/war.png")
        self.play_btn = Button("assets/play.png", 230, 250)
        self.mouse = Mouse()

    def run(self):
        self.background.draw()
        self.play_btn.draw()

        if self.mouse.is_over_object(self.play_btn):
            if self.mouse.is_button_pressed(1):
                globals.GAME_STATE = 1