valores = []
while True:
    valores.append(int(input("Digite um valor: ")))
    resp = str(input('Quer continuar?[S/N] ')).upper()
    if resp == 'N':
        break
print('-=' * 30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'Os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O Valor 5 faz parte da lista')
else:
    print('O valor 5 não está presente na lista')
