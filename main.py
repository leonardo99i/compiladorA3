class analisadorLexico:
    def __init__(self, codigo):
        self.codigo = codigo
        self.token = []
        self.posicao = 0

    def analise(self):
        while self.posicao < len(self.codigo):
            if self.codigo[self.posicao].isdigit():
                token = self.lerNumero()
                self.tokens.append(token)
            elif self.codigo