class Botao():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color, y_offset=0):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos + y_offset))

    """
        Inicializa um botão com os parâmetros fornecidos.

        Args:
            image (Surface): A imagem do botão.
            pos (tuple): A posição (x, y) do botão.
            text_input (str): O texto exibido no botão.
            font (Font): O objeto de fonte do texto.
            base_color (tuple): A cor do texto quando não está sendo clicado.
            hovering_color (tuple): A cor do texto quando o mouse está sobre o botão.
            y_offset (int, opcional): O deslocamento vertical do texto em relação à posição do botão.
    """


    def update(self, screen):
        if self.image is not None:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    """
        Atualiza a aparência do botão na tela.

        Args:
            screen (Surface): A superfície da tela onde o botão será desenhado.
    """
    


    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    """
        Verifica se o mouse está sobre o botão.

        Args:
            position (tuple): A posição (x, y) do mouse.

        Returns:
            bool: True se o mouse estiver sobre o botão, False caso contrário.
    """



    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)

    """
        Altera a cor do texto do botão se o mouse estiver sobre ele.

        Args:
            position (tuple): A posição (x, y) do mouse.
    """