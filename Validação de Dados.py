sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválido. Por favor, informe seu sexo ')).strip().upper()
print('Sexo {} registrado com secesso!'.format(sexo))
