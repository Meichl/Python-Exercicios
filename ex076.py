listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 16.00)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:-<30}', end='')
    else:
        print(f'R$ {listagem[pos]:>2.2f}')
