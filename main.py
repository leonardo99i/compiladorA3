from lexer import Lexer
from parser_1 import Parser
<<<<<<< HEAD
from converter import Converter
=======

>>>>>>> parent of 9cdf660 (quase o resultado esperado)

def analyze(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parser.parse()
<<<<<<< HEAD
    converter = Converter(parser.statements)
    converted_code = converter.convert()
    return converted_code

if __name__ == "__main__":
    code = '''
programa
inteiro x, y
{
    leia(x);
    leia(y);
    se (x > y)
    {
        escreva("x é maior que y");
    }
    senao
    {
        escreva("x não é maior que y");
    }
}
fimprog
'''
    converted_code = analyze(code)
    print(converted_code)
=======


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
>>>>>>> parent of 9cdf660 (quase o resultado esperado)
