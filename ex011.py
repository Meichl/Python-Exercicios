largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
área = largura * altura
print('Sua parede tem a dimensão {}x{} e sua área é {}m²'.format(largura, altura, área))
tinta = área / 2
print('Para pintar essa parede, você precisa de {}L de tinta'.format(tinta))