n = 0
cont = 0
soma = 0
# quando as variáveis são iguais pode colocar tudo na mesma linha
# n = cont = soma = 0
n = int(input('Digite um número [999 para parar] :')) #flag
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar] :'))#flag. não entra na soma
print('Vc digitou {} números e a soma é {}'.format(cont, soma))
