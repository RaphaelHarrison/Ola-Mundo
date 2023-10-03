x = float(input('Qual é o seu peso: '))
y = float(input('Qual é a sua altura: '))
imc = x / (y*2)
if imc < 18.5:
    print('Você está abaixo do peso ideal.')
elif imc >= 18.5 and imc <= 24.9:
    print('Você está no peso ideal.')
elif imc >= 25 and imc <= 29.9:
    print('Você está em sobrepeso.')
elif imc >= 30:
    print('Procure um médico.')
