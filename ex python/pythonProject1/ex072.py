cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número inteiro entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente ... ', end= '')
    print(f'Vc digitou o número {cont[num]}')
    opc = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if opc in 'N':
        print(f'Programa finalizado.')
        break
print('fim')



