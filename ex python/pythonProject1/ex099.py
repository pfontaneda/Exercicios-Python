from time import sleep


def maior(* num):
    cont = maior = 0
    print('**' * 15)
    print('Analisando cada número...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(0.5)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados {cont} números')
    print(f'E o maior é {maior}')


maior(4, 8, 7, 1, 6, 3)
maior(1, 5)
maior()
maior(7, 9, 5, 3, 1, 15, 21, 3)
