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
            #Para debug
            player.print_territories_names()

            player.reserves = player.get_round_reserve()
            player.allocate_reserve_loop()
            

        
                


    #fase de distribuição
    def distribuir_exercito(player, self ):
        x = player.territorios[0]
        min_terr = 3
        player.reserves = max( len( player.territorios )//2 , min_terr )
        #considerar continente
        #lidar com as cartas
        #o player.reserves são as tropas que o player ganha
        #fazer com que o usuário escolha onde colocar as tropas
        while(player.reserves != 0):
            print("Escolha 1 territorio para adicionar uma tropa")
            #mudar esse print e input 
            input(x)
            x.tropas += 1
            player.reserves -= 1
        self.combate(self, player)

    #fase de combate
    def combate(self, player):
        y = False
        x = player.territorios[0]
        for x in player.territorios:
            if(x.tropas > 1):
                y = True
        while(y == True):
            print("Voce deseja atacar?")
            input(y)
            if(y == True):
                z = False
                while(z == False):
                    choice = player.territorios[0]
                    print("Escolha o territorio do qual o ataque se originará")
                    input(choice)
                    if(choice.tropas > 1):
                        t = 1
                        print("Quantas tropas voce irá usar?")
                        input(t)
                        while(t >= choice.tropas or t < 1):
                            print("Número inválido,tente novamente")
                            print("Quantas tropas voce irá usar?")
                            input(t)
                        enemy = choice.vizinho[0]
                        print("Qual território voce irá atacar?")
                        input(enemy)
                        while(enemy.cor == choice.cor):
                            print("Território inválido,tente novamente")
                            print("Qual território voce irá atacar?")
                            input(enemy)
                        while(t > 0 or enemy.tropas > 0):
                            attack = random.randint(1,6)
                            defense = random.radint(1,6)
                            if(attack > defense):
                                enemy.tropas -= 1
                            else:
                                t -= 1
                        z = True
                    else:
                        print("Territorio inválido, tente novamente")
        #checar se o player ganhou
        self.movimento(player, self)

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
    

    def get_allocate_reserve_input(self):
        #Mudar essa função depois para receber inputs por clique no mapa e input na tela
        id = int(input("Escolha o ID de um território: "))
        amount = int(input("Escolha a quantidade de tropas para colocar: "))

        return self.territorios_dict[id], amount

    

