class Controlador:
    
    #Funções de cada subclasse de casa controlador através de polimorfismo
    def __init__(self):
        self.jogador = None
        return

    def controlar(self, input):
        return True
    
    def awaitsInput(self):
        return True
       