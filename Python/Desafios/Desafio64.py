num = cont = soma = 0
num = int(input('Digite um número.Obs:Digite 999 para parar o programa.\nInforme:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número.Obs:Digite 999 para parar o programa.\nInforme:'))
print(f'Você digitou {cont} e a soma deles da {soma}')