try:
    a = int(input('numerador:'))
    b = int(input('Divisor:'))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos problemas com os tipos de dados que vc digitou')
except ZeroDivisionError:
    print('Não é possível dividir por zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
except Exception as erro: #sempre o Exception é em letra maiúscula
    print(f'O problema encontrado foi: {erro.__class__}')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre, Grata')


