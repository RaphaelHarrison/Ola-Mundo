z = float(input('Digite o primeiro número:'))
y = float(input('Digite o segundo número:'))
if z > y:
    print(f'{z} é o número maior.')
elif y > z:
    print(f'{y} é o número maior.')
elif z == y :
  print(f'Os números são iguais.')