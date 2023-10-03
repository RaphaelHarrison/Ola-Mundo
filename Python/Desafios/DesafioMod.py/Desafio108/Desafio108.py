import moedas


p = int(input('Digite um número para receber seu aumento(+10%), sua diminuição(-10%), seu dobro(2x) e sua metade.\nNúmero: '))
print(f'A metade de {moedas.moeda(p)} é {moedas.metade(p, True)}')
print(f'O dobro de {moedas.moeda(p)} é {moedas.dobro(p, True)}')
print(f'Aumentado 10%, temos {moedas.aumentar(p, 10, True)}')
print(f'Reduzindo 13%, temos {moedas.diminuir(p, 13, True)}') 