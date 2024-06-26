class JogadorState():
    def __init__(self):
        return
    
    def isZombie(self): #método usado primariamente p/ interface gráfica (saber qual renderizar por ex)
        return False
    
    #Para os métodos abaixo: Implementar com polimorfismo para humanos e zumbis diferentemente
    def atualizarSuprimentos(self,int):
        return
    
    def encurralar(self):
        return
    
    def tentarFugir(self):
        return
    
    def usarCartaDistracao(self):
        return