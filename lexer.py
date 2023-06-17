import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.tokens = []

    def tokenize(self):
        while self.position < len(self.code):
            if self.code[self.position].isspace():
                self.position += 1
            elif self.code[self.position].isdigit():
                self.number()
            elif self.code[self.position].isalpha():
                self.identifier()
            elif self.code[self.position] == '"':
                self.string()
            else:
                self.special_character()

        return self.tokens

    def number(self):
        number = ''
        while self.position < len(self.code) and self.code[self.position].isdigit():
            number += self.code[self.position]
            self.position += 1

        self.tokens.append(('NUMERO', number))

    def identifier(self):
        identifier = ''
        while self.position < len(self.code) and (self.code[self.position].isalpha() or self.code[self.position].isdigit() or self.code[self.position] == '_'):
            identifier += self.code[self.position]
            self.position += 1

        if identifier.upper() == 'PROGRAMA':
            self.tokens.append(('PROGRAMA', identifier))
        elif identifier.upper() == 'FIMPROG':
            self.tokens.append(('FIM_PROG', identifier))
        elif identifier.upper() == 'INTEIRO':
            self.tokens.append(('INTEIRO', identifier))
        elif identifier.upper() == 'DECIMAL':
            self.tokens.append(('DECIMAL', identifier))
        elif identifier.upper() == 'SE':
            self.tokens.append(('SE', identifier))
        elif identifier.upper() == 'ENTAO':
            self.tokens.append(('ENTAO', identifier))
        elif identifier.upper() == 'SENÃO':
            self.tokens.append(('SENÃO', identifier))
        elif identifier.upper() == 'ESCREVA':
            self.tokens.append(('ESCREVA', identifier))
        elif identifier.upper() == 'LEIA':
            self.tokens.append(('LEIA', identifier))
        else:
            self.tokens.append(('IDENTIFICADOR', identifier))

    def string(self):
        string = ''
        self.position += 1  # Ignorar o primeiro caractere (aspas duplas)
        while self.position < len(self.code) and self.code[self.position] != '"':
            string += self.code[self.position]
            self.position += 1

        if self.position < len(self.code):
            self.position += 1  # Ignorar o último caractere (aspas duplas)

        self.tokens.append(('STRING', string))

    def special_character(self):
        if self.code[self.position] == '+':
            self.tokens.append(('SOMA', '+'))
        elif self.code[self.position] == '-':
            self.tokens.append(('SUBTRACAO', '-'))
        elif self.code[self.position] == '*':
            self.tokens.append(('MULTIPLICACAO', '*'))
        elif self.code[self.position] == '/':
            self.tokens.append(('DIVISAO', '/'))
        elif self.code[self.position] == ',':
            self.tokens.append(('VIRGULA', ','))
        elif self.code[self.position] == '>':
            self.tokens.append(('MAIOR', '>'))
        elif self.code[self.position] == '<':
            self.tokens.append(('MENOR', '<'))
        elif self.code[self.position] == '=':
            self.tokens.append(('IGUAL', '='))
        elif self.code[self.position] == '(':
            self.tokens.append(('ABRE_PARENTESES', '('))
        elif self.code[self.position] == ')':
            self.tokens.append(('FECHA_PARENTESES', ')'))
        elif self.code[self.position] == '{':
            self.tokens.append(('ABRE_CHAVE', '{'))
        elif self.code[self.position] == '}':
            self.tokens.append(('FECHA_CHAVE', '}'))
        else:
            raise SyntaxError(f"Token inválido: {self.code[self.position]}")

        self.position += 1
