import pygame


class Game:
    def __init__(self):
        self.background = pygame.image.load("assets/war-map-resized.png").convert_alpha()
        self.rect = self.background.get_rect()

    def run(self, scr):
        scr.blit(self.background, self.rect)