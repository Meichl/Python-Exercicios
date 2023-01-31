from datetime import date
nasc = int(input('Ano de Nascimento: '))
data = date.today().year
idade = data - nasc

print('Quem nasceu em {} tem {} anos em {}.'.format(nasc, idade, data))

if idade > 18:
    saldo = 18 - idade
    print('Você já deveria ter se alistado em há {} anos'.format(saldo))
    ano = data + saldo
    print('Seu alistamento foi em {}'.format(ano))
elif idade < 18:
    saldo = idade - 18
    print('Você ainda vai ter que se alistar em {} anos'.format(saldo))
    ano = data - saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade == 18:
    print('Você deve se alistar IMEDIATAMENTE nesse ano')
