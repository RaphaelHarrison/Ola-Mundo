cidade = str(input('Coloque o nome de uma cidade:')).strip().upper()
if cidade.split()[0] == 'SANTO':
    print('A cidade começa com nome Santo')
else:
    print('A cidade não começa com nome Santo')