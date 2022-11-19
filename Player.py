class player:

    def __init__( self , CartObj , alive , cor ):

        self.CartaObj = CartObj
        self.alive    = alive
        self.cor      = cor

        self.territorios = []

        # ----------------------------------------------------------------------------------------
        # territorio controlados por adversários, que fazem fronteira com o território do player
        self.border_territory = set() 
        pass
    
    def get_border_territory( self ):

        if self.border_territory:
            return
        
        terr_set = set( self.territorios )
        for terr in terr_set:
            viz = set( terr.vizinhos )
            self.border_territory = self.border_territory + viz - terr_set
    
    def add_territory( self , terr ):

        if terr in self.territorios:
            return
        
        self.territorios.append( terr )
        self.update_border( terr )
    
    def rmv_territory( self , terr ):

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
            pass