import re

def removerEspacosEmBranco(programa):
    return re.sub(r'\s+', '', programa)

def analisarPrograma():
    programa = ""
    primeira_linha = True
    print("Digite o código fictício abaixo (#fim para encerrar):\n")
    while True:
        linha = input()
        if linha.strip() == "#fim":
            break
        if primeira_linha:
            primeira_linha = False
        else:
            programa += "\n"
        programa += linha
    
    programa = removerEspacosEmBranco(programa)
    correspondencia = re.match(r'programa(.+?)fimprog.', programa, re.DOTALL)
    if correspondencia:
        bloco = correspondencia.group(1)
        codigo_c_resultante = analisarBloco(bloco)
        codigo_c_resultante = adicionarEstruturaC(codigo_c_resultante)
        return codigo_c_resultante
    else:
        raise SyntaxError('Programa inválido')

def analisarBloco(bloco):
    declaracoes, comandos = re.match(r'(.*?)\{(.*?)\}', bloco, re.DOTALL).groups()
    codigo_c_resultante = ""
    if declaracoes:
        codigo_c_resultante += analisarDeclaracoes(declaracoes)
    if comandos:
        codigo_c_resultante += analisarComandos(comandos)
    return codigo_c_resultante

def analisarDeclaracoes(declaracoes):
    codigo_c_resultante = ""
    declaracoes = re.findall(r'(\w+)\s+(\w+)(,?\s*\w+)*;', declaracoes)
    for tipo, identificadores in declaracoes:
        identificadores = re.findall(r'\w+', identificadores)
        for identificador in identificadores:
            codigo_c_resultante += f"{tipo} {identificador};\n"
    return codigo_c_resultante

def analisarComandos(comandos):
    codigo_c_resultante = ""
    comandos = re.findall(r'(\w+)\s*(\(.*?\))?\s*\{(.*?)\}', comandos, re.DOTALL)
    for comando, argumentos, bloco in comandos:
        if comando == "CmdLeitura":
            codigo_c_resultante += analisarCmdLeitura(argumentos)
        elif comando == "CmdEscrita":
            codigo_c_resultante += analisarCmdEscrita(argumentos)
        elif comando == "CmdIf":
            codigo_c_resultante += analisarCmdIf(argumentos, bloco)
        elif comando == "CmdExpr":
            codigo_c_resultante += analisarCmdExpr(argumentos)
    return codigo_c_resultante

def analisarCmdLeitura(argumentos):
    identificador = re.match(r'\(\s*(\w+)\s*\)', argumentos).group(1)
    return f"scanf(\"%d\", &{identificador});\n"

def analisarCmdEscrita(argumentos):
    if argumentos.startswith("\""):
        texto = argumentos.strip("\"")
        return f"printf(\"{texto}\\n\");\n"
    else:
        identificador = re.match(r'\(\s*(\w+)\s*\)', argumentos).group(1)
        return f"printf(\"%d\\n\", {identificador});\n"

def analisarCmdIf(argumentos, bloco):
    condicao = re.match(r'\(\s*(.+?)\s*\)', argumentos).group(1)
    codigo_c_resultante = f"if ({condicao}) {{\n{analisarBloco(bloco)}}}\n"
    return codigo_c_resultante

def analisarCmdExpr(argumentos):
    return f"{argumentos};\n"

def adicionarEstruturaC(codigo_c_resultante):
    codigo_c_resultante = "#include <stdio.h>\n\nint main() {\n" + codigo_c_resultante + "}\n"
    return codigo_c_resultante

if __name__ == "__main__":
    codigo_c_resultante = analisarPrograma()
    print("\nCódigo C resultante:\n")
    print(codigo_c_resultante)
