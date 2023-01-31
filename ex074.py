from random import randint
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Eu sorteei os valores {num}')
for n in num:
    print(f'{n} ', end='')
# metodo 'max', pra pegar o maior valor
print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')  # metodo 'min'
