# tuplas
lanche = 'hamburguer', 'suco', 'pizza', 'pudim'
print(lanche)
print(lanche[2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2])
print(lanche[-2:])
for comida in lanche:
    print(f'Hj eu comi {comida}')
for count in range(0, len(lanche)):
    print(f'Hj eu comi {lanche[count]}') #mostra o item na posição count. um de cada vez
# os dois for tem a mesma resposta, porém tem situações q só funciona de uma maneira ou de outra
for pos, comida in enumerate(lanche): #mostra a posição além do elemento
    print(f'Vou comer {comida} na posição {pos}')
print(sorted(lanche)) #mostra organizado os elementos
a = 5, 2, 4
b = 3, 6, 7, 5
c = a + b #junta os elementos das duas tuplas
print(c)
print(c.count(5)) #quantas vezes aparece o número 5
print(c.index(7)) #em q posição está o 7
pessoa = 'Patrícia', '48', 'F', '1.58'
print(pessoa)
del(pessoa) #apaga a tupla