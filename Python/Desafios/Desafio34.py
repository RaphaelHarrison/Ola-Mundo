salario = float(input('Qual é o seu salário?'))
au1 = salario + (salario * 10/100)
au2 = salario + (salario * 15/100)
if salario <= 1.250:
    print(f'Seu aumento vai ser de 10% {au1}.')
else:
    print(f'Seu aumento vai ser de 15% {au2}.')
