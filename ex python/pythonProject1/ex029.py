v = float(input('Digite a velocidade do seu carro:'))
if v >= 80:
    print('Vc ultrapassou o limite de velocidade e foi multado em R$ {:.2f} '.format((v-80)*7))
else:
    print('Parabéns, vc está dentro do limite de velocidade permitido')

