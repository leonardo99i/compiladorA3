class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token()

    def next_token(self):
        if self.tokens:
            self.current_token = self.tokens.pop(0)
        else:
            self.current_token = None

    def match(self, expected_token):
        if self.current_token and self.current_token[0] == expected_token:
            self.next_token()
        else:
            raise SyntaxError(f"Expected '{expected_token}', found '{self.current_token[0]}'")

    def program(self):
        self.match('PROGRAMA')
        self.declara()
        self.bloco()
        self.match('FIMPROG')

    def declara(self):
        self.match('INTEIRO')
        self.match('IDENTIFICADOR')
        while self.current_token and self.current_token[0] == 'VIRGULA':
            self.match('VIRGULA')
            self.match('IDENTIFICADOR')

    def bloco(self):
        while self.current_token and self.current_token[0] != 'FIMPROG':
            self.cmd()

    def cmd(self):
        if self.current_token and self.current_token[0] == 'LEIA':
            self.match('LEIA')
            self.match('ABRE_PAREN')
            self.match('IDENTIFICADOR')
            self.match('FECHA_PAREN')
        elif self.current_token and self.current_token[0] == 'ESCREVA':
            self.match('ESCREVA')
            self.match('ABRE_PAREN')
            if self.current_token and self.current_token[0] == 'TEXTO':
                self.match('TEXTO')
            else:
                self.match('IDENTIFICADOR')
            self.match('FECHA_PAREN')
        elif self.current_token and self.current_token[0] == 'IF':
            self.match('IF')
            self.match('ABRE_PAREN')
            self.expr()
            self.op_rel()
            self.expr()
            self.match('FECHA_PAREN')
            self.match('ABRE_CHAVE')
            while self.current_token and self.current_token[0] != 'FECHA_CHAVE':
                self.cmd()
            self.match('FECHA_CHAVE')
            if self.current_token and self.current_token[0] == 'ELSE':
                self.match('ELSE')
                self.match('ABRE_CHAVE')
                while self.current_token and self.current_token[0] != 'FECHA_CHAVE':
                    self.cmd()
                self.match('FECHA_CHAVE')
        elif self.current_token and self.current_token[0] == 'IDENTIFICADOR':
            self.match('IDENTIFICADOR')
            self.match('ATRIBUICAO')
            self.expr()

    def op_rel(self):
        if self.current_token and self.current_token[0] in ['IGUAL', 'DIFERENTE', 'MENOR', 'MENOR_IGUAL', 'MAIOR', 'MAIOR_IGUAL']:
            self.match(self.current_token[0])

    def expr(self):
        self.termo()
        while self.current_token and self.current_token[0] in ['SOMA', 'SUBTRACAO']:
            self.match(self.current_token[0])
            self.termo()

    def termo(self):
        self.fator()
        while self.current_token and self.current_token[0] in ['MULTIPLICACAO', 'DIVISAO']:
            self.match(self.current_token[0])
            self.fator()

    def fator(self):
        if self.current_token and self.current_token[0] == 'NUM_INTEIRO':
            self.match('NUM_INTEIRO')
        elif self.current_token and self.current_token[0] == 'NUM_DECIMAL':
            self.match('NUM_DECIMAL')
        elif self.current_token and self.current_token[0] == 'IDENTIFICADOR':
            self.match('IDENTIFICADOR')
        elif self.current_token and self.current_token[0] == 'ABRE_PAREN':
            self.match('ABRE_PAREN')
            self.expr()
            self.match('FECHA_PAREN')
        else:
            raise SyntaxError(f"Unexpected token: {self.current_token[0]}")

    def parse(self):
        self.program()
        if self.current_token:
            raise SyntaxError(f"Unexpected token: {self.current_token[0]}")
