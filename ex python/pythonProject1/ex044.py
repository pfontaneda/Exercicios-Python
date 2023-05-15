print('{:=^40}'.format(' LOJAS JUJUBALANDIA '))
valor = float(input('Qual o valor do produto? R$ '))
print('''Condições de pagamento:
[1] A vista no $$ ou pix : 10% desconto
[2] A vista no cartão: 5% desconto
[3] em até 2X no cartão: preço normal
[4] 3X ou mais no cartão: 20% acréscimo''')
pg = int(input('Digite a forma de pagamento conforme a tabela:'))
if pg == 1:
    print('O valor final é de R$ {:.2f}'.format(valor - (valor*10/100)))
elif pg == 2:
    print('O valor final é de R$ {:.2f}'.format(valor - (valor*5/100)))
elif pg == 3:
    print ('As parcelas serão de R$ {:.2f}'.format(valor / 2))
elif pg == 4:
    parcelas = int(input('Quantas parcelas?'))
    print('Cada parcela será de R$ {:.2f}'.format((valor + (valor*20/100))/parcelas))
else:
    pg = 0
    print('\033[31mOpção de pagamento inválida .Tente novamente.')





