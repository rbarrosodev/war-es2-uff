from asyncio.windows_events import NULL
from random import random

import Player
import CartaObj
import territorio

CORES = [ "branco" , "preto" , "vermelho" , "azul", "amarelo" , "verde" ]
class partida:
    def __init__(self ,n_humans, n_players = 6 ):

        self.n_players = min( n_players , 6 ) 
        self.n_humans  = min( n_humans , n_players )  # num de players
        self.n_npcs    = n_players - n_humans         # num de ias 

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
        total_players = self.v_player + self.npcs     # Total de membros na partida
        for i , terr in range(len(territorios)):
            territorio[x].cor = self.n_players[y].cor
            territorio[x].tropas = 1
            if(y < (n_humans - 1)):
                y += 1
            else:
                y = 0

        #come�ar a primeira rodada(ela s� ter� a primeira fase(calcular/ganhar tropas e coloc�-las no territ�rio escolhido pelos players)
        self.Prodada()

    #primeira rodada
    def Prodada(self):
        #aqui eu iria calcular o numero de tropas que cada jogador iria ganhar[criar uma fun��o em player] e
        #escolher onde colocar cada 1
        #falta implementar IA
        x = 0
        for x in range(self.n_humans):
            #reforco seria substituido pelo metodo
            print("Player %d possui %d tropas, escolha onde coloc�-las", x, reforco) 
            #aqui seria implementado colocar as tropas nos territorios desejados 
        #come�ar segunda rodada e loop(todas as outras ser�o iguais)
        #duas ideias:o que eu fiz aqui embaixo ou cada rodada(se ninguem ganhar) chama rodada(proximo player)
        #criar condi��o para acabar a partida(ultimo jogador humano sair,apenas 1 jogador estar vivo,jogoador completar objetivo)
        victory = False
        x = 0
        while(victory == False):
            rodada(v_players[x])
            if(x < (self.n_players - 1)):
                x += 1
            else:
                x = 0

    def rodada(self, player):
        #aqui teria tres estagios.o primeiro seria calcular refor�o e escolher onde colocar as tropas ganhas
        #segundo seria combate
        #terceiro seria mover as tropas para territ�rios adjacentes que sejam pertencentes ao jogador
        x = 0#placeholder

    #aqui deveria finalizar a partida(n�o sei se funciona assim)
    def Finalizar(self):
        self = NULL