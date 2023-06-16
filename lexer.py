import re

class Token:
    def __init__(self, tipo, lexema):
        self.tipo = tipo
        self.lexema = lexema

def analisador_lexico(codigo_fonte):
    padroes = [
        (r'programa\b', 'PROGRAMA'),
        (r'inteiro\b', 'INTEIRO'),
        (r'decimal\b', 'DECIMAL'),
        (r'leia\b', 'LEIA'),
        (r'escreva\b', 'ESCREVA'),
        (r'se\b', 'SE'),
        (r'entao\b', 'ENTAO'),
        (r'senao\b', 'SENAO'),
        (r'fimprog\b', 'FIMPROG'),
        (r'[a-zA-Z][a-zA-Z0-9]*', 'IDENTIFICADOR'),
        (r'\d+', 'NUMERO'),
        (r'\+', 'ADICAO'),
        (r'-', 'SUBTRACAO'),
        (r'\*', 'MULTIPLICACAO'),
        (r'/', 'DIVISAO'),
        (r'\(', 'ABRE_PARENTESE'),
        (r'\)', 'FECHA_PARENTESE'),
        (r'{', 'ABRE_CHAVE'),
        (r'}', 'FECHA_CHAVE'),
        (r':=', 'ATRIBUICAO'),
        (r'<>|<=|>=|<|>|==', 'OPERADOR_RELACIONAL'),
        (r',', 'VIRGULA'),
        (r';', 'PONTO_VIRGULA'),
        (r'"[^"]*"', 'TEXTO')
    ]

    codigo_fonte = re.sub(r'\s+', '', codigo_fonte)  # Remove espaços em branco
    posicao = 0
    tokens = []

    while posicao < len(codigo_fonte):
        lexema = None
        for padrao, tipo in padroes:
            resultado = re.match(padrao, codigo_fonte[posicao:])
            if resultado:
                lexema = resultado.group(0)
                break
        
        if lexema is None:
            print(f"Erro: Caractere inválido encontrado: '{codigo_fonte[posicao]}'")
            posicao += 1
            continue

        posicao += len(lexema)
        tokens.append(Token(tipo, lexema))

    return tokens
