class GrupoAssentamento:
    def __init__(self, cor, qtd):
        self.casas = []
        self.cor = cor
        self.qtd = qtd

    def inserirCasa(self,casa):
        self.casas.append(casa)
        casa.titulo.grupo = self
        
    def verificarPosseGrupo(self,jogador): #ainda não leva em conta titulo de assentamento
        for casa in self.casas:
            if casa.titulo.jogador != jogador:
                return False
        return True
    
    def printSelf(self): # pra debug
        print(self.cor)
        for casa in self.casas:
            print(casa.name, casa.id)
