frase = str(input('Digite uma frase: ')).strip().upper()
print('A letra A aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira posição da letra A foi: {}'.format(frase.find('A')+1))
print('A ultima posição da letra A foi: {}'.format(frase.rfind('A')+1))