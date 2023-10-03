id = int(input('Em que ano você nasceu?'))
a = 2023 - id
b = 18 - a
if a >= 18:
    print('Verifique como está seu alistamento, caso ja tenha passado pelo processo ignore a mensagem.')
else:
    print(f'Faltam  {b} para você se alistar.')

