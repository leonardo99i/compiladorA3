import re


def analisador_lexico(codigo):
    padroes = [
        ('VAR', r'VAR'),
        ('TIPO', r'INT|FLOAT'),
        ('SE', r'SE'),
        ('SENAO', r'SENAO'),
        ('ESCREVA', r'ESCREVA'),
        ('NOME_VARIAVEL', r'[a-zA-Z_]\w*'),
        ('OPERADOR', r'[<>]=?'),
        ('ATRIBUICAO', r'recebe'),
        ('INTEIRO', r'\d+'),
        ('PONTO_FLUTUANTE', r'\d+\.\d+'),
        ('DOIS_PONTOS', r':'),
        ('FIM_LINHA', r'\$'),
        ('ABRE_PARENTESES', r'\('),
        ('FECHA_PARENTESES', r'\)'),
        ('ASPAS_DUPLAS', r'"[^"]*"'),  # Alteração no padrão para capturar sequências entre aspas duplas
        ('ESPACO', r'\s+')
    ]

    tokens = []
    posicao = 0

    while posicao < len(codigo):
        match = None
        for nome_token, padrao in padroes:
            regex = re.compile(padrao)
            match = regex.match(codigo, posicao)
            if match:
                valor = match.group(0)
                if nome_token != 'ESPACO':  # Ignorar espaços em branco
                    tokens.append((nome_token, valor))
                posicao = match.end(0)
                break

        if not match:
            print(f"Erro: Caractere inválido encontrado: {codigo[posicao]}")
            return None

    return tokens


def analisador_sintatico(tokens):
    posicao = 0

    def obter_proximo_token():
        nonlocal posicao
        if posicao < len(tokens):
            posicao += 1
            return tokens[posicao - 1]
        else:
            return None

    def verificar_token_esperado(nome_token):
        token = obter_proximo_token()
        if token and token[0] == nome_token:
            return token
        else:
            return None

    def analisar_escreva():
        abrir_parenteses = verificar_token_esperado('ABRE_PARENTESES')
        if abrir_parenteses:
            texto = verificar_token_esperado('ASPAS_DUPLAS')
            if texto:
                fechar_parenteses = verificar_token_esperado('FECHA_PARENTESES')
                if fechar_parenteses:
                    fim_linha = verificar_token_esperado('FIM_LINHA')
                    if fim_linha:
                        return {
                            'texto': "'" + texto[1].strip('"') + "'"  # Adicionar aspas simples ao redor do texto capturado
                        }
        return None

    resultado = []
    while posicao < len(tokens):
        token = obter_proximo_token()
        if token and token[0] == 'ESCREVA':
            escreva = analisar_escreva()
            if escreva:
                resultado.append(escreva)
        elif token and token[0] == 'ESPACO':
            continue
        else:
            print(f"Erro de sintaxe: Token inválido encontrado: {token[1]}")
            return None

    return resultado


codigo = '''
ESCREVA("OLÁ")$
'''

tokens = analisador_lexico(codigo)
if tokens:
    codigo_python = analisador_sintatico(tokens)
    if codigo_python:
        print("Código em Python gerado:")
        for instrucao in codigo_python:
            print(f"print({instrucao['texto']})")
