import re

patterns = [
    (r'[ \t\n]+', None),  # Ignorar espaços em branco, tabs e quebras de linha
    (r'programa', 'PROGRAMA'),
    (r'fimprog', 'FIMPROG'),
    (r'inteiro', 'INTEIRO'),
    (r'decimal', 'DECIMAL'),
    (r'leia', 'LEIA'),
    (r'escreva', 'ESCREVA'),
    (r'if', 'IF'),
    (r'else', 'ELSE'),
    (r'\(', 'ABRE_PAREN'),
    (r'\)', 'FECHA_PAREN'),
    (r'\{', 'ABRE_CHAVE'),
    (r'\}', 'FECHA_CHAVE'),
    (r',', 'VIRGULA'),
    (r':=', 'ATRIBUICAO'),
    (r':', 'DOIS_PONTOS'),
    (r';', 'PONTO_VIRGULA'),
    (r'=', 'IGUAL'),
    (r'!=', 'DIFERENTE'),
    (r'<', 'MENOR'),
    (r'<=', 'MENOR_IGUAL'),
    (r'>', 'MAIOR'),
    (r'>=', 'MAIOR_IGUAL'),
    (r'\+', 'SOMA'),
    (r'-', 'SUBTRACAO'),
    (r'\*', 'MULTIPLICACAO'),
    (r'/', 'DIVISAO'),
    (r'"([^"\\]|\\.)*"', 'TEXTO'),  # String delimitada por aspas duplas
    (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENTIFICADOR'),  # Identificador
    (r'\d+\.\d+', 'NUM_DECIMAL'),  # Número decimal
    (r'\d+', 'NUM_INTEIRO')  # Número inteiro
]


class Lexer:
    def __init__(self, code):
        self.code = code
        self.position = 0

    def tokenize(self):
        tokens = []
        while self.position < len(self.code):
            match = None
            for pattern, token_type in patterns:
                regex = re.compile(pattern)
                match = regex.match(self.code, self.position)
                if match:
                    value = match.group(0)
                    if token_type:
                        tokens.append((token_type, value))
                    break
            if not match:
                raise SyntaxError(f"Invalid token: {self.code[self.position]}")
            else:
                self.position = match.end()
        return tokens
