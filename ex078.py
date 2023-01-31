listanum = []
maior = 0
menor = 0
for c in range(0,5):
    listanum.append(int(input(f'Digite um número na posição {c}: ')))
    if c == 0:
        maior = menor = listanum[c]
    else:
        if listanum[c] >maior:
            maior = listanum[c]
        elif listanum[c] <menor:
            menor = listanum[c]
print(f'Vc digitou os valores {listanum}, o maior foi {maior} e o menor foi {menor}')
for i, v in enumerate(listanum):
    if v == maior:
        print(f'{i}...', end ='')
for i, v in enumerate(listanum):
    if v == menor:
        print(f'{i}...', end='')