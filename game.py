import pygame
import Player
from button import Button


class Game:
    def __init__(self):
        self.background = pygame.image.load("assets/war-map-resized-clean.png").convert_alpha()
        self.rect = self.background.get_rect()
        self.player_list = []
        pygame.font.init()
        self.territory_font = pygame.font.SysFont('Army', 40)
        self.height_territories = 300
        self.showing_territories = True
        self.act_plyr = 0
        self.territorios = []
        self.territorios_dict = {}
        self.black_territory_img = pygame.image.load("assets/black-territory.png").convert_alpha()
        self.black_territory_img = pygame.transform.scale(self.black_territory_img, (50, 50))

        self.white_territory_img = pygame.image.load("assets/white-territory.png").convert_alpha()
        self.white_territory_img = pygame.transform.scale(self.white_territory_img, (50, 50))

        self.red_territory_img = pygame.image.load("assets/red-territory.png").convert_alpha()
        self.red_territory_img = pygame.transform.scale(self.red_territory_img, (50, 50))

        self.blue_territory_img = pygame.image.load("assets/blue-territory.png").convert_alpha()
        self.blue_territory_img = pygame.transform.scale(self.blue_territory_img, (50, 50))

        self.yellow_territory_img = pygame.image.load("assets/yellow-territory.png").convert_alpha()
        self.yellow_territory_img = pygame.transform.scale(self.yellow_territory_img, (50, 50))

        self.green_territory_img = pygame.image.load("assets/green-territory.png").convert_alpha()
        self.green_territory_img = pygame.transform.scale(self.green_territory_img, (50, 50))

    def run(self, scr, player_list):
        self.player_list = player_list
        scr.blit(self.background, self.rect)

        for j in self.player_list[0].territorios:
            print(j.nome)

        while self.showing_territories:
            pygame.event.get()
            scr.blit(self.background, self.rect)

            for plyr in self.player_list:
                for terr in plyr.territorios:
                    if terr.continente == 1:
                        self.allocate_territory_color(plyr, terr, scr)
                    if terr.continente == 2:
                        self.allocate_territory_color(plyr, terr, scr)
                    if terr.continente == 3:
                        self.allocate_territory_color(plyr, terr, scr)
                    if terr.continente == 4:
                        self.allocate_territory_color(plyr, terr, scr)
                    if terr.continente == 5:
                        self.allocate_territory_color(plyr, terr, scr)
                    if terr.continente == 6:
                        self.allocate_territory_color(plyr, terr, scr)

            # if self.act_plyr != len(self.player_list):
            #     pygame.event.get()
            #     for i in range(0, len(self.player_list)):
            #         player_text = self.territory_font.render("Jogador" + str(self.player_list[i].cor), False, (0, 0, 0))
            #         scr.blit(player_text, ((i * 400) + 300, 100))
            #         for idx, plyr in enumerate(self.player_list[i].territorios):
            #             territory_text = self.territory_font.render(f"{plyr.idt}: {plyr.nome}", False, (0, 0, 0))
            #             scr.blit(territory_text, ((i * 400) + 300, (idx * 50) + 150))
            #         # self.player_list[i].reserves = self.player_list[i].get_round_reserve()
            #         # self.allocate_reserve_loop(self.player_list[i])

            pygame.display.update()

    def get_allocate_reserve_input(self):
        id = int(input("ID do territorio: "))
        amount = int(input("Escolha a quantidade de tropas para colocar: "))

        return self.territorios_dict[id], amount

    def allocate_reserve_loop(self, player):
        while player.reserves != 0:
            territory, amount = self.get_allocate_reserve_input()
            player.allocate_reserve(territory, amount)

    def allocate_territory_color(self, plyr, terr, scr):
        if plyr.cor == 'white':
            self.territorios_dict[terr.idt] = Button(terr.pos_x, terr.pos_y, self.white_territory_img)
            if self.territorios_dict[terr.idt].draw(scr):
                print('cliquei')
        if plyr.cor == 'black':
            self.territorios_dict[terr.idt] = Button(terr.pos_x, terr.pos_y, self.black_territory_img)
            if self.territorios_dict[terr.idt].draw(scr):
                print('cliquei')
        if plyr.cor == 'red':
            self.territorios_dict[terr.idt] = Button(terr.pos_x, terr.pos_y, self.red_territory_img)
            if self.territorios_dict[terr.idt].draw(scr):
                print('cliquei')
        if plyr.cor == 'blue':
            self.territorios_dict[terr.idt] = Button(terr.pos_x, terr.pos_y, self.blue_territory_img)
            if self.territorios_dict[terr.idt].draw(scr):
                print('cliquei')
        if plyr.cor == 'yellow':
            self.territorios_dict[terr.idt] = Button(terr.pos_x, terr.pos_y, self.yellow_territory_img)
            if self.territorios_dict[terr.idt].draw(scr):
                print('cliquei')
        if plyr.cor == 'green':
            self.territorios_dict[terr.idt] = Button(terr.pos_x, terr.pos_y, self.green_territory_img)
            if self.territorios_dict[terr.idt].draw(scr):
                print('cliquei')


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
