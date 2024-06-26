from casa import *
class Assentamento(Casa):
    def __init__(self, id, distanceToNext, name, custo):
        super().__init__(id, distanceToNext, name)
        self.custo = custo

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        jogador.suprimentos -= self.custo
        return
    
    def drawCasa(self, coord, fonte, screen): #deve ser implementado na casa
        coord[0] += 0
        coord[1] -= 10
        textoCasa = fonte.render(
                f'nao comprada', True, (255, 255, 255))
            # Desenha a mensagem de vitória
        screen.blit(textoCasa, coord)