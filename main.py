import re

def analisarPrograma():
    programa = ""
    while True:
        linha = input("Digite uma linha do programa (ou '#fim' para encerrar):\n")
        if linha.strip() == "#fim":
            break
        programa += linha + "\n"
    
    programa = removerEspacosEmBranco(programa)
    correspondencia = re.match(r'programa(.+?)fimprog.', programa, re.DOTALL)
    if correspondencia:
        bloco = correspondencia.group(1)
        codigo_c_resultante = analisarBloco(bloco)
        return codigo_c_resultante
    else:
        raise SyntaxError('Programa inválido')

def analisarBloco(bloco):
    declaracoes, comandos = separarDeclaracoesComandos(bloco)
    codigo_c_resultante = analisarDeclaracoes(declaracoes)
    codigo_c_resultante += analisarComandos(comandos)
    return codigo_c_resultante

def separarDeclaracoesComandos(bloco):
    correspondencia = re.match(r'(.+?)(Cmd.*)', bloco, re.DOTALL)
    if correspondencia:
        declaracoes = correspondencia.group(1).strip()
        comandos = correspondencia.group(2).strip()
        return declaracoes, comandos
    else:
        raise SyntaxError('Bloco inválido')

def analisarDeclaracoes(declaracoes):
    correspondencia = re.findall(r'(inteiro|decimal)\s+(\w+(?:,\s*\w+)*)\s*;', declaracoes)
    codigo_c_resultante = ""
    for tipo, variaveis in correspondencia:
        variaveis = variaveis.split(',')
        for variavel in variaveis:
            codigo_c_resultante += f'{tipo} {variavel};\n'
    return codigo_c_resultante

def analisarComandos(comandos):
    comandos = comandos.strip()
    lista_comandos = re.findall(r'(CmdLeitura|CmdEscrita|CmdIf|CmdExpr)\s*\((.*?)\)(?:\s*\{(.*?)\})?', comandos)
    codigo_c_resultante = ""
    for comando, argumento, bloco in lista_comandos:
        if comando == 'CmdLeitura':
            codigo_c_resultante += analisarCmdLeitura(argumento)
        elif comando == 'CmdEscrita':
            codigo_c_resultante += analisarCmdEscrita(argumento)
        elif comando == 'CmdIf':
            codigo_c_resultante += analisarCmdIf(argumento, bloco)
        elif comando == 'CmdExpr':
            codigo_c_resultante += analisarCmdExpr(argumento)
    return codigo_c_resultante

def analisarCmdLeitura(argumento):
    correspondencia = re.match(r'(\w+)', argumento)
    if correspondencia:
        variavel = correspondencia.group(1)
        return f'scanf("%lf", &{variavel});\n'
    else:
        raise SyntaxError('Comando de leitura inválido')

def analisarCmdEscrita(argumento):
    if argumento.startswith('"') and argumento.endswith('"'):
        texto = argumento.strip('"')
        return f'printf("{texto}");\n'
    else:
        correspondencia = re.match(r'(\w+)', argumento)
        if correspondencia:
            variavel = correspondencia.group(1)
            return f'printf("%lf", {variavel});\n'
        else:
            raise SyntaxError('Comando de escrita inválido')

def analisarCmdIf(argumento, bloco):
    correspondencia = re.match(r'(.+?)\{(.*?)\}', bloco, re.DOTALL)
    if correspondencia:
        condicao = argumento.strip()
        bloco_if = correspondencia.group(2).strip()
        codigo_c_resultante = f'if ({condicao})' + '{\n'
        codigo_c_resultante += analisarComandos(bloco_if) + '}\n'
        return codigo_c_resultante
    else:
        raise SyntaxError('Comando if inválido')

def analisarCmdExpr(argumento):
    correspondencia = re.match(r'(\w+)\s*:=\s*(.+)', argumento)
    if correspondencia:
        variavel = correspondencia.group(1)
        expressao = correspondencia.group(2)
        return f'{variavel} = {expressao};\n'
    else:
        raise SyntaxError('Comando de expressão inválido')

def removerEspacosEmBranco(texto):
    return re.sub(r'\s+', '', texto)

# Exemplo de uso
codigo_c_resultante = analisarPrograma()
print("\nCódigo C resultante:\n")
print(codigo_c_resultante)
