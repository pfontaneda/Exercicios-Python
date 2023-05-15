num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop()
num.pop(1)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print('Não achei')
print(num)
print(f'Essa lista tem {len(num)} elementos')
valores = list()
valores.append(5)
valores.append(9)
valores.append(1)
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
elem = list()
for cont in range(0, 5):
    elem.append(int(input('Digite um valor: ')))
for c, v in enumerate(elem):
    print(f'Na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
a = [2, 4, 6, 8]
b = a # se vc diz q uma lista é igual a outra.. o q acontece numa, acontece na outra.
b[2] = 0
print(f'Lista A: {a}')
print(f'Lista B: {b}')
#pra criar uma cópia da lista sem ter a ligação:
b = a[:] #cria um fatiamento e aí não ficm interligadas as listas
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
