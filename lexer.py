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
            elif self.code[self.position].isalpha():
                self.identifier()
            elif self.code[self.position].isdigit():
                self.integer()
            elif self.code[self.position] == '"':
                self.string()
            elif self.code[self.position] in ['+', '-', '*', '/', '=', '>', '(', ')', '{', '}', ',', ';']:
                self.special_character()
            else:
                raise SyntaxError(f"Token inválido: {self.code[self.position]}")
        return self.tokens

    def identifier(self):
        identifier = ''
        while self.position < len(self.code) and (self.code[self.position].isalpha() or self.code[self.position].isdigit()):
            identifier += self.code[self.position]
            self.position += 1
        self.tokens.append(('IDENTIFICADOR', identifier))

    def integer(self):
        integer = ''
        while self.position < len(self.code) and self.code[self.position].isdigit():
            integer += self.code[self.position]
            self.position += 1
        self.tokens.append(('INTEIRO', integer))

    def string(self):
        string = ''
        self.position += 1
        while self.position < len(self.code) and self.code[self.position] != '"':
            string += self.code[self.position]
            self.position += 1
        self.position += 1
        self.tokens.append(('STRING', string))

    def special_character(self):
        special_char = self.code[self.position]
        self.position += 1
        self.tokens.append((special_char, special_char))
