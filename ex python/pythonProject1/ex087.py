matriz = [[],[],[]]
pares = maior = coluna = 0
for l in range(0,3): #linha
        for c in range(0,3): #coluna
                matriz[l].append(int(input(f"Digite um valor para [{l},{c}]: "))) #aqui alimenta a matriz
print('-='*30)
for l in range(0,3): #aqui diz o que fazer com a matriz
        for c in range(0,3):
                print(f'[{matriz[l][c]:^5}]', end='')
                if matriz[l][c] % 2 == 0:
                        pares += matriz[l][c]
        print()
print('-='*30)
print(f'A soma dos valores pares na matriz é: {pares}')
for l in range(0,3):
        coluna += matriz[l][2] #a coluna é fixa, o q muda são os valores das linhas
print(f'Valores da terceira coluna somados: {coluna}')
for c in range(0,3):
        if c == 0 or matriz[1][c > maior] :
                maior = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior}')
