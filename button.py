import pygame


class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def set_coords(self, x, y):
        self.rect.topleft = (x, y)

    def draw(self, scr):
        action = False

        scr.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()
        pygame.event.get()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        return action
