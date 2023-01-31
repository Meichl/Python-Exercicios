import math
angulo = float(input('Digite o angulo que você deseja em graus: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo de {} tem o Seno de {:.2f}\nO cosseno de {:.2f}\nE a tangente de {:.2f} '.format(angulo, seno, cosseno, tangente))