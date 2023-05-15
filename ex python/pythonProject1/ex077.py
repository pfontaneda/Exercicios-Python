frutas = ('abacate', 'ameixa', 'banana', 'caqui',
          'damasco', 'figo', 'goiaba', 'laranja')
for f in frutas: #cada palavra é uma lista de letras. então dá pra analisar separadamente
    print(f'\nNa palavra {f.upper()} temos as vogais: ', end='')
    for letra in f:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

