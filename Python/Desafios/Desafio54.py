from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input('Qual é o ano de nascimento: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Temos {totmaior} de pessoas que ja atingiram a maioridade e {totmenor} de pessoas menores de idade.')
