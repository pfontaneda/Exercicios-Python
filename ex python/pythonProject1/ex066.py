num = soma = quant =  0
while True:
    num = int(input('Digite um número (666 para parar): '))
    if num == 666:
        break
    soma += num
    quant += 1
print(f'Foram digitados {quant} números e a soma é {soma}')
