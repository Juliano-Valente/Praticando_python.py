peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input("Qual é a sua altura? (m) "))
imc = peso / (altura **2)
print("O seu IMC é {:.1f}".format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO!')
elif imc < 25:
    print('PARABÉNS VOCê ESTÁ NO PESO IDEAL!')
elif imc < 30:
    print('SOBREPESO!')
elif imc < 40:
    print('OBESIDADE!')
else:
    print('OBESIDADE MÓRBIDA!')


