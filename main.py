import re

def removerEspacosEmBranco(programa):
    return re.sub(r'\s+', '', programa)

def analisarPrograma(programa):
    programa = removerEspacosEmBranco(programa)
    return analisarProg(programa)

def analisarProg(programa):
    correspondencia = re.match(r'programa(.*?)fimprog\.', programa, re.DOTALL)
    if correspondencia:
        declaracoes, comandos = correspondencia.groups()
        declaracoes_analisadas = analisarDeclaracoes(declaracoes)
        comandos_analisados = analisarComandos(comandos)
        return f'{declaracoes_analisadas}\n{comandos_analisados}'
    else:
        raise SyntaxError('Programa inválido')

def analisarDeclaracoes(declaracoes):
    matches = re.findall(r'(inteiro|decimal)\s+(.+?)(?:,|$)', declaracoes)
    declaracoes_analisadas = [f'{tipo} {ids.strip()};' for tipo, ids in matches]
    return '\n'.join(declaracoes_analisadas)

def analisarComandos(comandos):
    matches = re.findall(r'(CmdLeitura|CmdEscrita|CmdExpr|CmdIf)\((.*?)\)', comandos)
    comandos_analisados = [analisarComando(cmd) for cmd in matches]
    return '\n'.join(comandos_analisados)

def analisarComando(comando):
    tipo, argumento = comando
    if tipo == 'CmdLeitura':
        return f'scanf("%d", &{argumento.strip()});'
    elif tipo == 'CmdEscrita':
        return f'printf("{argumento.strip()}\\n");'
    elif tipo == 'CmdExpr':
        identificador, expressao = argumento.split(':=')
        expressao_analisada = analisarExpressao(expressao)
        return f'{identificador.strip()} = {expressao_analisada};'
    elif tipo == 'CmdIf':
        correspondencia = re.match(r'\((.+?)\)(.+?)(else\{(.+?)\})?', argumento, re.DOTALL)
        condicao, bloco_se, else_match, bloco_senao = correspondencia.groups()
        bloco_se = analisarComandos(bloco_se)
        if else_match and bloco_senao:
            bloco_senao = analisarComandos(bloco_senao)
            return f'if ({condicao.strip()}) {{\n{bloco_se}\n}} else {{\n{bloco_senao}\n}}'
        else:
            return f'if ({condicao.strip()}) {{\n{bloco_se}\n}}'
    else:
        raise SyntaxError(f'Comando inválido: {comando}')

def analisarExpressao(expressao):
    expressao = removerEspacosEmBranco(expressao)
    if '+' in expressao:
        esquerda, direita = expressao.split('+', 1)
        return f'{analisarExpressao(esquerda)} + {analisarTermo(direita)}'
    elif '-' in expressao:
        esquerda, direita = expressao.split('-', 1)
        return f'{analisarExpressao(esquerda)} - {analisarTermo(direita)}'
    else:
        return analisarTermo(expressao)

def analisarTermo(termo):
    termo = removerEspacosEmBranco(termo)
    if '*' in termo:
        esquerda, direita = termo.split('*', 1)
        return f'{analisarTermo(esquerda)} * {analisarFator(direita)}'
    elif '/' in termo:
        esquerda, direita = termo.split('/', 1)
        return f'{analisarTermo(esquerda)} / {analisarFator(direita)}'
    else:
        return analisarFator(termo)

def analisarFator(fator):
    fator = removerEspacosEmBranco(fator)
    if fator.isdigit():
        return fator
    else:
        return fator

# Exemplo de programa na linguagem fictícia
exemplo_programa = '''
programa
  inteiro a, b, soma;
  CmdLeitura(a).
  CmdLeitura(b).
  soma := a + b.
  CmdEscrita("A soma é: ", soma).
fimprog.
'''

# Exibindo um exemplo de programa na linguagem fictícia
print("Exemplo de programa na linguagem fictícia:")
print(exemplo_programa)

# Solicitar o programa ao usuário
print("Digite o programa na linguagem fictícia (utilize o marcador #fim para indicar o final do programa):")
programa = ''
linha = input()
while linha != '#fim':
    programa += linha + '\n'
    linha = input()

# Chamando a função de análise e tradução
try:
    codigo_c_resultante = analisarPrograma(programa)

    # Exibindo o código C resultante
    print("Código C resultante:")
    print(codigo_c_resultante)
except SyntaxError as e:
    print(f"Erro de sintaxe: {e}")