import re


def analisador_lexico(codigo):
    padroes = [
        ('VAR', r'VAR'),
        ('TIPO', r'(INT|FLOAT)'),
        ('SE', r'SE'),
        ('SENAO', r'SENAO'),
        ('ESCREVA', r'ESCREVA'),
        ('NOME_VARIAVEL', r'[a-zA-Z_]\w*'),
        ('OPERADOR', r'[<>]=?'),
        ('ATRIBUICAO', r'recebe'),
        ('NUMERO', r'\d+(\.\d*)?'),  # Números inteiros e de ponto flutuante
        ('PONTO', r'.'),
        ('DOIS_PONTOS', r':'),
        ('FIM_LINHA', r'\$'),
        ('ABRE_PARENTESES', r'\('),
        ('FECHA_PARENTESES', r'\)'),
        ('ASPAS_DUPLAS', r'"'),
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

    def analisar_variavel():
        tipo = verificar_token_esperado('TIPO')
        if tipo:
            nome_variavel = verificar_token_esperado('NOME_VARIAVEL')
            if nome_variavel:
                atribuicao = verificar_token_esperado('ATRIBUICAO')
                if atribuicao:
                    valor_variavel = verificar_token_esperado('NUMERO')
                    if valor_variavel:
                        return {
                            'tipo': tipo[1],
                            'nome': nome_variavel[1],
                            'valor': valor_variavel[1]
                        }
        return None

    def analisar_se():
        condicao = verificar_token_esperado('NOME_VARIAVEL')
        if condicao:
            operador = verificar_token_esperado('OPERADOR')
            if operador:
                valor = verificar_token_esperado('NUMERO')
                if valor:
                    entao = verificar_token_esperado('SENAO')
                    if entao:
                        escreva_entao = verificar_token_esperado('ESCREVA')
                        if escreva_entao:
                            texto_entao = verificar_token_esperado('ASPAS_DUPLAS')
                            if texto_entao:
                                fim_linha = verificar_token_esperado('FIM_LINHA')
                                if fim_linha:
                                    return {
                                        'condicao': condicao[1],
                                        'operador': operador[1],
                                        'valor': valor[1],
                                        'entao': {
                                            'escreva': texto_entao[1]
                                        }
                                    }
        return None

    resultado = []
    while posicao < len(tokens):
        token = obter_proximo_token()
        if token and token[0] == 'VAR':
            variavel = analisar_variavel()
            if variavel:
                resultado.append(variavel)
        elif token and token[0] == 'SE':
            se = analisar_se()
            if se:
                resultado.append(se)
        elif token and token[0] == 'ESPACO':
            continue
        else:
            print(f"Erro de sintaxe: Token inválido encontrado: {token[1]}")
            return None

    return resultado


codigo = '''
VAR INT num1 recebe 1$
VAR FLOAT num2 recebe 0.0$

SE num1 > num2 ENTAO:
    ESCREVA("num1 eh maior que num2")$
SENAO:
    ESCREVA("num1 nao eh maior que num2")$
'''

tokens = analisador_lexico(codigo)
if tokens:
    codigo_python = analisador_sintatico(tokens)
    if codigo_python:
        print("Código em Python gerado:")
        for instrucao in codigo_python:
            if 'tipo' in instrucao:
                print(f"{instrucao['tipo']} {instrucao['nome']} = {instrucao['valor']}")
            elif 'condicao' in instrucao:
                print(f"if {instrucao['condicao']} {instrucao['operador']} {instrucao['valor']}:")
                print(f"    print({instrucao['entao']['escreva']})")
                print("else:")
                print(f"    # Bloco do SENAO")