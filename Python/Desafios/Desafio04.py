a = input('digite algo:')
#print('O tipo primitivo desse valor é de,', type(a))
print(f'O valor primitivo de {a} é de', type(a))
print('O valor tem espaços?', a.isspace())
print('Só tem letras?', a.isalpha())
print('Só tem números', a.isnumeric())
print('É decimal', a.isdecimal())
print('Está em caps', a.isupper())
print('Não está em caps', a.islower())


