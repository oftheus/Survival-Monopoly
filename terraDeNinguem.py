from casa import *
from baralho import *

class TerraDeNinguem(Casa):
   def __init__(self, id, distanceToNext, name):
        super().__init__(id, distanceToNext, name)
      
   def ativarEvento(self, jogador):
      baralhoInstance = Baralho.instance()
      carta = baralhoInstance.sorteia()
      carta.printSelf()
      jogador.controlador.controlar("Espera Click")
      carta.aplicarEfeito(jogador)
      baralhoInstance.sorteia()
      return