from time import sleep


def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1
    print('~~' * 16)
    print(f'Contagem de {inicio} até {fim}, de {passo} em {passo}')
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)  # se o sleep bugar. tem q coloca a função flush depois do end=', flush=True
            cont += passo
        print(' FIM ')
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont -= passo
        print(' FIM ')


contador(1, 10, 1)
contador(10, 0, 2)
print('~~' * 16)
print('Agora é sua vez de escolher como contar')
ini = int(input('início: '))
fin = int(input('fim:    '))
pas = int(input('passos: '))
contador(ini, fin, pas)
