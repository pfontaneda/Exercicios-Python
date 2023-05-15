def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO INTEIRO VÁLIDO\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[0;31mERRO! DIGITE UM NÚMERO REAL VÁLIDO\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[0;31mEntrada de dados interrompida pelo usuário\033[m')
            return 0
        else:
            return n


n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número real: ')
print(f'Você digitou {n1} para o inteiro e {n2 } para o real')
