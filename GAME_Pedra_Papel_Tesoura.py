from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
nome = str(input('Qual o nome do jogador?: '))
print('{:=^40}'.format('{} VS COMPUTADOR'.format(nome)))
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual É A SUA JOGADA? '))
print('-='*11)
print('O computador jogou {}'.format(itens[computador]))
print('{} jogou {}'.format(nome, itens[jogador]))
print('-='*11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('{} VENCE!'.format(nome))
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('JOGADA INVÁLIDA!')
elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('{} VENCE!'.format(nome))
    else:
        print('JOGADA INVÁLIDA!')


elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print('{} VENCE!'.format(nome))
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA!')








