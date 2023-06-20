codigo = '''
VAR x recebe "5"$
ESCREVA("Maior que 10")$
ESCREVA_VARIAVEL(x)$
'''

tokens = analisador_lexico(codigo)
if tokens:
    codigo_python = analisador_sintatico(tokens)
    if codigo_python:
        print("Código em Python gerado:")
        for instrucao in codigo_python:
            if instrucao['tipo'] == 'impressao_texto':
                print(f"print('{instrucao['texto']}')")
            elif instrucao['tipo'] == 'declaracao_atribuicao':
                print(f"{instrucao['nome_variavel']} = '{instrucao['valor']}'")
