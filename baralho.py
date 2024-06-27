from carta import *
class Baralho:

    _instance = None #Singleton

    def __init__(self):
        self.cartas = []

    @classmethod #copiei da internet
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
    
    def sorteiaCarta(self):
        #cartaSprite.trocar_carta()
        if len(self.cartas)>0:
            self.cartas[0].aplicarEfeito()