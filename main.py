from parser_1 import analisador_sintatico

# Teste do analisador sintático
codigo_fonte = '''
programa
inteiro x, y;
decimal z;
leia(x);
y := 10;
escreva('O valor de x é:', x);
escreva("O valor de y é:", y);
z := x + y * 2.5;
if (z > 100) {
    escreva('z é maior que 100');
} else {
    escreva('z é menor ou igual a 100');
}
fimprog.
'''

analisador_sintatico(codigo_fonte)
