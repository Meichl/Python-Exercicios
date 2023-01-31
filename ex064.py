n = 0  # OU n = cont = soma = 0
cont = 0
soma = 0
n = int(input('Digite um número [999 para parar]: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números.'.format(cont))
print('A soma entre eles foi {}'.format(soma))