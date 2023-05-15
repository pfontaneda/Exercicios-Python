a = float(input('Qual o tamanho da primeira reta?'))
b = float(input('E da segunda?'))
c = float(input('Da terceira?'))
if c < a + b and b< a + c and a < b + c:
    print('As retas formam um triângulo')
else:
    print('as retas NÃO formam um triângulo')

