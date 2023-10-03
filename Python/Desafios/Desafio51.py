primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimal = primeiro + (10-1) * razao
for c in range(primeiro,decimal,razao):
    print(c)