from antlr4 import *
from MinhaLinguagemLexer import MinhaLinguagemLexer
from MinhaLinguagemParser import MinhaLinguagemParser

# Classe de listener personalizado para implementar as ações semânticas
class MinhaLinguagemListener(ParseTreeListener):
    def __init__(self):
        self.saida = ""

    def enterDeclaracaoVariavel(self, ctx:MinhaLinguagemParser.DeclaracaoVariavelContext):
        nome_variavel = ctx.ID().getText()
        valor_variavel = self.visit(ctx.expression())
        self.saida += f"int {nome_variavel} = {valor_variavel};\n"

    def enterComandoImprimir(self, ctx:MinhaLinguagemParser.ComandoImprimirContext):
        valor = self.visit(ctx.expression())
        self.saida += f"printf(\"%d\\n\", {valor});\n"

    def enterComandoAtribuicao(self, ctx:MinhaLinguagemParser.ComandoAtribuicaoContext):
        nome_variavel = ctx.ID().getText()
        valor_variavel = self.visit(ctx.expression())
        self.saida += f"{nome_variavel} = {valor_variavel};\n"

    def enterComandoCondicional(self, ctx:MinhaLinguagemParser.ComandoCondicionalContext):
        condicao = self.visit(ctx.expression())
        self.saida += f"if ({condicao}) {{\n"
        self.visit(ctx.statement(0))
        self.saida += "}\n"
        if ctx.ELSE():
            self.saida += "else {\n"
            self.visit(ctx.statement(1))
            self.saida += "}\n"

    def visitExpressao(self, ctx:MinhaLinguagemParser.ExpressaoContext):
        if ctx.op:
            esquerda = self.visit(ctx.expression(0))
            direita = self.visit(ctx.expression(1))
            op = ctx.op.text
            return f"{esquerda} {op} {direita}"
        elif ctx.NUMBER():
            return ctx.NUMBER().getText()
        elif ctx.ID():
            return ctx.ID().getText()
        elif ctx.BOOLEAN():
            return ctx.BOOLEAN().getText()
        else:
            return self.visit(ctx.expression())

# Função para traduzir o código da linguagem fictícia para C
def traduzir_codigo(codigo):
    # Crie um objeto de fluxo de caracteres com o código
    input_stream = InputStream(codigo)

    # Crie um lexer com o objeto de fluxo de caracteres
    lexer = MinhaLinguagemLexer(input_stream)

    # Crie um objeto de tokenização
    token_stream = CommonTokenStream(lexer)

    # Crie um parser com o objeto de tokenização
    parser = MinhaLinguagemParser(token_stream)

    # Execute o parser e obtenha a árvore de análise
    tree = parser.program()

    # Crie um objeto de listener personalizado
    listener = MinhaLinguagemListener()

    # Visite a árvore de análise com o listener personalizado
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    return listener.saida

# Solicite ao usuário para digitar o código em "MinhaLinguagem"
codigo = input("Digite o código em MinhaLinguagem:\n")

# Traduza o código para a linguagem C
codigo_c = traduzir_codigo(codigo)

# Imprima o código C traduzido
print("\nCódigo traduzido para C:")
print(codigo_c)
