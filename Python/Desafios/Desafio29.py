vel = float(input('Qual é a velocidade do veiculo?'))
multa = (vel - 80) * 7
if vel>80:
    print(f'Você passou do limete de velocidade e foi multado em {multa} reais')
else:
    print('Você respeitou as leis, continue assim!')