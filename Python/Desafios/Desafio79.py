lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado não será adicionado.')
    r = str(input('Quer continuar?[S/N]\nEscolha: '))
    if r  in 'Nn':
        break
lista.sort()
print(f'Os números digitados são {lista}')