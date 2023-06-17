class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0
        self.current_character = self.code[self.position]
        self.tokens = []

    def advance(self):
        self.position += 1
        if self.position < len(self.code):
            self.current_character = self.code[self.position]
        else:
            self.current_character = None

    def skip_whitespace(self):
        while self.current_character is not None and self.current_character.isspace():
            self.advance()

    def special_character(self):
        if self.current_character == ';':
            self.tokens.append(('PONTO_VIRGULA', ';'))
            self.advance()
        elif self.current_character == '{':
            self.tokens.append(('ABRE_CHAVE', '{'))
            self.advance()
        elif self.current_character == '}':
            self.tokens.append(('FECHA_CHAVE', '}'))
            self.advance()

    def number(self):
        number = ''
        while self.current_character is not None and self.current_character.isdigit():
            number += self.current_character
            self.advance()
        self.tokens.append(('NUMERO', int(number)))

    def identifier(self):
        identifier = ''
        while self.current_character is not None and self.current_character.isalpha():
            identifier += self.current_character
            self.advance()
        if identifier == 'programa':
            self.tokens.append(('PROGRAMA', identifier))
        elif identifier == 'fimprog':
            self.tokens.append(('FIMPROG', identifier))
        elif identifier == 'inteiro':
            self.tokens.append(('INTEIRO', identifier))
        elif identifier == 'leia':
            self.tokens.append(('LEIA', identifier))
        elif identifier == 'escreva':
            self.tokens.append(('ESCREVA', identifier))
        elif identifier == 'se':
            self.tokens.append(('SE', identifier))
        elif identifier == 'senao':
            self.tokens.append(('SENAO', identifier))
        else:
            self.tokens.append(('IDENTIFICADOR', identifier))

    def tokenize(self):
        while self.current_character is not None:
            if self.current_character.isspace():
                self.skip_whitespace()
            elif self.current_character == ';' or self.current_character == '{' or self.current_character == '}':
                self.special_character()
            elif self.current_character.isdigit():
                self.number()
            elif self.current_character.isalpha():
                self.identifier()
            else:
                raise SyntaxError(f"Token inválido: {self.current_character}")

        return self.tokens
