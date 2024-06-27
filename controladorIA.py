import random
class IA:
    def __init__(self, dificuldade):
        super().__init__()
        self.dificuldade = dificuldade
        return

    def controlar(self, input):
        if input == "Comprar Casa": 
            #dificuldade por emquanto apenas torna IA mais provável a comprar casas
            return random.randint(0,100)+10*self.dificuldade > 50
        return False

       
    def awaitsInput(self):
        #print('IA')
        return False