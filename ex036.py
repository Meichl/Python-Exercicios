valor = int(input('Digite o valor da casa: R$'))
salário = int(input('Digite o salário: R$'))
anos = int(input('Em quantos anos vai financiar: '))
prestação = valor / (anos * 12)
# end = '' junta as linhas
if prestação > salário * 30 / 100:
    print('O valor da casa é R${:.2f}, no tempo estimado as prestações seriam R${:.2f}. Emprestimo negado por exceder '
          '30% do salário.'.format(valor, prestação))
elif prestação <= salário * 30 / 100:
    print('Emprestimo aprovado. As prestações de R${:.2f} não excedem 30% do seu salário. Valor total da casa R${:.2f}.'
          .format(prestação, valor))
