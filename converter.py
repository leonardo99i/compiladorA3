class Converter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.python_code = ''

    def generate_python_code(self):
        self.program()
        return self.python_code

    def program(self):
        self.python_code += 'def main():\n'
        self.match('PROGRAMA')
        self.match('IDENTIFICADOR')
        self.bloco()
        self.python_code += '\nif __name__ == "__main__":\n'
        self.python_code += '    main()\n'

    def bloco(self):
        self.declaracoes()

    def declaracoes(self):
        if self.current_token[1] in ['INTEIRO', 'DECIMAL']:
            self.declaracao_variaveis()
            self.declaracoes()

    def declaracao_variaveis(self):
        self.tipo()
        identifier = self.current_token[1]
        self.match('IDENTIFICADOR')
        self.mais_var(identifier)

    def mais_var(self, identifier):
        if self.current_token[1] == 'VIRGULA':
            self.match('VIRGULA')
            self.declaracao_variaveis()

    def tipo(self):
        if self.current_token[1] == 'INTEIRO':
            self.match('INTEIRO')
        elif self.current_token[1] == 'DECIMAL':
            self.match('DECIMAL')

    def match(self, expected_token):
        if self.position < len(self.tokens):
            self.current_token = self.tokens[self.position]
            self.position += 1
            if self.current_token[0] != expected_token:
                raise SyntaxError(f"Esperado '{expected_token}', encontrado '{self.current_token[0]}'")
        else:
            raise SyntaxError(f"Esperado '{expected_token}', encontrado fim do código")

