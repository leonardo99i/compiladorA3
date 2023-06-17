from lexer import Lexer

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current_token = None
        self.next_token = None
        self.token_index = -1
        self.advance()

    def advance(self):
        self.token_index += 1
        if self.token_index < len(self.tokens):
            self.current_token = self.tokens[self.token_index]
            if self.token_index + 1 < len(self.tokens):
                self.next_token = self.tokens[self.token_index + 1]
            else:
                self.next_token = None
        else:
            self.current_token = None
            self.next_token = None

    def parse(self):
        self.program()
<<<<<<< HEAD

    def program(self):
        self.match('PROGRAMA')
        self.match('IDENTIFICADOR')
        self.match('ABRE_CHAVE')
        self.declarations()
        self.statements()
        self.match('FECHA_CHAVE')
        self.match('FIM_PROG')

    def declarations(self):
        if self.current_token[0] == 'INTEIRO':
            self.match('INTEIRO')
            self.match('IDENTIFICADOR')
            while self.current_token[0] == 'VIRGULA':
                self.match('VIRGULA')
                self.match('IDENTIFICADOR')

    def statements(self):
        self.statement()
        while self.current_token[0] == 'PONTO_VIRGULA':
            self.match('PONTO_VIRGULA')
            self.statement()

    def statement(self):
        if self.current_token[0] == 'LEIA':
            self.read_statement()
        elif self.current_token[0] == 'ESCREVA':
            self.write_statement()
        elif self.current_token[0] == 'IDENTIFICADOR':
            self.assignment_statement()

    def read_statement(self):
        self.match('LEIA')
        self.match('ABRE_PARENTESES')
        self.match('IDENTIFICADOR')
        self.match('FECHA_PARENTESES')

    def write_statement(self):
        self.match('ESCREVA')
        self.match('ABRE_PARENTESES')
        self.expression()
        while self.current_token[0] == 'VIRGULA':
            self.match('VIRGULA')
            self.expression()
        self.match('FECHA_PARENTESES')

    def assignment_statement(self):
        self.match('IDENTIFICADOR')
        self.match('ATRIBUICAO')
        self.expression()

    def expression(self):
        self.term()
        while self.current_token[0] in ['MAIS', 'MENOS']:
            self.match(self.current_token[0])
            self.term()

    def term(self):
        self.factor()
        while self.current_token[0] in ['MULTIPLICACAO', 'DIVISAO']:
            self.match(self.current_token[0])
            self.factor()

    def factor(self):
        if self.current_token[0] == 'ABRE_PARENTESES':
            self.match('ABRE_PARENTESES')
            self.expression()
            self.match('FECHA_PARENTESES')
        elif self.current_token[0] == 'NUMERO':
            self.match('NUMERO')
        elif self.current_token[0] == 'IDENTIFICADOR':
            self.match('IDENTIFICADOR')
        else:
            raise SyntaxError(f"Token inválido: {self.current_token[0]}")

    def match(self, expected_token):
        if self.current_token[0] == expected_token:
            self.advance()
        else:
            raise SyntaxError(f"Esperado '{expected_token}', encontrado '{self.current_token[0]}'")
=======
        if self.current_token:
            raise SyntaxError(f"Unexpected token: {self.current_token[0]}")
>>>>>>> parent of 9cdf660 (quase o resultado esperado)
