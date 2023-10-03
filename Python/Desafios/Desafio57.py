print('Vamos começar o cadastramento.')
n = str(input('Digite seu nome: '))
sexo = str(input('Digite o seu sexo[M/F]\nInforme:')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido, digite novamente seu sexo[M/F]: ')).strip().upper()[0]
idade = int(input('Digite a sua idade: '))
while idade >= 100:
    idade = int(input('Idade invalida, digite sua idade: '))
print(f'Seu nome é {n}, você é do sexo {sexo} e sua idade é {idade}')