class player:

    def __init__( self , CartObj , alive , cor ):

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

    def allocate_reserve( self , terr ):

        if terr not in self.territorios:
            raise ValueError( f"Esse player não tem o territorio {terr.nome}" )
        
        if self.reserves == 0:
            return
        
        self.reserves -= 1
        terr.tropas += 1

    def move_army_terr( self , terr_start , terr_end ):

        #---------------------------------------------------------------
        # Ambos territorios devem estar sob posse do jogador
        for terr in ( terr_start , terr_end ):
            if terr not in self.territorios:
                raise ValueError( f"Esse player não tem o territorio {terr.nome}" )
        
        #--------------------------------------------------------------
        # O territorio de origem nao pode estar sem tropas.
        if terr_start.tropas == 1:
            raise ValueError(
                f"O territorio {terr_start.nome} não tem nenhuma tropa"
            )

        #-------------------------------------------------------------
        # Os territorios em questão devem fazer fronteira um com outro
        if terr_start not in set( terr_end.vizinhos):
            raise ValueError(
                f"{terr_start} nao é um territorio adjacente a {terr_end.nome}" 
            )
        
        terr_start.tropas -= 1
        terr_end.tropas -= 1
        
