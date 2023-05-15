from time import sleep
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
opção = 0
while opção != 5:
    print('''    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair do programa''')
    opção = int(input('Qual é a sua opção?'))
    if opção == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é: {}'.format(n1, n2, soma))
    elif opção == 2:
        produto = n1 * n2
        print('A multiplicação de {} e {} é {}'.format(n1, n2, produto))
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os novos números')
        n1 = int(input('Digite um número inteiro: '))
        n2 = int(input('Digite outro número inteiro: '))
    elif opção == 5:
        print('Finalizando...')
        sleep(1)
    else:
        print('Opção inválida. Digite novamente!')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa')
