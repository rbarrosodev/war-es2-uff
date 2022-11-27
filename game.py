import pygame
import Player
from button import Button


class Game:
    def __init__(self):
        self.background = pygame.image.load("assets/black-bg.jpg").convert_alpha()
        self.rect = self.background.get_rect()
        self.player_list = []
        pygame.font.init()
        self.territory_font = pygame.font.SysFont('Army', 40)
        self.height_territories = 300
        self.showing_territories = True
        self.act_plyr = 0

    def run(self, scr, player_list):
        self.player_list = player_list
        scr.blit(self.background, self.rect)

        while self.showing_territories:
            pygame.event.get()
            scr.blit(self.background, self.rect)

            if self.act_plyr != len(self.player_list):
                pygame.event.get()
                for i in range(0, len(self.player_list)):
                    player_text = self.territory_font.render("Jogador" + str(self.player_list[i].cor), False, (255, 255, 255))
                    scr.blit(player_text, ((i * 400) + 300, 100))
                    for idx, plyr in enumerate(self.player_list[i].territorios):
                        territory_text = self.territory_font.render(f"{plyr.idt}: {plyr.nome}", False, (255, 255, 255))
                        scr.blit(territory_text, ((i * 400) + 300, (idx * 50) + 150))

            pygame.display.update()

        # for player in self.player_list:
        #     if not player.is_npc:
        #         player_text = self.territory_font.render("Jogador" + str(player.cor), False, (255, 255, 255))
        #         scr.blit(player_text, ((scr.get_rect().width / 2) - 500, self.height_territories))
        #
        #         for i in player.territorios:
        #             self.height_territories += 50
        #             territory_text = self.territory_font.render(f"{i.idt}: {i.nome}", False, (255, 255, 255))
        #             scr.blit(territory_text, ((scr.get_rect().width / 2) - 500, self.height_territories))
        #
        #         # player.reserves = player.get_round_reserve()
        #         # self.allocate_reserve_loop(player)
        #     else:
        #         # Realizar Lógica da IA para colocar tropas
        #         pass

    # def print_territories_names(self, scr, plyr):
    #     player_text = self.territory_font.render("Jogador" + str(plyr.cor), False, (255, 255, 255))
    #     scr.blit(player_text, ((scr.get_rect().width / 2) - 500, self.height_territories))
    #
    #     for i in plyr.territorios:
    #         self.height_territories += 50
    #         territory_text = self.territory_font.render(f"{i.idt}: {i.nome}", False, (255, 255, 255))
    #         scr.blit(territory_text, ((scr.get_rect().width / 2) - 500, self.height_territories))
