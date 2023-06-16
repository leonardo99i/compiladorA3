# Arquivo: lexer.py
# Exemplo de arquivo para definição do lexer usando PLY

import ply.lex as lex

# Lista de tokens
tokens = (
    'PROGRAMA',
    'VAR',
    'ID',
    'INTEIRO',
    'DECIMAL',
    'DOISPONTOS',
    'PONTOVIRGULA',
)

# Regras de expressões regulares para os tokens
t_PROGRAMA = r'programa'
t_VAR = r'var'
t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_INTEIRO = r'\d+'
t_DECIMAL = r'\d+\.\d+'
t_DOISPONTOS = r':'
t_PONTOVIRGULA = r';'

# Ignorar caracteres em branco (espaços, tabulações e quebras de linha)
t_ignore = ' \t\n'

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido encontrado: '{t.value[0]}'")
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()

# Arquivo: parser.py
# Exemplo de arquivo para definição do parser usando PLY

import ply.yacc as yacc

# Importação dos tokens definidos pelo lexer
from lexer import tokens

# Definição das regras de produção
def p_programa(p):
    '''programa : PROGRAMA ID declaracoes'''
    pass

def p_declaracoes(p):
    '''declaracoes : declaracao
                   | declaracoes declaracao'''
    pass

def p_declaracao(p):
    '''declaracao : VAR ID DOISPONTOS tipo PONTOVIRGULA'''
    pass

def p_tipo(p):
    '''tipo : INTEIRO
            | DECIMAL'''
    pass

# Construção do parser
parser = yacc.yacc()

# Arquivo: main.py

# Importação do lexer e parser
from lexer import lexer
from parser_1 import parser

# Função para testar o lexer
def test_lexer(data):
    lexer.input(data)
    while True:
        token = lexer.token()
        if not token:
            break
        print(token)

# Função para testar o parser
def test_parser(data):
    result = parser.parse(data)
    print(result)

# Teste do lexer
test_lexer('programa var x: inteiro; y: decimal;')

# Teste do parser
test_parser('programa teste var x: inteiro; y: decimal;')

