from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados["ctps"] = int(input('Carteira de Trabalho (0 se não tiver): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('_-' * 20)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')

