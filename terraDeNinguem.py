from casa import *
from baralho import *


class TerraDeNinguem(Casa):
   def __init__(self, id, distanceToNext, name):
        super().__init__(id, distanceToNext, name)
      
   def ativarEvento(self, jogador):
      return
      #algo com baralho.
