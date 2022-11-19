from typing import List , Any

class cartaObj():

    @staticmethod
    def gerar_cartas() -> List[ Any ]:
        
        '''
        inicializa todas as cartas objetivo para os players
        '''

    #carta de objetivo deve ter texto(descri��o que os player ir�o ler),imagem(png da carta)
    # e condi��o de vit�ria(acho que vai ser individual,provavelmente teremos que criar isso na m�o)
    def criarCartaObj(self, texto, imagem):
        self.texto = texto
        self.imagem = imagem
        pass

    pass




