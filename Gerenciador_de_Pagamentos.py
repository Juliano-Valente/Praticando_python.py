print('{:=^40}'.format('LOJA VALENTE'))
preço = float(input('preço das compras? R$'))
print('''FORMA DE PAGAMENTO?
[1] Á VISTA DINHEIRO/CHEQUE
[2] Á VISTA CARTÃO
[3] 2X NO CARTÃO
[4] 3X OU MAIS NO CARTÃO''')
opção = int(input('Qual é a opção?: '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total /2
    print(' Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opção == 4:
    total = preço + (preço * 2 / 100)
    parcela = int(input('Quantas parcelas?:'))
    totparc = total / parcela
    print("Sua compra será parcelada em {}x de  R${:.2f} COM JUROS DE 20%".format(total, parcela))
else:
    print('OPÇÃO INVALIDA, TENTE NOVAMENTE!')
    
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total ))







