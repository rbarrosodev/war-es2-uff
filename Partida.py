from asyncio.windows_events import NULL
from random import random
from collections import deque

import Player
import CartaObj
import territorio

CORES = [ "branco" , "preto" , "vermelho" , "azul", "amarelo" , "verde" ]
class partida:
    def __init__(self ,n_humans, n_players = 6 ):

        self.n_players  = min( n_players , 6 ) 
        self.n_humans   = min( n_humans , n_players )  # num de players
        self.n_npcs     = n_players - n_humans         # num de ias
        self.num_rodada = 0 

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
            self.v_player.append( Player.player( card, True, cor ) )

        # ---------------------------------------------------------------------
        # inicializar npc
        self.npcs = []
        if self.n_npcs != 0:
            remaining_colors = [ cor for i , cor in enumerate( CORES ) if cores_disponiveis[ i ] ]
            npc_goal_cards   = self.goal_cards[ self.n_humans: ]
            for cor , card in zip( remaining_colors , npc_goal_cards ):
                self.npcs.append( None ) # aqui fazer o append do npc

        # ---------------------------------------------------------------------
        # distribuicao de territorios 
        territorios = territorio.get_territorios()
        random.shuffle( territorios )
        players = deque( self.v_player + self.npcs )    # Total de membros na partida
        for terr in territorios:
            player = players[ 0 ]
            terr.player = player
            terr.tropas = 1
            player.territorios.append( terr )
            players.rotate()

    def distribuir_exercito( self ):
        
        min_terr = 3
        for player in ( self.player + self.npcs ):
            player.reserves = max( len( player.territorios )//2 , min_terr )