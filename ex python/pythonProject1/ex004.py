n = input('Digite algo: ')
print('O tipo primitivo é ', type(n))
print('É alfanumerico? ', n.isalnum())
print('É letra? ', n.isalpha())
print(n.isascii())
print('Contém digitos? ', n.isdigit())
print('É escrito em letras minusculas? ', n.islower())
print('Tem decimais? ', n.isdecimal())
print(n.isidentifier())
print('É numerico? ', n.isnumeric())
print('Dá pra imprimir?', n.isprintable())
print(n.istitle())
print(n.isupper())

