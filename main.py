from lexer import Lexer
from parser_1 import Parser
from converter import Converter


def analyze(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()

    parser = Parser(tokens)
    parser.parse()

    converter = Converter(tokens)
    converted_code = converter.parse()

    return converted_code


if __name__ == "__main__":
    code = """
    PROGRAMA Teste
    {
        INTEIRO x, y;
        x = 5;
        y = 10;
        ESCREVA("O valor de x é ", x);
        ESCREVA("O valor de y é ", y);
        LEIA(x);
        ESCREVA("Novo valor de x é ", x);
    }
    FIM_PROG
    """

    converted_code = analyze(code)
    print(converted_code)
