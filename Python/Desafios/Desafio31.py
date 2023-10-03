km = float(input('Digite quantos km vai percorrer na viagem:'))
m = km * 0.50
m2 = km * 0.45
if km>200:
    print(f'O preço da passagem é {m}.')
else:
    print(f'O valor da passagem é {m2}')