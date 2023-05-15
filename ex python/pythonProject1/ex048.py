soma = 0 #acumulador, vai acumulando os valores achados
cont = 0 #contador, vai somando os números achados
for n in range(1, 501, 2):
    if n % 3 == 0:
        cont = cont + 1 #pode ser escrito cont += 1
        soma = soma + n #pode ser escrito soma += n
print('A soma dos {} números ímpares e divisíveis por 3 no intervalo solicitado é: {}'.format(cont, soma))



