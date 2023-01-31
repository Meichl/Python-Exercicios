n = c = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    if n < 0:
        print('Valor negativo')
        break
    for c in range(1, 11):
        produto = n * c
        print(f'{n} x {c} = {produto}')
print('Obrigado por calcular')
