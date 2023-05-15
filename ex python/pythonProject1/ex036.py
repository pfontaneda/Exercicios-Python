v = float(input('Seja bem vindo ao setor de empréstimos. Qual o valor da casa que planeja adquirir? R$'))
s = float(input('E qual seu salário mensal: R$'))
t = int(input('E pretende pagar em quantos anos?'))
if v/(t*12) <= s*0.30:
    print('Você atende as exigências para o empréstimo que terá parcelas de R${:.2f},por {} anos.'.format(v/(t*12) , t))
else:
    print('Lamentamos , mas vc não atende as exigências para o empréstimo')


