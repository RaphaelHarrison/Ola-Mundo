casa = float(input('Qual é o valor da casa?'))
sal = float(input('Quanto você recebe por mês?'))
ano = int(input('Em quantas prestações você deseja?'))
mes = casa / ano
pm = sal / (30/100)
if mes > pm:
    print('Você não vai poder comprar a casa pois o valor da prestação é 30% maior que seu salário.')
else:
    print(f'Você pagará {mes} pela casa.')
