"""
    Atributos:
    - nome: O nome da casa.
    - regiao: A região ocupada pela casa.
    - aluguel: O valor do aluguel para quem cair nessa casa.
    - preco_de_compra: O preço de compra do assentamento.
    - preco_construcao: O preço para construir no assentamento.
    - grupo: O grupo ao qual o assentamento pertence (por exemplo, rosa , verde).
    - log: Logística relacionada à casa, como informações adicionais ou eventos especiais.
    O atributo log poderia conter uma descrição de eventos especiais que ocorrem quando um jogador cai nessa casa. Por exemplo, para uma casa "Emboscada", o log poderia descrever a natureza da emboscada e suas consequências para o jogador.
"""

class Casa:
    #classe genérica usada pra outras classes
    def __init__(self, nome, regiao, log):
        self.nome = nome
        self.regiao = regiao 
        self.log = log

class Assentamento(Casa):
    def __init__(self, nome, aluguel, preco_de_compra, preco_construcao, grupo, regiao, log):
        super().__init__(nome, regiao, log)
        self.aluguel = aluguel
        self.preco_de_compra = preco_de_compra
        self.preco_construcao = preco_construcao
        self.grupo = grupo

class Emboscada(Casa):
    def __init__(self, nome, regiao, log):
        super().__init__(nome, regiao, log)

class PontoDePartida(Casa):
    def __init__(self, nome, regiao, log):
        super().__init__(nome, regiao, log)

class Encurralado(Casa):
    def __init__(self, nome, regiao, log):
        super().__init__(nome, regiao, log)

class ZonaDePerigo(Casa):
    def __init__(self, nome, regiao, log):
        super().__init__(nome, regiao, log)

class TerraDeNinguem(Casa):
    def __init__(self, nome, regiao, log):
        super().__init__(nome, regiao, log)

class PortoSeguro(Casa):
    def __init__(self, nome, regiao, log):
        super().__init__(nome, regiao, log)