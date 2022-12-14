import pandas as pd

class territorio:
    def __init__(self, nome, idt, continente, pos_x, pos_y, vizinhos = None):
        self.nome = nome 
        self.idt = idt
        if vizinhos is None:
            vizinhos = list() 
        self.vizinhos = vizinhos 
        self.continente = continente
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.tropas = 1
        self.player = None
    
    def __hash__(self):
        return hash( self.idt )

    def __str__( self ):

        s = [
        "-"*50,
        f"Nome = {self.nome}",
        f"idt = {self.idt}",
        f"tropas = {self.tropas}",
        f"continente = {self.continente}"
        ]
        
        return '\n'.join( s )

    
    @staticmethod
    def get_territorios():

        terr_df = pd.read_csv("Mapa/Territorios.csv")
        terr_df.set_index( "Id" , inplace = True )

        ter_d = {}
        for i , rec in terr_df.iterrows():
            nome = rec["Nome"]
            cont = rec["Continente_id"]
            position_x = rec["Position_x"]
            position_y = rec["Position_y"]
            terr = territorio(nome, i, cont, position_x, position_y)
            # print(nome, i)
            ter_d[i] = terr
        
        border_df = pd.read_csv("Mapa/Fronteiras.csv")
        for _ , rec in border_df.iterrows():

            id_1 = rec["Terr_id_1"]
            t1 = ter_d[ id_1 ]

            id_2 = rec["Terr_id_2"]
            t2 = ter_d[ id_2 ]

            t1.vizinhos.append( t2 )
            t2.vizinhos.append( t1 )
        
        return ter_d, list( ter_d.values() )
    
    def print_neighbors_names(self):
        for i in self.vizinhos:
            print(str(i.idt) + ": " + i.nome)