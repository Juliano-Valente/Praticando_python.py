num = int(input('Digite um número interiro: '))
print('''Escolha umas das bases para conversão: '
      [1] CONVERTER PARA BINÁRIO'
      [2] CONVERTER PARA OCTAL'
      [3] CONVERTER PARA HEXADECIMAL ''')
opção = int(input(' Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAl é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('INVALIDO!')
