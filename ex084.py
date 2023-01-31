pessoas = []
total = []
mai = men = 0
while True:
    pessoas.append(str(input('Nome: ')))
    pessoas.append(float(input('Peso: ')))
    if len(total) == 0:
        mai = men = pessoas[1]
    else:
        if pessoas[1] > mai:
            mai = pessoas[1]
        if pessoas[1] < men:
            men = pessoas[1]
    total.append(pessoas[:])
    pessoas.clear()
    resp = str(input('Quer continuar?[S/N] ')).upper()
    if resp == 'N':
        break
print(f'Os dados foram {total}')
print(f'Vc cadastrou {len(total)}')
print(f'O maior peso foi de {mai}')
for p in total:
    if p[1] == mai:
        print(f'{p[0]}', end='')
print(f'O menor peso foi {men}')
for p in total:
    if p[1] == men:
        print(f'{p[0]}', end='')

