dias = int(input('Dias alugados:'))
km = float(input('Km rodados:'))
pago = dias * 60
pago2 = km * 0.15
total = pago + pago2
print(f'O valor total a pagar é de {total}')
