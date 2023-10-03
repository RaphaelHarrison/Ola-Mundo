nome = input('Nome do aluno:')
x = float(input('Digite a Primeira nota:'))
y = float(input('Digite a Segunda nota:'))
m1 = (x + y)/2
if m1<5.0:
    print(f' {nome} foi reprovado.')
elif 5.0 <= m1 <= 6.9:
    print(f' {nome} está recuperação.')
elif m1 >6.9 :
    print(f' {nome} está aprovado.')