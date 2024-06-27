class JogadorState():
    def __init__(self):
        return
    
    def isZombie(self): #método usado primariamente p/ interface gráfica (saber qual renderizar por ex)
        return False
    
    #Para os métodos abaixo: Implementar com polimorfismo para humanos e zumbis diferentemente
    def atualizarSuprimentos(self,jogador,int):
        return
    
    def encurralar(self, jogador):
        jogador.preso = True
        jogador.rodadasPreso = 0
        jogador.peca.enviaPraPrisão()
    
    def tentarFugir(self, jogador):
        jogador.rodadasPreso+=1
        if jogador.rodadasPreso>3:
            jogador.libera()
        return not jogador.preso
    
    
    def usarCartaDistracao(self, jogador):
        if jogador.cartasEscape > 0:
            jogador.cartasEscape -= 1
            return True
        return False