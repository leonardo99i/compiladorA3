class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index]

    def parse(self):
        self.program()

    def program(self):
        self.match('PROGRAMA')
        self.match('IDENTIFICADOR')
        self.match('ABRE_CHAVE')
        self.declarations()
        self.commands()
        self.match('FECHA_CHAVE')
        self.match('FIMPROG')

    def declarations(self):
        while self.current_token[0] == 'INTEIRO':
            self.match('INTEIRO')
            self.variables()
            self.match(';')

    def variables(self):
        self.match('IDENTIFICADOR')
        while self.current_token[0] == ',':
            self.match(',')
            self.match('IDENTIFICADOR')

    def commands(self):
        while self.current_token[0] != 'FECHA_CHAVE':
            self.command()

    def command(self):
        if self.current_token[0] == 'IDENTIFICADOR':
            self.match('IDENTIFICADOR')
            self.match('=')
            self.expr_arit()
            self.match(';')
        elif self.current_token[0] == 'LEIA':
            self.match('LEIA')
            self.match('(')
            self.variables()
            self.match(')')
            self.match(';')
        elif self.current_token[0] == 'ESCREVA':
            self.match('ESCREVA')
            self.match('(')
            self.expr_string()
            self.match(')')
            self.match(';')
        elif self.current_token[0] == 'SE':
            self.match('SE')
            self.match('(')
            self.condicao()
            self.match(')')
            self.match('ABRE_CHAVE')
            self.commands()
            self.match('FECHA_CHAVE')
            if self.current_token[0] == 'SENAO':
                self.match('SENAO')
                self.match('ABRE_CHAVE')
                self.commands()
                self.match('FECHA_CHAVE')

    def expr_arit(self):
        self.termo()
        while self.current_token[0] in ['+', '-', '*', '/']:
            self.match(self.current_token[0])
            self.termo()

    def termo(self):
        self.fator()
        while self.current_token[0] in ['*', '/']:
            self.match(self.current_token[0])
            self.fator()

    def fator(self):
        if self.current_token[0] == 'IDENTIFICADOR':
            self.match('IDENTIFICADOR')
        elif self.current_token[0] == 'INTEIRO':
            self.match('INTEIRO')
        else:
            self.match('(')
            self.expr_arit()
            self.match(')')

    def expr_string(self):
        self.match('STRING')

    def condicao(self):
        self.expr_arit()
        self.match('>=')
        self.expr_arit()

    def match(self, expected_token):
        if self.current_token[0] == expected_token:
            self.index += 1
            if self.index < len(self.tokens):
                self.current_token = self.tokens[self.index]
        else:
            raise SyntaxError(f"Esperado '{expected_token}', encontrado '{self.current_token[0]}'")
