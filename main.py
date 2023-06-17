from lexer import Lexer
from parser_1 import Parser
from converter import Converter

def analyze(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parser.parse()
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
