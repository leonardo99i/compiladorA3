class Converter:
    def __init__(self, tokens):
        self.tokens = tokens
        self.index = 0
        self.current_token = self.tokens[self.index]

    def generate_python_code(self):
        code = ""
        while self.index < len(self.tokens):
            if self.current_token[0] == 'IDENTIFICADOR':
                code += self.current_token[1]
                self.match('IDENTIFICADOR')
                self.match('=')
                code += " = " + self.expr_arit()
                self.match(';')
            elif self.current_token[0] == 'LEIA':
                self.match('LEIA')
                self.match('(')
                code += self.variables()
                self.match(')')
                self.match(';')
            elif self.current_token[0] == 'ESCREVA':
                self.match('ESCREVA')
                self.match('(')
                code += "print(" + self.expr_string() + ")"
                self.match(')')
                self.match(';')
            elif self.current_token[0] == 'SE':
                self.match('SE')
                self.match('(')
                code += "if " + self.condicao() + ":\n"
                self.match(')')
                code += self.bloco()
                if self.current_token[0] == 'SENAO':
                    self.match('SENAO')
                    code += "else:\n"
                    code += self.bloco()
        return code

    def expr_arit(self):
        code = self.termo()
        while self.current_token[0] in ['+', '-', '*', '/']:
            operator = self.current_token[0]
            self.match(operator)
            code += " " + operator + " " + self.termo()
        return code

    def termo(self):
        code = self.fator()
        while self.current_token[0] in ['*', '/']:
            operator = self.current_token[0]
            self.match(operator)
            code += " " + operator + " " + self.fator()
        return code

    def fator(self):
        code = ""
        if self.current_token[0] == 'IDENTIFICADOR':
            code += self.current_token[1]
            self.match('IDENTIFICADOR')
        elif self.current_token[0] == 'INTEIRO':
            code += self.current_token[1]
            self.match('INTEIRO')
        else:
            self.match('(')
            code += "(" + self.expr_arit() + ")"
            self.match(')')
        return code

    def expr_string(self):
        code = self.current_token[1]
        self.match('STRING')
        return code

    def condicao(self):
        code = self.expr_arit()
        operator = self.current_token[0]
        self.match(operator)
        code += " " + operator + " " + self.expr_arit()
        return code

    def variables(self):
        code = self.current_token[1]
        self.match('IDENTIFICADOR')
        while self.current_token[0] == ',':
            self.match(',')
            code += ", " + self.current_token[1]
            self.match('IDENTIFICADOR')
        return code

    def bloco(self):
        code = ""
        self.match('ABRE_CHAVE')
        code += self.commands()
        self.match('FECHA_CHAVE')
        return code

    def commands(self):
        code = ""
        while self.current_token[0] != 'FECHA_CHAVE':
            code += self.command()
        return code

    def command(self):
        code = ""
        if self.current_token[0] == 'IDENTIFICADOR':
            code += self.current_token[1]
            self.match('IDENTIFICADOR')
            self.match('=')
            code += " = " + self.expr_arit()
            self.match(';')
            code += "\n"
        elif self.current_token[0] == 'LEIA':
            self.match('LEIA')
            self.match('(')
            code += "input()"
            self.match(')')
            self.match(';')
            code += "\n"
        elif self.current_token[0] == 'ESCREVA':
            self.match('ESCREVA')
            self.match('(')
            code += "print(" + self.expr_string() + ")"
            self.match(')')
            self.match(';')
            code += "\n"
        elif self.current_token[0] == 'SE':
            self.match('SE')
            self.match('(')
            code += "if " + self.condicao() + ":\n"
            self.match(')')
            code += self.bloco()
            if self.current_token[0] == 'SENAO':
                self.match('SENAO')
                code += "else:\n"
                code += self.bloco()
        return code

    def match(self, expected_token):
        if self.current_token[0] == expected_token:
            self.index += 1
            if self.index < len(self.tokens):
                self.current_token = self.tokens[self.index]
        else:
            raise SyntaxError(f"Esperado '{expected_token}', encontrado '{self.current_token[0]}'")
