n = int(input('Qual número quer ver a tabuada? '))
for t in range(1, 11):
    r = n * t
    print('{} x {:2} = {}'.format(n, t, r))

'''Ou:
n = int(input('Qual número quer ver a tabuada? '))
for t in range(1, 11):
    print('{} x {:2} = {}.format(n, t, n+t)
    '''