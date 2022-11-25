from typing import List , Any


#carta de objetivo deve ter texto(descri��o que os player ir�o ler),imagem(png da carta)
# e condi��o de vit�ria(acho que vai ser individual,provavelmente teremos que criar isso na m�o)

#Esta deste jeito para teste apenas
class cartaObj():

    def __init__(self , texto, imagem):
        self.texto = texto
        self.imagem = imagem

    @staticmethod
    def gerar_cartas() -> List[ Any ]:
        
        obj_cards_list = []
        for i in range(6):
            obj_cards_list.append(cartaObj("texto", "imagem"))

        return obj_cards_list

        '''
        inicializa todas as cartas objetivo para os players
        '''





