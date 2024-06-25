from casa import *


class TerraDeNinguem:
    def __init__(self, id, posicao, nome):
        self.id = id
        self.posicao = posicao
        self.nome = nome
        # Outros atributos aqui

    def ativarEvento(self, jogador):
        # Implementação do evento aqui
        print(f"Evento ativado na {self.nome}")
        # Lógica do evento aqui
