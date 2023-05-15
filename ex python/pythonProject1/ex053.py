frase = str(input('Escreva sua frase:')).replace(' ','').lower()
inverso = ''
for letra in range(len(frase) - 1 , -1, -1): #o primeiro -1 é pra pegar a ultima letra, o segudo é a primeira letra e o ultimo é pra inverter
    inverso += frase[letra]
if inverso == frase:
    print('Temos um palíndromo')
else:
    print('A frase digitada não é um palíndromo')
