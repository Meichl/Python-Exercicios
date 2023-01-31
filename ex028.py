from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar! haha')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) #Jogador tenta advinhar o numero
print('Processando...')
sleep(3)
if computador == jogador:
    print('Você acertou! Parabéns, você conseguiu me vencer.')
else:
    print('Voce errou, fracassado, eu pensei no número {} e não no {}!'.format(computador, jogador))




