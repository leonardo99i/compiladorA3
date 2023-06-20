import ply.lex as lex
import ply.yacc as yacc

# Definição dos tokens
tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'VAR',
    'EQUALS',
)

# Regras para os tokens
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_VAR = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_EQUALS = r'='

# Regra para lidar com números
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# Ignorar espaços em branco e tabulações
t_ignore = ' \t'

# Tratamento de erros
def t_error(t):
    print(f"Caractere inválido: '{t.value[0]}'")
    t.lexer.skip(1)

# Construção do analisador léxico
lexer = lex.lex()

# Variáveis globais
variables = {}  # Dicionário para armazenar as variáveis

# Código equivalente em Python
python_code = ""

# Regras gramaticais
def p_statement(p):
    '''
    statement : VAR EQUALS expression
              | expression
    '''
    global python_code

    if len(p) == 2:
        p[0] = p[1]  # Apenas expressão
        python_code = f"print({p[1]})"
    else:
        variables[p[1]] = p[3]  # Atribuição de variável
        p[0] = None
        python_code = f"{p[1]} = {p[3]}\nprint({p[1]})"

def p_expression(p):
    '''
    expression : expression PLUS term
               | expression MINUS term
               | expression TIMES term
               | expression DIVIDE term
               | term
    '''
    global python_code

    if len(p) == 2:
        p[0] = p[1]  # Apenas termo
        python_code = f"{p[1]}"
    else:
        if p[2] == '+':
            p[0] = p[1] + p[3]  # Soma
            python_code = f"{p[1]} + {p[3]}"
        elif p[2] == '-':
            p[0] = p[1] - p[3]  # Subtração
            python_code = f"{p[1]} - {p[3]}"
        elif p[2] == '*':
            p[0] = p[1] * p[3]  # Multiplicação
            python_code = f"{p[1]} * {p[3]}"
        elif p[2] == '/':
            p[0] = p[1] / p[3]  # Divisão
            python_code = f"{p[1]} / {p[3]}"

def p_term(p):
    '''
    term : NUMBER
         | VAR
    '''
    global python_code

    if isinstance(p[1], int):
        p[0] = p[1]  # Número
        python_code = str(p[1])
    else:
        p[0] = variables.get(p[1], 0)  # Valor da variável
        python_code = f"{p[1]}"

def p_error(p):
    if p:
        print(f"Erro de sintaxe no token '{p.value}'")
    else:
        print("Erro de sintaxe")

# Construção do analisador sintático
parser = yacc.yacc()

while True:
    try:
        var_name = input('Nome da variável > ')
        operation = input('Operação (+, -, *, /) > ')
        var1 = input('Valor da var1 > ')
        var2 = input('Valor da var2 > ')
    except EOFError:
        break

    variables['var1'] = int(var1)
    variables['var2'] = int(var2)

    if operation == '+':
        result = parser.parse(f"{var_name} = var1 + var2", lexer=lexer)
    elif operation == '-':
        result = parser.parse(f"{var_name} = var1 - var2", lexer=lexer)
    elif operation == '*':
        result = parser.parse(f"{var_name} = var1 * var2", lexer=lexer)
    elif operation == '/':
        result = parser.parse(f"{var_name} = var1 / var2", lexer=lexer)
    else:
        print("Operação inválida.")
        continue

    print(f"Resultado: {variables.get(var_name, 0)}")

    print("\nCódigo equivalente em Python:")
    print(f"{var_name} = {var1} {operation} {var2}")
    print(f"print({var_name})")
