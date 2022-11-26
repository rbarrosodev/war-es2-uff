import sys

import pygame
import Partida
from button import Button
import globals


class PlayersSelection:
    def __init__(self):
        self.CORES = ["branco", "preto", "vermelho", "azul", "amarelo", "verde"]
        self.n_players = 0
        self.actual_player = 1
        self.player_selecting = True
        self.cores_disponiveis = [True] * len(self.CORES)
        self.cores_escolhidas = []
        self.background = pygame.image.load("assets/playerselect.jpg").convert_alpha()
        self.two_players_img = pygame.image.load("assets/2-players.png").convert_alpha()
        self.two_players_btn = Button(450, 600, self.two_players_img)

        self.three_players_img = pygame.image.load("assets/3-players.png").convert_alpha()
        self.three_players_btn = Button(600, 600, self.three_players_img)

        self.four_players_img = pygame.image.load("assets/4-players.png").convert_alpha()
        self.four_players_btn = Button(750, 600, self.four_players_img)

        self.five_players_img = pygame.image.load("assets/5-players.png").convert_alpha()
        self.five_players_btn = Button(900, 600, self.five_players_img)

        self.six_players_img = pygame.image.load("assets/6-players.png").convert_alpha()
        self.six_players_btn = Button(1050, 600, self.six_players_img)

        self.rect = self.background.get_rect()
        pygame.font.init()
        self.my_font = pygame.font.SysFont('Army', 72)

    def run(self, scr):
        player_text = self.my_font.render('Quantos jogadores?', False, (255, 255, 255))
        scr.blit(self.background, self.rect)
        scr.blit(player_text, ((scr.get_rect().width / 2) - 350, 200))

        if self.two_players_btn.draw(scr):
            self.n_players = 2
            globals.GAME_STATE = 2
        if self.three_players_btn.draw(scr):
            self.n_players = 3
            globals.GAME_STATE = 2
        if self.four_players_btn.draw(scr):
            self.n_players = 4
            globals.GAME_STATE = 2
        if self.five_players_btn.draw(scr):
            self.n_players = 5
            globals.GAME_STATE = 2
        if self.six_players_btn.draw(scr):
            self.n_players = 6
            globals.GAME_STATE = 2

        if globals.GAME_STATE == 2:
            self.color_select(self.n_players, scr)

    def color_select(self, n_players, scr):
        white_plyr_img = pygame.image.load("assets/white-player.png").convert_alpha()
        white_plyr_btn = Button(450, 350, white_plyr_img)

        black_plyr_img = pygame.image.load("assets/black-player.png").convert_alpha()
        black_plyr_btn = Button(600, 350, black_plyr_img)

        red_plyr_img = pygame.image.load("assets/red-player.png").convert_alpha()
        red_plyr_btn = Button(750, 350, red_plyr_img)

        blue_plyr_img = pygame.image.load("assets/blue-player.png").convert_alpha()
        blue_plyr_btn = Button(900, 350, blue_plyr_img)

        yellow_plyr_img = pygame.image.load("assets/yellow-player.png").convert_alpha()
        yellow_plyr_btn = Button(1050, 350, yellow_plyr_img)

        green_plyr_img = pygame.image.load("assets/green-player.png").convert_alpha()
        green_plyr_btn = Button(1200, 350, green_plyr_img)

        while self.player_selecting:
            if self.actual_player == n_players + 1:
                globals.IN_PLAYER_SELECT = False
                globals.GAME_STATE = 2
                return
            pygame.event.get()
            scr.blit(self.background, self.rect)
            player_text = self.my_font.render(f"Jogador {self.actual_player} escolha a sua cor:", False,
                                              (255, 255, 255))
            scr.blit(player_text, ((scr.get_rect().width / 2) - 500, 200))

            if white_plyr_btn.draw(scr):
                self.cores_disponiveis[0] = False
                cor = self.CORES[0]
                self.cores_escolhidas.append(cor)
                print(self.cores_escolhidas)
                self.actual_player += 1
            if black_plyr_btn.draw(scr):
                self.cores_disponiveis[1] = False
                cor = self.CORES[1]
                self.cores_escolhidas.append(cor)
                print(self.cores_escolhidas)
            if red_plyr_btn.draw(scr):
                self.cores_disponiveis[2] = False
                cor = self.CORES[2]
                self.cores_escolhidas.append(cor)
            if blue_plyr_btn.draw(scr):
                self.cores_disponiveis[3] = False
                cor = self.CORES[3]
                self.cores_escolhidas.append(cor)
            if yellow_plyr_btn.draw(scr):
                self.cores_disponiveis[4] = False
                cor = self.CORES[4]
                self.cores_escolhidas.append(cor)
            if green_plyr_btn.draw(scr):
                self.cores_disponiveis[5] = False
                cor = self.CORES[5]
                self.cores_escolhidas.append(cor)

            pygame.display.update()
