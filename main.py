from lexer import Lexer
from parser_1 import Parser
from converter import Converter

def analyze(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parser.parse()
    converter = Converter(tokens)
    python_code = converter.generate_python_code()
    print(python_code)

if __name__ == "__main__":
    code = '''
programa
inteiro x, y
{
    leia(x)
    leia(y)
    se x > y
    {
        escreva("x é maior que y")
    }
    senao
    {
        escreva("x não é maior que y")
    }
}
fimprog
    '''

    analyze(code)
