print('-=' * 20)
print('Analisador de Triangulos...')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Com esses segmentos é possivel formar um triângulo ', end='')
    if r1 == r2 == r3: #forma tradicional = r1 == r2 and r2 == r3
        print('Equilátero')
    elif r1 != r2 != r3 != r1: #forma tradicional r1 != r2 and r2 != r3 and r3 != r1
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Com esses segumento não é possivel formar um triângulo.')