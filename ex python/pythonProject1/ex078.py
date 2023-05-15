num = []
maior = menor = 0
for c in range(0, 5):
    num.append(int(input(f'Digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('-=' * 30)
print(f'Vc digitou os valores {num}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(num): # i de indice e v de valor
    if v == maior:
        print(f'{i}...', end='')
print()  #quebra de linha
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(num): # i de indice e v de valor
    if v == menor:
        print(f'{i}...', end='')
print()
print('-=' * 30)

