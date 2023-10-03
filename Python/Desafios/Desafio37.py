num = int(input('Digite um número inteiro para a análise ser feita: '))
x = int(input('Escolha o tipo de análise:\n1-Binario\n2-Hexadecimal\n3-Octal\nInforme:'))

if x == 1:
    print(f'O número {num} em binário é:',(bin(num)))
elif x == 2:
    print(f'O número {num} em hexadecimal é: ',(hex(num)))
elif x == 3:
    print(f'O número {num} em octal é: ',(oct(num)))
else:
    print('Reinicie o programa')