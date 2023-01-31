numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado n irei colocar')
    r = str(input('Quer continuar?[S/N] ')).upper()
    if r == 'N':
        break
numeros.sort()
print(f'Vc digitou os valores {numeros}')