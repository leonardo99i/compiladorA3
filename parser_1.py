from lexer import analisador_lexico

tokens = []
posicao = 0

def verificar_token(token_esperado):
    global posicao

    if posicao < len(tokens) and tokens[posicao].tipo == token_esperado:
        posicao += 1
        return True
    return False

def prog():
    if verificar_token('PROGRAMA'):
        declara()
        bloco()
        if verificar_token('FIMPROG'):
            print("Análise sintática concluída com sucesso.")
        else:
            print("Erro: Esperado 'fimprog' após o bloco.")
    else:
        print("Erro: Esperado 'programa' no início do programa.")

def declara():
    if verificar_token('INTEIRO') or verificar_token('DECIMAL'):
        if verificar_token('IDENTIFICADOR'):
            while verificar_token(','):
                if not verificar_token('IDENTIFICADOR'):
                    print("Erro: Esperado identificador após ',' na declaração.")
                    return
        else:
            print("Erro: Esperado identificador após tipo na declaração.")
    else:
        print("Erro: Esperado tipo na declaração.")

def bloco():
    if verificar_token('ABRE_PARENTESE'):
        cmd()
        while verificar_token('FECHA_PARENTESE'):
            cmd()

def cmd():
    if verificar_token('LEIA'):
        if verificar_token('ABRE_PARENTESE'):
            if verificar_token('IDENTIFICADOR'):
                if verificar_token('FECHA_PARENTESE'):
                    return
                else:
                    print("Erro: Esperado ')' após o identificador no comando de leitura.")
            else:
                print("Erro: Esperado identificador após '(' no comando de leitura.")
        else:
            print("Erro: Esperado '(' no comando de leitura.")
    elif verificar_token('ESCREVA'):
        if verificar_token('ABRE_PARENTESE'):
            if verificar_token('TEXTO') or verificar_token('IDENTIFICADOR'):
                if verificar_token('FECHA_PARENTESE'):
                    return
                else:
                    print("Erro: Esperado ')' após o texto ou identificador no comando de escrita.")
            else:
                print("Erro: Esperado texto ou identificador após '(' no comando de escrita.")
        else:
            print("Erro: Esperado '(' no comando de escrita.")
    elif verificar_token('IDENTIFICADOR'):
        if verificar_token('ATRIBUICAO'):
            expr()
        else:
            print("Erro: Esperado ':=' após o identificador no comando de atribuição.")
    elif verificar_token('IF'):
        if verificar_token('ABRE_PARENTESE'):
            expr()
            if verificar_token('OP_REL'):
                expr()
                if verificar_token('FECHA_PARENTESE'):
                    if verificar_token('ABRE_CHAVE'):
                        while not verificar_token('FECHA_CHAVE'):
                            cmd()
                    else:
                        print("Erro: Esperado '{' após o 'if'.")
                        return
                    if verificar_token('ELSE'):
                        if verificar_token('ABRE_CHAVE'):
                            while not verificar_token('FECHA_CHAVE'):
                                cmd()
                        else:
                            print("Erro: Esperado '{' após o 'else'.")
                            return
                else:
                    print("Erro: Esperado ')' após a expressão do 'if'.")
                    return
            else:
                print("Erro: Esperado operador relacional após a primeira expressão do 'if'.")
                return
        else:
            print("Erro: Esperado '(' após o 'if'.")
            return
    else:
        print("Erro: Comando inválido encontrado.")

def expr():
    termo()
    while verificar_token('ADICAO') or verificar_token('SUBTRACAO'):
        termo()

def termo():
    fator()
    while verificar_token('MULTIPLICACAO') or verificar_token('DIVISAO'):
        fator()

def fator():
    if verificar_token('NUMERO') or verificar_token('IDENTIFICADOR'):
        return
    elif verificar_token('ABRE_PARENTESE'):
        expr()
        if verificar_token('FECHA_PARENTESE'):
            return
        else:
            print("Erro: Esperado ')' após a expressão.")
    else:
        print("Erro: Fator inválido encontrado.")

# Teste do analisador sintático
def analisador_sintatico(codigo_fonte):
    global tokens, posicao

    tokens = analisador_lexico(codigo_fonte)
    posicao = 0

    prog()

codigo_fonte = '''
programa
inteiro x, y;
decimal z;
leia(x);
y := 10;
escreva('O valor de x é:', x);
escreva("O valor de y é:", y);
z := x + y * 2.5;
if (z > 100) {
    escreva('z é maior que 100');
} else {
    escreva('z é menor ou igual a 100');
}
fimprog.
'''

analisador_sintatico(codigo_fonte)
