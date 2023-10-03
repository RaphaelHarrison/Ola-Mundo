let = input('Digite uma frase:')
min = let.lower().replace('á','a').replace('à','a').replace('ã','a').replace('â','a')
qnt = min.count('a')
pri = min.find('a')
ult = min.rfind('a')
print(f'A frase {let} possui essa quantidade de letras A = {qnt}\nA primeira vez que ela aparece é no caractere {pri}'
      f'e aparece por ultimo no caractere {ult}')