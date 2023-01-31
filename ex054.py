from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(pessoas)))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('No total tem {} pessoas de maior e {} de menor'.format(totmaior, totmenor))

