lista = list()
for c in range(0, 5):
    n = int(input('Digite um número:'))
    if c == 0 or n > lista[-1]: #se o numero for o primeiro ou se ele for maior que o último da lista
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        pos = 0 #posição
        while pos < len(lista): #vai varrer a lista até o fim
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos} da lista...')
                break
            pos += 1 # pra ir passando a posição
print('_-' * 30)
print(f'Os números digitados em ordem foram: {lista}')


