n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999: # a flag será 999 , entao não entra na soma
        break
    s += n
# print('A soma vale : {}'.format(s))
#versão atualizada do format: coloca f no inicio antes da aspa e o que quer dentro do{}. fstring chama
print(f'A soma vale {s}')
