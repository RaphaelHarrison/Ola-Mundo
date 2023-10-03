x = int(input('Digite um número: '))
z = input('Você quer saber os pares ou os impares do número escolhido anteriormente?\n1-Pares\n2-Impares\nEscolha: ')
if z == '1':
    for c in range(0, x, 2):
        print(c)
    print(f'Esses são os números pares de {x}')
elif z == '2':
    for c in range(0, x, 3):
        print(c)
    print(f'Esses são os números impares de {x}')
    
