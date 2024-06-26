class Casa:
    def __init__(self, id, distanceToNext, name):
        self.id = id
        self.distanceToNext = distanceToNext
        self.name = name

    def ativarEvento(self, jogador): #fzr overload desse compartamento pra cada subclasse
        jogador.suprimentos = jogador.suprimentos - 200
        return
    
    def drawCasa(self, coord, fonte, screen): #deve ser implementado na casa
        return
        coord[0] += 0
        coord[1] -= 10
        textoCasa = fonte.render(
                f'nao comprada', True, (255, 255, 255))
            # Desenha a mensagem de vitória
        screen.blit(textoCasa, coord)