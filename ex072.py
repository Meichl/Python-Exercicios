numeros = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro',
           'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez')

while True:
    num = int(input('Digite um número entre 0 e 10: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.', end='')

print(f'Você escreveu o {numeros[num]}')
