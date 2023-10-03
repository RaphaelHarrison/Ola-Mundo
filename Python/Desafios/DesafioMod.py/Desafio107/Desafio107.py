import moedas


num = int(input('Digite um número para receber seu aumento(+10%), sua diminuição(-10%), seu dobro(2x) e sua metade.\nNúmero: '))

aumento = moedas.aumentar(num)
print(f'Com o aumento de 10% o valor foi de {num} para {aumento}.')

diminui = moedas.diminuir(num)
print(f'Com a diminuição de 10% o valor foi de {num} para {diminui}.')

dobr = moedas.dobro(num)
print(f'Com a multiplicação o valor foi de {num} para {dobr}.')

metade = moedas.metade(num)
print(f'Com a divisão o valor foi de {num} para {metade}.')

