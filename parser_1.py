class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token_index = 0

    def match(self, expected_token):
        if self.current_token[0] == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Esperado '{expected_token}', encontrado '{self.current_token[0]}'")

    def advance(self):
        if self.next_token_index < len(self.tokens):
            self.current_token = self.tokens[self.next_token_index]
            self.next_token_index += 1
        else:
            self.current_token = None

    def program(self):
        self.match('PROGRAMA')
        self.match('IDENTIFICADOR')
        self.match('PONTO_VIRGULA')

        while self.current_token is not None:
            self.statement()

        self.match('FIM_PROGRAMA')

    def statement(self):
        self.match('IDENTIFICADOR')
        self.match('ATRIBUICAO')
        self.expression()
        self.match('PONTO_VIRGULA')

    def expression(self):
        self.term()
        while self.current_token[0] in ['ADICAO', 'SUBTRACAO']:
            self.match(self.current_token[0])
            self.term()

    def term(self):
        self.factor()
        while self.current_token[0] in ['MULTIPLICACAO', 'DIVISAO']:
            self.match(self.current_token[0])
            self.factor()

    def factor(self):
        if self.current_token[0] == 'IDENTIFICADOR':
            self.match('IDENTIFICADOR')
        elif self.current_token[0] == 'NUMERO':
            self.match('NUMERO')
        else:
            raise SyntaxError(f"Token inválido: {self.current_token[0]}")
