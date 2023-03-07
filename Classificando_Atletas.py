from datetime import date
atual = date.today().year
nascimento = int(input('ANO DE NASCIMENTO: '))
idade = atual - nascimento
print('O ATLETA TEM {} ANOS.'.format(idade))
if idade <= 9:
    print('Sua categoria é MIRIM!')
elif idade <= 14:
    print('Sua categoria é INFANTIL!')
elif idade <= 19:
    print('Sua categoria é JUNIOR!')
elif idade <= 25:
    print('Sua categoria é SÊNIOR!')
else:
    print('Sua categoria é MATER!')


