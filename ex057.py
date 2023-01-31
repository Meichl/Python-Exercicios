sexo = str(input('Informe seu seco: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos. Por favor, informe seu sexo novamente:')).strip().upper()[0]
print('Sexo {} registrado'.format(sexo))