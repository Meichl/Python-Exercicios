reais = float(input('Quantos reais voce tem? R$'))
dolares = reais / 5.08
print('Com R${:.2f} você pode comprar U$${:.2f}.'.format(reais, dolares))
