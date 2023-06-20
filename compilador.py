import ply.lex as lex
import ply.yacc as yacc

# Lista de tokens
tokens = (
    'VAR',
    'TIPO',
    'NOME_VARIAVEL',
    'ATRIBUICAO',
    'NUMERO',
    'TEXTO',
    'FIM_LINHA',
)

# Expressões regulares para os tokens
t_VAR = r'VAR'
t_TIPO = r'INT|FLOAT|STRING'
t_NOME_VARIAVEL = r'[a-zA-Z_]\w*'
t_ATRIBUICAO = r'recebe'
t_NUMERO = r'-?\d+(\.\d+)?'
t_TEXTO = r'"[^"]*"'
t_FIM_LINHA = r'\$'

# Regra para tratar espaços em branco
t_ignore = ' \t'

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido: {t.value[0]}")
    t.lexer.skip(1)

# Criação do analisador léxico
lexer = lex.lex()

# Regras de análise sintática
def p_programa(p):
    '''
    programa : declaracoes
    '''

def p_declaracoes(p):
    '''
    declaracoes : declaracoes declaracao FIM_LINHA
                | declaracao FIM_LINHA
    '''

def p_declaracao(p):
    '''
    declaracao : VAR NOME_VARIAVEL ATRIBUICAO valor
               | VAR NOME_VARIAVEL
    '''
    if len(p) == 4:
        p[0] = (p[2], None)
    else:
        p[0] = (p[2], p[4])

def p_valor(p):
    '''
    valor : NUMERO
          | TEXTO
    '''
    p[0] = p[1]

# Tratamento de erros de sintaxe
def p_error(p):
    if p:
        print(f"Erro de sintaxe: Token inválido: {p.value}")
    else:
        print("Erro de sintaxe: Fim inesperado do código")

# Criação do analisador sintático
parser = yacc.yacc()

# Função para analisar o código
def analisar_codigo(codigo):
    return parser.parse(codigo)

# Função para gerar código em Python
def gerar_codigo_python(codigo):
    arvore_sintatica = analisar_codigo(codigo)
    if arvore_sintatica:
        codigo_python = ""
        for declaracao in arvore_sintatica:
            nome_variavel, valor = declaracao
            if valor is None:
                codigo_python += f"{nome_variavel} = None\n"
            else:
                codigo_python += f"{nome_variavel} = {valor}\n"
        return codigo_python

    return None

# Teste
codigo = '''
VAR x
x recebe 5$
VAR y recebe "Hello, World!"$
'''

codigo_python = gerar_codigo_python(codigo)
if codigo_python:
    print("Código em Python gerado:")
    print(codigo_python)
