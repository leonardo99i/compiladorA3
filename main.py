import re

def removerEspacosEmBranco(texto):
    return re.sub(r'\s+', '', texto)

def analisarPrograma(programa):
    programa = removerEspacosEmBranco(programa)
    correspondencia = re.match(r'programa(.*?)#fim', programa, re.DOTALL)
    if correspondencia:
        bloco = correspondencia.group(1)
        codigo_c_resultante = analisarBloco(bloco)
        return codigo_c_resultante
    else:
        raise SyntaxError('Programa inválido')

def analisarBloco(bloco):
    bloco = removerEspacosEmBranco(bloco)
    declaracoes, comandos = re.split(r';', bloco)
    codigo_c_resultante = ''
    codigo_c_resultante += analisarDeclaracoes(declaracoes)
    codigo_c_resultante += analisarComandos(comandos)
    return codigo_c_resultante

def analisarDeclaracoes(declaracoes):
    declaracoes = removerEspacosEmBranco(declaracoes)
    lista_declaracoes = re.split(r',', declaracoes)
    codigo_c_resultante = ''
    for declaracao in lista_declaracoes:
        tipo, variaveis = re.match(r'(inteiro|decimal)(.+)', declaracao).groups()
        variaveis = re.split(r',', variaveis)
        for variavel in variaveis:
            codigo_c_resultante += f'{tipo} {variavel};\n'
    return codigo_c_resultante

def analisarComandos(comandos):
    comandos = removerEspacosEmBranco(comandos)
    lista_comandos = re.split(r'\.', comandos)
    codigo_c_resultante = ''
    for comando in lista_comandos:
        comando = removerEspacosEmBranco(comando)
        if comando.startswith('CmdLeitura'):
            variavel = re.match(r'CmdLeitura\((.+)\)', comando).group(1)
            codigo_c_resultante += f'scanf("%lf", &{variavel});\n'
        elif comando.startswith('CmdEscrita'):
            texto = re.match(r'CmdEscrita\("(.+)"\)', comando).group(1)
            codigo_c_resultante += f'printf("{texto}\\n");\n'
        elif comando.startswith('CmdExpr'):
            atribuicao = re.match(r'CmdExpr\((.+)\)', comando).group(1)
            codigo_c_resultante += analisarAtribuicao(atribuicao)
    return codigo_c_resultante

def analisarAtribuicao(atribuicao):
    atribuicao = removerEspacosEmBranco(atribuicao)
    variavel, expressao = re.match(r'(.+):=(.+)', atribuicao).groups()
    expressao_c = analisarExpressao(expressao)
    return f'{variavel} = {expressao_c};\n'

def analisarExpressao(expressao):
    expressao = removerEspacosEmBranco(expressao)
    termo_esquerda, termos_direita = re.match(r'(.+)(\+|\-)(.+)', expressao).groups()
    termo_esquerda_c = analisarTermo(termo_esquerda)
    termos_direita_c = analisarTermosDireita(termos_direita)
    return f'{termo_esquerda_c} {termos_direita_c}'

def analisarTermosDireita(termos):
    termos = removerEspacosEmBranco(termos)
    if re.match(r'(\+|\-)(.+)', termos):
        operador, termo = re.match(r'(\+|\-)(.+)', termos).groups()
        termo_c = analisarTermo(termo)
        return f'{operador} {termo_c}'
    else:
        return ''

def analisarTermo(termo):
    termo = removerEspacosEmBranco(termo)
    fator_esquerda, fatores_direita = re.match(r'(.+)(\*|\/)(.+)', termo).groups()
    fator_esquerda_c = analisarFator(fator_esquerda)
    fatores_direita_c = analisarFatoresDireita(fatores_direita)
    return f'{fator_esquerda_c} {fatores_direita_c}'

def analisarFatoresDireita(fatores):
    fatores = removerEspacosEmBranco(fatores)
    if re.match(r'(\*|\/)(.+)', fatores):
        operador, fator = re.match(r'(\*|\/)(.+)', fatores).groups()
        fator_c = analisarFator(fator)
        return f'{operador} {fator_c}'
    else:
        return ''

def analisarFator(fator):
    fator = removerEspacosEmBranco(fator)
    if fator.isnumeric():
        return fator
    else:
        return fator

programa = ''
linha = input("Digite o programa na linguagem fictícia (digite #fim para encerrar):\n")
while linha != '#fim':
    programa += linha + '\n'
    linha = input()

codigo_c_resultante = analisarPrograma(programa)
print(codigo_c_resultante)