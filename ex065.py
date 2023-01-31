res = 'S'
soma = quant = media = maior = menor = 0
while res != 'N': # OU res in 'Ss':
    n = int(input('Digite um número: '))
    soma += n
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    res = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
media = soma / quant
print('Você digitou {} e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))