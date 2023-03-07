frase = str(input('Digite uma frase: '.strip().upper()))
palavras = frase.split()
junto = ' '.join(palavras)
print('Você digitou a frase {}'.format(frase))
inverso = ' '
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada NÃo é um PALÍNDROMO!')



