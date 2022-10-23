from asyncio.windows_events import NULL
from random import random

import Player
class partida:
    #n_humans são o número de jogadores humanos e n_npcs o número de IAs
    def CriarPartida(self , n_humans, n_npcs):
        self.n_humans = n_humans
        self.n_npcs = n_npcs
        self.n_players = n_npcs + n_humans
        #essa parte deveria checar se existe um número suficiente de jogadores para jogar o jogo
        #qualquer coisa acerta esse if
        if(n_humans < 1 or (n_humans == 1 and n_npcs < 1)):
            print("A partida não pode ser criada")
            Finalizar(self)
        #embaralhar as cartas objetivo e distribuí-las(várias maneiras de fazer isso)Ainda não implementei
        Card[0] = "carta objetivo"
        #criar jogadores
        #coloquei como metodo para a criação do player a carta objetivo.Vc pode criar um metodo só para isso e 
        #colocar essa parte da criação de jogadores antes da "criação" e embaralho/distribuição das cartas
        self.V_player[n_players] = V_player[self.n_players]
        x = 0
        #aqui seria a escolha das cores
        for x in range(n_humans):
            pilar = 1
            while(pilar == 1):
                print("Jogador %d escolha sua cor:Digite 1 para branco,2 para amarelo,3 para vermelho,4 para verde,5 para azul e 6 para preto", x)
                cor = input("Digite um número: ")
                if(cor == 1):
                    Cor = "Branco"
                    pilar = 0 
                elif(cor == 2):
                    Cor = "Amarelo"
                    pilar = 0
                elif(cor == 3):
                    Cor = "Vermelho"
                    pilar = 0
                elif(cor == 4):
                    Cor = "Verde"
                    pilar = 0
                elif(cor == 5):
                    Cor = "Azul"
                    pilar = 0
                elif(cor == 6):
                    Cor = "Preto"
                    pilar = 0
                else:
                    print("erro,tente novamente")
            #implementar algo para impedir que dois players escolham mesma cor
            self.V_player[x] = Player.player.criar_player(Card[0] , True, Cor)
        x = 0
        for x in range(n_npcs):
            #criar função que cria player IA,escolhendo a cor e carta delas
            n_npcs = n_npcs#placeholder
        #distribuir randomicamente os territórios e adicionar 1 tropa para cada 
        #territorios[] é o vetor de territórios
        #não sei quantos território tem vou chutar 50
        #falta colocar de forma aleatória os territórios no vetor
        territorios[50]
        y = 0
        x = 0
        for x in range(len(territorios)):
            territorio[x].cor = self.n_players[y].cor
            territorio[x].tropas = 1
            if(y < (n_humans - 1)):
                y += 1
            else:
                y = 0

        #começar a primeira rodada(ela só terá a primeira fase(calcular/ganhar tropas e colocá-las no território escolhido pelos players)
         Prodada(self)

    #primeira rodada
    def Prodada(self):
        #aqui eu iria calcular o numero de tropas que cada jogador iria ganhar[criar uma função em player] e
        #escolher onde colocar cada 1
        #falta implementar IA
        x = 0
        for x in range(self.n_humans):
            #reforco seria substituido pelo metodo
            print("Player %d possui %d tropas, escolha onde colocá-las", x, reforco) 
            #aqui seria implementado colocar as tropas nos territorios desejados 
        #começar segunda rodada e loop(todas as outras serão iguais)
        #duas ideias:o que eu fiz aqui embaixo ou cada rodada(se ninguem ganhar) chama rodada(proximo player)
        #criar condição para acabar a partida(ultimo jogador humano sair,apenas 1 jogador estar vivo,jogoador completar objetivo)
        victory = False
        x = 0
        while(victory == False):
            rodada(v_players[x])
            if(x < (self.n_players - 1)):
                x += 1
            else:
                x = 0

    def rodada(self, player):
        #aqui teria tres estagios.o primeiro seria calcular reforço e escolher onde colocar as tropas ganhas
        #segundo seria combate
        #terceiro seria mover as tropas para territórios adjacentes que sejam pertencentes ao jogador
        x = 0#placeholder

    #aqui deveria finalizar a partida(não sei se funciona assim)
    def Finalizar(self):
        self = NULL