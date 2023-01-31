from random import randint
print('Jogo do Par ou Impar')
computador = 0
vitorias = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 11)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Impar?[P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}, dando o total de {total}')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            vitorias += 1
        else:
            print('Você perdeu')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            vitorias += 1
        else:
            print('Você perdeu')
            break
print(f'Game Over! Você venceu {vitorias} vezes')