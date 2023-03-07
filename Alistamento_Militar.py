from datetime import date
atual = date.today().year
nasc = int(input(' Ano de Nascimento: '))
idade = atual - nasc
print('Quem nasceu em {} tem {} em {}'.format(nasc, idade,atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento séra em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Voçê já deveria ter se alistado hà {} anos'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))




