# é sobre o mesmo número de parênteses abertos e fechados nas expressões matemáticas
expr = str(input('Digite a expressão matemática: '))
parenteses = []
for simb in expr:
    if simb == '(':
        parenteses.append('(')
    elif simb == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
# ele vai add cada "(" e cada vez q achar ")" vai retirar pq "achou o par. Se ao final zerar é pq a expressão está correta
if len(parenteses) == 0:
    print('Sua expressão matemática está correta!')
else:
    print('Sua expressão matemática está errada')
