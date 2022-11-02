class player:
    #CartObj � a carta objetivo do jogador, alive � bolleano(se ainda est� no jogo) e cor � a cor do ex�cito
    #n�o sei qual seria a melhor maneira de conectar o player com os territ�rios que ele possui
    #por enquanto vou supor que o territ�rio ter� como atributo a cor do player que o tem
    def criarPlayer(self, CartObj , alive, cor):
        self.CartaObj = CartObj
        self.alive    = alive
        self.cor      = cor

        self.territorios = []
        pass
    
    def domina(self, n_territorios):
        self.n_territorios = n_territorios
    
    #implementar fun��o que checa se ele dominou um continente(cada continente oferece bonus de tropa)



