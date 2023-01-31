print('=' * 20)
print('10 Termos PA')
print('=' * 20)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for n in range(primeiro, décimo + 1, razão):
    print('{}'.format(n), end='-> ')
print('Acabou')