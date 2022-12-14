class player:

    def __init__( self , CartObj , alive , cor, is_npc ):

        self.CartaObj = CartObj # objetivo
        self.alive    = alive

        #---------------------------------------------------
        # pra aparecer no mapa
        self.cor = cor

        #------------------------------------------------------
        # Sob o controle do player
        self.territorios = []

        # ----------------------------------------------------------------------------------------
        # territorio controlados por adversários, que fazem fronteira com o território do player
        self.border_territory = set()

        #-----------------------------------------------------------------------------------------
        # Reforços que podem ser que podem ser alocados ao inicio da rodada
        self.reserves = 0

        #Contagem de quantas trocas de carta de território já foram feitas
        card_exchange = 0

        self.is_npc = is_npc

        pass
    
    ###### GESTAO DE TERRITORIOS ####################

    def get_border_territory( self ):

        '''
        Acha todos os territorios que sao fronteiricos aos territorios 
        do player
        '''

        if self.border_territory:
            return
        
        terr_set = set( self.territorios )
        for terr in terr_set:
            viz = set( terr.vizinhos )
            self.border_territory = ( self.border_territory | viz ) - terr_set
    
    def add_territory( self , terr ):
        
        '''
        Adiciona um novo territorio a lista do player e atualiza o conjunto
        de fronteiras como efeito colateral.
        '''

        if terr in self.territorios:
            return
        
        self.territorios.append( terr )
        self.update_border( terr )
    
    def rmv_territory( self , terr ):
        
        '''
        Remove um territorio da lista do player e atualiza o conjunto
        de fronteiras como efeito colateral.
        '''

        if not( terr in self.territorios ):
            return
        
        self.territorios.remove( terr )
        self.update_border( terr , add = False )

    def update_border( self , terr , add = True ):

        #-----------------------------------------------------------
        # Quando adicionar ou remover o território, o conjunto dos territórios
        # adjacentes deve ser atualizado
        border_set = self.border_territory
        terr_set   = set( self.territorios )
        viz_ter    = set( terr.vizinhos )

        if add:
            self.border_territory = border_set - { terr } + ( viz_ter - terr_set )
        else:
            #-----------------------------------------------------------
            # Solução de força bruta, achar solução otimizada quando
            # tiver tempo.
            self.border_territory = set()
            self.get_border_territory()
    
    ############################# GESTAO DE EXERCITOS ##################################

    def allocate_reserve(self, terr, amount ):
        #Raise trocado por print para não parar a run
        if terr not in self.territorios:
            print( f"Esse player não tem o territorio {terr.nome}" )
            return False
        
        if self.reserves < amount:
            print( f"Esse player não reservas suficientes {str(self.reserves)} < {str(amount)}" )
            return False
        
        
        self.reserves -= amount
        terr.tropas += amount
    
    #Função para pegar numero de novos soldados no começo do round
    def get_round_reserve(self):
        return max( len( self.territorios )//2 , 3)
    
    #Função para trocar carta de território por nova reserva
    def exchange_card(self):
        self.card_exchange += 1
        #Regra tirada da tabela do jogo:
        if self.card_exchange <= 5:
            #4, 6, 8, 10, 12
            self.reserves += 4 + 2 * (self.card_exchange - 1)
        elif self.card_exchange == 6:
            self.reserves += 15
        else:
            #25, 30, 35 ...
            self.reserves += 5 * (self.card_exchange - 2)

        #Falta implementar remoção das cartas do player ..

    def move_army_terr(self , terr_origin , terr_target, amount):

        #---------------------------------------------------------------
        # Esta sendo usado para ataque também
        # if terr_origin not in self.territorios or terr_target not in self.territorios:
        #     print( f"Esse player não tem o territorio " )
        
        #--------------------------------------------------------------
        # O territorio de origem nao pode ficar sem troaps.
        if terr_origin.tropas - amount <= 1:
            print(f"O territorio {terr_origin.nome} não tem nenhuma tropa")

        #-------------------------------------------------------------
        # Os territorios em questão devem fazer fronteira um com outro
        if terr_origin not in set( terr_target.vizinhos):
            print(f"{terr_origin} nao é um territorio adjacente a {terr_target.nome}" )
        
        terr_origin.tropas -= amount
        terr_target.tropas += amount

    #Testar se tem tropas disponiveis para ataque
    def available_for_attack(self):
        for i in self.territorios:
            if i.tropas > 1 : return True
        
        return False

    #Para debug
    def print_territories_names(self):
        print("Jogador: " + str(self.cor))
        for i in self.territorios:
            print(str(i.idt) + ": " + i.nome)
    

        
