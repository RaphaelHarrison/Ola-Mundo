x = float(input('Digite o valor do item: '))
y = input('Qual é a forma de pagamento?\n1-À vista no dinheiro\n2-À vista no cartão\n3-Duas vezes no cartão\n4-Três vezes ou mais no cartão\nInforme: ')
dinheiro = x - (10/100)
cartão = x - (5/100)
dcartão = x
maisdeduas = x + (20/100)
if y == '1':
    print(f'O total a pagar é {dinheiro}')
elif y == '2':
    print(f'O total a pagar é {cartão}')
elif y == '3':
    print(f'O total a pagar é {dcartão}')
elif y == '4':
    print(f'O total a pagar é {maisdeduas}')