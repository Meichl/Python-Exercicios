print('{:=^40}'.format('LOJA GERONIMO'))
preço = int(input('Qual o valor? R$'))
print('''Qual a forma de pagamento?
[ 1 ] à vista no dinheiro/cheque (10% de desconto)
[ 2 ] à vista no cartão (5% de desconto)
[ 3 ] em até 2x no cartão (sem desconto)
[ 4 ] em 3x ou mais no cartão (20% de juros)''')
opção = int(input('Selecione a forma de pagamento: '))
if opção == 1:
    total = preço - (preço * 10/100)
    print('Pagando à vista no dinheiro/cheque o preço fica R${:.2f} com 10% de desconto.'.format(total))
elif opção == 2:
    total = preço - (preço * 5/100)
    print('Pagando à vista no cartão o preço fica R${:.2f} com 5% de desconto'.format(total))
elif opção == 3:
    parcelas = preço / 2
    total = preço
    print('Pagando em 2 parcelas, fica divido de 2x R${:.2f}'.format(parcelas))
elif opção == 4:
    parcelas = (int(input('Em quantas parcelas? ')))
    total = preço + (preço * 20/100)
    parcelado = total / parcelas
    print('Pagando em {} parcelas, fica dividido de {}x R${:.2f}'.format(parcelas,parcelas, parcelado))
else:
    total = preço
    print('Opção invalida de pagamento, tente novamente')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final'.format(preço, total))