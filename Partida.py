#from asyncio.windows_events import NULL
from pickle import TRUE
import random

from collections import deque
from re import A

import Player
import CartaObj
from territorio import territorio

CORES = [ "branco" , "preto" , "vermelho" , "azul", "amarelo" , "verde" ]
class partida:
    def __init__(self ,n_humans, n_players = 6 ):

        self.n_players  = min( n_players , 6 ) 
        self.n_humans   = min( n_humans , n_players )  # num de players
        self.n_npcs     = n_players - n_humans         # num de ias
        self.num_rodada = 0
        self.v_player = []
        self.npcs = []
        #players + npc
        self.players_list = []
        self.territorios_dict = {} #Dicionario de territórios para ser acessado pela partida

        # ---------------------------------------------------------------------------------------
        # essa parte deveria checar se existe um n�mero suficiente de jogadores para jogar o jogo
        # qualquer coisa acerta esse if
        if( self.n_players == 1 ):
            print("A partida não pode ser criada")
            del self
            return
        
        #---------------------------------------------------------------------------------------
        # embaralhar as cartas objetivo e distribuí-las(várias maneiras de fazer isso)Ainda não implementei
        goal_cards = CartaObj.cartaObj.gerar_cartas()
        random.shuffle( goal_cards )
        self.goal_cards = goal_cards[ : self.n_players ]

        # aqui seria a escolha das cores
        cores_disponiveis = [ True ]*len( CORES )
        cores_escolhidas = []
        for x in range(n_humans):
            while True :

                print( f"Jogador {x} escolha a sua cor:")
                for i , cor in enumerate( CORES ):
                    if not cores_disponiveis[ i ]:
                        continue
                    print( f"{i} -> {cor}")
                print()

                try:
                    cor_escolhida = int( input("Digite um número: ") )
                except ValueError:
                    print( "Entrada Inválida" )
                    continue

                if cor_escolhida > len( CORES ) or cor_escolhida < 0:
                    print( "Entrada Inválida" )
                    continue

                if not cores_disponiveis[ cor_escolhida ]:
                    print( "Essa cor ja foi escolhida" )
                    continue
                
                cores_disponiveis[ cor_escolhida ] = False
                Cor = CORES[ cor_escolhida ]
                cores_escolhidas.append( Cor )
                break
        
        # ---------------------------------------------------------------------
        # criar jogadores
        self.v_player = []
        for cor , card in zip( cores_escolhidas , self.goal_cards[ :self.n_humans ] ):
            self.v_player.append( Player.player( card, True, cor, False ) )

        # ---------------------------------------------------------------------
        # inicializar npc
        self.npcs = []
        if self.n_npcs != 0:
            remaining_colors = [ cor for i , cor in enumerate( CORES ) if cores_disponiveis[ i ] ]
            npc_goal_cards   = self.goal_cards[ self.n_humans: ]
            for cor , card in zip( remaining_colors , npc_goal_cards ):
                self.npcs.append( Player.player( card, True, cor, True )  ) 

        # ---------------------------------------------------------------------
        # distribuicao de territorios 
        self.territorios_dict, territorios = territorio.get_territorios()
        random.shuffle( territorios )
        players = deque( self.v_player + self.npcs )    # Total de membros na partida
        for terr in territorios:
            player = players[ 0 ]
            terr.player = player
            terr.tropas = 1
            player.territorios.append( terr )
            players.rotate()
        
        #Lista geral (players + npc)
        self.players_list = list(players)

        #Inicio do jogo
        for player in (self.players_list):
            if not player.is_npc: 
                #Para debug
                player.print_territories_names()

                player.reserves = player.get_round_reserve()
                player.allocate_reserve_loop()
            else:
                #Realizar Lógica da IA para colocar tropas
                pass
            
    #Fase inicial da rodada
    def fase_de_tropas(self, player):
        if not player.is_npc:
            #Para debug
            player.print_territories_names()

            #Receber exercitos
            player.reserves = player.get_round_reserve()

            #Troca de cartas
            #Realizar troca de cartas de território, se possivel, para aumentar as reservas

            #Colocar exercitos nos territórios
            player.allocate_reserve_loop()
        else:
            #Realizar Lógica da IA para colocar tropas
            pass 
    
    #Função base para o combate , retorna verdadeiro apenas se o território alvo não tiver mais tropas para defender
    def attack_territory(self, origin, target, amount):
        if target not in origin.vizinhos:
            print("Territórios não fazem fronteira")
            return
        
        if amount < 2:
            print("são necessários mais tropas para atacar")
            return
        
        #Realizar combate
        attack_dices = self.get_actual_combat_troops(amount)
        defense_dices = self.get_actual_combat_troops(target.tropas)

        attack_dice_list = [random.randint(1,6) for i in range(attack_dices)]
        defense_dice_list = [random.randint(1,6) for i in range(defense_dices)]

        attack_dice_list.sort()
        defense_dice_list.sort()

        #Guardar defesas
        attack_losses = 0
        defense_losses = 0

        for i in range(min(attack_dice_list, defense_dice_list)):
            #São comparados com a regra do war
            if attack_dice_list[i] > defense_dice_list[i]:
                #Esse dado de ataque ganhou
                defense_losses -= 1
            else:
                attack_losses -= 1
        
        #Atualizar tropas em cada território
        origin.tropas -= attack_losses
        target.tropas -= defense_losses
        
        #Testar se território foi capturado
        if target.tropas == 0:
            return True
        else:
            return False

    #fase de combate
    def combate(self, player):
        if not player.is_npc:
            while(player.available_for_attack()):
                #Receber origem do ataque
                #Receber alvo do ataque
                #Receber quantidade de tropas utilizadas

                #Para debug
                player.print_territories_names()

                #Mudar depois para receber com clique do mouse os inputs
                origin_id = int(input("ID do território de origem"))
                origin_territory = self.territorios_dict[origin_id]

                origin_territory.print_neighbors_names()
                
                target_id = int(input("ID do território alvo do ataque"))

                target_territory = self.territorios_dict[target_id]

                amount = int(input("Quantidade de tropas para se utilizar"))
                if amount > origin_territory.tropas:
                    print("Numero de tropas indisponiveis nesse territorio")
                    #Passa para próxima iteração do loop
                    continue 

                target_has_no_troops_left = self.attack_territory(origin_territory, target_territory, amount)

                #Ganhou o território
                if target_has_no_troops_left:
                    #Implementar mover possível para o território
                    pass

                #Testar se quer parar de atacar
                #Modificar input para clique do mouse
                if int(input("Se deseja parar de atacar digite 0") == 0):
                    break
        else:
            #Realizar Lógica da IA para combate
            pass
        

    #fase de movimentação
    def movimento(player, self):
        y = player.territorios[0]
        x = True
        print("Você deseja movimentar alguma tropa")
        input(x)
        while(x == TRUE):
             print("Escolha 1 territorio para mover uma tropa")
             input(y)
             if(y.tropas < 2 or y.vizinho == None):
                 print("O movimento é inválido")
             else:
                 z = player.territorios[0].vizinho[0]
                 m = False
                 for z in y.vizinho:
                     if(y.z.cor == player.cor):
                         m = True
                 if(m == True):
                     y.tropas -= 1
                     print("Escolha o territorio vizinho que a tropa irá se mover")
                     input(y)
                     y.tropas += 1
                 else:
                     print("O movimento é inválido")
             print("Você deseja movimentar alguma tropa")
             input(x)
        y = -1
        for x in self.v_player:
            y +=1
            if(x == player):
                if(x == self.v_player[self.n_players]):
                    self.distribuir_exercito(self.v_player[0], self)
                else:
                    self.distribuir_exercito(self.v_player[y+1], self)
         
    
    #Função para retornar numero de dados em combate
    def get_actual_combat_troops(amount):
        if amount < 4:
            #Se forem até 3 tropas atacando:
            return amount - 1
        else:
            return 3

    def get_allocate_reserve_input(self):
        #Mudar essa função depois para receber inputs por clique no mapa e input na tela
        id = int(input("Escolha o ID de um território: "))
        amount = int(input("Escolha a quantidade de tropas para colocar: "))

        return self.territorios_dict[id], amount


    def game_loop(self):
        pass

    

