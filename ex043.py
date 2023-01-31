peso = float(input('Qual seu peso(Kg)? '))
alt = float(input('Qual sua altura(m)? '))
imc = peso / (alt ** 2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('A pessoa está abaixo do peso normal. Cuidado')
elif 18.5 <= imc < 25:
    print('A pessoa está no peso ideal.')
elif 25 <= imc < 30:
    print('A pessoa está com sobrepeso. Atenção')
elif 30 <= imc < 40:
    print('A pessoa está com obesidade. Cuidado')
elif imc >= 40:
    print('A pessoa está com obesidade Morbida. MUITO CUIDADO')