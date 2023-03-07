from time import sleep
n1 = int(input('Promeiro valor: '))
n2 = int(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''  [1] Somar
  [2] Multiplicar
  [3] Maior
  [4] Novos números
  [5] Sair do programa''')
    opcao = int(input('>>>>>>Qual é a sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}.'.format(n1, n2, soma))
    elif opcao == 2:
        mult = n1 * n2
        print('O resultado entre {} x {} é {}.'.format(n1, n2, mult))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Promeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('FINALIZANDO!...')
        sleep(2)
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
print('Fim do programa! Volte sempre!')




