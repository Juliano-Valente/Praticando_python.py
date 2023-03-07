from random import randint
computador = randint( 1, 10)
print('**Oi, sou seu computador ... Acabei de pensar em um número entre 0 e 10.**')
print('Séra que vc consegue advinhar qual foi? ')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais... Tente mais uma vez.")
        else:
            print('Menos ... Tente mais uma vez.')
print('Acertou com {} tentativas. PARABÉNS!'.format(palpite))
