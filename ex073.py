times = ('Palmeiras', 'Internacional', 'Fluminense', 'Flamengo',
         'Corinthians', 'Athletico-PR', 'Atlético-MG', 'América-MG', 'Goiás',
         'São Paulo', 'Botafogo', 'Santos', 'Bragantino', 'Fortaleza', 'Ceará SC',
         'Coritiba', 'Avaí', 'Cuiabá', 'Atlético-GO', 'Juventude')

print('=' * 20)
print(f'Lista de times do Brasileirão 2022: {times}')
print('=' * 20)
print(f'Os cinco primeiros são: {times[0:5]}')
print('=' * 20)
print(f'Os ultimos colocados são: {times[16:]}')  # ou times[-4:]
print('=' * 20)
print(f'Em ordem alfabetica: {sorted(times)}')
print('=' * 20)
print(f'O Corinthians está em {times.index("Corinthians")+1} posição')
