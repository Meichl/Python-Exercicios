salário = float(input('Digite o seu salario: R$'))
if salário >= 1250:
    novo = salário + (salário * 10/100)
    print('Seu salário de R${:.2f}, recebeu um aumento de 10% e agora é R${:.2f}'.format(salário, novo))
else:
    novo = salário + (salário * 15/100)
    print('Seu salário de R${:.2f}, recebeu um aumento de 15% e agora é R${:.2f}'.format(salário, novo))
print('Parabéns pelo aumento!')

