from casas import *

class Tabuleiro:
    def __init__(self, jogadores, configuracao_jogo, log):
        
        """
        Inicializa o tabuleiro do jogo
        Parâmetros:
        - jogadores: Lista de jogadores no jogo.
        - configuracao_jogo: Configurações específicas do jogo. Tipo a dificuldade da IA
        - log: Logística relacionada ao tabuleiro, como informações adicionais ou eventos especiais.
        """
        
        self.jogadores = jogadores
        self.log = log
        self.configuracao_jogo = configuracao_jogo

        self.casas = [] # Lista para armazenar todas as casas do tabuleiro
        self.regiao_das_casas = {}   # Dicionário para mapear regiões para casas


        # Adiciona cada casa ao tabuleiro com sua região correspondente :
        
        self.adicionar_casa(Casa("Ponto de Partida", log), regiao=(0, 650, 150, 800))
        self.adicionar_casa(Emboscada("Emboscada", log), regiao=(0,0,150,150))
        self.adicionar_casa(Assentamento("Vilareijo da Solidariedade", 60, 2, 50, (10, 30, 90, 160, 250), "vermelho", log), regiao=(0,150,150,250))
        self.adicionar_casa(TerraDeNinguem("Terra De Ninguém", log), regiao=(0,250,150,350))
        self.adicionar_casa(Assentamento("Bastião da Determinação", 60, 2, 50, (10, 30, 90, 160, 250), "vermelho", log), regiao=(0,350,150,450))
        self.adicionar_casa(ZonaDePerigo("Zona de Perigo", log), regiao=(0,450,150,550))
        self.adicionar_casa(Assentamento("Oásis dos Devastadores", 60, 2, 50, (10, 30, 90, 160, 250), "vermelho", log), regiao=(0,550,150,650))

        self.adicionar_casa(Assentamento("Aldeia da Esperança", 60, 2, 50, (10, 30, 90, 160, 250), "amarelo", log), regiao=(150,650,250,800))
        self.adicionar_casa(TerraDeNinguem("Terra De Ninguém", log), regiao=(250,650,350,800))
        self.adicionar_casa(Assentamento("Coloônia da Nova Ordem", 60, 2, 50, (10, 30, 90, 160, 250), "amarelo", log), regiao=(350,650,450,800))
        self.adicionar_casa(Assentamento("Refúgio da Aurora", 60, 2, 50, (10, 30, 90, 160, 250), "amarelo", log), regiao=(450,650,550,800))
        self.adicionar_casa(ZonaDePerigo("Zona de Perigo", log), regiao=(550,650,650,800))
        self.adicionar_casa(Assentamento("Aldeia dos Corajosos", 60, 2, 50, (10, 30, 90, 160, 250), "verde", log), regiao=(650,650,750,800))
        self.adicionar_casa(TerraDeNinguem("Terra De Ninguém", log), regiao=(750,650,850,800))
        self.adicionar_casa(Assentamento("Vilareijo da Renovação", 60, 2, 50, (10, 30, 90, 160, 250), "verde", log), regiao=(850,650,950,800))
        self.adicionar_casa(Assentamento("Povoado da Salvação", 60, 2, 50, (10, 30, 90, 160, 250), "verde", log), regiao=(950,650,1050,800))
        self.adicionar_casa(Encurralado("Encurralado", log), regiao=(1050,650,1200,800))

        self.adicionar_casa(ZonaDePerigo("Zona de Perigo", log), regiao=(1050,550,1200,650))
        self.adicionar_casa(Assentamento("Refúgio da Redenção", 60, 2, 50, (10, 30, 90, 160, 250), "laranja", log), regiao=(1050,450,1200,550))
        self.adicionar_casa(TerraDeNinguem("Terra De Ninguém", log), regiao=(1050,350,1200,450))
        self.adicionar_casa(Assentamento("Refúgio dos Ressurgentes", 60, 2, 50, (10, 30, 90, 160, 250), "laranja", log), regiao=(1050,250,1200,350))
        self.adicionar_casa(Assentamento("Núcleo da Nova Civilização", 60, 2, 50, (10, 30, 90, 160, 250), "laranja", log), regiao=(1050,150,1200,250))
        self.adicionar_casa(PortoSeguro("Porto Seguro", log), regiao=(1050,0,1200,150))

        self.adicionar_casa(Assentamento("Reduto da Renovação", 60, 2, 50, (10, 30, 90, 160, 250), "rosa", log), regiao=(950,0,1050,150))
        self.adicionar_casa(ZonaDePerigo("Zona de Perigo", log), regiao=(850,0,950,150))
        self.adicionar_casa(Assentamento("Vilareijo dos Valentes", 60, 2, 50, (10, 30, 90, 160, 250), "rosa", log), regiao=(750,0,850,150))
        self.adicionar_casa(Assentamento("Aldeia dos Remanescentes", 60, 2, 50, (10, 30, 90, 160, 250), "rosa", log), regiao=(650,0,750,150))
        self.adicionar_casa(TerraDeNinguem("Terra De Ninguém", log), regiao=(550,0,650,150))
        self.adicionar_casa(Assentamento("Cidadela da Esperança", 60, 2, 50, (10, 30, 90, 160, 250), "azul", log), regiao=(450,0,550,150))
        self.adicionar_casa(Assentamento("Bastião da Determinação Final", 60, 2, 50, (10, 30, 90, 160, 250), "azul", log), regiao=(350,0,450,150))
        self.adicionar_casa(ZonaDePerigo("Zona de Perigo", log), regiao=(250,0,350,150))
        self.adicionar_casa(Assentamento("Enclave da Resposta", 60, 2, 50, (10, 30, 90, 160, 250), "azul", log), regiao=(150,0,250,150))


    def adicionar_casa(self, casa, regiao):
        """
        Adiciona uma casa ao tabuleiro e a mapeia para uma região.

        Parâmetros:
        - casa: Objeto representando a casa a ser adicionada.
        - regiao: Tupla representando as coordenadas ou limites da região (esquerda, topo, largura, altura).
        """
        self.casas.append(casa)
        self.regiao_das_casas[regiao] = casa

    def get_regiao_casa(self, index):
        """
        Obtém a região da casa no índice fornecido no tabuleiro.

        Parâmetros:
        - index: Índice da casa.

        Retorna:
        A região da casa, se existir, ou None se o índice estiver fora dos limites.
        """
        if 0 <= index < len(self.casas):
            return self.casas[index].regiao
        else:
            return None
