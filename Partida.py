# from asyncio.windows_events import NULL
from pickle import TRUE
import random

from collections import deque
from re import A

import Player
import CartaObj
from territorio import territorio

CORES = ["branco", "preto", "vermelho", "azul", "amarelo", "verde"]


class partida:
    def __init__(self, n_humans, cores_disponiveis, cores_escolhidas, n_players=6):
        self.n_players = min(n_players, 6)
        self.n_humans = min(n_humans, n_players)  # num de players
        self.n_npcs = n_players - n_humans  # num de ias
        self.num_rodada = 0
        self.v_player = []
        self.npcs = []
        self.cores_disponiveis = cores_disponiveis
        self.cores_escolhidas = cores_escolhidas
        # players + npc
        self.players_list = []
        self.territorios_dict = {}  # Dicionario de territórios para ser acessado pela partida
        self.over = False

        # embaralhar as cartas objetivo e distribuí-las(várias maneiras de fazer isso)Ainda não implementei
        goal_cards = CartaObj.cartaObj.gerar_cartas()
        random.shuffle(goal_cards)
        self.goal_cards = goal_cards[: self.n_players]

        # criar jogadores
        self.v_player = []
        for cor, card in zip(self.cores_escolhidas, self.goal_cards[:self.n_humans]):
            plyr = Player.player(card, True, cor, False)
            self.v_player.append(plyr)

        # ---------------------------------------------------------------------
        # inicializar npc
        self.npcs = []
        # if self.n_npcs != 0:
        #     remaining_colors = [cor for i, cor in enumerate(CORES) if self.cores_disponiveis[i]]
        #     npc_goal_cards = self.goal_cards[self.n_humans:]
        #     for cor, card in zip(remaining_colors, npc_goal_cards):
        #         self.npcs.append(Player.player(card, True, cor, True))

                # ---------------------------------------------------------------------
        # distribuicao de territorios 
        self.territorios_dict, territorios = territorio.get_territorios()
        random.shuffle(territorios)
        players = deque(self.v_player + self.npcs)  # Total de membros na partida
        for terr in territorios:
            player = players[0]
            terr.player = player
            terr.tropas = 1
            player.territorios.append(terr)
            players.rotate()

        # Lista geral (players + npc)
        self.players_list = list(players)
        print(self.players_list)

        # # Inicio do jogo
        # for player in (self.players_list):
        #     if not player.is_npc:
        #         player.print_territories_names()
        #
        #         player.reserves = player.get_round_reserve()
        #         # self.allocate_reserve_loop(player)
        #     else:
        #         # Realizar Lógica da IA para colocar tropas
        #         pass
        #
        # # Após preparação, iniciar game_loop
        # self.game_loop()

    # Fase inicial da rodada
    def fase_de_tropas(self, player):
        print("FASE DE TROPAS PLAYER: " + str(player.cor))
        print("-------------------------------------------------------------")
        if not player.is_npc:
            # Para debug
            player.print_territories_names()

            # Receber exercitos
            player.reserves = player.get_round_reserve()

            # Troca de cartas
            # Realizar troca de cartas de território, se possivel, para aumentar as reservas

            # Colocar exercitos nos territórios
            self.allocate_reserve_loop(player)
        else:
            # Realizar Lógica da IA para colocar tropas
            pass

            # Função base para o combate , retorna verdadeiro apenas se o território alvo não tiver mais tropas para defender

    def attack_territory(self, origin, target, amount):
        if target not in origin.vizinhos:
            print("Territórios não fazem fronteira")
            return

        if amount < 2:
            print("são necessários mais tropas para atacar")
            return

        # Realizar combate
        attack_dices = partida.get_actual_combat_troops(amount, False)
        defense_dices = partida.get_actual_combat_troops(target.tropas, True)

        attack_dice_list = [random.randint(1, 6) for i in range(attack_dices)]
        defense_dice_list = [random.randint(1, 6) for i in range(defense_dices)]

        attack_dice_list.sort()
        defense_dice_list.sort()

        # Guardar defesas
        attack_losses = 0
        defense_losses = 0

        print(attack_dice_list)
        print(defense_dice_list)

        for i in range(min(len(attack_dice_list), len(defense_dice_list))):
            # São comparados com a regra do war
            if attack_dice_list[i] > defense_dice_list[i]:
                # Esse dado de ataque ganhou
                defense_losses += 1
            else:
                attack_losses += 1

        print("Atacante sofreu: " + str(attack_losses))
        print("Defensor sofreu: " + str(defense_losses))

        # Atualizar tropas em cada território
        origin.tropas -= attack_losses
        target.tropas -= defense_losses

        # Testar se território foi capturado
        if target.tropas == 0:
            return True
        else:
            return False

    # fase de combate
    def fase_combate(self, player):
        print("FASE DE COMBATE PLAYER: " + str(player.cor))
        print("-------------------------------------------------------------")
        if not player.is_npc:
            while (player.available_for_attack()):
                # Receber origem do ataque
                # Receber alvo do ataque
                # Receber quantidade de tropas utilizadas
                print("Comece o ataque")
                # Para debug
                player.print_territories_names()

                # Mudar depois para receber com clique do mouse os inputs
                origin_id = int(input("ID do território de origem: "))
                origin_territory = self.territorios_dict[origin_id]

                origin_territory.print_neighbors_names()

                target_id = int(input("ID do território alvo do ataque: "))

                target_territory = self.territorios_dict[target_id]

                amount = int(input("Quantidade de tropas para se utilizar: "))
                if amount > origin_territory.tropas:
                    print("Numero de tropas indisponiveis nesse territorio")
                    # Passa para próxima iteração do loop
                    continue

                if target_territory.player == origin_territory.player:
                    print("Esse território já é seu")
                    # Passa para próxima iteração do loop
                    continue

                target_has_no_troops_left = self.attack_territory(origin_territory, target_territory, amount)

                # Ganhou o território
                if target_has_no_troops_left:
                    print("território capturado!")
                    target_territory.player = player
                    # Para debug
                    print("Tropas no território de origem: " + str(origin_territory.tropas))
                    # Modificar input para clique de
                    amount_to_move = int(input("Digite quantos exércitos você deseja mover para o novo território: "))
                    player.move_army_terr(origin_territory, target_territory, amount_to_move)

                # Testar se quer parar de atacar
                # Modificar input para clique do mouse
                if input("Se deseja parar de atacar digite 0: ") == '0':
                    print("parou?")
                    break
        else:
            # Realizar Lógica da IA para combate
            pass
        if(len(player.territorios) == 42):
            print("O player %s ganhou!", player.cor)
            self.over = True

    # fase de movimentação
    def fase_movimento(self, player):
        print("FASE DE MOVIMENTAÇÃO PLAYER: " + str(player.cor))
        print("-------------------------------------------------------------")
        if not player.is_npc:
            is_mooving = True
            while (is_mooving):
                # Modificar input para clique do mouse
                # Receber origem
                # Receber alvo
                # Receber quantidade de tropas utilizadas

                print("Comece a movimentação")
                # Para debug
                player.print_territories_names()

                # Mudar depois para receber com clique do mouse os inputs
                origin_id = int(input("ID do território de origem: "))
                origin_territory = self.territorios_dict[origin_id]

                origin_territory.print_neighbors_names()

                target_id = int(input("ID do território alvo:  "))

                target_territory = self.territorios_dict[target_id]

                # Modificar para input pela tela
                amount = int(input("Quantidade de tropas para mover"))

                player.move_army_terr(origin_territory, target_territory, amount)

                if input("Se deseja parar de mover digite 0: ") == '0':
                    break


        else:
            # Implementar lógica de IA para fase de movimentação
            pass

    # Helper functions

    # Função para retornar numero de dados em combate
    def get_actual_combat_troops(amount, defesa):
        if amount < 4:
            # Se forem até 3 tropas atacando:
            if defesa:
                return amount
            else:
                return amount - 1
        else:
            return 3

    # def get_allocate_reserve_input(self):
    #     # Mudar essa função depois para receber inputs por clique no mapa e input na tela
    #     id = int(input("ID do territorio: "))
    #     amount = int(input("Escolha a quantidade de tropas para colocar: "))
    #
    #     return self.territorios_dict[id], amount
    #
    # def allocate_reserve_loop(self, player):
    #     while player.reserves != 0:
    #         territory, amount = self.get_allocate_reserve_input()
    #         player.allocate_reserve(territory, amount)

    def game_loop(self):
        rodada = 1
        while not self.over:
            for player in self.players_list:
                self.fase_de_tropas(player)

                self.fase_combate(player)

                self.fase_movimento(player)

            rodada += 1
