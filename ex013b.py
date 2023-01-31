preço = float(input('Qual o preço do produto? R$'))
desconto = preço - (preço * 10 / 100)
parcelado = preço + (preço * 5 / 100)
print('O preço do produto é R${:.2f}, pagando a vista fica R${:.2f} e parcelado fica R${:.2f}'.format(preço, desconto, parcelado))