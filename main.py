import sys
import time
from lexer import Lexer
from parser_1 import Parser
from converter import Converter

def analyze(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    parser.program()
    converter = Converter(tokens)
    converted_code = converter.convert()
    return converted_code

def main():
    code = """
    PROGRAMA
        IDENTIFICADOR;
        IDENTIFICADOR = NUMERO * NUMERO;
        IDENTIFICADOR = IDENTIFICADOR + NUMERO;
    FIM_PROGRAMA
    """
    converted_code = analyze(code)
    print(converted_code.convert())

if __name__ == "__main__":
    main()
