num = int(input('Digite um número inteiro:'))
print('''Escolha uma base de conversão:
[1] BINARIA
[2] OCTAL
[3] HEXADECIMAL''')
base = int(input('Digite sua opção:'))
if base == 1:
    print('{} convertido para binário é: {}'.format(num , bin(num)[2:]))
elif base == 2:
    print('{} convertido para octal é: {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido para hexadecimal é: {}'.format(num, hex(num)[2:]))


