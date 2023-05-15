peso = float(input('Qual seu peso kg)?'))
altura = float(input('Qual sua altura (metros)?'))
imc = peso / (altura ** 2)
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('e vc está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('e vc está no peso ideal. Parabéns!!')
elif imc >= 25 and imc < 30:
    print('e vc está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('e vc está com obesidade')
else:
    print('e vc está com obesidade mórbida.')



