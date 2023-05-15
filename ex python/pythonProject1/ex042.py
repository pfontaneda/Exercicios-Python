a = float(input('Qual o tamanho da primeira reta?'))
b = float(input('Qual o tamanho da segunda'))
c = float(input('Qual o tamanho da terceira?'))
if a < b + c and b < a + c and c < a + b:
    print('as retas podem formar um retângulo')
    if a == b == c:
        print('equilátero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('As retas NÂO formam um retângulo')





