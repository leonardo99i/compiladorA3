from ply import lex, yacc

# Definição do analisador léxico
tokens = [
    'PROGRAMA',
    'INTEIRO',
    'DECIMAL',
    'LEIA',
    'ESCREVA',
    'SE',
    'ENTAO',
    'SENAO',
    'FIMPROG',
    'IDENTIFICADOR',
    'NUMERO',
    'ADICAO',
    'SUBTRACAO',
    'MULTIPLICACAO',
    'DIVISAO',
    'ABRE_PARENTESE',
    'FECHA_PARENTESE',
    'ABRE_CHAVE',
    'FECHA_CHAVE',
    'ATRIBUICAO',
    'OPERADOR_RELACIONAL',
    'VIRGULA',
    'PONTO_VIRGULA',
    'TEXTO'
]

# Regras de expressões regulares para os tokens
t_PROGRAMA = r'programa\b'
t_INTEIRO = r'inteiro\b'
t_DECIMAL = r'decimal\b'
t_LEIA = r'leia\b'
t_ESCREVA = r'escreva\b'
t_SE = r'se\b'
t_ENTAO = r'entao\b'
t_SENAO = r'senao\b'
t_FIMPROG = r'fimprog\b'
t_IDENTIFICADOR = r'[a-zA-Z][a-zA-Z0-9]*'
t_NUMERO = r'\d+'
t_ADICAO = r'\+'
t_SUBTRACAO = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ABRE_CHAVE = r'\{'
t_FECHA_CHAVE = r'\}'
t_ATRIBUICAO = r':='
t_OPERADOR_RELACIONAL = r'<>|<=|>=|<|>|=='
t_VIRGULA = r','
t_PONTO_VIRGULA = r';'
t_TEXTO = r'"[^"]*"'

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Função para tratar erros
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()

# Definição das regras de análise sintática
def p_prog(p):
    '''
    prog : PROGRAMA declara bloco FIMPROG PONTO_VIRGULA
    '''
    print("Análise sintática concluída com sucesso.")

def p_declara(p):
    '''
    declara : tipo lista_identificadores PONTO_VIRGULA
    '''
    pass

def p_tipo(p):
    '''
    tipo : INTEIRO
         | DECIMAL
    '''
    pass

def p_lista_identificadores(p):
    '''
    lista_identificadores : IDENTIFICADOR
                          | IDENTIFICADOR VIRGULA lista_identificadores
    '''
    pass

def p_bloco(p):
    '''
    bloco : ABRE_CHAVE cmd FECHA_CHAVE
    '''
    pass

def p_cmd(p):
    '''
    cmd : LEIA ABRE_PARENTESE IDENTIFICADOR FECHA_PARENTESE
        | ESCREVA ABRE_PARENTESE (TEXTO | IDENTIFICADOR) FECHA_PARENTESE
        | IDENTIFICADOR ATRIBUICAO expr
        | SE ABRE_PARENTESE expr OPERADOR_RELACIONAL expr FECHA_PARENTESE bloco SENAO bloco
    '''
    pass

def p_expr(p):
    '''
    expr : termo
         | termo ADICAO expr
         | termo SUBTRACAO expr
    '''
    pass

def p_termo(p):
    '''
    termo : fator
          | fator MULTIPLICACAO termo
          | fator DIVISAO termo
    '''
    pass

def p_fator(p):
    '''
    fator : NUMERO
          | IDENTIFICADOR
          | ABRE_PARENTESE expr FECHA_PARENTESE
    '''
    pass

# Função para tratar erros de análise sintática
def p_error(p):
    print("Erro de sintaxe.")

# Criação do analisador sintático
parser = yacc.yacc()

# Função para realizar a análise sintática
def analisador_sintatico(codigo_fonte):
    parser.parse(codigo_fonte)

# Teste do analisador sintático
codigo_fonte = '''
programa
inteiro x, y;
leia(x);
y := 10;
escreva('O valor de x é:', x);
escreva("O valor de y é:", y);
fimprog.
'''

analisador_sintatico(codigo_fonte)
