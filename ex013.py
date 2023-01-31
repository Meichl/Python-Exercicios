salario = float(input('Qual o seu salário atual? R$'))
novo = salario + (salario * 15 / 100)
print('Seu salário de R${:.2f} recebeu um aumento de 15%, então agora é R${:.2f}'.format(salario,novo))