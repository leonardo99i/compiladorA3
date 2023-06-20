import re


def analisador_lexico(codigo):
    padroes = [
        ('VAR', r'VAR'),
        ('TIPO', r'INT|FLOAT|STRING'),
        ('SE', r'SE'),
        ('SENAO', r'SENAO'),
        ('ESCREVA', r'ESCREVA'),
        ('NOME_VARIAVEL', r'[a-zA-Z_]\w*'),
        ('OPERADOR', r'[<>]=?'),
        ('ATRIBUICAO', r'recebe'),
        ('INTEIRO', r'-?\d+'),
        ('PONTO_FLUTUANTE', r'\d+\.\d+'),
        ('DOIS_PONTOS', r':'),
        ('FIM_LINHA', r'\$'),
        ('ABRE_PARENTESES', r'\('),
        ('FECHA_PARENTESES', r'\)'),
        ('ASPAS_DUPLAS', r'"[^"]*"'),
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
                            'tipo': 'impressao_texto',
                            'texto': texto[1].strip('"')
                        }
        return None

    def analisar_variavel():
        nome_variavel = verificar_token_esperado('NOME_VARIAVEL')
        if nome_variavel:
            atribuicao = verificar_token_esperado('ATRIBUICAO')
            if atribuicao:
                valor = verificar_token_esperado('INTEIRO') or verificar_token_esperado('PONTO_FLUTUANTE')
                if valor:
                    fim_linha = verificar_token_esperado('FIM_LINHA')
                    if fim_linha:
                        return {
                            'tipo': 'declaracao_atribuicao',
                            'nome_variavel': nome_variavel[1],
                            'valor': valor[1]
                        }
        return None

    resultado = []
    while posicao < len(tokens):
        token = obter_proximo_token()
        if token and token[0] == 'VAR':
            variavel = analisar_variavel()
            if variavel:
                resultado.append(variavel)
        elif token and token[0] == 'ESCREVA':
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
VAR x recebe 5$
ESCREVA("Maior que 10")$
ESCREVA_VARIAVEL(x)$
'''

tokens = analisador_lexico(codigo)
if tokens:
    codigo_python = analisador_sintatico(tokens)
    if codigo_python:
        print("Código em Python gerado:")
        for instrucao in codigo_python:
            if instrucao['tipo'] == 'impressao_texto':
                print(f"print('{instrucao['texto']}')")
            elif instrucao['tipo'] == 'declaracao_atribuicao':
                print(f"{instrucao['nome_variavel']} = {instrucao['valor']}")
