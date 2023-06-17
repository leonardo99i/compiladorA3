from lexer import Lexer
from parser_1 import Parser, Converter

def analyze(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    converter = Converter(tokens)
    converter.parse()


if __name__ == '__main__':
    code = """
    programa
        inteiro x, y
        leia(x)
        leia(y)
        if (x > y) {
            escreva("x é maior que y")
        } else {
            escreva("x não é maior que y")
        }
    fimprog
    """

    analyze(code)
