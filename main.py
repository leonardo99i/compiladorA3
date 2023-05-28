import re

def removerEspacosEmBranco(programa):
    return re.sub(r'\s+', '', programa)

def analisarPrograma(programa):
    programa = removerEspacosEmBranco(programa)
    return analisarProg(programa)

def analisarProg(programa):
    correspondencia = re.match(r'programa(.*?)Declara(.*?)Blocofimprog\.', programa, re.DOTALL)
    if correspondencia:
        declaracoes = analisarDeclaracoes(correspondencia.group(1))
        bloco = analisarBloco(correspondencia.group(2))
        return f'{declaracoes}\n{bloco}'
    else:
        raise SyntaxError('Programa inválido')

def analisarDeclaracoes(declaracoes):
    matches = re.findall(r'(inteiro|decimal)(.*?)\.', declaracoes)
    declaracoes_analisadas = [f'{tipo} {ids.strip()};' for tipo, ids in matches]
    return '\n'.join(declaracoes_analisadas)

def analisarBloco(bloco):
    comandos = re.findall(r'Cmd(.*?)\.', bloco)
    comandos_analisados = [analisarComando(cmd) for cmd in comandos]
    return '\n'.join(comandos_analisados)

def analisarComando(comando):
    if comando.startswith('Leia'):
        return analisarComandoLeitura(comando)
    elif comando.startswith('Escreva'):
        return analisarComandoEscrita(comando)
    elif comando.startswith('Se'):
        return analisarComandoSe(comando)
    elif ':' in comando:
        return analisarComandoExpressao(comando)
    else:
        raise SyntaxError(f'Comando inválido: {comando}')

def analisarComandoLeitura(comando):
    correspondencia = re.match(r'leia\((.*?)\)', comando)
    if correspondencia:
        identificador = correspondencia.group(1)
        return f'scanf("%d", &{identificador.strip()});'
    else:
        raise SyntaxError(f'Comando de leitura inválido: {comando}')

def analisarComandoEscrita(comando):
    correspondencia = re.match(r'escreva\("(.*)"\)', comando)
    if correspondencia:
        texto = correspondencia.group(1)
        return f'printf("{texto}\\n");'
    else:
        correspondencia = re.match(r'escreva\((.*?)\)', comando)
        if correspondencia:
            identificador = correspondencia.group(1)
            return f'printf("%d\\n", {identificador.strip()});'
        else:
            raise SyntaxError(f'Comando de escrita inválido: {comando}')

def analisarComandoSe(comando):
    correspondencia = re.match(r'se\((.*?)\)\{(.*?)\}(senao\{(.*?)\})?', comando)
    if correspondencia:
        condicao = analisarExpressao(correspondencia.group(1))
        bloco_se = analisarBloco(correspondencia.group(2))
        bloco_senao = analisarBloco(correspondencia.group(4)) if correspondencia.group(4) else ''
        return f'se ({condicao}) {{\n{bloco_se}\n}} senao {{\n{bloco_senao}\n}}'
    else:
        raise SyntaxError(f'Comando "se" inválido: {comando}')

def analisarComandoExpressao(comando):
    identificador, expressao = comando.split(':=')
    expressao_analisada = analisarExpressao(expressao)
    return f'{identificador.strip()} = {expressao_analisada};'

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
  inteiro x, y.
  CmdExpr: x := 10 + 20.
  CmdEscrita(x).
fimprog.
'''

# Exibindo um exemplo de programa na linguagem fictícia
print("Exemplo de programa na linguagem fictícia:")
print(exemplo_programa)

# Solicitar o programa ao usuário
programa = input("Digite o programa na linguagem fictícia: ")

# Chamando a função de análise e tradução
codigo_c_resultante = analisarPrograma(programa)

# Exibindo o código C resultante
print(codigo_c_resultante)