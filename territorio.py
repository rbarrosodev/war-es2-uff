import pandas as pd

class territorio:

    @staticmethod
    def get_territorios():

        terr_df = pd.read_csv("Mapa/Territorios.csv")
        terr_df.set_index( "Id" )
        ter_d = {}
        for i , rec in terr_df.iterrows():
            nome = rec["Nome"]
            terr = territorio( nome , i )
            ter_d[ i ] = terr
        
        border_df = pd.read_csv("Mapa/Fronteiras.csv")
        for _ , rec in border_df.iterrows():

            id_1 = rec["Terr_id_1"]
            t1 = ter_d[ id_1 ]

            id_2 = rec["Terr_id_2"]
            t2 = ter_d[ id_2 ]

            t1.vizinhos.append( t2 )
            t2.vizinhos.append( t1 )
        
        return list( ter_d.values() )

    def __init__( self , nome , idt , vizinhos = None ):

        self.nome = nome 
        self.idt = idt
        if vizinhos is None:
            vizinhos = list() 
        self.vizinhos = vizinhos 
        
        self.tropas = 0
        self.player = None
    
    def __hash__(self):
        return hash( self.idt )

