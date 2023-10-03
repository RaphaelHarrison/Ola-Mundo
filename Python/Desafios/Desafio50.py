soma = 0
cont = 0
for c in range(1,7):
    x = int(input('Digite um número inteiro:'))
    if x % 2 == 0:
        cont = cont + 1
        soma = soma + x
print(f'Dos números digitados, a soma dos PARES({cont}) da: {soma}')   